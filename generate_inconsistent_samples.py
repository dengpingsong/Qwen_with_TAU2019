#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成AE和AS预测不一致的样本分析
Created on 2025-06-20
"""

import pandas as pd
import numpy as np
import os
from pathlib import Path

def compare_predictions():
    """比较AE和AS的预测结果，找出不一致的样本"""
    
    # 读取AE预测结果
    ae_result_path = "experiment_results/Qwen_AE_FC_Classification/2025-06-20_15-07-44/prediction_results_AE_FC.csv"
    as_result_path = "experiment_results/Qwen_AS_FC_Classification/2025-06-20_15-14-21/prediction_results_AS_FC.csv"
    
    if not os.path.exists(ae_result_path):
        print(f"AE结果文件不存在: {ae_result_path}")
        return None
    
    if not os.path.exists(as_result_path):
        print(f"AS结果文件不存在: {as_result_path}")
        return None
    
    # 读取预测结果
    ae_df = pd.read_csv(ae_result_path)
    as_df = pd.read_csv(as_result_path)
    
    print(f"AE预测结果: {len(ae_df)} 条")
    print(f"AS预测结果: {len(as_df)} 条")
    
    # 检查列名
    print(f"AE列名: {ae_df.columns.tolist()}")
    print(f"AS列名: {as_df.columns.tolist()}")
    
    # 假设有filename和predicted_label列
    if 'filename' in ae_df.columns and 'predicted_label' in ae_df.columns:
        # 合并两个数据框
        merged_df = pd.merge(ae_df, as_df, on='filename', suffixes=('_ae', '_as'))
        
        # 找出预测不一致的样本
        inconsistent_mask = merged_df['predicted_label_ae'] != merged_df['predicted_label_as']
        inconsistent_samples = merged_df[inconsistent_mask].copy()
        
        print(f"总样本数: {len(merged_df)}")
        print(f"不一致样本数: {len(inconsistent_samples)}")
        print(f"不一致率: {len(inconsistent_samples)/len(merged_df)*100:.2f}%")
        
        if len(inconsistent_samples) > 0:
            # 保存不一致样本
            inconsistent_samples.to_csv('inconsistent_predictions.csv', index=False)
            print(f"不一致样本已保存到: inconsistent_predictions.csv")
            
            # 显示一些统计信息
            print("\n不一致样本的AE预测分布:")
            print(inconsistent_samples['predicted_label_ae'].value_counts().head(10))
            
            print("\n不一致样本的AS预测分布:")
            print(inconsistent_samples['predicted_label_as'].value_counts().head(10))
            
            # 创建适合AudioSet分析的格式
            audioset_analysis_data = []
            for _, row in inconsistent_samples.iterrows():
                # 构建完整的音频文件路径
                audio_file = f"TAU-urban-acoustic-scenes-2019-development/audio/{row['filename']}"
                if os.path.exists(audio_file):
                    audioset_analysis_data.append({
                        'filename': row['filename'],
                        'audio_path': audio_file,
                        'ae_prediction': row['predicted_label_ae'],
                        'as_prediction': row['predicted_label_as'],
                        'true_label': row.get('true_label_ae', row.get('true_label', 'unknown'))
                    })
            
            # 保存AudioSet分析用的数据
            audioset_df = pd.DataFrame(audioset_analysis_data)
            audioset_df.to_csv('inconsistent_samples_for_audioset.csv', index=False)
            print(f"AudioSet分析数据已保存到: inconsistent_samples_for_audioset.csv")
            print(f"有效音频文件数: {len(audioset_df)}")
            
            return audioset_df
        else:
            print("没有找到不一致的样本")
            return None
    else:
        print("预测结果文件格式不符合预期")
        return None

if __name__ == "__main__":
    result = compare_predictions()
