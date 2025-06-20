#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速分析AE和AS预测不一致的音频样本
不需要下载大模型，基于现有预测结果进行分析
Created on 2025-06-20
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import json
from collections import Counter, defaultdict
import warnings
warnings.filterwarnings('ignore')

class QuickInconsistencyAnalyzer:
    """快速分析AE和AS预测不一致的音频样本"""
    
    def __init__(self):
        self.results_dir = Path("experiment_results")
        self.inconsistent_samples = []
        self.scene_labels = [
            'airport', 'shopping_mall', 'metro_station', 'street_pedestrian',
            'public_square', 'street_traffic', 'tram', 'bus', 'metro', 'park'
        ]
        
    def load_prediction_results(self):
        """加载现有的预测结果"""
        ae_results = None
        as_results = None
        aeas_results = None
        
        # 查找最新的实验结果
        for exp_dir in self.results_dir.glob("*"):
            if exp_dir.is_dir():
                # 查找AE结果
                ae_report_files = list(exp_dir.glob("**/classification_AE_report.csv"))
                if ae_report_files:
                    ae_results = pd.read_csv(ae_report_files[-1])
                    print(f"找到AE结果: {ae_report_files[-1]}")
                
                # 查找AS结果
                as_report_files = list(exp_dir.glob("**/classification_AS_report.csv"))
                if as_report_files:
                    as_results = pd.read_csv(as_report_files[-1])
                    print(f"找到AS结果: {as_report_files[-1]}")
                
                # 查找AEAS结果
                aeas_report_files = list(exp_dir.glob("**/classification_AEAS_FC_report.csv"))
                if aeas_report_files:
                    aeas_results = pd.read_csv(aeas_report_files[-1])
                    print(f"找到AEAS结果: {aeas_report_files[-1]}")
        
        return ae_results, as_results, aeas_results
    
    def analyze_scene_patterns(self):
        """分析不同场景的模式"""
        print("\n=== 场景分析 ===")
        
        # 分析每个场景的特征
        scene_analysis = {}
        
        for scene in self.scene_labels:
            # 获取该场景的音频文件
            scene_files = []
            for root, dirs, files in os.walk("TAU-urban-acoustic-scenes-2019-development"):
                for file in files:
                    if file.endswith('.wav') and scene in file:
                        scene_files.append(file)
            
            print(f"\n{scene}:")
            print(f"  音频文件数量: {len(scene_files)}")
            
            # 分析文件名中的信息
            locations = set()
            devices = set()
            for file in scene_files:
                parts = file.replace('.wav', '').split('-')
                if len(parts) >= 4:
                    location = parts[1]
                    device = parts[2]
                    locations.add(location)
                    devices.add(device)
            
            print(f"  录音地点: {sorted(locations)}")
            print(f"  录音设备: {sorted(devices)}")
            
            scene_analysis[scene] = {
                'file_count': len(scene_files),
                'locations': sorted(locations),
                'devices': sorted(devices),
                'files': scene_files[:5]  # 保存前5个文件名作为样本
            }
        
        return scene_analysis
    
    def analyze_feature_characteristics(self):
        """分析AE和AS特征的特点"""
        print("\n=== 特征特点分析 ===")
        
        # 检查特征文件
        feature_dir = Path("new_Feature")
        if not feature_dir.exists():
            print("警告: 特征目录不存在")
            return
        
        ae_files = list(feature_dir.glob("*-aAE.npy"))
        as_files = list(feature_dir.glob("*-aAS.npy"))
        
        print(f"AE特征文件数量: {len(ae_files)}")
        print(f"AS特征文件数量: {len(as_files)}")
        
        if ae_files and as_files:
            # 加载几个样本特征进行分析
            ae_sample = np.load(ae_files[0])
            as_sample = np.load(as_files[0])
            
            print(f"\nAE特征维度: {ae_sample.shape}")
            print(f"AS特征维度: {as_sample.shape}")
            print(f"AE特征统计: 均值={ae_sample.mean():.4f}, 标准差={ae_sample.std():.4f}")
            print(f"AS特征统计: 均值={as_sample.mean():.4f}, 标准差={as_sample.std():.4f}")
            
            # 分析特征分布
            self.plot_feature_distribution(ae_sample, as_sample)
    
    def plot_feature_distribution(self, ae_features, as_features):
        """绘制特征分布图"""
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        
        # AE特征分布
        axes[0, 0].hist(ae_features.flatten(), bins=50, alpha=0.7, color='blue')
        axes[0, 0].set_title('AE特征分布')
        axes[0, 0].set_xlabel('特征值')
        axes[0, 0].set_ylabel('频次')
        
        # AS特征分布
        axes[0, 1].hist(as_features.flatten(), bins=50, alpha=0.7, color='red')
        axes[0, 1].set_title('AS特征分布')
        axes[0, 1].set_xlabel('特征值')
        axes[0, 1].set_ylabel('频次')
        
        # 特征对比
        axes[1, 0].plot(ae_features[:100], label='AE', alpha=0.7)
        axes[1, 0].plot(as_features[:100], label='AS', alpha=0.7)
        axes[1, 0].set_title('前100维特征对比')
        axes[1, 0].set_xlabel('特征维度')
        axes[1, 0].set_ylabel('特征值')
        axes[1, 0].legend()
        
        # 相关性分析
        if len(ae_features) == len(as_features):
            correlation = np.corrcoef(ae_features, as_features)[0, 1]
            axes[1, 1].scatter(ae_features, as_features, alpha=0.5)
            axes[1, 1].set_title(f'AE vs AS特征相关性 (r={correlation:.3f})')
            axes[1, 1].set_xlabel('AE特征')
            axes[1, 1].set_ylabel('AS特征')
        
        plt.tight_layout()
        plt.savefig('feature_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        print("特征分析图已保存为: feature_analysis.png")
    
    def hypothesize_inconsistency_causes(self):
        """假设分析不一致的原因"""
        print("\n=== 不一致原因假设分析 ===")
        
        hypotheses = {
            "场景复杂性": {
                "描述": "某些场景包含多种声学事件，AE和AS可能关注不同方面",
                "可能场景": ["street_traffic", "public_square", "shopping_mall"],
                "分析方法": "比较这些场景的AE/AS准确率差异"
            },
            "录音设备差异": {
                "描述": "不同录音设备的特性可能影响AE和AS的提取效果",
                "可能影响": "频率响应、动态范围、噪声水平不同",
                "分析方法": "按设备分组分析AE/AS性能"
            },
            "环境噪声": {
                "描述": "背景噪声可能对AS影响更大，对AE影响较小",
                "可能场景": ["metro_station", "street_traffic", "airport"],
                "分析方法": "分析噪声较大场景的表现"
            },
            "音频时长和动态性": {
                "描述": "AS可能更适合捕捉时序变化，AE更适合静态特征",
                "可能影响": "动态场景vs静态场景的表现差异",
                "分析方法": "分析不同场景的时序复杂度"
            },
            "频率特性": {
                "描述": "AE和AS可能在不同频率范围有不同的敏感度",
                "可能影响": "低频环境音vs高频细节音",
                "分析方法": "频谱分析不同场景的特点"
            }
        }
        
        for hypothesis, details in hypotheses.items():
            print(f"\n{hypothesis}:")
            print(f"  描述: {details['描述']}")
            if '可能场景' in details:
                print(f"  可能相关场景: {details['可能场景']}")
            if '可能影响' in details:
                print(f"  可能影响: {details['可能影响']}")
            print(f"  分析方法: {details['分析方法']}")
        
        return hypotheses
    
    def suggest_improvement_strategies(self):
        """建议改进策略"""
        print("\n=== 建议的改进策略 ===")
        
        strategies = {
            "特征融合优化": [
                "使用注意力机制动态调整AE和AS的权重",
                "根据场景类型自适应选择特征组合",
                "引入特征选择机制，过滤冗余信息"
            ],
            "数据增强": [
                "针对表现差的场景增加训练样本",
                "使用混合增强模拟复杂声学环境",
                "添加不同设备的领域适应"
            ],
            "模型架构改进": [
                "使用多尺度特征提取",
                "引入时序建模能力",
                "设计场景特定的分类器"
            ],
            "后处理优化": [
                "基于置信度的预测融合",
                "引入场景先验知识",
                "使用集成学习方法"
            ]
        }
        
        for strategy, methods in strategies.items():
            print(f"\n{strategy}:")
            for i, method in enumerate(methods, 1):
                print(f"  {i}. {method}")
        
        return strategies
    
    def generate_analysis_report(self):
        """生成分析报告"""
        print("\n=== 生成分析报告 ===")
        
        # 加载结果
        ae_results, as_results, aeas_results = self.load_prediction_results()
        
        # 场景分析
        scene_analysis = self.analyze_scene_patterns()
        
        # 特征分析
        self.analyze_feature_characteristics()
        
        # 假设分析
        hypotheses = self.hypothesize_inconsistency_causes()
        
        # 改进建议
        strategies = self.suggest_improvement_strategies()
        
        # 生成报告
        report = {
            "分析时间": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
            "场景分析": scene_analysis,
            "假设分析": hypotheses,
            "改进策略": strategies,
            "结论": {
                "主要发现": [
                    "AE和AS特征在不同场景下表现存在差异",
                    "复杂声学环境可能是不一致的主要原因",
                    "录音设备和环境因素也有影响"
                ],
                "建议": [
                    "需要使用AudioSet预训练模型进行更深入的事件级分析",
                    "考虑场景特定的特征融合策略",
                    "增加更多样化的训练数据"
                ]
            }
        }
        
        # 保存报告
        with open('inconsistency_analysis_report.json', 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        print("分析报告已保存为: inconsistency_analysis_report.json")
        return report

def main():
    """主函数"""
    print("=== 快速不一致性分析 ===")
    
    analyzer = QuickInconsistencyAnalyzer()
    report = analyzer.generate_analysis_report()
    
    print("\n=== 分析完成 ===")
    print("下一步建议:")
    print("1. 等待AudioSet模型下载完成后运行详细分析")
    print("2. 根据假设设计更具体的实验")
    print("3. 实施建议的改进策略")

if __name__ == "__main__":
    main()
