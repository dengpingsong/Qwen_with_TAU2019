from pathlib import Path
import librosa
import numpy as np
import torch
from transformers import Qwen2AudioForConditionalGeneration, AutoProcessor
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")
from transformers import logging
logging.set_verbosity_error()
import csv

# ---------------- 1. 加载模型和 processor ----------------
processor = AutoProcessor.from_pretrained("Qwen/Qwen2-Audio-7B-Instruct")
model = Qwen2AudioForConditionalGeneration.from_pretrained(
    "Qwen/Qwen2-Audio-7B-Instruct",
    device_map="auto"
)
model.eval()  # 推理模式

# ---------------- 2. 音频文件路径 ----------------
audio_folder = Path("./TAU-urban-acoustic-scenes-2019-development/audio")
audio_files = sorted(audio_folder.glob("*.wav"))

if not audio_files:
    print("未找到任何 .wav 文件！")
    exit()

# ---------------- 3. 输出目录 ----------------
output_folder = Path("./new_Feature")
output_folder.mkdir(parents=True, exist_ok=True)

# ---------------- 4. 批处理参数 ----------------
batch_size = 1000
total_files = len(audio_files)
num_batches = (total_files + batch_size - 1) // batch_size

print(f"总音频文件数: {total_files}")
print(f"批次大小: {batch_size}")
print(f"总批次数: {num_batches}")

# ---------------- 5. 加载单条音频 ----------------
def load_local_audio(path: str) -> np.ndarray:
    file_path = Path(path)
    if not file_path.exists() or file_path.stat().st_size == 0:
        raise FileNotFoundError(f"音频文件 {path} 不存在或为空")
    audio, _ = librosa.load(
        path,
        sr=processor.feature_extractor.sampling_rate,
        mono=True
    )
    return audio

# ---------------- 6. 主处理循环 ----------------
output_records = []

for batch_idx in range(num_batches):
    start_idx = batch_idx * batch_size
    end_idx   = min((batch_idx + 1) * batch_size, total_files)
    batch_files = audio_files[start_idx:end_idx]

    print(f"\n处理批次 {batch_idx + 1}/{num_batches}，文件 {start_idx + 1}-{end_idx}")

    for audio_file in tqdm(batch_files, desc=f"批次 {batch_idx + 1}/{num_batches}", unit="file"):
        try:
            # 加载音频
            audio = load_local_audio(str(audio_file))

            # 构造对话
            conversation = [
                {
                    "role": "system",
                    "content": "You need to separate audio into 2 parts, figure out whether audio recorded in the airport."
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "audio",
                            "audio_url": "<|AUDIO|>",
                            "local_path": str(audio_file)
                        }
                    ]
                }
            ]

            # 模板化 & tokenize
            text = processor.apply_chat_template(
                conversation,
                tokenize=False,
                add_generation_prompt=True
            )
            inputs = processor(
                text=text,
                audios=[audio],
                return_tensors="pt",
                padding=True
            )
            inputs = {k: v.to(model.device) for k, v in inputs.items()}

            # 一次调用同时拿到生成文本与 hidden_states
            with torch.no_grad():
                gen_out = model.generate(
                    **inputs,
                    output_hidden_states=True,
                    return_dict_in_generate=True,
                    max_new_tokens=64
                )

            # 解码文本
            generated_text = processor.batch_decode(
                gen_out.sequences,
                skip_special_tokens=True
            )[0].strip()

            # 取最后一层 hidden_states (shape: [batch, seq_len, hidden_dim])
            hidden_states = gen_out.hidden_states[-1][-1].cpu().numpy()  # 取最后一个解码步

            # 保存特征
            original_name = audio_file.stem + "_bi-scene"
            np.save(output_folder / f"{original_name}.npy", hidden_states)

            # 记录结果
            output_records.append({
                "file": audio_file.name,
                "generated_text": generated_text
            })

        except Exception as e:
            print(f"\n处理文件 {audio_file.name} 时出错：{e}")
            continue

# ---------------- 7. 写入 CSV ----------------
csv_output_path = Path("model_bi_outputs.csv")
with open(csv_output_path, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["file", "generated_text"])
    writer.writeheader()
    writer.writerows(output_records)

print("\n所有音频文件处理完成！生成文本已保存到 model_bi_outputs.csv")