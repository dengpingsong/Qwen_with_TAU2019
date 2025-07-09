# 简化版音频场景分类工具使用说明

## 概述

这套工具将原来的多个 Python 脚本整合成了4个简单的功能性脚本：

1. **extract_features.py** - 音频特征提取
2. **train_classifier.py** - 分类器训练
3. **run_experiments.py** - 批量实验运行
4. **config.py** - 配置参数

## 主要改进

- ✅ **去除类设计** - 改用简单的函数实现
- ✅ **统一接口** - 所有脚本使用相同的参数命名
- ✅ **简化配置** - 用简单的字典替代复杂的配置类
- ✅ **减少依赖** - 最小化外部依赖
- ✅ **易于使用** - 提供命令行接口和批量运行

## 使用方法

### 1. 特征提取

```bash
# 提取 AE 特征 (默认)
python extract_features.py

# 提取其他类型特征
python extract_features.py --mode AS
python extract_features.py --mode bi
python extract_features.py --mode clustering

# 自定义路径
python extract_features.py --mode AE --audio_folder ./audio --output_folder ./features
```

### 2. 训练分类器

```bash
# 训练 SVM 分类器 (默认)
python train_classifier.py --feature_type AE

# 训练其他分类器
python train_classifier.py --feature_type AE --classifier rf
python train_classifier.py --feature_type AS --classifier lr

# 自定义参数
python train_classifier.py --feature_type bi --classifier svm --training_size 1500
```

### 3. 运行完整实验

```bash
# 运行单个完整实验 (特征提取 + 训练)
python run_experiments.py --mode single --feature_types AE --classifiers svm

# 批量运行多个实验
python run_experiments.py --mode batch --feature_types AE AS bi --classifiers svm rf lr

# 只提取特征
python run_experiments.py --mode extract --feature_types AE AS

# 只训练分类器
python run_experiments.py --mode train --feature_types AE --classifiers svm rf
```

## 支持的选项

### 特征类型 (feature_types)
- **AE**: Audio Event 特征
- **AS**: Acoustic Scene 特征  
- **bi**: 二分类场景特征 (机场/非机场)
- **clustering**: 聚类特征
- **general**: 通用特征

### 分类器类型 (classifiers)
- **svm**: 支持向量机 (线性核)
- **rf**: 随机森林
- **lr**: 逻辑回归

## 输出结果

每个实验会在 `./results/{feature_type}_{classifier_type}/` 目录下生成：

- `model_{feature_type}_{classifier_type}.pkl` - 训练好的模型
- `report_{feature_type}_{classifier_type}.csv` - 分类报告
- `confusion_{feature_type}_{classifier_type}.csv` - 混淆矩阵数据
- `confusion_{feature_type}_{classifier_type}.png` - 混淆矩阵图

## 配置修改

可以直接编辑 `config.py` 文件来修改默认参数：

```python
# 修改训练样本数
TRAIN_CONFIG['training_sample_size'] = 3000

# 修改数据路径
DATA_PATHS['audio_folder'] = "/path/to/your/audio"

# 修改分类器参数
CLASSIFIER_PARAMS['svm']['C'] = 2.0
```

## 常用命令示例

```bash
# 快速开始 - 运行 AE+SVM 实验
python run_experiments.py

# 批量测试所有特征和分类器组合
python run_experiments.py --mode batch \
    --feature_types AE AS bi \
    --classifiers svm rf lr

# 只提取所有类型特征
python run_experiments.py --mode extract \
    --feature_types AE AS bi clustering

# 使用已有特征训练多个分类器
python run_experiments.py --mode train \
    --feature_types AE \
    --classifiers svm rf lr
```

## 与原脚本的对应关系

| 原脚本 | 新脚本 | 功能 |
|--------|--------|------|
| Qwen_*_weight.py | extract_features.py | 特征提取 |
| Qwen_*_weight_env.py | train_classifier.py | 分类训练 |
| training_config.py | config.py | 配置管理 |
| 多个分析脚本 | run_experiments.py | 批量运行 |

## 注意事项

1. **内存管理**: 大批量处理时注意内存使用
2. **GPU 支持**: 特征提取会自动使用可用的 GPU
3. **文件路径**: 确保音频文件和元数据文件路径正确
4. **依赖安装**: 确保安装了所有必要的 Python 包

## 故障排除

1. **找不到音频文件**: 检查 `--audio_folder` 路径
2. **找不到特征文件**: 先运行特征提取步骤
3. **内存不足**: 减少 `batch_size` 或 `training_size`
4. **模型加载失败**: 检查网络连接和 Hugging Face 访问
