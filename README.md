# Qwen TAU2019 城市音频场景分类项目

## 项目概述

本项目基于TAU Urban Acoustic Scenes 2019数据集，使用Qwen模型提取的音频特征进行城市音频场景分类研究。项目实现了多种分类方法，包括传统机器学习、深度学习和特征融合等技术。

## 🎯 项目目标

- 利用Qwen模型提取的音频特征进行城市声场景分类
- 比较不同特征类型（AE、AS）的分类性能
- 探索特征融合和聚类增强等技术
- 建立自动化的实验结果管理系统

## 📁 项目结构

```
Qwen_with_TAU2019/
├── 📊 数据集
│   └── TAU-urban-acoustic-scenes-2019-development/
├── 🧠 特征文件  
│   └── new_Feature/                    # Qwen提取的音频特征
│       ├── *-aAE.npy                  # AE特征文件
│       └── *-aAS.npy                  # AS特征文件
├── 🚀 主要实验脚本
│   ├── Qwen_AEweight_env.py           # AE特征 + PCA + SVM
│   ├── Qwen_ASweight_env.py           # AS特征 + PCA + SVM  
│   ├── Qwen_AEweight_FC_env.py        # AE特征 + 全连接网络
│   ├── Qwen_ASweight_FC_env.py        # AS特征 + 全连接网络
│   ├── Qwen_AEAS_FC_env.py            # AE+AS特征融合 + 全连接网络
│   └── Qwen_AEAS_Clustering_env.py    # AE+AS特征 + 聚类增强分类
├── 🔧 辅助脚本
│   ├── Qwen_AE_weight.py              # AE权重分析
│   ├── Qwen_AS_weight.py              # AS权重分析
│   ├── Qwen_task1_accuracy.py         # 任务1准确率评估
│   ├── Qwen_Task1_fastver.py          # 任务1快速版本
│   ├── Qwen_task2_part1.py            # 任务2第一部分
│   └── Qwen_Task2_SVM.py              # 任务2 SVM实现
├── 📈 分析工具
│   ├── analyze_prediction_differences.py  # 预测差异分析
│   └── compare_AE_AS_reports.py           # AE/AS结果比较
├── 🗃️ 结果管理系统
│   ├── result_manager.py              # 结果管理器核心
│   ├── test_result_manager.py         # 测试脚本
│   ├── experiment_results/            # 按时间分类的实验结果
│   └── archived_results/              # 历史结果存档
└── 📖 文档
    ├── README.md                      # 项目总览（本文件）
    └── README_结果管理系统.md          # 结果管理系统说明
```

## 🔬 实验方法

### 1. 传统机器学习方法

#### AE特征分类 (`Qwen_AEweight_env.py`)
- **特征**: Qwen提取的AE特征
- **预处理**: 标准化 + PCA降维
- **模型**: 支持向量机(SVM)
- **输出目录**: `experiment_results/Qwen_AE_Classification/`

#### AS特征分类 (`Qwen_ASweight_env.py`)
- **特征**: Qwen提取的AS特征
- **预处理**: 标准化 + PCA降维
- **模型**: 支持向量机(SVM)
- **输出目录**: `experiment_results/Qwen_AS_Classification/`

### 2. 深度学习方法

#### AE特征深度学习 (`Qwen_AEweight_FC_env.py`)
- **特征**: Qwen提取的AE特征
- **模型**: 全连接神经网络
- **设备支持**: GPU/MPS/CPU自动选择
- **输出目录**: `experiment_results/Qwen_AE_FC_Classification/`

#### AS特征深度学习 (`Qwen_ASweight_FC_env.py`)
- **特征**: Qwen提取的AS特征
- **模型**: 全连接神经网络
- **设备支持**: GPU/MPS/CPU自动选择
- **输出目录**: `experiment_results/Qwen_AS_FC_Classification/`

### 3. 特征融合方法

#### AE+AS特征融合 (`Qwen_AEAS_FC_env.py`)
- **特征**: AE和AS特征拼接融合
- **模型**: 全连接神经网络
- **优势**: 利用多种特征的互补信息
- **输出目录**: `experiment_results/Qwen_AEAS_FC_Classification/`

### 4. 聚类增强方法

#### 聚类增强分类 (`Qwen_AEAS_Clustering_env.py`)
- **特征**: AE+AS特征融合
- **方法**: K-means聚类 + 分类器
- **技术**: PCA降维 + 聚类增强
- **输出目录**: `experiment_results/Qwen_AEAS_Clustering_Classification/`

## 🎵 数据集信息

### TAU Urban Acoustic Scenes 2019 Development Dataset

- **场景类别**: 10个城市声场景
  - Airport (机场)
  - Bus (公交车)
  - Metro (地铁)
  - Metro station (地铁站)
  - Park (公园)
  - Public square (公共广场)
  - Shopping mall (购物中心)
  - Street pedestrian (步行街)
  - Street traffic (交通街道)
  - Tram (电车)

- **数据规模**: 每个场景包含多个音频文件
- **特征提取**: 使用Qwen模型提取AE和AS特征

## 🏆 性能指标

所有实验都会自动计算和保存以下指标：

- **准确率 (Accuracy)**: 整体分类准确率
- **精确率 (Precision)**: 各类别精确率
- **召回率 (Recall)**: 各类别召回率
- **F1分数 (F1-score)**: 各类别F1分数
- **混淆矩阵**: 详细的分类结果矩阵
- **训练曲线**: 损失和准确率变化曲线（深度学习方法）

## 🛠️ 环境要求

### Python依赖
```bash
numpy>=1.21.0
pandas>=1.3.0
scikit-learn>=1.0.0
torch>=1.9.0
matplotlib>=3.5.0
seaborn>=0.11.0
tqdm>=4.62.0
```

### 硬件要求
- **CPU**: 支持多核处理
- **内存**: 建议8GB以上
- **GPU**: 可选，支持CUDA或MPS加速
- **存储**: 建议10GB以上可用空间

## 🚀 快速开始

### 1. 环境准备
```bash
# 克隆项目
git clone [项目地址]
cd Qwen_with_TAU2019

# 安装依赖
pip install -r requirements.txt
```

### 2. 运行实验
```bash
# 运行AE特征分类实验
python Qwen_AEweight_env.py

# 运行AS特征分类实验  
python Qwen_ASweight_env.py

# 运行深度学习实验
python Qwen_AEweight_FC_env.py

# 运行特征融合实验
python Qwen_AEAS_FC_env.py

# 运行聚类增强实验
python Qwen_AEAS_Clustering_env.py
```

### 3. 查看结果
实验结果会自动保存到 `experiment_results/` 目录下，按时间戳分类：
```
experiment_results/
├── Qwen_AE_Classification/2025-06-20_14-30-15/
├── Qwen_AS_Classification/2025-06-20_14-35-22/
└── ...
```

## 📊 结果管理系统

本项目配备了完善的自动化结果管理系统：

### 主要功能
- ✅ **自动时间戳分类**: 按 `年-月-日_时-分-秒` 格式创建结果文件夹
- ✅ **多格式支持**: 支持CSV、JSON、图片、模型文件等
- ✅ **实验日志**: 自动记录运行时间和操作日志
- ✅ **实验摘要**: 生成标准化的实验总结
- ✅ **历史管理**: 自动整理和存档历史结果

### 生成文件类型
每次实验都会生成：
- `run_log.txt` - 详细运行日志
- `experiment_summary.json` - 机器可读的实验摘要
- `experiment_summary.txt` - 人类可读的实验摘要
- `performance_summary.txt` - 性能总结
- `classification_report.csv` - 分类报告
- `confusion_matrix.csv` - 混淆矩阵数据
- `confusion_matrix.png` - 混淆矩阵可视化
- 模型文件和其他结果文件

## 📈 分析工具

### 预测差异分析 (`analyze_prediction_differences.py`)
- 比较不同模型的预测差异
- 分析错误分类样本
- 生成详细的差异报告

### AE/AS结果比较 (`compare_AE_AS_reports.py`)
- 对比AE和AS特征的分类性能
- 生成性能对比图表
- 提供改进建议

## 🔍 实验建议

### 参数调优
1. **PCA维度**: 建议在0.9-0.99之间调整保留方差比例
2. **SVM参数**: 可调整C值和核函数类型
3. **神经网络**: 调整学习率、批大小、网络层数
4. **聚类数量**: 根据数据特性调整聚类中心数量

### 性能优化
1. **数据预处理**: 确保特征标准化
2. **特征选择**: 考虑特征重要性分析
3. **模型集成**: 可尝试多模型融合
4. **交叉验证**: 使用k折交叉验证提高可靠性

## 📝 实验记录

### 典型实验流程
1. **数据加载**: 加载TAU2019数据集和Qwen特征
2. **数据预处理**: 特征标准化、降维、编码
3. **模型训练**: 根据选择的方法训练模型
4. **结果评估**: 计算各种性能指标
5. **结果保存**: 自动保存到时间戳文件夹
6. **可视化**: 生成混淆矩阵、训练曲线等图表

### 结果对比
各方法的典型性能范围（实际结果可能因数据和参数而异）：
- **AE+PCA+SVM**: 75-85%
- **AS+PCA+SVM**: 70-80%
- **AE+深度学习**: 80-90%
- **AS+深度学习**: 75-85%
- **AE+AS特征融合**: 85-95%
- **聚类增强方法**: 80-90%

## 🤝 贡献指南

### 添加新实验
1. 创建新的实验脚本
2. 导入并使用 `ResultManager`
3. 按照标准格式保存结果
4. 更新README文档

### 代码规范
- 使用清晰的变量名和注释
- 遵循Python PEP8规范
- 添加适当的错误处理
- 包含必要的文档字符串

## 📞 技术支持

### 常见问题
1. **内存不足**: 减少批大小或样本数量
2. **GPU不可用**: 系统会自动切换到CPU
3. **特征文件缺失**: 检查 `new_Feature/` 目录
4. **依赖包问题**: 使用 `pip install -r requirements.txt`

### 调试技巧
- 检查 `run_log.txt` 中的详细日志
- 使用小数据集进行初步测试
- 验证特征文件的完整性
- 确保CSV文件格式正确

## 📄 许可证

本项目遵循相应的开源许可证，详见LICENSE文件。

## 🙏 致谢

- TAU Urban Acoustic Scenes 2019数据集提供者
- Qwen模型开发团队
- 开源社区的各种工具和库

---

**最后更新**: 2025年6月20日  
**版本**: v1.0  
**作者**: [项目作者]

> 💡 **提示**: 本项目持续更新中，如有问题或建议，欢迎提交Issue或Pull Request！
