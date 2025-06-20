#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简化的音频场景不一致样本分析工具
使用PANNs进行AudioSet事件检测，代码简洁易读
"""

import pandas as pd
import numpy as np
import librosa
import torch
import torch.nn.functional as F
from panns_inference import AudioTagging, SoundEventDetection, labels
import os
import json
from datetime import datetime

def load_audioset_model():
    """加载AudioSet模型"""
    try:
        print("正在加载AudioSet模型...")
        model = AudioTagging(checkpoint_path=None, device='cpu')
        print("AudioSet模型加载成功")
        return model
    except Exception as e:
        print(f"AudioSet模型加载失败: {e}")
        return None

def analyze_audio_with_panns(audio_path, model):
    """使用PANNs分析音频文件"""
    try:
        # 加载音频
        audio, sr = librosa.load(audio_path, sr=32000, duration=10.0)
        
        # 确保音频长度
        if len(audio) < 32000:  # 至少1秒
            audio = np.pad(audio, (0, 32000 - len(audio)), mode='constant')
        
        # 使用模型进行推理
        clipwise_output, embedding = model.inference(audio[None, :])  # 添加batch维度
        
        # 获取前5个最可能的标签
        sorted_indexes = np.argsort(clipwise_output[0])[::-1]
        top_labels = []
        
        for i in range(min(5, len(sorted_indexes))):
            idx = sorted_indexes[i]
            score = clipwise_output[0][idx]
            if score > 0.1:  # 只保留置信度 > 0.1 的标签
                label_name = labels[idx]
                top_labels.append({
                    'label': label_name,
                    'score': float(score)
                })
        
        return top_labels
        
    except Exception as e:
        print(f"PANNs分析失败: {e}")
        return []

def get_audio_basic_features(audio_path):
    """获取音频基本特征（备用方案）"""
    try:
        audio, sr = librosa.load(audio_path, sr=22050, duration=10.0)
        
        # 计算基本特征
        rms = float(np.mean(librosa.feature.rms(y=audio)))
        spectral_centroid = float(np.mean(librosa.feature.spectral_centroid(y=audio, sr=sr)))
        zero_crossing_rate = float(np.mean(librosa.feature.zero_crossing_rate(audio)))
        
        # 简单的场景特征推断
        features = {
            'rms_energy': rms,
            'spectral_centroid': spectral_centroid,
            'zero_crossing_rate': zero_crossing_rate
        }
        
        # 基于特征的简单分类提示
        if rms > 0.02 and spectral_centroid > 2000:
            scene_hint = "high_energy_traffic"
        elif rms < 0.01 and zero_crossing_rate < 0.05:
            scene_hint = "quiet_indoor"
        else:
            scene_hint = "mixed_environment"
            
        features['scene_hint'] = scene_hint
        return features
        
    except Exception as e:
        print(f"基本特征提取失败: {e}")
        return {}

def analyze_prediction_differences():
    """分析预测不一致的样本"""
    
    # 读取预测不一致的样本
    try:
        inconsistent = pd.read_csv('detailed_inconsistent_samples.csv')
        print(f"加载了 {len(inconsistent)} 个预测不一致的样本")
    except Exception as e:
        print(f"无法读取不一致样本文件: {e}")
        return
    
    if len(inconsistent) == 0:
        print("没有发现预测不一致的样本")
        return
    
    # 加载AudioSet模型
    audioset_model = load_audioset_model()
    
    # 限制分析样本数量
    max_samples = -1
    samples_to_analyze = inconsistent.head(max_samples)
    
    results = []
    audio_base_path = "TAU-urban-acoustic-scenes-2019-development/audio"
    
    print(f"\n开始分析 {len(samples_to_analyze)} 个不一致样本...")
    
    for idx, (_, row) in enumerate(samples_to_analyze.iterrows(), 1):
        print(f"\n分析样本 {idx}/{len(samples_to_analyze)}")
        
        # 从base_name构建音频文件名
        base_name = row['base_name']
        filename = base_name + '-a.wav'  # 原始音频文件是.wav格式，需要加-a后缀
        audio_path = os.path.join(audio_base_path, filename)
        
        # 基本信息
        sample_info = {
            'filename': filename,
            'base_name': base_name,
            'true_scene': row['true_label_ae'],  # 使用AE的真实标签
            'ae_prediction': row['predicted_label_ae'],
            'as_prediction': row['predicted_label_as'],
            'ae_confidence': 1.0,  # 原始文件没有置信度，设为默认值
            'as_confidence': 1.0,
        }
        
        print(f"  文件: {filename}")
        print(f"  真实场景: {sample_info['true_scene']}")
        print(f"  AE预测: {sample_info['ae_prediction']}")
        print(f"  AS预测: {sample_info['as_prediction']}")
        
        # AudioSet事件分析
        audioset_events = []
        if audioset_model and os.path.exists(audio_path):
            try:
                audioset_events = analyze_audio_with_panns(audio_path, audioset_model)
                events_str = [f"{event['label']}({event['score']:.3f})" for event in audioset_events[:3]]
                print(f"  AudioSet事件: {events_str}")
            except Exception as e:
                print(f"  AudioSet分析失败: {e}")
        
        # 备用特征分析
        audio_features = {}
        if os.path.exists(audio_path):
            audio_features = get_audio_basic_features(audio_path)
            if audio_features:
                print(f"  音频特征: RMS={audio_features.get('rms_energy', 0):.4f}, "
                      f"频谱重心={audio_features.get('spectral_centroid', 0):.0f}Hz")
        
        sample_info.update({
            'audioset_events': audioset_events,
            'audio_features': audio_features,
            'analysis_timestamp': datetime.now().isoformat()
        })
        
        results.append(sample_info)
    
    # 保存详细结果
    output_file = f"inconsistent_samples_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\n详细分析结果已保存到: {output_file}")
    
    # 生成分析报告
    generate_analysis_report(results)

def generate_analysis_report(results):
    """生成分析报告"""
    
    report_lines = [
        f"# 音频场景预测不一致样本分析报告",
        f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"分析样本数量: {len(results)}",
        "",
        "## 分析统计",
    ]
    
    # 统计各种模式
    scene_stats = {}
    prediction_patterns = {}
    
    for result in results:
        true_scene = result['true_scene']
        ae_pred = result['ae_prediction']
        as_pred = result['as_prediction']
        
        scene_stats[true_scene] = scene_stats.get(true_scene, 0) + 1
        
        pattern = f"{ae_pred} vs {as_pred}"
        prediction_patterns[pattern] = prediction_patterns.get(pattern, 0) + 1
    
    # 真实场景分布
    report_lines.extend([
        "",
        "### 真实场景分布",
        "| 场景 | 数量 |",
        "| --- | --- |"
    ])
    
    for scene, count in sorted(scene_stats.items()):
        report_lines.append(f"| {scene} | {count} |")
    
    # 预测模式分布
    report_lines.extend([
        "",
        "### 预测不一致模式 (AE vs AS)",
        "| 预测模式 | 数量 |",
        "| --- | --- |"
    ])
    
    for pattern, count in sorted(prediction_patterns.items(), key=lambda x: x[1], reverse=True):
        report_lines.append(f"| {pattern} | {count} |")
    
    # 详细样本信息
    report_lines.extend([
        "",
        "## 详细样本分析",
        ""
    ])
    
    for i, result in enumerate(results, 1):
        report_lines.extend([
            f"### 样本 {i}: {result['filename']}",
            f"- **真实场景**: {result['true_scene']}",
            f"- **AE预测**: {result['ae_prediction']}",
            f"- **AS预测**: {result['as_prediction']}",
        ])
        
        # AudioSet事件
        if result['audioset_events']:
            events_str = ", ".join([f"{e['label']}({e['score']:.3f})" 
                                  for e in result['audioset_events'][:3]])
            report_lines.append(f"- **检测到的事件**: {events_str}")
        
        # 音频特征
        if result['audio_features']:
            features = result['audio_features']
            report_lines.append(f"- **音频特征**: RMS={features.get('rms_energy', 0):.4f}, "
                              f"频谱重心={features.get('spectral_centroid', 0):.0f}Hz, "
                              f"场景提示={features.get('scene_hint', 'unknown')}")
        
        report_lines.append("")
    
    # 保存报告
    report_file = f"inconsistent_analysis_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))
    
    print(f"分析报告已保存到: {report_file}")

if __name__ == "__main__":
    print("=== 音频场景预测不一致样本分析工具 ===")
    analyze_prediction_differences()
    print("\n分析完成!")
