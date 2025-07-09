#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简化的批量实验运行脚本
Created on 2025-07-03
"""

import subprocess
import sys
import time
import argparse
from pathlib import Path
from config import FEATURE_TYPES, CLASSIFIER_PARAMS, DATA_PATHS


def run_command(cmd, description):
    """运行命令并返回结果"""
    print(f"\n{'='*50}")
    print(f"运行: {description}")
    print(f"命令: {' '.join(cmd)}")
    print(f"{'='*50}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✓ {description} 成功完成")
            return True
        else:
            print(f"✗ {description} 失败")
            if result.stderr:
                print(f"错误: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"✗ 运行 {description} 时出错: {e}")
        return False


def extract_features(feature_type, audio_folder=None, output_folder=None):
    """提取特征"""
    audio_folder = audio_folder or DATA_PATHS['audio_folder']
    output_folder = output_folder or DATA_PATHS['feature_folder']
    cmd = [
        sys.executable, "extract_features.py",
        "--mode", feature_type,
        "--audio_folder", audio_folder,
        "--output_folder", output_folder
    ]
    
    return run_command(cmd, f"提取 {feature_type} 特征")


def train_classifier(feature_type, classifier_type, data_dir=None,
                    csv_path=None, output_dir=None):
    """训练分类器"""
    data_dir = data_dir or DATA_PATHS['feature_folder']
    csv_path = csv_path or DATA_PATHS['meta_csv']
    output_dir = output_dir or DATA_PATHS['results_folder']
    output_dir = f"{output_dir}/{feature_type}_{classifier_type}"
    
    cmd = [
        sys.executable, "train_classifier.py",
        "--feature_type", feature_type,
        "--classifier", classifier_type,
        "--data_dir", data_dir,
        "--csv_path", csv_path,
        "--output_dir", output_dir
    ]
    
    return run_command(cmd, f"训练 {feature_type}+{classifier_type} 分类器")


def run_single_experiment(feature_type, classifier_type, extract_feat=True):
    """运行单个完整实验"""
    print(f"\n🚀 开始实验: {feature_type} + {classifier_type}")
    
    success = True
    
    # 特征提取
    if extract_feat:
        if not extract_features(feature_type):
            print(f"❌ {feature_type} 特征提取失败")
            return False
    
    # 分类训练
    if not train_classifier(feature_type, classifier_type):
        print(f"❌ {feature_type}+{classifier_type} 分类训练失败")
        return False
    
    print(f"✅ 实验 {feature_type}+{classifier_type} 成功完成")
    return True


def run_batch_experiments(feature_types, classifier_types, extract_features_once=True):
    """批量运行实验"""
    total = len(feature_types) * len(classifier_types)
    current = 0
    success_count = 0
    
    print(f"🎯 开始批量实验")
    print(f"特征类型: {feature_types}")
    print(f"分类器类型: {classifier_types}")
    print(f"总实验数: {total}")
    
    start_time = time.time()
    
    for i, feature_type in enumerate(feature_types):
        for j, classifier_type in enumerate(classifier_types):
            current += 1
            
            print(f"\n📊 实验 {current}/{total}: {feature_type}_{classifier_type}")
            
            # 只在第一个分类器时提取特征
            should_extract = extract_features_once and (j == 0)
            
            if run_single_experiment(feature_type, classifier_type, should_extract):
                success_count += 1
    
    # 总结
    end_time = time.time()
    total_time = end_time - start_time
    
    print(f"\n{'='*60}")
    print(f"📈 批量实验完成总结")
    print(f"{'='*60}")
    print(f"总耗时: {total_time:.1f} 秒")
    print(f"成功实验: {success_count}/{total}")
    print(f"成功率: {success_count/total*100:.1f}%")
    
    return success_count == total


def main():
    parser = argparse.ArgumentParser(description="批量实验运行器")
    
    parser.add_argument("--mode", choices=["extract", "train", "single", "batch"],
                       default="single", help="运行模式")
    
    parser.add_argument("--feature_types", nargs='+', 
                       choices=list(FEATURE_TYPES.keys()),
                       default=["AE"], help="特征类型")
    
    parser.add_argument("--classifiers", nargs='+',
                       choices=list(CLASSIFIER_PARAMS.keys()),
                       default=["svm"], help="分类器类型")
    
    parser.add_argument("--audio_folder", 
                       default=DATA_PATHS['audio_folder'],
                       help="音频文件夹")
    
    parser.add_argument("--feature_folder", default=DATA_PATHS['feature_folder'],
                       help="特征文件夹")
    
    parser.add_argument("--csv_path",
                       default=DATA_PATHS['meta_csv'],
                       help="元数据文件")
    
    parser.add_argument("--output_dir", default=DATA_PATHS['results_folder'],
                       help="结果输出目录")
    
    args = parser.parse_args()
    
    if args.mode == "extract":
        # 只提取特征
        for feature_type in args.feature_types:
            extract_features(feature_type, args.audio_folder, args.feature_folder)
    
    elif args.mode == "train":
        # 只训练分类器
        for feature_type in args.feature_types:
            for classifier in args.classifiers:
                train_classifier(feature_type, classifier, args.feature_folder, 
                               args.csv_path, args.output_dir)
    
    elif args.mode == "single":
        # 运行单个实验
        feature_type = args.feature_types[0]
        classifier = args.classifiers[0]
        run_single_experiment(feature_type, classifier)
    
    elif args.mode == "batch":
        # 批量实验
        run_batch_experiments(args.feature_types, args.classifiers)


if __name__ == "__main__":
    main()
