# 实验结果管理系统使用说明

## 概述
这个系统已经为你的TAU2019音频分类项目添加了自动的结果管理功能。每次运行实验时，所有结果文件都会按照时间戳自动分类保存。

## 系统功能

### 1. 自动文件整理
- 现有的60个结果文件已经移动到：`archived_results/archive_2025-06-20_13-12-49/`
- 包含所有的CSV报告、PNG图像、模型文件等
- 生成了整理日志文件：`organize_log.txt`

### 2. 时间戳分类
每次运行脚本时，结果会保存到以下格式的文件夹：
```
experiment_results/
├── Qwen_AE_Classification/
│   └── 2025-06-20_14-30-15/    # 年-月-日_时-分-秒
│       ├── run_log.txt
│       ├── experiment_summary.json
│       ├── performance_summary.txt
│       └── [其他结果文件]
├── Qwen_AS_Classification/
├── Qwen_AE_FC_Classification/
└── Qwen_AS_FC_Classification/
```

### 3. 修改的脚本

以下脚本已经添加了结果管理功能：

#### `Qwen_AEweight_env.py`
- 项目名称: `Qwen_AE_Classification`
- 自动保存: 分类报告、混淆矩阵、图像
- 实验摘要: 包含准确率、样本数、PCA维度等

#### `Qwen_ASweight_env.py`
- 项目名称: `Qwen_AS_Classification`
- 自动保存: 分类报告、混淆矩阵、图像
- 实验摘要: 包含准确率、样本数、PCA维度等

#### `Qwen_AEweight_FC_env.py`
- 项目名称: `Qwen_AE_FC_Classification`
- 自动保存: 模型文件、训练结果、性能摘要
- 实验摘要: 包含准确率、模型架构、设备信息等

#### `Qwen_ASweight_FC_env.py`
- 项目名称: `Qwen_AS_FC_Classification`
- 自动保存: 模型文件、训练结果、性能摘要
- 实验摘要: 包含准确率、模型架构、设备信息等

#### `Qwen_AEAS_FC_env.py` ⭐ 新增
- 项目名称: `Qwen_AEAS_FC_Classification`
- 自动保存: 特征融合模型、分类报告、混淆矩阵
- 实验摘要: 包含融合特征维度、准确率、设备信息等
- 特色: AE+AS特征融合分类

#### `Qwen_AEAS_Clustering_env.py` ⭐ 新增
- 项目名称: `Qwen_AEAS_Clustering_Classification`
- 自动保存: 聚类结果、分类报告、可视化图表
- 实验摘要: 包含聚类数量、PCA维度、分类准确率等
- 特色: 聚类增强分类方法

## 使用方法

### 运行实验脚本
正常运行任何env脚本，结果会自动分类保存：
```bash
# 传统机器学习方法
python Qwen_AEweight_env.py     # AE + PCA + SVM
python Qwen_ASweight_env.py     # AS + PCA + SVM

# 深度学习方法
python Qwen_AEweight_FC_env.py  # AE + 全连接网络
python Qwen_ASweight_FC_env.py  # AS + 全连接网络

# 特征融合和高级方法
python Qwen_AEAS_FC_env.py            # AE+AS特征融合
python Qwen_AEAS_Clustering_env.py    # 聚类增强分类
```

### 直接使用结果管理器
```python
from result_manager import ResultManager

# 创建管理器
rm = ResultManager(project_name="你的实验名称")

# 保存各种格式文件
rm.save_csv(dataframe, "results.csv")
rm.save_json(data, "config.json")
rm.save_text("实验日志", "log.txt")

# 保存实验摘要
rm.create_experiment_summary("模型名称", 0.95, {"其他指标": "值"})

# 结束实验
rm.finish("实验完成")
```

## 生成的文件说明

每次实验运行后，会在时间戳文件夹中生成：

1. **run_log.txt** - 运行日志，记录所有操作时间
2. **experiment_summary.json** - JSON格式的实验摘要
3. **experiment_summary.txt** - 文本格式的实验摘要
4. **performance_summary.txt** - 性能总结
5. **原始结果文件** - 分类报告、混淆矩阵、模型文件等

## 优势

1. **历史记录完整** - 每次实验都有独立的时间戳文件夹
2. **易于比较** - 可以轻松比较不同时间的实验结果
3. **自动化管理** - 无需手动整理文件
4. **详细日志** - 记录每个操作的时间和内容
5. **标准化输出** - 统一的实验摘要格式

## 注意事项

- 确保有足够的磁盘空间存储历史结果
- 结果管理器会自动创建必要的目录
- 所有原始脚本的输出逻辑保持不变，只是额外添加了分类保存功能
- 如果需要清理旧的实验结果，可以手动删除相应的时间戳文件夹

## 文件结构示例

```
/Users/apple/Documents/Qwen_with_TAU2019/
├── archived_results/           # 历史文件存档
│   └── archive_2025-06-20_13-12-49/
├── experiment_results/         # 新的实验结果
│   ├── Qwen_AE_Classification/
│   ├── Qwen_AS_Classification/
│   ├── Qwen_AE_FC_Classification/
│   ├── Qwen_AS_FC_Classification/
│   ├── Qwen_AEAS_FC_Classification/           # 新增
│   └── Qwen_AEAS_Clustering_Classification/   # 新增
├── result_manager.py          # 结果管理器
├── Qwen_AEweight_env.py       # 修改后的脚本
├── Qwen_ASweight_env.py       # 修改后的脚本
├── Qwen_AEweight_FC_env.py    # 修改后的脚本
├── Qwen_ASweight_FC_env.py    # 修改后的脚本
├── Qwen_AEAS_FC_env.py        # 修改后的脚本 (新增)
└── Qwen_AEAS_Clustering_env.py # 修改后的脚本 (新增)
```

现在你的所有实验结果都会自动按时间分类保存了！
