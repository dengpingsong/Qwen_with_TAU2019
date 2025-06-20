#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的音频分类网络架构定义
Created on 2025-06-20
"""

import torch
import torch.nn as nn
from torch.utils.data import Dataset

class AudioClassificationNet(nn.Module):
    """
    单层全连接音频分类网络
    适用于AE、AS和融合特征的分类任务
    """
    
    def __init__(self, input_dim, num_classes):
        super(AudioClassificationNet, self).__init__()
        # 单层全连接网络：直接从输入到输出
        self.network = nn.Linear(input_dim, num_classes)
    
    def forward(self, x):
        return self.network(x)

class AudioFeatureDataset(Dataset):
    """
    统一的音频特征数据集类
    """
    
    def __init__(self, features, labels):
        self.features = torch.FloatTensor(features)
        self.labels = torch.LongTensor(labels)
    
    def __len__(self):
        return len(self.features)
    
    def __getitem__(self, idx):
        return self.features[idx], self.labels[idx]

if __name__ == "__main__":
    # 测试网络
    model = AudioClassificationNet(input_dim=1000, num_classes=10)
    test_input = torch.randn(32, 1000)
    output = model(test_input)
    print(f"输入形状: {test_input.shape}")
    print(f"输出形状: {output.shape}")
    print(f"参数数量: {sum(p.numel() for p in model.parameters()):,}")
