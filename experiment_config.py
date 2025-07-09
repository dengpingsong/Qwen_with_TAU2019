#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
实验配置管理器
统一管理所有实验的配置参数
Created on 2025-07-03
"""

import torch.optim as optim
from torch.optim.lr_scheduler import CosineAnnealingLR, StepLR
from typing import Dict, Any, Optional
import json
from pathlib import Path


class ExperimentConfig:
    """实验配置管理器"""
    
    # 默认配置
    DEFAULT_CONFIGS = {
        # 特征提取配置
        'feature_extraction': {
            'model_name': "Qwen/Qwen2-Audio-7B-Instruct",
            'batch_size': 1000,
            'max_new_tokens': 64,
            'audio_sr': None,  # 使用模型默认采样率
            'output_folder': "./new_Feature"
        },
        
        # 分类训练配置
        'classification': {
            'training_sample_size': 2000,
            'test_size': 0.2,
            'random_state': 42,
            'batch_size': 200,
            'pca_components': 0.95,
            'classifiers': {
                'svm': {
                    'kernel': 'linear',
                    'C': 1.0
                },
                'random_forest': {
                    'n_estimators': 100,
                    'random_state': 42
                },
                'logistic_regression': {
                    'random_state': 42,
                    'max_iter': 1000
                }
            }
        },
        
        # 神经网络训练配置
        'neural_network': {
            'batch_size': 64,
            'learning_rate': 0.001,
            'max_epochs': 500,
            'early_stopping_patience': 15,
            'weight_decay': 1e-4,
            'lr_early_stop': True,
            'lr_threshold': 1e-5,
            'val_acc_early_stop': True,
            'val_acc_patience': 50,
            'progress_interval': 5
        },
        
        # 学习率调度器配置
        'scheduler': {
            'cosine': {
                'T_max': 100,
                'eta_min': 1e-6
            },
            'step': {
                'step_size': 10,
                'gamma': 0.5
            }
        },
        
        # 数据路径配置
        'data_paths': {
            'audio_folder': "./TAU-urban-acoustic-scenes-2019-development/audio",
            'meta_csv': "./TAU-urban-acoustic-scenes-2019-development/meta.csv",
            'feature_folder': "./new_Feature",
            'results_folder': "./experiment_results"
        },
        
        # 特征类型配置
        'feature_types': {
            'AE': {
                'suffix': 'AE',
                'description': 'Audio Event features',
                'prompt': "You need to analysis audio event, whether this audio have Audio Event."
            },
            'AS': {
                'suffix': 'AS',
                'description': 'Acoustic Scene features',
                'prompt': "You need to analysis acoustic scene, figure out which scene this audio belong to."
            },
            'bi': {
                'suffix': '_bi-scene',
                'description': 'Binary scene classification features',
                'prompt': "You need to separate audio into 2 parts, figure out whether audio recorded in the airport."
            },
            'clustering': {
                'suffix': '_clustering',
                'description': 'Clustering features',
                'prompt': "You need to analysis this audio for clustering purpose."
            },
            'general': {
                'suffix': '_general',
                'description': 'General audio features',
                'prompt': "Please analyze this audio file."
            }
        }
    }
    
    def __init__(self, config_file: Optional[str] = None):
        """
        初始化配置管理器
        
        Args:
            config_file: 配置文件路径，如果提供则从文件加载配置
        """
        self.config = self.DEFAULT_CONFIGS.copy()
        
        if config_file and Path(config_file).exists():
            self.load_from_file(config_file)
    
    def get(self, key: str, default: Any = None) -> Any:
        """获取配置值"""
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key: str, value: Any):
        """设置配置值"""
        keys = key.split('.')
        config = self.config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
    
    def update(self, updates: Dict[str, Any]):
        """批量更新配置"""
        def deep_update(base: dict, updates: dict):
            for key, value in updates.items():
                if isinstance(value, dict) and key in base and isinstance(base[key], dict):
                    deep_update(base[key], value)
                else:
                    base[key] = value
        
        deep_update(self.config, updates)
    
    def get_feature_config(self, feature_type: str) -> Dict[str, Any]:
        """获取特定特征类型的配置"""
        return self.get(f'feature_types.{feature_type}', {})
    
    def get_classifier_config(self, classifier_type: str) -> Dict[str, Any]:
        """获取特定分类器的配置"""
        return self.get(f'classification.classifiers.{classifier_type}', {})
    
    def get_extraction_config(self) -> Dict[str, Any]:
        """获取特征提取配置"""
        return self.get('feature_extraction', {})
    
    def get_classification_config(self) -> Dict[str, Any]:
        """获取分类训练配置"""
        return self.get('classification', {})
    
    def get_neural_network_config(self) -> Dict[str, Any]:
        """获取神经网络配置"""
        return self.get('neural_network', {})
    
    def get_data_paths(self) -> Dict[str, str]:
        """获取数据路径配置"""
        return self.get('data_paths', {})
    
    def create_optimizer(self, model_parameters, optimizer_type: str = 'adam'):
        """创建优化器"""
        nn_config = self.get_neural_network_config()
        lr = nn_config.get('learning_rate', 0.001)
        weight_decay = nn_config.get('weight_decay', 1e-4)
        
        if optimizer_type.lower() == 'adam':
            return optim.Adam(model_parameters, lr=lr, weight_decay=weight_decay)
        elif optimizer_type.lower() == 'sgd':
            return optim.SGD(model_parameters, lr=lr, weight_decay=weight_decay, momentum=0.9)
        elif optimizer_type.lower() == 'adamw':
            return optim.AdamW(model_parameters, lr=lr, weight_decay=weight_decay)
        else:
            raise ValueError(f"不支持的优化器类型: {optimizer_type}")
    
    def create_scheduler(self, optimizer, scheduler_type: str = 'cosine'):
        """创建学习率调度器"""
        scheduler_config = self.get('scheduler', {})
        
        if scheduler_type.lower() == 'cosine':
            config = scheduler_config.get('cosine', {})
            return CosineAnnealingLR(
                optimizer,
                T_max=config.get('T_max', 100),
                eta_min=config.get('eta_min', 1e-6)
            )
        elif scheduler_type.lower() == 'step':
            config = scheduler_config.get('step', {})
            return StepLR(
                optimizer,
                step_size=config.get('step_size', 10),
                gamma=config.get('gamma', 0.5)
            )
        else:
            raise ValueError(f"不支持的调度器类型: {scheduler_type}")
    
    def save_to_file(self, file_path: str):
        """保存配置到文件"""
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)
    
    def load_from_file(self, file_path: str):
        """从文件加载配置"""
        with open(file_path, 'r', encoding='utf-8') as f:
            file_config = json.load(f)
        
        self.update(file_config)
    
    def create_experiment_config(self, 
                               feature_type: str,
                               classifier_type: str,
                               custom_config: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """创建特定实验的配置"""
        config = {
            'feature_type': feature_type,
            'classifier_type': classifier_type,
            'feature_config': self.get_feature_config(feature_type),
            'classifier_config': self.get_classifier_config(classifier_type),
            'extraction_config': self.get_extraction_config(),
            'classification_config': self.get_classification_config(),
            'data_paths': self.get_data_paths()
        }
        
        if custom_config:
            config.update(custom_config)
        
        return config
    
    def print_config(self, section: Optional[str] = None):
        """打印配置信息"""
        if section:
            config_to_print = self.get(section, {})
            print(f"\n=== {section.upper()} 配置 ===")
        else:
            config_to_print = self.config
            print("\n=== 完整配置 ===")
        
        print(json.dumps(config_to_print, indent=2, ensure_ascii=False))


# 全局配置实例
global_config = ExperimentConfig()


def get_config() -> ExperimentConfig:
    """获取全局配置实例"""
    return global_config


def load_config(config_file: str) -> ExperimentConfig:
    """加载配置文件"""
    return ExperimentConfig(config_file)


# 便捷函数
def get_feature_types() -> list:
    """获取所有支持的特征类型"""
    return list(global_config.get('feature_types', {}).keys())


def get_classifier_types() -> list:
    """获取所有支持的分类器类型"""
    return list(global_config.get('classification.classifiers', {}).keys())


def get_data_path(key: str) -> str:
    """获取数据路径"""
    return global_config.get(f'data_paths.{key}', '')


if __name__ == "__main__":
    # 示例用法
    config = ExperimentConfig()
    
    # 打印配置
    config.print_config('feature_extraction')
    config.print_config('classification')
    
    # 获取特定配置
    print("\n支持的特征类型:", get_feature_types())
    print("支持的分类器类型:", get_classifier_types())
    
    # 创建实验配置
    exp_config = config.create_experiment_config('AE', 'svm')
    print("\n实验配置示例:")
    print(json.dumps(exp_config, indent=2, ensure_ascii=False))
