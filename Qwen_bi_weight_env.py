import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from tqdm import tqdm
import pickle
import random
import seaborn as sns
import matplotlib.pyplot as plt

# 读取元数据
csv_path = "./TAU-urban-acoustic-scenes-2019-development/meta.csv"
df = pd.read_csv(csv_path,delimiter='\t')
# 参数设置
TRAINING_SAMPLE_SIZE = 2000
BATCH_SIZE = 200
data_dir = "./new_Feature"

# 筛选有效文件
all_files = []
for file in os.listdir(data_dir):
    filename_key = 'audio/' + file.replace(".npy", ".wav").replace("_bi-scene", "")
    if filename_key in df["filename"].values:
        label = df.loc[df["filename"] == filename_key, "scene_label"].values[0]
        all_files.append((file, label))

random.seed(42)
random.shuffle(all_files)

training_files = all_files[:TRAINING_SAMPLE_SIZE]
remaining_files = all_files[TRAINING_SAMPLE_SIZE:]

# 加载训练数据
X_train_full, y_train_full = [], []
for file, label in tqdm(training_files, desc="加载训练数据"):
    try:
        data = np.load(os.path.join(data_dir, file)).flatten()
        X_train_full.append(data)
        y_train_full.append(label)
    except Exception as e:
        print(f"加载失败: {file} - {e}")

X_train = np.array(X_train_full)
y_train = np.array(y_train_full)

# 训练/验证集划分
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

# 标准化与降维
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)

pca = PCA(n_components=0.95)
X_train_pca = pca.fit_transform(X_train_scaled)
X_val_pca = pca.transform(X_val_scaled)

# 训练 SVM 模型
svm_model = SVC(kernel="linear", C=1.0)
svm_model.fit(X_train_pca, y_train)

# 验证集准确率
y_val_pred = svm_model.predict(X_val_pca)
val_acc = accuracy_score(y_val, y_val_pred)
print(f"验证集准确率: {val_acc:.4f}")

# 保存模型
with open("trained_model__bi-scene.pkl", "wb") as f:
    pickle.dump({'scaler': scaler, 'pca': pca, 'svm_model': svm_model}, f)

# 保留验证集标签和预测
y_val_saved = y_val.copy()
y_val_pred_saved = y_val_pred.copy()

# 释放训练数据内存
del X_train_full, y_train_full, X_train, y_train
del X_train_scaled, X_train_pca
del X_val, y_val, X_val_scaled, X_val_pca, y_val_pred
import gc
gc.collect()

# 分批预测
def load_batch_data(file_batch):
    X, y, files = [], [], []
    for file, label in file_batch:
        try:
            data = np.load(os.path.join(data_dir, file)).flatten()
            X.append(data)
            y.append(label)
            files.append(file)
        except Exception as e:
            print(f"读取失败: {file} - {e}")
    return np.array(X), np.array(y), files

all_preds, all_labels, all_names = [], [], []
for i in tqdm(range(0, len(remaining_files), BATCH_SIZE), desc="预测中"):
    batch = remaining_files[i:i+BATCH_SIZE]
    X_batch, y_batch, file_names = load_batch_data(batch)
    if len(X_batch) == 0:
        continue
    X_scaled = scaler.transform(X_batch)
    X_pca = pca.transform(X_scaled)
    preds = svm_model.predict(X_pca)
    all_preds.extend(preds)
    all_labels.extend(y_batch)
    all_names.extend(file_names)

# 合并验证与预测结果
y_test = np.concatenate([y_val_saved, np.array(all_labels)])
y_pred = np.concatenate([y_val_pred_saved, np.array(all_preds)])

# 输出准确率和报告
print(f"总准确率: {accuracy_score(y_test, y_pred):.4f}")
report_df = pd.DataFrame(classification_report(y_test, y_pred, output_dict=True)).transpose()
report_df.to_csv("classification_PCA__bi-scene_report.csv")

# 混淆矩阵可视化
conf_mat = confusion_matrix(y_test, y_pred, labels=np.unique(y_test))
conf_df = pd.DataFrame(conf_mat, index=np.unique(y_test), columns=np.unique(y_test))
conf_df.to_csv("confusion_matrix__bi-scene.csv")

plt.figure(figsize=(12, 10))
sns.heatmap(conf_df, annot=True, fmt='d', cmap="Blues")
plt.title("Confusion Matrix - AE Classification")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.tight_layout()
plt.savefig("confusion_matrix__bi-scene.png")
plt.show()
