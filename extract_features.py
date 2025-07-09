#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简化的音频特征提取脚本
支持批量提取Qwen音频特征
Created on 2025-07-03
"""

from pathlib import Path
import librosa
import numpy as np
import torch
from transformers import Qwen2AudioForConditionalGeneration, AutoProcessor
from tqdm import tqdm
import warnings
import csv
import argparse
from config import FEATURE_CONFIG, FEATURE_TYPES, DATA_PATHS

warnings.filterwarnings("ignore")
from transformers import logging
logging.set_verbosity_error()


def load_model():
    """加载Qwen模型"""
    print("正在加载Qwen模型...")
    model_name = FEATURE_CONFIG['model_name']
    processor = AutoProcessor.from_pretrained(model_name)
    model = Qwen2AudioForConditionalGeneration.from_pretrained(
        model_name,
        device_map="auto"
    )
    model.eval()
    print("模型加载完成!")
    return processor, model


def load_audio(path, processor):
    """加载音频文件"""
    audio, _ = librosa.load(
        path,
        sr=processor.feature_extractor.sampling_rate,
        mono=True
    )
    return audio


def get_prompt(mode):
    """获取提示词"""
    return FEATURE_TYPES.get(mode, FEATURE_TYPES['general'])['prompt']


def extract_single_feature(audio_file, processor, model, mode):
    """提取单个文件的特征"""
    # 加载音频
    audio = load_audio(str(audio_file), processor)
    
    # 构造对话
    conversation = [
        {
            "role": "system",
            "content": get_prompt(mode)
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
    
    # 处理
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
    
    # 生成特征
    with torch.no_grad():
        gen_out = model.generate(
            **inputs,
            output_hidden_states=True,
            return_dict_in_generate=True,
            max_new_tokens=FEATURE_CONFIG['max_new_tokens']
        )
    
    # 获取文本和特征
    generated_text = processor.batch_decode(
        gen_out.sequences,
        skip_special_tokens=True
    )[0].strip()
    
    hidden_states = gen_out.hidden_states[-1][-1].cpu().numpy()
    
    return hidden_states, generated_text


def extract_features(audio_folder, output_folder, mode="AE", batch_size=1000):
    """批量提取特征"""
    # 设置路径
    audio_folder = Path(audio_folder)
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)
    
    # 获取音频文件
    audio_files = sorted(audio_folder.glob("*.wav"))
    if not audio_files:
        print(f"在 {audio_folder} 中未找到 .wav 文件！")
        return
    
    print(f"找到 {len(audio_files)} 个音频文件")
    print(f"提取模式: {mode}")
    
    # 加载模型
    processor, model = load_model()
    
    # 处理文件
    results = []
    for i, audio_file in enumerate(tqdm(audio_files, desc="提取特征")):
        try:
            # 提取特征
            features, text = extract_single_feature(audio_file, processor, model, mode)
            
            # 保存特征
            if mode == "bi":
                feature_name = audio_file.stem + "_bi-scene"
            else:
                feature_name = audio_file.stem + mode
            
            np.save(output_folder / f"{feature_name}.npy", features)
            
            # 记录结果
            results.append({
                "file": audio_file.name,
                "feature_file": f"{feature_name}.npy",
                "generated_text": text,
                "mode": mode
            })
            
        except Exception as e:
            print(f"处理 {audio_file.name} 时出错: {e}")
            continue
    
    # 保存结果
    csv_file = output_folder / f"extraction_results_{mode}.csv"
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["file", "feature_file", "generated_text", "mode"])
        writer.writeheader()
        writer.writerows(results)
    
    print(f"特征提取完成! 结果保存到 {csv_file}")


def main():
    parser = argparse.ArgumentParser(description="音频特征提取")
    parser.add_argument("--audio_folder", default=DATA_PATHS['audio_folder'],
                       help="音频文件夹")
    parser.add_argument("--output_folder", default=DATA_PATHS['feature_folder'],
                       help="输出文件夹")
    parser.add_argument("--mode", choices=list(FEATURE_TYPES.keys()),
                       default="AE", help="提取模式")
    parser.add_argument("--batch_size", type=int, default=FEATURE_CONFIG['batch_size'],
                       help="批次大小")
    
    args = parser.parse_args()
    
    extract_features(
        audio_folder=args.audio_folder,
        output_folder=args.output_folder,
        mode=args.mode,
        batch_size=args.batch_size
    )


if __name__ == "__main__":
    main()
