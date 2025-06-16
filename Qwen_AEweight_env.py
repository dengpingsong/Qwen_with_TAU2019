import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from tqdm import tqdm
import pickle
import random

# 读取 CSV
csv_path = "./TAU-urban-acoustic-scenes-2019-development/meta.csv"
df = pd.read_csv(csv_path, index_col=3, delimiter='\t')

# 设定参数
TRAINING_SAMPLE_SIZE = 2000
BATCH_SIZE = 200
data_dir = "./new_Feature"

# 获取所有符合条件的文件列表
all_files = []
for file in os.listdir(data_dir):
    if file.endswith(".npy") and "AS" not in file:
        filename_key = 'audio/' + file.replace(".npy", ".wav").replace("AE", "")
        if filename_key in df["filename"].values:
            label = df.loc[df["filename"] == filename_key, "scene_label"].values[0]
            all_files.append((file, label))

print(f"找到 {len(all_files)} 个数据文件")

# 随机打乱
random.seed(42)
random.shuffle(all_files)

# 拆分数据
training_files = all_files[:TRAINING_SAMPLE_SIZE]
remaining_files = all_files[TRAINING_SAMPLE_SIZE:]

print(f"训练样本: {len(training_files)} 个文件")
print(f"剩余样本: {len(remaining_files)} 个文件")

# 加载训练数据
X_train_full, y_train_full = [], []
for file, label in tqdm(training_files, desc="加载训练数据"):
    try:
        data = np.load(os.path.join(data_dir, file)).flatten()
        X_train_full.append(data)
        y_train_full.append(label)
    except Exception as e:
        print(f"加载文件 {file} 出错: {e}")

X_train_full = np.array(X_train_full)
y_train_full = np.array(y_train_full)
print(f"成功加载 {len(X_train_full)} 个训练样本，特征维度: {X_train_full.shape[1]}")

# 划分训练集/验证集
X_train, X_val, y_train, y_val = train_test_split(X_train_full, y_train_full, test_size=0.2, random_state=42)

# 标准化 & PCA
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)

pca = PCA(n_components=0.95)
X_train_pca = pca.fit_transform(X_train_scaled)
X_val_pca = pca.transform(X_val_scaled)

print(f"PCA降维后特征数量: {X_train_pca.shape[1]}")

# SVM 模型训练
svm_model = SVC(kernel="linear", C=1.0, probability=True)
svm_model.fit(X_train_pca, y_train)

# 验证集预测
y_val_pred = svm_model.predict(X_val_pca)
val_accuracy = accuracy_score(y_val, y_val_pred)
print(f"验证集准确率: {val_accuracy:.4f}")

# 保存模型
model_data = {'scaler': scaler, 'pca': pca, 'svm_model': svm_model}
with open('trained_model_AE.pkl', 'wb') as f:
    pickle.dump(model_data, f)
print("模型已保存到 trained_model_AE.pkl")

# 加载并预测剩余数据
def load_batch_data(file_batch):
    X_batch, y_batch, file_names = [], [], []
    for file, label in file_batch:
        try:
            data = np.load(os.path.join(data_dir, file)).flatten()
            X_batch.append(data)
            y_batch.append(label)
            file_names.append(file)
        except Exception as e:
            print(f"加载文件 {file} 出错: {e}")
    if not X_batch:
        return None, None, None
    return np.array(X_batch), np.array(y_batch), file_names

print("开始分批预测剩余数据...")

all_predictions = []
all_true_labels = []
all_file_names = []

for i in tqdm(range(0, len(remaining_files), BATCH_SIZE), desc="分批预测"):
    batch_files = remaining_files[i:i+BATCH_SIZE]
    X_batch, y_batch, file_names = load_batch_data(batch_files)
    if X_batch is None:
        continue
    X_batch_scaled = scaler.transform(X_batch)
    X_batch_pca = pca.transform(X_batch_scaled)
    y_pred_batch = svm_model.predict(X_batch_pca)
    all_predictions.extend(y_pred_batch)
    all_true_labels.extend(y_batch)
    all_file_names.extend(file_names)

# 评估
y_test = np.concatenate([y_val, np.array(all_true_labels)])
y_pred = np.concatenate([y_val_pred, np.array(all_predictions)])
print(f"总预测样本数: {len(y_test)}")

# 保存预测结果
results_df = pd.DataFrame({
    'file_name': all_file_names,
    'true_label': all_true_labels,
    'predicted_label': all_predictions
})
results_df.to_csv('prediction_results_AE.csv', index=False)
print("预测结果已保存到 prediction_results_AE.csv")

# 分类报告
accuracy = accuracy_score(y_test, y_pred)
print(f"总体分类准确率: {accuracy:.4f}")

report = classification_report(y_test, y_pred, output_dict=True)
report_df = pd.DataFrame(report).transpose()
report_df.to_csv("classification_PCA_AE_report.csv", index=True)
print("分类报告已保存为 CSV 文件：classification_PCA_AE_report.csv")