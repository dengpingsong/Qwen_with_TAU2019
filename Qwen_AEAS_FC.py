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
import random
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm

# 读取 CSV
csv_path = "./TAU-urban-acoustic-scenes-2019-development/meta.csv"
df = pd.read_csv(csv_path, index_col=3, delimiter='\t')

# 自动选择设备和精度
if torch.cuda.is_available():
    device = "cuda"
elif torch.backends.mps.is_available():
    device = "mps"
else:
    device = "cpu"
print(f"使用设备: {device}")

TRAINING_SAMPLE_SIZE = 2000
BATCH_SIZE = 64
EPOCHS = 30
LEARNING_RATE = 1e-3
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
            feat = np.concatenate([ae_feat, as_feat])
            X.append(feat)
            y.append(label)
        except Exception as e:
            print(f"加载文件 {ae_file}, {as_file} 出错: {e}")
    return np.array(X), np.array(y)

X, y = load_features(training_files)
print(f"训练样本: {X.shape}, 标签: {y.shape}")

# 标签编码
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# 标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 划分训练/验证集
X_train, X_val, y_train, y_val = train_test_split(X_scaled, y_encoded, test_size=0.2, random_state=42)

# PyTorch 数据集
class FeatureDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.long)
    def __len__(self):
        return len(self.X)
    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

train_dataset = FeatureDataset(X_train, y_train)
val_dataset = FeatureDataset(X_val, y_val)
train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE)

# 简单全连接网络
class SimpleFC(nn.Module):
    def __init__(self, input_dim, num_classes):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(input_dim, 256),
            nn.ReLU(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, num_classes)
        )
    def forward(self, x):
        return self.fc(x)

model = SimpleFC(X_train.shape[1], len(le.classes_)).to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

# 训练
for epoch in range(EPOCHS):
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
    print(f"Epoch {epoch+1}/{EPOCHS}, Loss: {avg_loss:.4f}")

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
print(f"验证集准确率: {val_acc:.4f}")

# 分类报告
report = classification_report(val_labels, val_preds, target_names=le.classes_, output_dict=True)
pd.DataFrame(report).transpose().to_csv("classification_PCA_AEAS_FC_report.csv")

# 混淆矩阵
cm = confusion_matrix(val_labels, val_preds)
pd.DataFrame(cm, index=le.classes_, columns=le.classes_).to_csv("confusion_matrix_AEAS_FC.csv")
plt.figure(figsize=(12,10))
sns.heatmap(cm, annot=True, fmt='d', cmap="Blues", xticklabels=le.classes_, yticklabels=le.classes_)
plt.title("Confusion Matrix")
plt.ylabel("True Label")
plt.xlabel("Predicted Label")
plt.tight_layout()
plt.savefig("confusion_matrix_AEAS_FC.png")
plt.close()

# 分批加载和推理剩余数据
def load_batch_features(file_pairs_batch):
    X_batch, y_batch, file_names = [], [], []
    for ae_file, as_file, label in file_pairs_batch:
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
        return None, None, None
    return np.array(X_batch), np.array(y_batch), file_names

print("开始分批推理剩余数据...")
from tqdm import tqdm

INFERENCE_BATCH_SIZE = 100
all_predictions = []
all_true_labels = []
all_file_names = []

for i in tqdm(range(0, len(remaining_files), INFERENCE_BATCH_SIZE), desc="分批推理"):
    batch_files = remaining_files[i:i+INFERENCE_BATCH_SIZE]
    X_batch, y_batch, file_names = load_batch_features(batch_files)
    if X_batch is None:
        continue
    
    # 标准化
    X_batch_scaled = scaler.transform(X_batch)
    
    # 转换为张量并推理
    X_batch_tensor = torch.tensor(X_batch_scaled, dtype=torch.float32).to(device)
    with torch.no_grad():
        model.eval()
        out = model(X_batch_tensor)
        y_pred_batch = out.argmax(dim=1).cpu().numpy()
    
    all_predictions.extend(y_pred_batch)
    all_true_labels.extend(le.transform(y_batch))
    all_file_names.extend(file_names)

# 合并验证集和推理结果进行总体评估
y_test = np.concatenate([val_labels, np.array(all_true_labels)])
y_pred = np.concatenate([val_preds, np.array(all_predictions)])
print(f"总预测样本数: {len(y_test)}")

# 保存预测结果
results_df = pd.DataFrame({
    'file_name': all_file_names,
    'true_label': le.inverse_transform(all_true_labels),
    'predicted_label': le.inverse_transform(all_predictions)
})
results_df.to_csv('prediction_results_AEAS_FC.csv', index=False)
print("预测结果已保存到 prediction_results_AEAS_FC.csv")

# 总体分类报告
total_accuracy = accuracy_score(y_test, y_pred)
print(f"总体分类准确率: {total_accuracy:.4f}")

report = classification_report(y_test, y_pred, target_names=le.classes_, output_dict=True)
pd.DataFrame(report).transpose().to_csv("classification_AEAS_FC_report.csv")
print("分类报告已保存为 classification_AEAS_FC_report.csv")

# 总体混淆矩阵
cm_total = confusion_matrix(y_test, y_pred)
pd.DataFrame(cm_total, index=le.classes_, columns=le.classes_).to_csv("confusion_matrix_AEAS_FC_total.csv")
plt.figure(figsize=(12,10))
sns.heatmap(cm_total, annot=True, fmt='d', cmap="Blues", xticklabels=le.classes_, yticklabels=le.classes_)
plt.title("Total Confusion Matrix (Validation + Test)")
plt.ylabel("True Label")
plt.xlabel("Predicted Label")
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig("confusion_matrix_AEAS_FC_total.png")
plt.close()
print("总体混淆矩阵图像已保存为 confusion_matrix_AEAS_FC_total.png")

# 保存模型
torch.save({
    'model_state_dict': model.state_dict(),
    'scaler': scaler,
    'label_encoder': le
}, 'trained_model_AEAS_FC.pth')
print("模型和相关对象已保存为 trained_model_AEAS_FC.pth")
