import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import IncrementalPCA
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from tqdm import tqdm  # 引入进度条库
import matplotlib.pyplot as plt
import seaborn as sns
import random
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']  # 支持中文显示
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

# 读取 CSV
csv_path = "./TAU-urban-acoustic-scenes-2019-development/meta.csv"
df = pd.read_csv(csv_path,index_col=3, delimiter='\t')

# 设定批处理参数
BATCH_SIZE = 200  # 每批处理的文件数量
data_dir = "./new_Feature"

# 获取所有符合条件的文件列表
all_files = []
for file in os.listdir(data_dir):
    if file.endswith(".npy") and file.find("AS") == -1:  # 确保文件名不包含 "AS"，只处理AE文件
        filename_key = 'audio/'+file.replace(".npy", ".wav")  # 添加 .wav 后缀以匹配 CSV
        filename_key = filename_key.replace("AE", "")  # 去掉AE以匹配 CSV 中的文件名
        
        # 检查 filename_key 是否在 CSV 中
        if filename_key in df["filename"].values:
            label = df.loc[df["filename"] == filename_key, "scene_label"].values[0]
            all_files.append((file, label))

print(f"找到 {len(all_files)} 个数据文件")

# 随机打乱文件列表
random.seed(42)
random.shuffle(all_files)

# 划分训练集和测试集
split_idx = int(len(all_files) * 0.8)
train_files = all_files[:split_idx]
test_files = all_files[split_idx:]

print(f"训练集: {len(train_files)} 个文件，测试集: {len(test_files)} 个文件")

# 初始化预处理器和模型
scaler = StandardScaler()
pca = None
classifier = SGDClassifier(loss='hinge', random_state=42, max_iter=1000)

# 标签编码
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
all_labels = [label for _, label in all_files]
label_encoder.fit(all_labels)

def load_batch_data(file_batch):
    """加载一批数据"""
    X_batch = []
    y_batch = []
    
    for file, label in file_batch:
        file_path = os.path.join(data_dir, file)
        try:
            data = np.load(file_path).flatten()
            X_batch.append(data)
            y_batch.append(label)
        except Exception as e:
            print(f"加载文件 {file} 时出错: {e}")
            continue
    
    if len(X_batch) == 0:
        return None, None
    
    return np.array(X_batch), np.array(y_batch)

print("开始分批训练...")

# 第一阶段：拟合预处理器
print("第一阶段：拟合预处理器...")
for i in tqdm(range(0, len(train_files), BATCH_SIZE), desc="预处理器拟合"):
    batch_files = train_files[i:i+BATCH_SIZE]
    X_batch, y_batch = load_batch_data(batch_files)
    
    if X_batch is None:
        continue
    
    # 部分拟合标准化器
    scaler.partial_fit(X_batch)
    
    # 第一次处理时初始化PCA
    if pca is None:
        # 使用IncrementalPCA，组件数量不能超过批次样本数量
        n_features = X_batch.shape[1]
        n_samples = X_batch.shape[0]
        # 组件数量取样本数、特征数和期望值的最小值
        n_components = min(n_samples, n_features, 200)  # 限制最大200个组件
        pca = IncrementalPCA(n_components=n_components, batch_size=min(BATCH_SIZE, n_samples))
        print(f"初始化IncrementalPCA - 批次大小: {n_samples}, 特征数量: {n_features}, PCA组件数量: {n_components}")
    
    # 标准化后进行PCA拟合
    X_batch_scaled = scaler.transform(X_batch)
    pca.partial_fit(X_batch_scaled)

# 第二阶段：训练分类器
print("第二阶段：训练分类器...")
for i in tqdm(range(0, len(train_files), BATCH_SIZE), desc="模型训练"):
    batch_files = train_files[i:i+BATCH_SIZE]
    X_batch, y_batch = load_batch_data(batch_files)
    
    if X_batch is None:
        continue
    
    # 预处理
    X_batch_scaled = scaler.transform(X_batch)
    X_batch_pca = pca.transform(X_batch_scaled)
    y_batch_encoded = label_encoder.transform(y_batch)
    
    # 增量训练
    classifier.partial_fit(X_batch_pca, y_batch_encoded, classes=range(len(label_encoder.classes_)))

print("训练完成！开始测试...")

# 测试阶段
y_test_true = []
y_test_pred = []

for i in tqdm(range(0, len(test_files), BATCH_SIZE), desc="模型测试"):
    batch_files = test_files[i:i+BATCH_SIZE]
    X_batch, y_batch = load_batch_data(batch_files)
    
    if X_batch is None:
        continue
    
    # 预处理
    X_batch_scaled = scaler.transform(X_batch)
    X_batch_pca = pca.transform(X_batch_scaled)
    
    # 预测
    y_pred_batch = classifier.predict(X_batch_pca)
    y_pred_batch_labels = label_encoder.inverse_transform(y_pred_batch)
    
    y_test_true.extend(y_batch)
    y_test_pred.extend(y_pred_batch_labels)

# 转换为numpy数组
y_test = np.array(y_test_true)
y_pred = np.array(y_test_pred)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print(f"增量学习分类准确率: {accuracy:.4f}")

# 生成分类报告
report = classification_report(y_test, y_pred, output_dict=True)

# 将分类报告转换为 DataFrame
report_df = pd.DataFrame(report).transpose()

# 将分类报告保存为 CSV
report_csv_path = "classification_PCA_AE_report.csv"
report_df.to_csv(report_csv_path, index=True)

print(f"分类报告已保存为 CSV 文件：{report_csv_path}")

# 生成混淆矩阵
cm = confusion_matrix(y_test, y_pred)
print(f"\n混淆矩阵:\n{cm}")

# 获取类别标签
class_labels = sorted(np.unique(np.concatenate([y_test, y_pred])))

# 创建混淆矩阵的 DataFrame
cm_df = pd.DataFrame(cm, index=class_labels, columns=class_labels)

# 保存混淆矩阵为 CSV
cm_csv_path = "confusion_matrix.csv"
cm_df.to_csv(cm_csv_path, index=True)
print(f"混淆矩阵已保存为 CSV 文件：{cm_csv_path}")

# 可视化混淆矩阵
plt.figure(figsize=(12, 10))
sns.heatmap(cm_df, annot=True, fmt='d', cmap='Blues', 
            cbar_kws={'label': '预测数量'})
plt.title('混淆矩阵', fontsize=16, fontweight='bold')
plt.xlabel('预测标签', fontsize=12)
plt.ylabel('真实标签', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()

# 保存混淆矩阵图
cm_plot_path = "AE_confusion_matrix.png"
plt.savefig(cm_plot_path, dpi=300, bbox_inches='tight')
print(f"混淆矩阵图已保存为：{cm_plot_path}")
plt.show()

# 计算并显示每个类别的准确率
class_accuracy = cm.diagonal() / cm.sum(axis=1)
print(f"\n各类别准确率:")
for i, label in enumerate(class_labels):
    print(f"{label}: {class_accuracy[i]:.2f}")

# 保存各类别准确率
class_acc_df = pd.DataFrame({
    'Class': class_labels,
    'Accuracy': class_accuracy
})
class_acc_csv_path = "AE_class_accuracy.csv"
class_acc_df.to_csv(class_acc_csv_path, index=False)
print(f"各类别准确率已保存为 CSV 文件：{class_acc_csv_path}")
