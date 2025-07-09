#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速测试脚本
用于验证整合后的脚本是否正常工作
Created on 2025-07-03
"""

import sys
import subprocess
from pathlib import Path
from config import FEATURE_TYPES, CLASSIFIER_PARAMS, DATA_PATHS

def test_config():
    """测试配置文件"""
    print("🔧 测试配置文件...")
    
    print(f"支持的特征类型: {list(FEATURE_TYPES.keys())}")
    print(f"支持的分类器: {list(CLASSIFIER_PARAMS.keys())}")
    print(f"数据路径配置: {DATA_PATHS}")
    
    # 检查路径是否存在
    audio_path = Path(DATA_PATHS['audio_folder'])
    meta_path = Path(DATA_PATHS['meta_csv'])
    
    if audio_path.exists():
        print(f"✅ 音频文件夹存在: {audio_path}")
        audio_count = len(list(audio_path.glob("*.wav")))
        print(f"   找到 {audio_count} 个音频文件")
    else:
        print(f"❌ 音频文件夹不存在: {audio_path}")
    
    if meta_path.exists():
        print(f"✅ 元数据文件存在: {meta_path}")
    else:
        print(f"❌ 元数据文件不存在: {meta_path}")
    
    print()

def test_scripts():
    """测试脚本语法"""
    print("📝 测试脚本语法...")
    
    scripts = [
        "extract_features.py",
        "train_classifier.py", 
        "run_experiments.py",
        "config.py"
    ]
    
    for script in scripts:
        if Path(script).exists():
            try:
                # 测试语法
                result = subprocess.run([sys.executable, "-m", "py_compile", script], 
                                      capture_output=True, text=True)
                if result.returncode == 0:
                    print(f"✅ {script} 语法正确")
                else:
                    print(f"❌ {script} 语法错误:")
                    print(f"   {result.stderr}")
            except Exception as e:
                print(f"❌ 测试 {script} 时出错: {e}")
        else:
            print(f"❌ 脚本不存在: {script}")
    
    print()

def test_help():
    """测试帮助信息"""
    print("❓ 测试帮助信息...")
    
    scripts = [
        "extract_features.py",
        "train_classifier.py",
        "run_experiments.py"
    ]
    
    for script in scripts:
        if Path(script).exists():
            try:
                result = subprocess.run([sys.executable, script, "--help"], 
                                      capture_output=True, text=True, timeout=10)
                if result.returncode == 0:
                    print(f"✅ {script} 帮助信息正常")
                else:
                    print(f"❌ {script} 帮助信息错误")
            except subprocess.TimeoutExpired:
                print(f"⏰ {script} 超时")
            except Exception as e:
                print(f"❌ 测试 {script} 帮助时出错: {e}")
    
    print()

def test_imports():
    """测试导入"""
    print("📦 测试模块导入...")
    
    try:
        import config
        print("✅ config 模块导入成功")
        
        # 测试配置访问
        feature_types = list(config.FEATURE_TYPES.keys())
        print(f"   特征类型: {feature_types}")
        
        classifiers = list(config.CLASSIFIER_PARAMS.keys())
        print(f"   分类器: {classifiers}")
        
    except Exception as e:
        print(f"❌ config 模块导入失败: {e}")
    
    print()

def main():
    """主函数"""
    print("🚀 开始测试整合后的脚本...")
    print("=" * 50)
    
    test_config()
    test_imports()
    test_scripts()
    test_help()
    
    print("=" * 50)
    print("✨ 测试完成!")
    print("\n📋 快速使用指南:")
    print("1. 提取特征: python extract_features.py --mode AE")
    print("2. 训练分类器: python train_classifier.py --feature_type AE --classifier svm")
    print("3. 完整实验: python run_experiments.py --mode single")
    print("4. 批量实验: python run_experiments.py --mode batch")

if __name__ == "__main__":
    main()
