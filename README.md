# Qwen TAU2019 城市音频场景分类项目

## 项目概述

本项目基于TAU Urban Acoustic Scenes 2019数据集，使用Qwen模型提取的音频特征进行城市音频场景分类研究。项目实现了多种分类方法，包括传统机器学习、深度学习和特征融合等技术。

## 🚀 核心特性

### 1. 智能训练管理
- **动态Epochs**: 不再需要预设固定的训练轮数，支持最大500轮，实际由早停机制智能控制
- **双重早停机制**:
  - 主要机制：学习率降至1e-5时自动停止（基于余弦退火调度器）
  - 辅助机制：验证准确率连续20轮无提升时停止
- **余弦退火学习率调度**: 从0.001开始，100轮为一个周期，最小值1e-6
- **自动最佳模型保存**: 训练过程中自动保存验证准确率最高的模型

### 2. 统一网络架构
- 所有FC脚本使用相同的`AudioClassificationNet`网络结构
- 网络层次：输入 → 512 → 256 → 128 → 64 → 输出
- 支持ReLU激活和Dropout正则化
- 统一的数据集处理类`AudioFeatureDataset`

### 3. 集中参数配置
- 所有训练参数集中在`training_config.py`中管理
- 支持灵活的配置获取和默认值设置
- 包含数据处理、模型训练、早停等全部配置

### 4. 自动结果管理
- 实验结果按时间戳自动分类保存
- 支持模型文件、CSV报告、图像、日志等多种格式
- 自动生成实验摘要和性能报告
- 历史结果自动归档，避免覆盖

### 5. 详细进度监控
- 每5轮显示详细训练进度（可配置）
- 实时显示：损失、训练准确率、验证准确率、学习率
- 训练结束提供完整摘要：实际训练轮数、早停原因、最佳性能

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
├── ⚙️ 统一架构和配置
│   ├── simple_network.py              # 统一网络架构定义
│   ├── training_config.py             # 集中训练参数配置
│   ├── test_training_config.py        # 配置测试脚本
│   └── requirements.txt               # 项目依赖
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
- **模型**: 统一的AudioClassificationNet网络架构
- **训练**: 支持动态epochs，智能早停，余弦退火学习率
- **设备支持**: GPU/MPS/CPU自动选择
- **输出目录**: `experiment_results/Qwen_AE_FC_Classification/`

#### AS特征深度学习 (`Qwen_ASweight_FC_env.py`)
- **特征**: Qwen提取的AS特征
- **模型**: 统一的AudioClassificationNet网络架构
- **训练**: 支持动态epochs，智能早停，余弦退火学习率
- **设备支持**: GPU/MPS/CPU自动选择
- **输出目录**: `experiment_results/Qwen_AS_FC_Classification/`

### 3. 特征融合方法

#### AE+AS特征融合 (`Qwen_AEAS_FC_env.py`)
- **特征**: AE和AS特征拼接融合
- **模型**: 统一的AudioClassificationNet网络架构
- **训练**: 支持动态epochs，智能早停，余弦退火学习率
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

### 2. 测试配置
```bash
# 测试训练配置和早停机制
python test_training_config.py

# 测试结果管理器
python test_result_manager.py

# 运行智能训练演示（使用合成数据）
python demo_intelligent_training.py
```

### 3. 运行实验
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

### 4. 查看结果
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
1. **早停机制**: 可在`training_config.py`中调整学习率阈值和验证耐心值
2. **学习率调度**: 调整余弦退火的周期长度和最小学习率
3. **网络架构**: 可在`simple_network.py`中修改网络层数和节点数
4. **PCA维度**: 建议在0.9-0.99之间调整保留方差比例
5. **批处理大小**: 根据内存情况调整batch_size

### 性能优化
1. **数据预处理**: 确保特征标准化
2. **智能早停**: 利用学习率阈值避免过拟合
3. **模型选择**: 训练过程自动保存最佳模型
4. **进度监控**: 实时观察训练状态，及时调整参数

## 📝 实验记录

### 典型实验流程
1. **数据加载**: 加载TAU2019数据集和Qwen特征
2. **数据预处理**: 特征标准化、降维、编码
3. **模型初始化**: 使用统一的网络架构和参数配置
4. **智能训练**: 动态epochs，余弦退火学习率，双重早停机制
5. **最佳模型保存**: 训练过程中自动保存验证准确率最高的模型
6. **结果评估**: 使用最佳模型计算各种性能指标
7. **结果保存**: 自动保存到时间戳文件夹，包含训练摘要
8. **可视化**: 生成混淆矩阵、训练曲线等图表

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
