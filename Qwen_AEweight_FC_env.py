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
import warnings
from result_manager import ResultManager
warnings.filterwarnings('ignore')

# 读取 CSV
csv_path = "./TAU-urban-acoustic-scenes-2019-development/meta.csv"
df = pd.read_csv(csv_path, index_col=3, delimiter='\t')

# 初始化结果管理器
rm = ResultManager(project_name="Qwen_AE_FC_Classification")
rm._log("开始 AE 全连接网络分类实验")

# 自动选择设备
if torch.cuda.is_available():
    device = "cuda"
elif torch.backends.mps.is_available():
    device = "mps"
else:
    device = "cpu"
print(f"使用设备: {device}")
rm._log(f"使用设备: {device}")

# 设定参数
TRAINING_SAMPLE_SIZE = 2000  # 用于训练模型的样本数量
BATCH_SIZE = 64  # 训练批次大小
INFERENCE_BATCH_SIZE = 200  # 分批预测时的批次大小
EPOCHS = 30  # 训练轮数
LEARNING_RATE = 1e-3  # 学习率
data_dir = "./new_Feature"

# 获取所有符合条件的文件列表
all_files = []
for file in os.listdir(data_dir):
    if file.endswith(".npy") and "AS" not in file:  # 只处理AE特征
        filename_key = 'audio/' + file.replace(".npy", ".wav").replace("AE", "")  # 匹配CSV格式
        
        # 检查 filename_key 是否在 CSV 中
        if filename_key in df["filename"].values:
            label = df.loc[df["filename"] == filename_key, "scene_label"].values[0]
            all_files.append((file, label))

print(f"找到 {len(all_files)} 个AE特征文件")

# 随机打乱文件列表
random.seed(42)
random.shuffle(all_files)

# 第一步：加载训练样本用于训练模型
training_files = all_files[:TRAINING_SAMPLE_SIZE]
remaining_files = all_files[TRAINING_SAMPLE_SIZE:]

print(f"训练样本: {len(training_files)} 个文件")
print(f"剩余样本: {len(remaining_files)} 个文件")

print("加载训练数据...")
X_train_full, y_train_full = [], []

for file, label in tqdm(training_files, desc="加载训练数据"):
    file_path = os.path.join(data_dir, file)
    try:
        data = np.load(file_path).flatten()  # 展平数据
        X_train_full.append(data)
        y_train_full.append(label)
    except Exception as e:
        print(f"加载文件 {file} 时出错: {e}")
        continue

X_train_full = np.array(X_train_full)
y_train_full = np.array(y_train_full)

print(f"成功加载 {len(X_train_full)} 个训练样本，特征维度: {X_train_full.shape[1]}")

# 标签编码
le = LabelEncoder()
y_train_encoded = le.fit_transform(y_train_full)
print(f"类别数量: {len(le.classes_)}")
print(f"类别列表: {le.classes_}")

# 划分训练集和验证集
X_train, X_val, y_train, y_val = train_test_split(
    X_train_full, y_train_encoded, test_size=0.2, random_state=42
)

# 数据标准化
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)

print(f"训练集大小: {X_train_scaled.shape}")
print(f"验证集大小: {X_val_scaled.shape}")

# PyTorch Dataset
class AEFeatureDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.long)
    
    def __len__(self):
        return len(self.X)
    
    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

# 创建数据加载器
train_dataset = AEFeatureDataset(X_train_scaled, y_train)
val_dataset = AEFeatureDataset(X_val_scaled, y_val)
train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE, shuffle=False)

# 定义全连接神经网络
class AEClassificationNet(nn.Module):
    def __init__(self, input_dim, num_classes):
        super(AEClassificationNet, self).__init__()
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

# 创建模型
model = AEClassificationNet(X_train_scaled.shape[1], len(le.classes_)).to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE, weight_decay=1e-5)
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.5)

print(f"模型参数数量: {sum(p.numel() for p in model.parameters()):,}")

# 训练模型
print("开始训练模型...")
train_losses = []
val_accuracies = []
best_val_acc = 0.0

for epoch in range(EPOCHS):
    # 训练阶段
    model.train()
    total_loss = 0
    train_correct = 0
    train_total = 0
    
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item()
        pred = output.argmax(dim=1, keepdim=True)
        train_correct += pred.eq(target.view_as(pred)).sum().item()
        train_total += target.size(0)
    
    avg_loss = total_loss / len(train_loader)
    train_acc = train_correct / train_total
    train_losses.append(avg_loss)
    
    # 验证阶段
    model.eval()
    val_correct = 0
    val_total = 0
    
    with torch.no_grad():
        for data, target in val_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            pred = output.argmax(dim=1, keepdim=True)
            val_correct += pred.eq(target.view_as(pred)).sum().item()
            val_total += target.size(0)
    
    val_acc = val_correct / val_total
    val_accuracies.append(val_acc)
    
    # 保存最佳模型
    if val_acc > best_val_acc:
        best_val_acc = val_acc
        torch.save({
            'model_state_dict': model.state_dict(),
            'scaler': scaler,
            'label_encoder': le,
            'best_val_acc': best_val_acc,
            'input_dim': X_train_scaled.shape[1]
        }, 'best_model_AE_FC.pth')
    
    scheduler.step()
    
    if (epoch + 1) % 5 == 0:
        print(f'Epoch [{epoch+1}/{EPOCHS}], Loss: {avg_loss:.4f}, '
              f'Train Acc: {train_acc:.4f}, Val Acc: {val_acc:.4f}')

print(f"训练完成! 最佳验证准确率: {best_val_acc:.4f}")

# 绘制训练曲线
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(train_losses)
plt.title('Training Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(val_accuracies)
plt.title('Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.grid(True)

plt.tight_layout()
plt.savefig('training_curves_AE_FC.png')
plt.close()
print("训练曲线已保存为 training_curves_AE_FC.png")

# 加载最佳模型进行最终验证
checkpoint = torch.load('best_model_AE_FC.pth')
model.load_state_dict(checkpoint['model_state_dict'])

# 验证集预测
model.eval()
val_predictions = []
val_true_labels = []

with torch.no_grad():
    for data, target in val_loader:
        data, target = data.to(device), target.to(device)
        output = model(data)
        pred = output.argmax(dim=1)
        val_predictions.extend(pred.cpu().numpy())
        val_true_labels.extend(target.cpu().numpy())

val_accuracy = accuracy_score(val_true_labels, val_predictions)
print(f"最终验证集准确率: {val_accuracy:.4f}")

# 第二步：分批预测剩余数据
print("开始分批预测剩余数据...")

def load_batch_data(file_batch):
    """加载一批数据用于预测"""
    X_batch = []
    y_batch = []
    file_names = []
    
    for file, label in file_batch:
        file_path = os.path.join(data_dir, file)
        try:
            data = np.load(file_path).flatten()  # 展平数据
            X_batch.append(data)
            y_batch.append(label)
            file_names.append(file)
        except Exception as e:
            print(f"加载文件 {file} 时出错: {e}")
            continue
    
    if len(X_batch) == 0:
        return None, None, None
    
    return np.array(X_batch), np.array(y_batch), file_names

# 分批预测剩余数据
all_predictions = []
all_true_labels = []
all_file_names = []

for i in tqdm(range(0, len(remaining_files), INFERENCE_BATCH_SIZE), desc="分批预测"):
    batch_files = remaining_files[i:i+INFERENCE_BATCH_SIZE]
    X_batch, y_batch, file_names = load_batch_data(batch_files)
    
    if X_batch is None:
        continue
    
    # 预处理
    X_batch_scaled = scaler.transform(X_batch)
    
    # 转换为张量并预测
    X_batch_tensor = torch.tensor(X_batch_scaled, dtype=torch.float32).to(device)
    
    with torch.no_grad():
        model.eval()
        output = model(X_batch_tensor)
        y_pred_batch = output.argmax(dim=1).cpu().numpy()
    
    all_predictions.extend(y_pred_batch)
    all_true_labels.extend(le.transform(y_batch))
    all_file_names.extend(file_names)

# 合并验证集和预测结果
y_test = np.concatenate([val_true_labels, np.array(all_true_labels)])
y_pred = np.concatenate([val_predictions, np.array(all_predictions)])

print(f"总预测样本数: {len(y_test)}")

# 保存预测结果
results_df = pd.DataFrame({
    'file_name': all_file_names,
    'true_label': le.inverse_transform(all_true_labels),
    'predicted_label': le.inverse_transform(all_predictions)
})
results_df.to_csv('prediction_results_AE_FC.csv', index=False)
print("预测结果已保存到 prediction_results_AE_FC.csv")

# 计算总体准确率
accuracy = accuracy_score(y_test, y_pred)
print(f"总体分类准确率: {accuracy:.4f}")

# 生成分类报告
report = classification_report(y_test, y_pred, target_names=le.classes_, output_dict=True)

# 将分类报告转换为 DataFrame
report_df = pd.DataFrame(report).transpose()

# 将分类报告保存为 CSV
report_csv_path = "classification_AE_FC_report.csv"
report_df.to_csv(report_csv_path, index=True)

print(f"分类报告已保存为 CSV 文件：{report_csv_path}")

# 计算混淆矩阵
conf_mat = confusion_matrix(y_test, y_pred, labels=range(len(le.classes_)))

# 将混淆矩阵保存为 CSV
confusion_df = pd.DataFrame(conf_mat, index=le.classes_, columns=le.classes_)
confusion_csv_path = "confusion_matrix_AE_FC.csv"
confusion_df.to_csv(confusion_csv_path)
print(f"混淆矩阵已保存为 CSV 文件：{confusion_csv_path}")

# 可视化混淆矩阵
plt.figure(figsize=(12, 10))
sns.heatmap(confusion_df, annot=True, fmt='d', cmap="Blues")
plt.title("AE FC Model Confusion Matrix")
plt.ylabel("True Label")
plt.xlabel("Predicted Label")
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()

# 保存混淆矩阵图像
confusion_img_path = "confusion_matrix_AE_FC.png"
plt.savefig(confusion_img_path)
print(f"混淆矩阵图像已保存为：{confusion_img_path}")
plt.close()

# 保存最终模型
torch.save({
    'model_state_dict': model.state_dict(),
    'scaler': scaler,
    'label_encoder': le,
    'input_dim': X_train_scaled.shape[1],
    'num_classes': len(le.classes_),
    'final_accuracy': accuracy,
    'model_architecture': 'AEClassificationNet'
}, 'trained_model_AE_FC.pth')

print("最终模型已保存到 trained_model_AE_FC.pth")

# 使用结果管理器保存模型
rm.copy_file('best_model_AE_FC.pth', 'best_model_AE_FC.pth')
rm.copy_file('trained_model_AE_FC.pth', 'trained_model_AE_FC.pth')

# 性能总结
performance_summary = f"""
{"="*60}
AE特征 + FC神经网络 性能总结
{"="*60}
训练样本数: {len(X_train_full)}
测试样本数: {len(y_test)}
特征维度: {X_train_scaled.shape[1]}
类别数量: {len(le.classes_)}
最佳验证准确率: {best_val_acc:.4f}
最终测试准确率: {accuracy:.4f}
训练轮数: {EPOCHS}
使用设备: {device}
{"="*60}
"""
print(performance_summary)

# 使用结果管理器保存性能摘要
rm.save_text(performance_summary, "performance_summary.txt")

# 创建实验摘要
rm.create_experiment_summary(
    model_name="AE_FC_Neural_Network",
    accuracy=accuracy,
    other_metrics={
        "training_samples": len(X_train_full),
        "test_samples": len(y_test),
        "feature_dimensions": X_train_scaled.shape[1],
        "num_classes": len(le.classes_),
        "best_validation_accuracy": best_val_acc,
        "epochs": EPOCHS,
        "device": device
    }
)

print("\n所有处理完成！")
print("生成的文件:")
print("- best_model_AE_FC.pth: 最佳验证模型")
print("- trained_model_AE_FC.pth: 最终训练模型")

# 结束实验
rm.finish("AE全连接网络分类实验完成")
print("- training_curves_AE_FC.png: 训练曲线图")
print("- prediction_results_AE_FC.csv: 预测结果")
print("- classification_AE_FC_report.csv: 分类报告")
print("- confusion_matrix_AE_FC.csv: 混淆矩阵数据")
print("- confusion_matrix_AE_FC.png: 混淆矩阵图像")
