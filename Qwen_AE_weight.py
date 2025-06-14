from pathlib import Path
import librosa
import numpy as np
import torch
from transformers import Qwen2AudioForConditionalGeneration, AutoProcessor

# 1. 加载模型和 processor
processor = AutoProcessor.from_pretrained("Qwen/Qwen2-Audio-7B-Instruct")
model = Qwen2AudioForConditionalGeneration.from_pretrained("Qwen/Qwen2-Audio-7B-Instruct", device_map="auto")

# 2. 设定音频文件路径
audio_folder = Path("./TAU-urban-acoustic-scenes-2019-development/audio")
audio_files = list(audio_folder.glob("*.wav"))

if not audio_files:
    print("未找到任何 .wav 文件！")
    exit()

# 3. 设定特征存储路径
output_folder = Path("./new_Feature")
output_folder.mkdir(parents=True, exist_ok=True)

# 4. 设置批处理参数
batch_size = 1000
total_files = len(audio_files)
num_batches = (total_files + batch_size - 1) // batch_size

print(f"总音频文件数: {total_files}")
print(f"批次大小: {batch_size}")
print(f"总批次数: {num_batches}")

# 5. 加载音频的函数
def load_local_audio(path: str) -> np.ndarray:
    file_path = Path(path)
    if not file_path.exists() or file_path.stat().st_size == 0:
        raise FileNotFoundError(f"音频文件 {path} 不存在或为空")

    audio, sr = librosa.load(
        path,
        sr=processor.feature_extractor.sampling_rate,
        mono=True
    )
    return audio

# 6. 分批处理音频文件
for batch_idx in range(num_batches):
    start_idx = batch_idx * batch_size
    end_idx = min((batch_idx + 1) * batch_size, total_files)
    batch_files = audio_files[start_idx:end_idx]
    
    print(f"\n处理批次 {batch_idx + 1}/{num_batches}")
    print(f"处理文件 {start_idx + 1} 到 {end_idx}")
    
    # 处理当前批次的每个音频文件
    for i, audio_file in enumerate(batch_files):
        try:
            # 加载单个音频
            audio = load_local_audio(str(audio_file))
            
            # 生成对话内容（仅包含当前音频）
            conversation = [
                {"role": "system", "content": "You need to focus on describe every events in the audio."},
                {
                    "role": "user",
                    "content": [{
                        "type": "audio",
                        "audio_url": "<|AUDIO|>",
                        "local_path": str(audio_file)
                    }]
                }
            ]
            
            # 生成文本
            text = processor.apply_chat_template(conversation, tokenize=False, add_generation_prompt=True)
            
            # 使用 processor 处理音频和文本
            inputs = processor(text=text, audios=[audio], return_tensors="pt", padding=True)
            inputs = {k: v.to(next(model.parameters()).device) for k, v in inputs.items()}
            
            model.eval()
            with torch.no_grad():
                # 获取模型输出
                outputs = model(**inputs, output_hidden_states=True)
                
                # 获取最后一层 hidden state
                hidden_states = outputs.hidden_states[-1].cpu().numpy()
                
                # 保存特征
                original_name = Path(audio_file).stem
                original_name += "AE"
                output_path = output_folder / f"{original_name}.npy"
                np.save(output_path, hidden_states)
                
                print(f"已保存特征文件：{output_path}，维度：{hidden_states.shape}")
                
        except Exception as e:
            print(f"处理文件 {audio_file} 时出错：{str(e)}")
            continue

print("\n所有音频文件处理完成！")