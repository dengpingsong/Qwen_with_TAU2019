#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
音频场景分类训练器
支持多种特征类型和分类算法的统一训练脚本
Created on 2025-07-03
"""

import numpy as np
import pandas as pd
import os
import argparse
import pickle
import random
import gc
from pathlib import Path
from typing import List, Tuple, Dict, Optional, Any

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from tqdm import tqdm
import seaborn as sns
import matplotlib.pyplot as plt

try:
    from result_manager import ResultManager
    HAS_RESULT_MANAGER = True
except ImportError:
    HAS_RESULT_MANAGER = False
    print("Warning: result_manager not found, will use basic logging")


class AudioSceneClassifier:
    """音频场景分类器"""
    
    def __init__(self, 
                 feature_type: str = "AE",
                 classifier_type: str = "svm",
                 project_name: Optional[str] = None):
        """
        初始化分类器
        
        Args:
            feature_type: 特征类型 (AE, AS, bi, clustering等)
            classifier_type: 分类器类型 (svm, rf, lr)
            project_name: 项目名称
        """
        self.feature_type = feature_type
        self.classifier_type = classifier_type
        self.project_name = project_name or f"Qwen_{feature_type}_Classification"
        
        # 初始化结果管理器
        if HAS_RESULT_MANAGER:
            self.result_manager = ResultManager(project_name=self.project_name)
            self.result_manager._log(f"开始 {feature_type} 特征分类实验")
        else:
            self.result_manager = None
        
        # 初始化组件
        self.scaler = None
        self.pca = None
        self.classifier = None
        
    def _log(self, message: str):
        """记录日志"""
        if self.result_manager:
            self.result_manager._log(message)
        else:
            print(f"[{self.project_name}] {message}")
    
    def get_feature_files(self, data_dir: str, csv_path: str) -> List[Tuple[str, str]]:
        """获取特征文件列表"""
        df = pd.read_csv(csv_path, delimiter='\t')
        
        all_files = []
        feature_suffix_map = {
            "AE": "AE",
            "AS": "AS", 
            "bi": "_bi-scene",
            "clustering": "_clustering",
            "general": "_general"
        }
        
        suffix = feature_suffix_map.get(self.feature_type, self.feature_type)
        
        for file in os.listdir(data_dir):
            if file.endswith(".npy") and suffix in file:
                # 根据特征类型调整文件名匹配逻辑
                if self.feature_type == "bi":
                    filename_key = 'audio/' + file.replace(".npy", ".wav").replace("_bi-scene", "")
                elif self.feature_type in ["AE", "AS"]:
                    filename_key = 'audio/' + file.replace(".npy", ".wav").replace(suffix, "")
                else:
                    filename_key = 'audio/' + file.replace(".npy", ".wav").replace(suffix, "")
                
                if filename_key in df["filename"].values:
                    label = df.loc[df["filename"] == filename_key, "scene_label"].values[0]
                    all_files.append((file, label))
        
        return all_files
    
    def load_batch_data(self, file_batch: List[Tuple[str, str]], data_dir: str) -> Tuple[np.ndarray, np.ndarray, List[str]]:
        """加载批次数据"""
        X, y, files = [], [], []
        for file, label in file_batch:
            try:
                data = np.load(os.path.join(data_dir, file)).flatten()
                X.append(data)
                y.append(label)
                files.append(file)
            except Exception as e:
                self._log(f"加载文件失败: {file} - {e}")
        
        return np.array(X), np.array(y), files
    
    def create_classifier(self) -> Any:
        """创建分类器"""
        if self.classifier_type == "svm":
            return SVC(kernel="linear", C=1.0)
        elif self.classifier_type == "rf":
            return RandomForestClassifier(n_estimators=100, random_state=42)
        elif self.classifier_type == "lr":
            return LogisticRegression(random_state=42, max_iter=1000)
        else:
            raise ValueError(f"不支持的分类器类型: {self.classifier_type}")
    
    def train(self, 
              data_dir: str,
              csv_path: str,
              training_sample_size: int = 2000,
              test_size: float = 0.2,
              pca_components: float = 0.95,
              batch_size: int = 200) -> Dict[str, Any]:
        """训练分类器"""
        
        self._log(f"开始训练 - 特征类型: {self.feature_type}, 分类器: {self.classifier_type}")
        
        # 1. 获取文件列表
        all_files = self.get_feature_files(data_dir, csv_path)
        self._log(f"找到 {len(all_files)} 个特征文件")
        
        if len(all_files) == 0:
            raise ValueError("未找到匹配的特征文件")
        
        # 2. 随机打乱和分割
        random.seed(42)
        random.shuffle(all_files)
        
        training_files = all_files[:training_sample_size]
        remaining_files = all_files[training_sample_size:]
        
        self._log(f"训练样本: {len(training_files)} 个文件")
        self._log(f"测试样本: {len(remaining_files)} 个文件")
        
        # 3. 加载训练数据
        X_train_full, y_train_full = [], []
        for file, label in tqdm(training_files, desc="加载训练数据"):
            try:
                data = np.load(os.path.join(data_dir, file)).flatten()
                X_train_full.append(data)
                y_train_full.append(label)
            except Exception as e:
                self._log(f"加载训练文件失败: {file} - {e}")
        
        X_train = np.array(X_train_full)
        y_train = np.array(y_train_full)
        
        # 4. 训练/验证集划分
        X_train, X_val, y_train, y_val = train_test_split(
            X_train, y_train, test_size=test_size, random_state=42
        )
        
        self._log(f"训练集大小: {X_train.shape}")
        self._log(f"验证集大小: {X_val.shape}")
        
        # 5. 数据预处理
        self.scaler = StandardScaler()
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_val_scaled = self.scaler.transform(X_val)
        
        self.pca = PCA(n_components=pca_components)
        X_train_pca = self.pca.fit_transform(X_train_scaled)
        X_val_pca = self.pca.transform(X_val_scaled)
        
        self._log(f"PCA后维度: {X_train_pca.shape[1]}")
        
        # 6. 训练分类器
        self.classifier = self.create_classifier()
        self.classifier.fit(X_train_pca, y_train)
        
        # 7. 验证
        y_val_pred = self.classifier.predict(X_val_pca)
        val_acc = accuracy_score(y_val, y_val_pred)
        self._log(f"验证集准确率: {val_acc:.4f}")
        
        # 保存验证结果
        y_val_saved = y_val.copy()
        y_val_pred_saved = y_val_pred.copy()
        
        # 8. 释放内存
        del X_train_full, y_train_full, X_train, y_train
        del X_train_scaled, X_train_pca
        del X_val, y_val, X_val_scaled, X_val_pca, y_val_pred
        gc.collect()
        
        # 9. 分批预测剩余数据
        all_preds, all_labels, all_names = [], [], []
        for i in tqdm(range(0, len(remaining_files), batch_size), desc="批量预测"):
            batch = remaining_files[i:i+batch_size]
            X_batch, y_batch, file_names = self.load_batch_data(batch, data_dir)
            
            if len(X_batch) == 0:
                continue
                
            X_scaled = self.scaler.transform(X_batch)
            X_pca = self.pca.transform(X_scaled)
            preds = self.classifier.predict(X_pca)
            
            all_preds.extend(preds)
            all_labels.extend(y_batch)
            all_names.extend(file_names)
        
        # 10. 合并所有结果
        y_test = np.concatenate([y_val_saved, np.array(all_labels)])
        y_pred = np.concatenate([y_val_pred_saved, np.array(all_preds)])
        
        final_acc = accuracy_score(y_test, y_pred)
        self._log(f"总体准确率: {final_acc:.4f}")
        
        # 11. 生成报告
        results = {
            'accuracy': final_acc,
            'validation_accuracy': val_acc,
            'y_true': y_test,
            'y_pred': y_pred,
            'feature_type': self.feature_type,
            'classifier_type': self.classifier_type,
            'pca_components': X_train_pca.shape[1] if 'X_train_pca' in locals() else self.pca.n_components_
        }
        
        return results
    
    def save_model(self, output_path: str):
        """保存训练好的模型"""
        model_data = {
            'scaler': self.scaler,
            'pca': self.pca,
            'classifier': self.classifier,
            'feature_type': self.feature_type,
            'classifier_type': self.classifier_type
        }
        
        with open(output_path, 'wb') as f:
            pickle.dump(model_data, f)
        
        self._log(f"模型已保存到: {output_path}")
    
    def load_model(self, model_path: str):
        """加载训练好的模型"""
        with open(model_path, 'rb') as f:
            model_data = pickle.load(f)
        
        self.scaler = model_data['scaler']
        self.pca = model_data['pca']
        self.classifier = model_data['classifier']
        self.feature_type = model_data.get('feature_type', self.feature_type)
        self.classifier_type = model_data.get('classifier_type', self.classifier_type)
        
        self._log(f"模型已从 {model_path} 加载")
    
    def save_results(self, results: Dict[str, Any], output_dir: str = "."):
        """保存结果"""
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # 保存分类报告
        report_df = pd.DataFrame(classification_report(
            results['y_true'], 
            results['y_pred'], 
            output_dict=True
        )).transpose()
        
        report_path = output_dir / f"classification_report_{self.feature_type}_{self.classifier_type}.csv"
        report_df.to_csv(report_path)
        
        # 保存混淆矩阵
        conf_mat = confusion_matrix(
            results['y_true'], 
            results['y_pred'], 
            labels=np.unique(results['y_true'])
        )
        conf_df = pd.DataFrame(
            conf_mat, 
            index=np.unique(results['y_true']), 
            columns=np.unique(results['y_true'])
        )
        
        conf_path = output_dir / f"confusion_matrix_{self.feature_type}_{self.classifier_type}.csv"
        conf_df.to_csv(conf_path)
        
        # 可视化混淆矩阵
        plt.figure(figsize=(12, 10))
        sns.heatmap(conf_df, annot=True, fmt='d', cmap="Blues")
        plt.title(f"Confusion Matrix - {self.feature_type} {self.classifier_type.upper()}")
        plt.xlabel("Predicted Label")
        plt.ylabel("True Label")
        plt.tight_layout()
        
        plot_path = output_dir / f"confusion_matrix_{self.feature_type}_{self.classifier_type}.png"
        plt.savefig(plot_path)
        plt.close()
        
        self._log(f"结果已保存到: {output_dir}")


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="音频场景分类训练器")
    parser.add_argument("--feature_type", type=str, 
                       choices=["AE", "AS", "bi", "clustering", "general"],
                       default="AE",
                       help="特征类型")
    parser.add_argument("--classifier", type=str,
                       choices=["svm", "rf", "lr"],
                       default="svm",
                       help="分类器类型")
    parser.add_argument("--data_dir", type=str,
                       default="./new_Feature",
                       help="特征文件目录")
    parser.add_argument("--csv_path", type=str,
                       default="./TAU-urban-acoustic-scenes-2019-development/meta.csv",
                       help="元数据CSV文件路径")
    parser.add_argument("--training_size", type=int, default=2000,
                       help="训练样本数量")
    parser.add_argument("--test_size", type=float, default=0.2,
                       help="验证集比例")
    parser.add_argument("--pca_components", type=float, default=0.95,
                       help="PCA保留的方差比例")
    parser.add_argument("--batch_size", type=int, default=200,
                       help="批处理大小")
    parser.add_argument("--output_dir", type=str, default="./results",
                       help="结果输出目录")
    parser.add_argument("--save_model", action="store_true",
                       help="是否保存模型")
    
    args = parser.parse_args()
    
    # 创建分类器
    classifier = AudioSceneClassifier(
        feature_type=args.feature_type,
        classifier_type=args.classifier
    )
    
    # 训练
    results = classifier.train(
        data_dir=args.data_dir,
        csv_path=args.csv_path,
        training_sample_size=args.training_size,
        test_size=args.test_size,
        pca_components=args.pca_components,
        batch_size=args.batch_size
    )
    
    # 保存结果
    classifier.save_results(results, args.output_dir)
    
    # 保存模型
    if args.save_model:
        model_path = Path(args.output_dir) / f"trained_model_{args.feature_type}_{args.classifier}.pkl"
        classifier.save_model(str(model_path))
    
    print(f"\n训练完成!")
    print(f"最终准确率: {results['accuracy']:.4f}")


if __name__ == "__main__":
    main()
