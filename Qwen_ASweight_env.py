import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from tqdm import tqdm  # 引入进度条库
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']  # 支持中文显示
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

# 读取 CSV
csv_path = "./TAU-urban-acoustic-scenes-2019-development/meta.csv"
df = pd.read_csv(csv_path,index_col=3, delimiter='\t')

# 读取 npy 文件
data_dir = "./new_Feature"
X, y = [], []

# 读取数据并加入进度条
for file in tqdm(os.listdir(data_dir), desc="加载数据", unit="文件"):
    if file.endswith(".npy") and file.find("AE") == -1:  # 确保文件名不包含 "AS"
        file_path = os.path.join(data_dir, file)
        filename_key = 'audio/'+file.replace(".npy", ".wav")  # 添加 .wav 后缀以匹配 CSV
        filename_key = filename_key.replace("AS", "")  # 去掉AE以匹配 CSV 中的文件名

        # 检查 filename_key 是否在 CSV 中
        if filename_key in df["filename"].values:
            X.append(np.load(file_path).flatten())  # 展平数据
            y.append(df.loc[df["filename"] == filename_key, "scene_label"].values[0])

# 转换为 numpy 数组
X = np.array(X)
y = np.array(y)

# **添加数据检查**
if len(X) == 0:
    raise ValueError("没有加载任何数据，请检查 CSV 和 npy 文件名是否匹配！")

# 数据集划分
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 数据标准化
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# **加入 PCA**
pca = PCA(n_components=0.95)  # 选 95% 的信息
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)

# 训练 SVM
svm_model = SVC(kernel="linear", C=1.0)

# 使用 tqdm 显示训练的进度
tqdm.write("开始训练模型...")
svm_model.fit(X_train, y_train)  # 训练模型

# 预测并显示进度
tqdm.write("开始预测...")
y_pred = []
for i in tqdm(range(len(X_test)), desc="预测进度", unit="样本"):
    y_pred.append(svm_model.predict([X_test[i]]))  # 逐个预测
y_pred = np.array(y_pred).flatten()  # 转换为 numpy 数组

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print(f"SVM + PCA 分类准确率: {accuracy:.2f}")

# 生成分类报告
report = classification_report(y_test, y_pred, output_dict=True)

# 将分类报告转换为 DataFrame
report_df = pd.DataFrame(report).transpose()

# 将分类报告保存为 CSV
report_csv_path = "classification_PCA_AS_report.csv"
report_df.to_csv(report_csv_path, index=True)

print(f"分类报告已保存为 CSV 文件：{report_csv_path}")

# 生成混淆矩阵
cm = confusion_matrix(y_test, y_pred)
print(f"\n混淆矩阵:\n{cm}")

# 获取类别标签
class_labels = sorted(np.unique(y))

# 创建混淆矩阵的 DataFrame
cm_df = pd.DataFrame(cm, index=class_labels, columns=class_labels)

# 保存混淆矩阵为 CSV
cm_csv_path = "AS_confusion_matrix.csv"
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
cm_plot_path = "confusion_matrix.png"
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
class_acc_csv_path = "AS_class_accuracy.csv"
class_acc_df.to_csv(class_acc_csv_path, index=False)
print(f"各类别准确率已保存为 CSV 文件：{class_acc_csv_path}")
