#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
结果管理系统测试脚本
"""

from result_manager import ResultManager
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_result_manager():
    """测试结果管理器的各种功能"""
    
    print("🧪 开始测试结果管理系统...")
    
    # 创建结果管理器
    rm = ResultManager(project_name="Test_Classification")
    rm._log("开始测试实验")
    
    # 模拟一些实验数据
    test_data = {
        'epoch': [1, 2, 3, 4, 5],
        'accuracy': [0.82, 0.87, 0.91, 0.94, 0.95],
        'loss': [0.45, 0.32, 0.21, 0.15, 0.12]
    }
    
    # 1. 保存CSV文件
    df = pd.DataFrame(test_data)
    rm.save_csv(df, "training_history.csv")
    
    # 2. 保存JSON配置
    config = {
        "model_type": "CNN",
        "learning_rate": 0.001,
        "batch_size": 32,
        "epochs": 5
    }
    rm.save_json(config, "experiment_config.json")
    
    # 3. 创建并保存图表
    plt.figure(figsize=(10, 6))
    plt.subplot(1, 2, 1)
    plt.plot(test_data['epoch'], test_data['accuracy'], 'b-', marker='o')
    plt.title('Accuracy over Epochs')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.grid(True)
    
    plt.subplot(1, 2, 2)
    plt.plot(test_data['epoch'], test_data['loss'], 'r-', marker='s')
    plt.title('Loss over Epochs')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.grid(True)
    
    plt.tight_layout()
    rm.save_figure(plt.gcf(), "training_curves.png")
    plt.close()
    
    # 4. 保存文本日志
    log_content = """
测试实验日志
==============
开始时间: 2025-06-20 13:15:00
模型类型: CNN测试模型
数据集: 模拟数据

训练过程:
- Epoch 1: Acc=0.82, Loss=0.45
- Epoch 2: Acc=0.87, Loss=0.32
- Epoch 3: Acc=0.91, Loss=0.21
- Epoch 4: Acc=0.94, Loss=0.15
- Epoch 5: Acc=0.95, Loss=0.12

结论: 模型训练成功，达到95%准确率
"""
    rm.save_text(log_content, "test_experiment_log.txt")
    
    # 5. 创建实验摘要
    rm.create_experiment_summary(
        model_name="Test_CNN_Model",
        accuracy=0.95,
        other_metrics={
            "final_loss": 0.12,
            "training_epochs": 5,
            "best_epoch": 5,
            "convergence_speed": "fast"
        }
    )
    
    # 6. 结束实验
    experiment_summary = """
测试实验完成！
- 成功测试了CSV保存功能
- 成功测试了JSON保存功能
- 成功测试了图表保存功能
- 成功测试了文本保存功能
- 成功创建了实验摘要
- 所有功能正常工作 ✅
"""
    
    output_dir = rm.finish(experiment_summary)
    
    print("✅ 测试完成！")
    print(f"📁 结果保存在: {output_dir}")
    print("\n生成的文件:")
    print("- training_history.csv")
    print("- experiment_config.json") 
    print("- training_curves.png")
    print("- test_experiment_log.txt")
    print("- experiment_summary.json")
    print("- experiment_summary.txt")
    print("- run_log.txt")
    print("- run_summary.txt")
    
    return output_dir

if __name__ == "__main__":
    test_result_manager()
