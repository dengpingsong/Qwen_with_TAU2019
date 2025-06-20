#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
结果管理器 - 按时间戳分类保存和整理实验结果
Created on 2025-06-20
"""

import os
import json
import pickle
import shutil
import glob
from datetime import datetime
import pandas as pd
from pathlib import Path

class ResultManager:
    """结果管理器，按时间戳分类保存结果"""
    
    def __init__(self, base_dir="experiment_results", project_name="Qwen_TAU2019"):
        self.base_dir = base_dir
        self.project_name = project_name
        self.timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.output_dir = os.path.join(base_dir, project_name, self.timestamp)
        os.makedirs(self.output_dir, exist_ok=True)
        
        # 创建运行日志
        self.log_file = os.path.join(self.output_dir, "run_log.txt")
        self._log(f"开始运行: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self._log(f"输出目录: {self.output_dir}")
    
    def _log(self, message):
        """写入日志"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(f"[{timestamp}] {message}\n")
        print(f"[{timestamp}] {message}")
    
    def save_text(self, content, filename):
        """保存文本文件"""
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        self._log(f"保存文本文件: {filename}")
        return filepath
    
    def save_json(self, data, filename):
        """保存JSON文件"""
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        self._log(f"保存JSON文件: {filename}")
        return filepath
    
    def save_pickle(self, data, filename):
        """保存pickle文件"""
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'wb') as f:
            pickle.dump(data, f)
        self._log(f"保存pickle文件: {filename}")
        return filepath
    
    def save_csv(self, data, filename):
        """保存CSV文件"""
        filepath = os.path.join(self.output_dir, filename)
        if isinstance(data, pd.DataFrame):
            data.to_csv(filepath, index=False, encoding='utf-8')
        else:
            pd.DataFrame(data).to_csv(filepath, index=False, encoding='utf-8')
        self._log(f"保存CSV文件: {filename}")
        return filepath
    
    def save_model(self, model, filename):
        """保存模型文件"""
        filepath = os.path.join(self.output_dir, filename)
        import torch
        if hasattr(model, 'state_dict'):
            torch.save(model.state_dict(), filepath)
        else:
            torch.save(model, filepath)
        self._log(f"保存模型文件: {filename}")
        return filepath
    
    def save_figure(self, fig, filename, dpi=300):
        """保存图片文件"""
        filepath = os.path.join(self.output_dir, filename)
        fig.savefig(filepath, dpi=dpi, bbox_inches='tight')
        self._log(f"保存图片文件: {filename}")
        return filepath
    
    def copy_file(self, source_path, new_name=None):
        """复制文件到结果目录"""
        if not os.path.exists(source_path):
            self._log(f"警告: 源文件不存在 {source_path}")
            return None
        
        filename = new_name or os.path.basename(source_path)
        dest_path = os.path.join(self.output_dir, filename)
        
        shutil.copy2(source_path, dest_path)
        self._log(f"复制文件: {filename}")
        return dest_path
    
    def create_experiment_summary(self, model_name, accuracy, other_metrics=None):
        """创建实验摘要"""
        summary = {
            "experiment_info": {
                "model_name": model_name,
                "timestamp": self.timestamp,
                "output_directory": self.output_dir
            },
            "performance_metrics": {
                "accuracy": accuracy,
                **(other_metrics or {})
            },
            "run_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        self.save_json(summary, "experiment_summary.json")
        
        # 也保存为文本格式
        summary_text = f"""
实验摘要
========================================
模型名称: {model_name}
运行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
输出目录: {self.output_dir}

性能指标:
- 准确率: {accuracy}
"""
        if other_metrics:
            for key, value in other_metrics.items():
                summary_text += f"- {key}: {value}\n"
        
        self.save_text(summary_text, "experiment_summary.txt")
        return summary
    
    def finish(self, summary=None):
        """结束运行，保存摘要"""
        end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._log(f"运行结束: {end_time}")
        
        if summary:
            self.save_text(summary, "run_summary.txt")
        
        self._log(f"所有结果已保存到: {self.output_dir}")
        return self.output_dir

def organize_existing_files(workspace_dir="/Users/apple/Documents/Qwen_with_TAU2019"):
    """整理现有的结果文件"""
    print("开始整理现有文件...")
    
    # 创建存档目录
    archive_dir = os.path.join(workspace_dir, "archived_results")
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    archive_path = os.path.join(archive_dir, f"archive_{current_time}")
    os.makedirs(archive_path, exist_ok=True)
    
    # 定义要整理的文件类型
    file_patterns = [
        "*.csv", "*.txt", "*.png", "*.json", "*.pth", 
        "*report*", "*results*", "*confusion*", "*accuracy*",
        "*performance*", "*summary*", "*analysis*"
    ]
    
    moved_files = []
    
    for pattern in file_patterns:
        files = glob.glob(os.path.join(workspace_dir, pattern))
        for file_path in files:
            # 跳过脚本文件和新创建的管理文件
            filename = os.path.basename(file_path)
            if (filename.endswith('.py') or 
                filename == 'result_manager.py' or
                'archived_results' in file_path):
                continue
            
            # 移动文件到存档目录
            dest_path = os.path.join(archive_path, filename)
            try:
                shutil.move(file_path, dest_path)
                moved_files.append((file_path, dest_path))
                print(f"移动: {filename} -> {archive_path}")
            except Exception as e:
                print(f"移动失败 {filename}: {e}")
    
    # 创建整理日志
    log_content = f"""文件整理日志
==========================================
整理时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
存档目录: {archive_path}
移动文件数量: {len(moved_files)}

移动的文件:
"""
    
    for original, new in moved_files:
        log_content += f"- {os.path.basename(original)}\n"
    
    with open(os.path.join(archive_path, "organize_log.txt"), 'w', encoding='utf-8') as f:
        f.write(log_content)
    
    print(f"\n整理完成！共移动 {len(moved_files)} 个文件到: {archive_path}")
    return archive_path

def create_timestamped_output_dir(base_output_dir="results"):
    """创建按时间戳命名的输出目录（兼容函数）"""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_dir = os.path.join(base_output_dir, timestamp)
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

if __name__ == "__main__":
    # 整理现有文件
    organize_existing_files()
    
    # 演示结果管理器的使用
    print("\n演示结果管理器...")
    rm = ResultManager()
    
    # 模拟保存一些结果
    rm.save_text("这是一个测试实验", "test_experiment.txt")
    rm.create_experiment_summary("Test_Model", 0.95, {"precision": 0.92, "recall": 0.89})
    
    rm.finish("测试完成")
