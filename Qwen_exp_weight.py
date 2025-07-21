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

# 使用 MPS 设备加载模型
device = "mps" if torch.backends.mps.is_available() else "cpu"
model = Qwen2AudioForConditionalGeneration.from_pretrained(
    "Qwen/Qwen2-Audio-7B-Instruct"
).to(device)
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
def process_files(files, output_dir):
    import pandas as pd

    # 读取 meta.csv 和构建 few-shot 样本
    meta_path = Path("TAU-urban-acoustic-scenes-2019-development/meta.csv")
    df = pd.read_csv(meta_path, sep=None, engine="python")
    df.columns = [c.strip() for c in df.columns]
    if 'scene_label' not in df.columns:
        raise ValueError(f"meta.csv缺少'scene_label'列，实际列名：{df.columns}")
    categories = df['scene_label'].unique()
    few_shot_examples = []
    for cat in categories:
        sample_row = df[df['scene_label'] == cat].iloc[0]
        # 修正样本音频路径拼接，避免audio/audio/重复
        sample_file = Path("TAU-urban-acoustic-scenes-2019-development") / sample_row['filename'].lstrip('/')
        few_shot_examples.append({
            "role": "user",
            "content": [
                {"type": "audio", "audio_url": "<|AUDIO|>", "local_path": str(sample_file)},
                {"type": "text", "text": f"类别: {cat}"}
            ]
        })

    output_records = []
    for audio_file in tqdm(files, desc="处理进度", position=0):
        try:
            # 构建prompt和音频列表
            conversation = [
                {"role": "system", "content": "你需要根据给定的音频样例和类别，判断新音频属于哪个类别。"},
            ]
            audios_list = []
            for ex in few_shot_examples:
                conversation.append(ex)
                sample_audio = librosa.load(ex["content"][0]["local_path"], sr=processor.feature_extractor.sampling_rate, mono=True)[0]
                audios_list.append(sample_audio)
            # 加入待分类音频
            conversation.append({
                "role": "user",
                "content": [
                    {"type": "audio", "audio_url": "<|AUDIO|>", "local_path": str(audio_file)}
                ]
            })
            audio = librosa.load(str(audio_file), sr=processor.feature_extractor.sampling_rate, mono=True)[0]
            audios_list.append(audio)
            text = processor.apply_chat_template(conversation, tokenize=False, add_generation_prompt=True)
            inputs = processor(text=text, audios=audios_list, return_tensors="pt", padding=True)
            inputs = {k: v.to(model.device) for k, v in inputs.items()}
            with torch.no_grad():
                gen_out = model.generate(
                    **inputs,
                    output_hidden_states=True,
                    return_dict_in_generate=True,
                    max_new_tokens=64
                )
            generated_text = processor.batch_decode(gen_out.sequences, skip_special_tokens=True)[0].strip()
            hidden_states = gen_out.hidden_states[-1][-1].cpu().numpy()
            original_name = Path(audio_file).stem + "_bi-scene"
            np.save(Path(output_dir) / f"{original_name}.npy", hidden_states)
            output_records.append({"file": Path(audio_file).name, "generated_text": generated_text})
        except Exception as e:
            print(f"处理文件 {audio_file} 时出错：{e}")
    # 写入csv
    csv_output_path = Path(output_dir) / f"model_bi_outputs.csv"
    with open(csv_output_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["file", "generated_text"])
        writer.writeheader()
        writer.writerows(output_records)
    print(f"处理完成，结果写入 {csv_output_path}")

# ----------- 主进程运行 -----------
if __name__ == "__main__":
    total_files = len(audio_files)
    print(f"总文件数: {total_files}")
    # 划分批次
    batch_size = 1000
    num_batches = (total_files + batch_size - 1) // batch_size
    for i in range(num_batches):
        start = i * batch_size
        end = min((i + 1) * batch_size, total_files)
        files = audio_files[start:end]
        process_files(files, output_folder)
    print("所有文件处理完成！")