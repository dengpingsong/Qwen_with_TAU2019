#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
训练配置参数
Created on 2025-06-20
"""

import torch.optim as optim
from torch.optim.lr_scheduler import CosineAnnealingLR, StepLR

# 训练基本参数
TRAINING_CONFIG = {
    'batch_size': 64,
    'learning_rate': 0.001,
    'max_epochs': 500,  # 最大训练轮数，作为兜底限制
    'early_stopping_patience': 15,
    'weight_decay': 1e-4,
    # 基于学习率的早停（主要早停机制）
    'lr_early_stop': True,
    'lr_threshold': 1e-5,  # 当学习率降到这个值时停止训练
    # 基于验证准确率的早停（辅助早停机制）
    'val_acc_early_stop': True,
    'val_acc_patience': 20,  # 验证准确率不提升的容忍轮数
    # 显示进度频率
    'progress_interval': 5,  # 每5轮显示一次进度
}

# 数据参数
DATA_CONFIG = {
    'training_sample_size': 2000,
    'test_size': 0.2,
    'random_state': 42
}

# 学习率调度器配置
SCHEDULER_CONFIG = {
    # 余弦退火配置（推荐使用）
    'cosine': {
        'T_max': 100,  # 余弦退火周期
        'eta_min': 1e-6  # 最小学习率
    },
    
    # 阶梯式调整配置
    'step': {
        'step_size': 10,
        'gamma': 0.5
    }
}

def create_optimizer(model_parameters, config=None):
    """创建优化器"""
    if config is None:
        config = TRAINING_CONFIG
    
    return optim.Adam(
        model_parameters, 
        lr=config['learning_rate'],
        weight_decay=config.get('weight_decay', 1e-4)
    )

def create_scheduler(optimizer, scheduler_type='cosine'):
    """创建学习率调度器"""
    if scheduler_type == 'cosine':
        return CosineAnnealingLR(
            optimizer,
            T_max=SCHEDULER_CONFIG['cosine']['T_max'],
            eta_min=SCHEDULER_CONFIG['cosine']['eta_min']
        )
    elif scheduler_type == 'step':
        return StepLR(
            optimizer,
            step_size=SCHEDULER_CONFIG['step']['step_size'],
            gamma=SCHEDULER_CONFIG['step']['gamma']
        )
    else:
        raise ValueError(f"不支持的调度器类型: {scheduler_type}")

def get_learning_rate(optimizer):
    """获取当前学习率"""
    for param_group in optimizer.param_groups:
        return param_group['lr']

def should_early_stop(current_lr, val_acc_history, config=None):
    """
    判断是否应该早停
    
    Args:
        current_lr: 当前学习率
        val_acc_history: 验证准确率历史列表
        config: 配置字典
    
    Returns:
        (should_stop, reason): 是否停止和停止原因
    """
    if config is None:
        config = TRAINING_CONFIG
    
    # 基于学习率的早停
    if config.get('lr_early_stop', True):
        lr_threshold = config.get('lr_threshold', 1e-5)
        if current_lr <= lr_threshold:
            return True, f"学习率降至 {current_lr:.2e}，低于阈值 {lr_threshold:.2e}"
    
    # 基于验证准确率的早停
    if config.get('val_acc_early_stop', True) and len(val_acc_history) >= 2:
        patience = config.get('val_acc_patience', 20)
        if len(val_acc_history) > patience:
            # 检查最近patience轮是否有提升
            recent_max = max(val_acc_history[-patience:])
            best_overall = max(val_acc_history[:-patience]) if len(val_acc_history) > patience else 0
            
            if recent_max <= best_overall:
                return True, f"验证准确率连续 {patience} 轮未提升"
    
    return False, ""

def print_training_progress(epoch, total_epochs, train_loss, train_acc, val_acc, current_lr, best_val_acc):
    """打印训练进度"""
    progress = (epoch + 1) / total_epochs * 100
    print(f'Epoch [{epoch+1:3d}/{total_epochs}] ({progress:5.1f}%) | '
          f'Loss: {train_loss:.4f} | Train Acc: {train_acc:.4f} | '
          f'Val Acc: {val_acc:.4f} | Best: {best_val_acc:.4f} | LR: {current_lr:.2e}')

def print_training_summary(total_epochs_trained, max_epochs, best_val_acc, early_stop_reason=""):
    """打印训练总结"""
    print(f"\n{'='*50}")
    print(f"训练完成!")
    print(f"实际训练轮数: {total_epochs_trained}/{max_epochs}")
    print(f"最佳验证准确率: {best_val_acc:.4f}")
    if early_stop_reason:
        print(f"早停原因: {early_stop_reason}")
    else:
        print("训练完成原因: 达到最大训练轮数")
    print(f"{'='*50}")

def get_config_value(key, default=None):
    """获取配置值的便捷函数"""
    return TRAINING_CONFIG.get(key, default)
