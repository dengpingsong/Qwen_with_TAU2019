import numpy as np
import pandas as pd
import os
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
import random
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm
import warnings
from result_manager import ResultManager
warnings.filterwarnings('ignore')

# 读取 CSV
csv_path = "./TAU-urban-acoustic-scenes-2019-development/meta.csv"
df = pd.read_csv(csv_path, index_col=3, delimiter='\t')

# 初始化结果管理器
rm = ResultManager(project_name="Qwen_AEAS_Clustering_Classification")
rm._log("开始 AE+AS 特征融合聚类分类实验")

# 自动选择设备
if torch.cuda.is_available():
    device = "cuda"
elif torch.backends.mps.is_available():
    device = "mps"
else:
    device = "cpu"
print(f"使用设备: {device}")
rm._log(f"使用设备: {device}")

# 参数设置
TRAINING_SAMPLE_SIZE = 2000
BATCH_SIZE = 64
EPOCHS = 30
LEARNING_RATE = 1e-4
N_CLUSTERS = 10  # 聚类数量
PCA_COMPONENTS = 500  # PCA降维维度
data_dir = "./new_Feature"

# 获取所有 AE/AS 成对文件
all_files = []
for file in os.listdir(data_dir):
    if file.endswith("AE.npy"):
        as_file = file.replace("AE.npy", "AS.npy")
        if os.path.exists(os.path.join(data_dir, as_file)):
            filename_key = 'audio/' + file.replace(".npy", ".wav").replace("AE", "")
            if filename_key in df["filename"].values:
                label = df.loc[df["filename"] == filename_key, "scene_label"].values[0]
                all_files.append((file, as_file, label))

print(f"找到 {len(all_files)} 对 AE/AS 特征文件")

# 随机打乱数据
random.seed(42)
random.shuffle(all_files)
training_files = all_files[:TRAINING_SAMPLE_SIZE]
remaining_files = all_files[TRAINING_SAMPLE_SIZE:]

# 加载特征并拼接
def load_features(file_pairs):
    X, y = [], []
    for ae_file, as_file, label in file_pairs:
        try:
            ae_feat = np.load(os.path.join(data_dir, ae_file)).flatten()
            as_feat = np.load(os.path.join(data_dir, as_file)).flatten()
            # 合并AE和AS特征
            feat = np.concatenate([ae_feat, as_feat])
            X.append(feat)
            y.append(label)
        except Exception as e:
            print(f"加载文件 {ae_file}, {as_file} 出错: {e}")
    return np.array(X), np.array(y)

print("加载训练特征...")
X, y = load_features(training_files)
print(f"原始特征维度: {X.shape}, 标签数量: {y.shape}")

# 标签编码
le = LabelEncoder()
y_encoded = le.fit_transform(y)
print(f"共有 {len(le.classes_)} 个类别: {le.classes_}")

# 标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PCA降维
print("执行PCA降维...")
pca = PCA(n_components=PCA_COMPONENTS, random_state=42)
X_pca = pca.fit_transform(X_scaled)
print(f"PCA降维后特征维度: {X_pca.shape}")
print(f"PCA解释方差比: {pca.explained_variance_ratio_.sum():.4f}")

# 聚类分析
print(f"执行K-means聚类 (k={N_CLUSTERS})...")
kmeans = KMeans(n_clusters=N_CLUSTERS, random_state=42, n_init=10)
cluster_labels = kmeans.fit_predict(X_pca)

# 分析聚类结果
print("聚类结果分析:")
cluster_scene_distribution = pd.DataFrame({
    'cluster': cluster_labels,
    'scene': y
}).groupby(['cluster', 'scene']).size().unstack(fill_value=0)

print("各聚类中场景分布:")
print(cluster_scene_distribution)

# 保存聚类分布
cluster_scene_distribution.to_csv("cluster_scene_distribution.csv")

# 可视化聚类结果
if PCA_COMPONENTS >= 2:
    plt.figure(figsize=(15, 5))
    
    # 原始PCA可视化
    plt.subplot(1, 3, 1)
    colors = plt.cm.tab10(y_encoded / len(le.classes_))
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=colors, alpha=0.6, s=10)
    plt.title("PCA by Scene Labels")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    
    # 聚类结果可视化
    plt.subplot(1, 3, 2)
    colors = plt.cm.tab20(cluster_labels / N_CLUSTERS)
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=colors, alpha=0.6, s=10)
    plt.title("K-means Clustering")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    
    # 聚类中心
    plt.subplot(1, 3, 3)
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=colors, alpha=0.3, s=5)
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
                c='red', marker='x', s=100, linewidths=3)
    plt.title("Cluster Centers")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    
    plt.tight_layout()
    plt.savefig("clustering_visualization.png", dpi=150)
    plt.close()
    print("聚类可视化已保存为 clustering_visualization.png")

# 创建增强特征：原始特征 + 聚类特征
def create_enhanced_features(X_original, cluster_labels):
    """创建包含聚类信息的增强特征"""
    # 独热编码聚类标签
    cluster_onehot = np.zeros((len(cluster_labels), N_CLUSTERS))
    cluster_onehot[np.arange(len(cluster_labels)), cluster_labels] = 1
    
    # 聚类中心距离特征
    cluster_distances = np.zeros((len(X_original), N_CLUSTERS))
    for i, center in enumerate(kmeans.cluster_centers_):
        cluster_distances[:, i] = np.linalg.norm(X_original - center, axis=1)
    
    # 合并特征
    enhanced_features = np.concatenate([
        X_original,  # 原始PCA特征
        cluster_onehot,  # 聚类独热编码
        cluster_distances  # 到各聚类中心的距离
    ], axis=1)
    
    return enhanced_features

# 创建增强特征
print("创建增强特征...")
X_enhanced = create_enhanced_features(X_pca, cluster_labels)
print(f"增强特征维度: {X_enhanced.shape}")

# 划分训练/验证集
X_train, X_val, y_train, y_val = train_test_split(
    X_enhanced, y_encoded, test_size=0.2, random_state=42
)

# PyTorch 数据集
class ClusterEnhancedDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.long)
    
    def __len__(self):
        return len(self.X)
    
    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

train_dataset = ClusterEnhancedDataset(X_train, y_train)
val_dataset = ClusterEnhancedDataset(X_val, y_val)
train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE)

# 聚类增强神经网络
class ClusterEnhancedNet(nn.Module):
    def __init__(self, input_dim, num_classes, n_clusters):
        super().__init__()
        self.n_clusters = n_clusters
        
        # 特征提取层
        self.feature_extractor = nn.Sequential(
            nn.Linear(input_dim, 512),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256, 128),
            nn.ReLU(),
        )
        
        # 聚类感知层
        self.cluster_attention = nn.Sequential(
            nn.Linear(128 + n_clusters, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
        )
        
        # 分类层
        self.classifier = nn.Linear(32, num_classes)
        
    def forward(self, x):
        # 分离不同类型的特征
        pca_features = x[:, :PCA_COMPONENTS]
        cluster_onehot = x[:, PCA_COMPONENTS:PCA_COMPONENTS+self.n_clusters]
        cluster_distances = x[:, PCA_COMPONENTS+self.n_clusters:]
        
        # 特征提取
        features = self.feature_extractor(x)
        
        # 结合聚类信息
        combined = torch.cat([features, cluster_onehot], dim=1)
        cluster_aware = self.cluster_attention(combined)
        
        # 分类
        output = self.classifier(cluster_aware)
        return output

model = ClusterEnhancedNet(X_enhanced.shape[1], len(le.classes_), N_CLUSTERS).to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE, weight_decay=1e-5)

# 训练模型
print("开始训练聚类增强模型...")
train_losses = []
val_accuracies = []

for epoch in range(EPOCHS):
    # 训练
    model.train()
    total_loss = 0
    for xb, yb in train_loader:
        xb, yb = xb.to(device), yb.to(device)
        optimizer.zero_grad()
        out = model(xb)
        loss = criterion(out, yb)
        loss.backward()
        optimizer.step()
        total_loss += loss.item() * xb.size(0)
    
    avg_loss = total_loss / len(train_loader.dataset)
    train_losses.append(avg_loss)
    
    # 验证
    model.eval()
    val_preds, val_labels = [], []
    with torch.no_grad():
        for xb, yb in val_loader:
            xb, yb = xb.to(device), yb.to(device)
            out = model(xb)
            preds = out.argmax(dim=1).cpu().numpy()
            val_preds.extend(preds)
            val_labels.extend(yb.cpu().numpy())
    
    val_acc = accuracy_score(val_labels, val_preds)
    val_accuracies.append(val_acc)
    
    if (epoch + 1) % 5 == 0:
        print(f"Epoch {epoch+1}/{EPOCHS}, Loss: {avg_loss:.4f}, Val Acc: {val_acc:.4f}")

print(f"最终验证集准确率: {val_accuracies[-1]:.4f}")

# 训练曲线
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(train_losses)
plt.title("Training Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")

plt.subplot(1, 2, 2)
plt.plot(val_accuracies)
plt.title("Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.tight_layout()
plt.savefig("training_curves_clustering.png")
plt.close()

# 处理剩余数据
def process_remaining_data_with_clustering(remaining_files):
    """处理剩余数据并应用聚类增强"""
    print("处理剩余数据...")
    
    all_predictions = []
    all_true_labels = []
    all_file_names = []
    
    INFERENCE_BATCH_SIZE = 100
    
    for i in tqdm(range(0, len(remaining_files), INFERENCE_BATCH_SIZE), desc="分批处理"):
        batch_files = remaining_files[i:i+INFERENCE_BATCH_SIZE]
        
        # 加载批次数据
        X_batch, y_batch, file_names = [], [], []
        for ae_file, as_file, label in batch_files:
            try:
                ae_feat = np.load(os.path.join(data_dir, ae_file)).flatten()
                as_feat = np.load(os.path.join(data_dir, as_file)).flatten()
                feat = np.concatenate([ae_feat, as_feat])
                X_batch.append(feat)
                y_batch.append(label)
                file_names.append(ae_file)
            except Exception as e:
                print(f"加载文件 {ae_file}, {as_file} 出错: {e}")
        
        if not X_batch:
            continue
            
        X_batch = np.array(X_batch)
        
        # 标准化和PCA
        X_batch_scaled = scaler.transform(X_batch)
        X_batch_pca = pca.transform(X_batch_scaled)
        
        # 聚类预测
        batch_cluster_labels = kmeans.predict(X_batch_pca)
        
        # 创建增强特征
        X_batch_enhanced = create_enhanced_features(X_batch_pca, batch_cluster_labels)
        
        # 模型预测
        X_batch_tensor = torch.tensor(X_batch_enhanced, dtype=torch.float32).to(device)
        with torch.no_grad():
            model.eval()
            out = model(X_batch_tensor)
            y_pred_batch = out.argmax(dim=1).cpu().numpy()
        
        all_predictions.extend(y_pred_batch)
        all_true_labels.extend(le.transform(y_batch))
        all_file_names.extend(file_names)
    
    return all_predictions, all_true_labels, all_file_names

# 处理剩余数据
all_predictions, all_true_labels, all_file_names = process_remaining_data_with_clustering(remaining_files)

# 合并所有预测结果
y_test = np.concatenate([val_labels, np.array(all_true_labels)])
y_pred = np.concatenate([val_preds, np.array(all_predictions)])
print(f"总预测样本数: {len(y_test)}")

# 保存预测结果
results_df = pd.DataFrame({
    'file_name': all_file_names,
    'true_label': le.inverse_transform(all_true_labels),
    'predicted_label': le.inverse_transform(all_predictions)
})
results_df.to_csv('prediction_results_clustering.csv', index=False)
print("预测结果已保存到 prediction_results_clustering.csv")

# 总体评估
total_accuracy = accuracy_score(y_test, y_pred)
print(f"聚类增强模型总体准确率: {total_accuracy:.4f}")

# 分类报告
report = classification_report(y_test, y_pred, target_names=le.classes_, output_dict=True)
pd.DataFrame(report).transpose().to_csv("classification_clustering_report.csv")
print("分类报告已保存为 classification_clustering_report.csv")

# 混淆矩阵
cm_total = confusion_matrix(y_test, y_pred)
pd.DataFrame(cm_total, index=le.classes_, columns=le.classes_).to_csv("confusion_matrix_clustering.csv")

plt.figure(figsize=(12, 10))
sns.heatmap(cm_total, annot=True, fmt='d', cmap="Blues", 
            xticklabels=le.classes_, yticklabels=le.classes_)
plt.title("Confusion Matrix - Clustering Enhanced Model")
plt.ylabel("True Label")
plt.xlabel("Predicted Label")
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig("confusion_matrix_clustering.png", dpi=150)
plt.close()
print("混淆矩阵已保存为 confusion_matrix_clustering.png")

# 聚类性能分析
print("\n聚类性能分析:")
cluster_accuracy = {}
for cluster_id in range(N_CLUSTERS):
    cluster_mask = cluster_labels == cluster_id
    if np.sum(cluster_mask) > 0:
        cluster_y_true = y_encoded[cluster_mask]
        cluster_y_pred = val_preds[:len(cluster_y_true)]  # 简化处理
        if len(cluster_y_pred) > 0:
            cluster_acc = accuracy_score(cluster_y_true, cluster_y_pred[:len(cluster_y_true)])
            cluster_accuracy[cluster_id] = cluster_acc
            print(f"聚类 {cluster_id}: 样本数 {np.sum(cluster_mask)}, 准确率 {cluster_acc:.4f}")

# 保存聚类性能
cluster_perf_df = pd.DataFrame(list(cluster_accuracy.items()), 
             columns=['cluster_id', 'accuracy'])
cluster_perf_df.to_csv("cluster_performance.csv", index=False)

# 使用结果管理器保存聚类性能
rm.save_csv(cluster_perf_df, "cluster_performance.csv")

# # 保存模型和相关对象
# torch.save({
#     'model_state_dict': model.state_dict(),
#     'scaler': scaler,
#     'pca': pca,
#     'kmeans': kmeans,
#     'label_encoder': le,
#     'n_clusters': N_CLUSTERS,
#     'pca_components': PCA_COMPONENTS
# }, 'trained_model_clustering.pth')
# print("聚类增强模型已保存为 trained_model_clustering.pth")

# 性能总结
performance_summary = f"""
{"="*60}
AE+AS特征融合 + 聚类增强分类 性能总结
{"="*60}
训练样本数: {len(X_train)}
测试样本数: {len(y_test)}
融合特征维度: {X_train.shape[1]}
PCA降维维度: {PCA_COMPONENTS}
聚类数量: {N_CLUSTERS}
类别数量: {len(le.classes_)}
最终测试准确率: {total_accuracy:.4f}
使用设备: {device}
{"="*60}
"""

print(performance_summary)

# 使用结果管理器保存性能摘要
rm.save_text(performance_summary, "performance_summary.txt")

# 创建实验摘要
rm.create_experiment_summary(
    model_name="AEAS_Clustering_Enhanced_Classification",
    accuracy=total_accuracy,
    other_metrics={
        "training_samples": len(X_train),
        "test_samples": len(y_test),
        "fused_feature_dimensions": X_train.shape[1],
        "pca_components": PCA_COMPONENTS,
        "n_clusters": N_CLUSTERS,
        "num_classes": len(le.classes_),
        "device": device,
        "method": "clustering_enhanced_classification"
    }
)

print("\n聚类增强处理完成!")
print(f"- 使用了 {N_CLUSTERS} 个聚类")
print(f"- PCA降维到 {PCA_COMPONENTS} 维")
print(f"- 最终模型准确率: {total_accuracy:.4f}")

# 结束实验
rm.finish("AE+AS特征融合聚类增强分类实验完成")
