#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简化的音频场景分类脚本
支持多种特征和分类器
Created on 2025-07-03
"""

import numpy as np
import pandas as pd
import os
import argparse
import pickle
import random
from pathlib import Path
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
from config import TRAIN_CONFIG, CLASSIFIER_PARAMS, FEATURE_TYPES, DATA_PATHS


def get_feature_files(data_dir, csv_path, feature_type):
    """获取特征文件列表"""
    df = pd.read_csv(csv_path, delimiter='\t')
    
    # 根据特征类型确定后缀
    suffix = FEATURE_TYPES.get(feature_type, {'suffix': feature_type})['suffix']
    
    all_files = []
    for file in os.listdir(data_dir):
        if file.endswith(".npy") and suffix in file:
            # 构造对应的音频文件名
            if feature_type == "bi":
                filename_key = 'audio/' + file.replace(".npy", ".wav").replace("_bi-scene", "")
            else:
                filename_key = 'audio/' + file.replace(".npy", ".wav").replace(suffix, "")
            
            # 查找对应的标签
            if filename_key in df["filename"].values:
                label = df.loc[df["filename"] == filename_key, "scene_label"].values[0]
                all_files.append((file, label))
    
    return all_files


def load_batch_data(file_batch, data_dir):
    """加载批次数据"""
    X, y, files = [], [], []
    for file, label in file_batch:
        try:
            data = np.load(os.path.join(data_dir, file)).flatten()
            X.append(data)
            y.append(label)
            files.append(file)
        except Exception as e:
            print(f"加载 {file} 失败: {e}")
    
    return np.array(X), np.array(y), files


def create_classifier(classifier_type):
    """创建分类器"""
    params = CLASSIFIER_PARAMS.get(classifier_type, {})
    
    if classifier_type == "svm":
        return SVC(**params)
    elif classifier_type == "rf":
        return RandomForestClassifier(**params)
    elif classifier_type == "lr":
        return LogisticRegression(**params)
    else:
        raise ValueError(f"不支持的分类器: {classifier_type}")


def train_classifier(data_dir, csv_path, feature_type, classifier_type, 
                    training_size=None, test_size=None, pca_components=None, 
                    batch_size=None, output_dir="./results"):
    """训练分类器"""
    
    # 使用配置文件的默认值
    training_size = training_size or TRAIN_CONFIG['training_sample_size']
    test_size = test_size or TRAIN_CONFIG['test_size']
    pca_components = pca_components or TRAIN_CONFIG['pca_components']
    batch_size = batch_size or TRAIN_CONFIG['batch_size']
    
    print(f"开始训练: {feature_type} + {classifier_type}")
    
    # 1. 获取文件列表
    all_files = get_feature_files(data_dir, csv_path, feature_type)
    print(f"找到 {len(all_files)} 个特征文件")
    
    if len(all_files) == 0:
        raise ValueError("未找到匹配的特征文件")
    
    # 2. 随机分割
    random.seed(42)
    random.shuffle(all_files)
    
    training_files = all_files[:training_size]
    remaining_files = all_files[training_size:]
    
    print(f"训练样本: {len(training_files)} 个")
    print(f"测试样本: {len(remaining_files)} 个")
    
    # 3. 加载训练数据
    print("加载训练数据...")
    X_train_full, y_train_full = [], []
    for file, label in tqdm(training_files):
        try:
            data = np.load(os.path.join(data_dir, file)).flatten()
            X_train_full.append(data)
            y_train_full.append(label)
        except Exception as e:
            print(f"加载 {file} 失败: {e}")
    
    X_train = np.array(X_train_full)
    y_train = np.array(y_train_full)
    
    # 4. 训练/验证分割
    X_train, X_val, y_train, y_val = train_test_split(
        X_train, y_train, test_size=test_size, random_state=42
    )
    
    print(f"训练集: {X_train.shape}")
    print(f"验证集: {X_val.shape}")
    
    # 5. 数据预处理
    print("数据预处理...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_val_scaled = scaler.transform(X_val)
    
    pca = PCA(n_components=pca_components)
    X_train_pca = pca.fit_transform(X_train_scaled)
    X_val_pca = pca.transform(X_val_scaled)
    
    print(f"PCA后维度: {X_train_pca.shape[1]}")
    
    # 6. 训练分类器
    print("训练分类器...")
    classifier = create_classifier(classifier_type)
    classifier.fit(X_train_pca, y_train)
    
    # 7. 验证
    y_val_pred = classifier.predict(X_val_pca)
    val_acc = accuracy_score(y_val, y_val_pred)
    print(f"验证集准确率: {val_acc:.4f}")
    
    # 保存验证结果
    y_val_saved = y_val.copy()
    y_val_pred_saved = y_val_pred.copy()
    
    # 8. 批量预测剩余数据
    print("预测测试数据...")
    all_preds, all_labels = [], []
    
    for i in tqdm(range(0, len(remaining_files), batch_size)):
        batch = remaining_files[i:i+batch_size]
        X_batch, y_batch, _ = load_batch_data(batch, data_dir)
        
        if len(X_batch) == 0:
            continue
            
        X_scaled = scaler.transform(X_batch)
        X_pca = pca.transform(X_scaled)
        preds = classifier.predict(X_pca)
        
        all_preds.extend(preds)
        all_labels.extend(y_batch)
    
    # 9. 合并结果
    y_test = np.concatenate([y_val_saved, np.array(all_labels)])
    y_pred = np.concatenate([y_val_pred_saved, np.array(all_preds)])
    
    final_acc = accuracy_score(y_test, y_pred)
    print(f"总体准确率: {final_acc:.4f}")
    
    # 10. 保存结果
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 保存模型
    model_path = output_dir / f"model_{feature_type}_{classifier_type}.pkl"
    with open(model_path, 'wb') as f:
        pickle.dump({
            'scaler': scaler,
            'pca': pca,
            'classifier': classifier,
            'feature_type': feature_type,
            'classifier_type': classifier_type
        }, f)
    
    # 保存分类报告
    report = classification_report(y_test, y_pred, output_dict=True)
    report_df = pd.DataFrame(report).transpose()
    report_path = output_dir / f"report_{feature_type}_{classifier_type}.csv"
    report_df.to_csv(report_path)
    
    # 保存和绘制混淆矩阵
    conf_matrix = confusion_matrix(y_test, y_pred)
    labels = sorted(list(set(y_test)))
    conf_df = pd.DataFrame(conf_matrix, index=labels, columns=labels)
    
    conf_path = output_dir / f"confusion_{feature_type}_{classifier_type}.csv"
    conf_df.to_csv(conf_path)
    
    # 绘制混淆矩阵
    plt.figure(figsize=(10, 8))
    sns.heatmap(conf_df, annot=True, fmt='d', cmap="Blues")
    plt.title(f"Confusion Matrix - {feature_type} {classifier_type.upper()}")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.tight_layout()
    
    plot_path = output_dir / f"confusion_{feature_type}_{classifier_type}.png"
    plt.savefig(plot_path)
    plt.close()
    
    print(f"结果保存到: {output_dir}")
    
    return {
        'accuracy': final_acc,
        'validation_accuracy': val_acc,
        'model_path': str(model_path),
        'report_path': str(report_path)
    }


def main():
    parser = argparse.ArgumentParser(description="音频场景分类")
    parser.add_argument("--feature_type", choices=list(FEATURE_TYPES.keys()),
                       default="AE", help="特征类型")
    parser.add_argument("--classifier", choices=list(CLASSIFIER_PARAMS.keys()),
                       default="svm", help="分类器类型")
    parser.add_argument("--data_dir", default=DATA_PATHS['feature_folder'],
                       help="特征文件目录")
    parser.add_argument("--csv_path", default=DATA_PATHS['meta_csv'],
                       help="元数据文件")
    parser.add_argument("--training_size", type=int, default=TRAIN_CONFIG['training_sample_size'],
                       help="训练样本数")
    parser.add_argument("--output_dir", default=DATA_PATHS['results_folder'],
                       help="输出目录")
    
    args = parser.parse_args()
    
    results = train_classifier(
        data_dir=args.data_dir,
        csv_path=args.csv_path,
        feature_type=args.feature_type,
        classifier_type=args.classifier,
        training_size=args.training_size,
        output_dir=args.output_dir
    )
    
    print(f"\n训练完成!")
    print(f"最终准确率: {results['accuracy']:.4f}")
    print(f"验证准确率: {results['validation_accuracy']:.4f}")


if __name__ == "__main__":
    main()
