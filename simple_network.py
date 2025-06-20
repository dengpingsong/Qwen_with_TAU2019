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
    统一的音频分类全连接网络
    适用于AE、AS和融合特征的分类任务
    """
    
    def __init__(self, input_dim, num_classes):
        super(AudioClassificationNet, self).__init__()
        self.network = nn.Sequential(
            # 第一层
            nn.Linear(input_dim, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(),
            nn.Dropout(0.3),
            
            # 第二层
            nn.Linear(1024, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Dropout(0.3),
            
            # 第三层
            nn.Linear(512, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(0.2),
            
            # 第四层
            nn.Linear(256, 128),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.Dropout(0.2),
            
            # 输出层
            nn.Linear(128, num_classes)
        )
    
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
