#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简化的配置文件
实验的基本参数设置
Created on 2025-07-03
"""

# 数据路径配置
DATA_PATHS = {
    'audio_folder': "./TAU-urban-acoustic-scenes-2019-development/audio",
    'meta_csv': "./TAU-urban-acoustic-scenes-2019-development/meta.csv", 
    'feature_folder': "./new_Feature",
    'results_folder': "./results"
}

# 特征提取配置
FEATURE_CONFIG = {
    'model_name': "Qwen/Qwen2-Audio-7B-Instruct",
    'max_new_tokens': 64,
    'batch_size': 1000
}

# 分类训练配置
TRAIN_CONFIG = {
    'training_sample_size': 2000,
    'test_size': 0.2,
    'random_state': 42,
    'batch_size': 200,
    'pca_components': 0.95
}

# 分类器参数
CLASSIFIER_PARAMS = {
    'svm': {
        'kernel': 'linear',
        'C': 1.0
    },
    'rf': {
        'n_estimators': 100,
        'random_state': 42
    },
    'lr': {
        'random_state': 42,
        'max_iter': 1000
    }
}

# 特征类型配置
FEATURE_TYPES = {
    'AE': {
        'suffix': 'AE',
        'prompt': "You need to analysis audio event, whether this audio have Audio Event."
    },
    'AS': {
        'suffix': 'AS', 
        'prompt': "You need to analysis acoustic scene, figure out which scene this audio belong to."
    },
    'bi': {
        'suffix': '_bi-scene',
        'prompt': "You need to separate audio into 2 parts, figure out whether audio recorded in the airport."
    },
    'clustering': {
        'suffix': '_clustering',
        'prompt': "You need to analysis this audio for clustering purpose."
    },
    'general': {
        'suffix': '_general',
        'prompt': "Please analyze this audio file."
    }
}

# 支持的选项
SUPPORTED_FEATURES = list(FEATURE_TYPES.keys())
SUPPORTED_CLASSIFIERS = list(CLASSIFIER_PARAMS.keys())

# 便捷函数
def get_feature_suffix(feature_type):
    """获取特征文件后缀"""
    return FEATURE_TYPES.get(feature_type, {}).get('suffix', feature_type)

def get_feature_prompt(feature_type):
    """获取特征提取提示词"""
    return FEATURE_TYPES.get(feature_type, {}).get('prompt', "Please analyze this audio file.")

def get_classifier_params(classifier_type):
    """获取分类器参数"""
    return CLASSIFIER_PARAMS.get(classifier_type, {})
