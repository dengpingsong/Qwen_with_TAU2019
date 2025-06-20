import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Rectangle
import warnings
warnings.filterwarnings('ignore')

def load_classification_report(file_path):
    """加载分类报告文件"""
    try:
        df = pd.read_csv(file_path, index_col=0)
        # 去除accuracy、macro avg、weighted avg行，只保留类别结果
        class_names = [idx for idx in df.index if idx not in ['accuracy', 'macro avg', 'weighted avg']]
        return df.loc[class_names]
    except Exception as e:
        print(f"加载文件 {file_path} 时出错: {e}")
        return None

def load_confusion_matrix(file_path):
    """加载混淆矩阵文件"""
    try:
        df = pd.read_csv(file_path, index_col=0)
        return df
    except Exception as e:
        print(f"加载文件 {file_path} 时出错: {e}")
        return None

def compare_classification_reports(ae_report_path, as_report_path):
    """比较AE和AS分类报告"""
    print("="*60)
    print("PCA AE vs AS 分类报告比较分析")
    print("="*60)
    
    # 加载报告
    ae_report = load_classification_report(ae_report_path)
    as_report = load_classification_report(as_report_path)
    
    if ae_report is None or as_report is None:
        print("无法加载报告文件")
        return None, None
    
    # 确保两个报告有相同的类别
    common_classes = list(set(ae_report.index) & set(as_report.index))
    common_classes.sort()
    
    ae_report = ae_report.loc[common_classes]
    as_report = as_report.loc[common_classes]
    
    # 计算差异
    metrics = ['precision', 'recall', 'f1-score']
    comparison_results = {}
    
    print("\n各类别指标比较 (AE - AS):")
    print("-" * 80)
    print(f"{'类别':<18} {'Precision差异':<15} {'Recall差异':<15} {'F1-Score差异':<15}")
    print("-" * 80)
    
    for metric in metrics:
        comparison_results[metric] = ae_report[metric] - as_report[metric]
    
    for class_name in common_classes:
        prec_diff = comparison_results['precision'][class_name]
        recall_diff = comparison_results['recall'][class_name]
        f1_diff = comparison_results['f1-score'][class_name]
        
        print(f"{class_name:<18} {prec_diff:<15.4f} {recall_diff:<15.4f} {f1_diff:<15.4f}")
    
    # 整体性能比较
    print("\n" + "="*60)
    print("整体性能对比:")
    print("="*60)
    
    # 计算整体平均值
    ae_avg = ae_report[metrics].mean()
    as_avg = as_report[metrics].mean()
    
    print(f"{'指标':<15} {'AE平均值':<15} {'AS平均值':<15} {'差异(AE-AS)':<15}")
    print("-" * 60)
    for metric in metrics:
        print(f"{metric:<15} {ae_avg[metric]:<15.4f} {as_avg[metric]:<15.4f} {ae_avg[metric]-as_avg[metric]:<15.4f}")
    
    # 找出表现差异最大的类别
    print("\n" + "="*60)
    print("表现差异分析:")
    print("="*60)
    
    for metric in metrics:
        diff_series = comparison_results[metric]
        
        # AE表现更好的类别
        ae_better = diff_series[diff_series > 0].sort_values(ascending=False)
        # AS表现更好的类别
        as_better = diff_series[diff_series < 0].sort_values()
        
        print(f"\n{metric.upper()} - AE表现更好的类别:")
        for class_name, diff in ae_better.head(3).items():
            print(f"  {class_name}: +{diff:.4f}")
        
        print(f"\n{metric.upper()} - AS表现更好的类别:")
        for class_name, diff in as_better.head(3).items():
            print(f"  {class_name}: {diff:.4f}")
    
    return ae_report, as_report, comparison_results

def compare_confusion_matrices(ae_cm_path, as_cm_path):
    """比较AE和AS混淆矩阵"""
    print("\n" + "="*60)
    print("混淆矩阵比较分析")
    print("="*60)
    
    # 加载混淆矩阵
    ae_cm = load_confusion_matrix(ae_cm_path)
    as_cm = load_confusion_matrix(as_cm_path)
    
    if ae_cm is None or as_cm is None:
        print("无法加载混淆矩阵文件")
        return None, None, None
    
    # 确保两个矩阵有相同的类别和顺序
    common_classes = list(set(ae_cm.index) & set(as_cm.index))
    common_classes.sort()
    
    ae_cm = ae_cm.loc[common_classes, common_classes]
    as_cm = as_cm.loc[common_classes, common_classes]
    
    # 计算差异矩阵 (AE - AS)
    diff_cm = ae_cm - as_cm
    
    # 计算总体准确率
    ae_accuracy = np.trace(ae_cm) / ae_cm.sum().sum()
    as_accuracy = np.trace(as_cm) / as_cm.sum().sum()
    
    print(f"AE模型准确率: {ae_accuracy:.4f}")
    print(f"AS模型准确率: {as_accuracy:.4f}")
    print(f"准确率差异 (AE-AS): {ae_accuracy-as_accuracy:.4f}")
    
    # 分析对角线元素差异（正确分类的差异）
    print(f"\n各类别正确分类数量差异 (AE - AS):")
    print("-" * 40)
    diagonal_diff = np.diag(diff_cm)
    for i, class_name in enumerate(common_classes):
        print(f"{class_name:<18}: {diagonal_diff[i]:>6.0f}")
    
    return ae_cm, as_cm, diff_cm

def visualize_comparison(ae_report, as_report, comparison_results, ae_cm, as_cm, diff_cm):
    """可视化比较结果"""
    
    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False
    
    # 创建大图
    fig = plt.figure(figsize=(20, 15))
    
    # 1. 指标比较柱状图
    ax1 = plt.subplot(2, 3, 1)
    metrics = ['precision', 'recall', 'f1-score']
    x = np.arange(len(ae_report.index))
    width = 0.35
    
    for i, metric in enumerate(metrics):
        plt.subplot(2, 3, i+1)
        ae_values = ae_report[metric].values
        as_values = as_report[metric].values
        
        plt.bar(x - width/2, ae_values, width, label='AE', alpha=0.8)
        plt.bar(x + width/2, as_values, width, label='AS', alpha=0.8)
        
        plt.xlabel('类别')
        plt.ylabel(metric.capitalize())
        plt.title(f'{metric.capitalize()} 比较')
        plt.xticks(x, ae_report.index, rotation=45, ha='right')
        plt.legend()
        plt.grid(True, alpha=0.3)
    
    # 4. 差异热力图
    plt.subplot(2, 3, 4)
    diff_matrix = np.array([comparison_results[metric].values for metric in metrics]).T
    sns.heatmap(diff_matrix, 
                xticklabels=metrics,
                yticklabels=ae_report.index,
                annot=True, 
                fmt='.3f', 
                center=0,
                cmap='RdBu_r',
                cbar_kws={'label': 'AE - AS 差异'})
    plt.title('指标差异热力图 (AE - AS)')
    plt.xlabel('指标')
    plt.ylabel('类别')
    
    # 5. 混淆矩阵差异
    plt.subplot(2, 3, 5)
    sns.heatmap(diff_cm, 
                annot=True, 
                fmt='d', 
                center=0,
                cmap='RdBu_r',
                xticklabels=diff_cm.columns,
                yticklabels=diff_cm.index,
                cbar_kws={'label': '预测数量差异 (AE - AS)'})
    plt.title('混淆矩阵差异 (AE - AS)')
    plt.xlabel('预测类别')
    plt.ylabel('真实类别')
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    
    # 6. 整体性能对比雷达图
    ax6 = plt.subplot(2, 3, 6, projection='polar')
    
    # 计算每个类别的平均F1分数
    ae_f1_mean = ae_report['f1-score'].mean()
    as_f1_mean = as_report['f1-score'].mean()
    ae_prec_mean = ae_report['precision'].mean()
    as_prec_mean = as_report['precision'].mean()
    ae_recall_mean = ae_report['recall'].mean()
    as_recall_mean = as_report['recall'].mean()
    
    categories = ['Precision', 'Recall', 'F1-Score']
    ae_values = [ae_prec_mean, ae_recall_mean, ae_f1_mean]
    as_values = [as_prec_mean, as_recall_mean, as_f1_mean]
    
    # 添加第一个点以闭合图形
    ae_values += ae_values[:1]
    as_values += as_values[:1]
    
    angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]
    
    ax6.plot(angles, ae_values, 'o-', linewidth=2, label='AE', color='blue')
    ax6.fill(angles, ae_values, alpha=0.25, color='blue')
    ax6.plot(angles, as_values, 'o-', linewidth=2, label='AS', color='red')
    ax6.fill(angles, as_values, alpha=0.25, color='red')
    
    ax6.set_xticks(angles[:-1])
    ax6.set_xticklabels(categories)
    ax6.set_ylim(0, 1)
    ax6.set_title('整体性能对比', pad=20)
    ax6.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
    ax6.grid(True)
    
    plt.tight_layout()
    plt.savefig('PCA_AE_AS_comparison_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 创建专门的差异混淆矩阵图
    plt.figure(figsize=(12, 10))
    
    # 创建自定义colormap，突出显示差异
    mask_positive = diff_cm > 0
    mask_negative = diff_cm < 0
    mask_zero = diff_cm == 0
    
    # 绘制热力图
    ax = sns.heatmap(diff_cm, 
                     annot=True, 
                     fmt='d', 
                     center=0,
                     cmap='RdBu_r',
                     xticklabels=diff_cm.columns,
                     yticklabels=diff_cm.index,
                     cbar_kws={'label': '预测数量差异 (AE模型 - AS模型)'},
                     square=True)
    
    # 添加标题和标签
    plt.title('混淆矩阵差异分析\n(正值表示AE模型预测更多，负值表示AS模型预测更多)', 
              fontsize=14, pad=20)
    plt.xlabel('预测类别', fontsize=12)
    plt.ylabel('真实类别', fontsize=12)
    
    # 旋转标签以便阅读
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    
    # 添加网格线
    for i in range(len(diff_cm.index)):
        for j in range(len(diff_cm.columns)):
            if diff_cm.iloc[i, j] > 0:
                # AE表现更好的区域用绿色边框
                rect = Rectangle((j, i), 1, 1, linewidth=2, 
                               edgecolor='green', facecolor='none')
                ax.add_patch(rect)
            elif diff_cm.iloc[i, j] < 0:
                # AS表现更好的区域用红色边框
                rect = Rectangle((j, i), 1, 1, linewidth=2, 
                               edgecolor='red', facecolor='none')
                ax.add_patch(rect)
    
    # 添加图例
    from matplotlib.lines import Line2D
    legend_elements = [Line2D([0], [0], color='green', lw=2, label='AE预测更多'),
                      Line2D([0], [0], color='red', lw=2, label='AS预测更多')]
    plt.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1.02, 1))
    
    plt.tight_layout()
    plt.savefig('confusion_matrix_difference_AE_AS.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\n可视化图表已保存:")
    print(f"- 综合比较分析: PCA_AE_AS_comparison_analysis.png")
    print(f"- 混淆矩阵差异: confusion_matrix_difference_AE_AS.png")

def generate_summary_report(ae_report, as_report, comparison_results, ae_cm, as_cm, diff_cm):
    """生成总结报告"""
    
    # 计算整体统计
    ae_accuracy = np.trace(ae_cm) / ae_cm.sum().sum()
    as_accuracy = np.trace(as_cm) / as_cm.sum().sum()
    
    # 保存详细比较结果
    detailed_comparison = pd.DataFrame({
        'AE_precision': ae_report['precision'],
        'AS_precision': as_report['precision'],
        'precision_diff': comparison_results['precision'],
        'AE_recall': ae_report['recall'],
        'AS_recall': as_report['recall'],
        'recall_diff': comparison_results['recall'],
        'AE_f1': ae_report['f1-score'],
        'AS_f1': as_report['f1-score'],
        'f1_diff': comparison_results['f1-score']
    })
    
    detailed_comparison.to_csv('detailed_AE_AS_comparison.csv')
    
    # 保存差异矩阵
    diff_cm.to_csv('confusion_matrix_difference_AE_AS.csv')
    
    # 生成总结报告
    summary = []
    summary.append("="*80)
    summary.append("PCA AE vs AS 模型比较总结报告")
    summary.append("="*80)
    summary.append(f"报告生成时间: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}")
    summary.append("")
    
    summary.append("1. 整体性能对比:")
    summary.append(f"   AE模型准确率: {ae_accuracy:.4f}")
    summary.append(f"   AS模型准确率: {as_accuracy:.4f}")
    summary.append(f"   准确率差异: {ae_accuracy-as_accuracy:.4f}")
    summary.append("")
    
    summary.append("2. 平均指标对比:")
    for metric in ['precision', 'recall', 'f1-score']:
        ae_avg = ae_report[metric].mean()
        as_avg = as_report[metric].mean()
        summary.append(f"   {metric}: AE={ae_avg:.4f}, AS={as_avg:.4f}, 差异={ae_avg-as_avg:.4f}")
    summary.append("")
    
    summary.append("3. 表现最好的模型 (按类别):")
    for metric in ['precision', 'recall', 'f1-score']:
        ae_better_count = (comparison_results[metric] > 0).sum()
        as_better_count = (comparison_results[metric] < 0).sum()
        equal_count = (comparison_results[metric] == 0).sum()
        summary.append(f"   {metric}: AE更好={ae_better_count}类, AS更好={as_better_count}类, 相等={equal_count}类")
    summary.append("")
    
    summary.append("4. 各类别差异最大的前3名:")
    for metric in ['precision', 'recall', 'f1-score']:
        diff_abs = comparison_results[metric].abs().sort_values(ascending=False)
        summary.append(f"   {metric}差异最大:")
        for i, (class_name, diff_val) in enumerate(diff_abs.head(3).items()):
            actual_diff = comparison_results[metric][class_name]
            summary.append(f"     {i+1}. {class_name}: {actual_diff:.4f}")
    summary.append("")
    
    summary.append("5. 关键发现:")
    # 找出整体趋势
    if ae_accuracy > as_accuracy:
        summary.append(f"   - AE模型整体准确率更高 (+{ae_accuracy-as_accuracy:.4f})")
    else:
        summary.append(f"   - AS模型整体准确率更高 (+{as_accuracy-ae_accuracy:.4f})")
    
    # 找出最大改进
    best_improvement = comparison_results['f1-score'].max()
    best_class = comparison_results['f1-score'].idxmax()
    if best_improvement > 0:
        summary.append(f"   - AE在{best_class}类别上F1分数提升最大: +{best_improvement:.4f}")
    
    worst_decline = comparison_results['f1-score'].min()
    worst_class = comparison_results['f1-score'].idxmin()
    if worst_decline < 0:
        summary.append(f"   - AE在{worst_class}类别上F1分数下降最大: {worst_decline:.4f}")
    
    summary.append("")
    summary.append("6. 输出文件:")
    summary.append("   - detailed_AE_AS_comparison.csv: 详细比较数据")
    summary.append("   - confusion_matrix_difference_AE_AS.csv: 混淆矩阵差异")
    summary.append("   - PCA_AE_AS_comparison_analysis.png: 综合分析图表")
    summary.append("   - confusion_matrix_difference_AE_AS.png: 差异混淆矩阵图")
    summary.append("   - AE_AS_comparison_summary.txt: 本总结报告")
    summary.append("="*80)
    
    # 保存总结报告
    with open('AE_AS_comparison_summary.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(summary))
    
    # 打印总结
    print('\n'.join(summary))

def load_prediction_results(ae_file_path, as_file_path):
    """加载AE和AS的预测结果文件"""
    try:
        ae_df = pd.read_csv(ae_file_path)
        as_df = pd.read_csv(as_file_path)
        
        print(f"AE预测结果: {len(ae_df)} 条记录")
        print(f"AS预测结果: {len(as_df)} 条记录")
        
        return ae_df, as_df
    except Exception as e:
        print(f"加载预测结果文件时出错: {e}")
        return None, None

def find_inconsistent_samples(ae_df, as_df):
    """找出AE和AS预测不一致的样本"""
    # 基于文件名匹配样本（去掉文件扩展名中的aAE/aAS部分）
    ae_df['base_name'] = ae_df['file_name'].str.replace('-aAE.npy', '').str.replace('-aAS.npy', '')
    as_df['base_name'] = as_df['file_name'].str.replace('-aAE.npy', '').str.replace('-aAS.npy', '')
    
    # 合并数据
    merged_df = pd.merge(ae_df, as_df, on='base_name', suffixes=('_ae', '_as'))
    
    # 找出预测不一致的样本
    inconsistent_mask = merged_df['predicted_label_ae'] != merged_df['predicted_label_as']
    inconsistent_samples = merged_df[inconsistent_mask].copy()
    
    print(f"\n总样本数: {len(merged_df)}")
    print(f"预测一致的样本: {len(merged_df) - len(inconsistent_samples)}")
    print(f"预测不一致的样本: {len(inconsistent_samples)}")
    print(f"不一致率: {len(inconsistent_samples)/len(merged_df)*100:.2f}%")
    
    return inconsistent_samples, merged_df

def analyze_inconsistent_patterns(inconsistent_samples):
    """分析不一致样本的模式"""
    print("\n" + "="*60)
    print("不一致样本分析")
    print("="*60)
    
    # 按真实标签分析不一致情况
    print("\n1. 按真实场景分析不一致率:")
    print("-" * 40)
    
    true_label_analysis = {}
    for true_label in inconsistent_samples['true_label_ae'].unique():
        scene_samples = inconsistent_samples[inconsistent_samples['true_label_ae'] == true_label]
        true_label_analysis[true_label] = {
            'count': len(scene_samples),
            'ae_predictions': scene_samples['predicted_label_ae'].value_counts().to_dict(),
            'as_predictions': scene_samples['predicted_label_as'].value_counts().to_dict()
        }
        print(f"{true_label}: {len(scene_samples)} 个不一致样本")
    
    # 分析最常见的不一致模式
    print("\n2. 最常见的不一致模式:")
    print("-" * 40)
    
    inconsistent_patterns = inconsistent_samples.groupby(['true_label_ae', 'predicted_label_ae', 'predicted_label_as']).size().sort_values(ascending=False)
    
    for (true_label, ae_pred, as_pred), count in inconsistent_patterns.head(10).items():
        print(f"真实:{true_label} -> AE预测:{ae_pred}, AS预测:{as_pred} ({count}次)")
    
    return true_label_analysis, inconsistent_patterns

def generate_inconsistent_samples_for_audioset(inconsistent_samples):
    """为AudioSet分析生成不一致样本文件"""
    import json
    
    # 选择最具代表性的不一致样本
    analysis_samples = []
    
    # 按真实标签分组，每个场景选择几个代表性样本
    for true_label in inconsistent_samples['true_label_ae'].unique():
        scene_samples = inconsistent_samples[inconsistent_samples['true_label_ae'] == true_label]
        
        # 选择前5个样本
        selected_samples = scene_samples.head(5)
        
        for _, sample in selected_samples.iterrows():
            # 构造原始音频文件路径
            base_name = sample['base_name']
            audio_file = f"{base_name}.wav"
            
            analysis_samples.append({
                "audio_file": audio_file,
                "base_name": base_name,
                "true_scene": sample['true_label_ae'],
                "ae_prediction": sample['predicted_label_ae'],
                "as_prediction": sample['predicted_label_as'],
                "inconsistency_type": f"AE:{sample['predicted_label_ae']} vs AS:{sample['predicted_label_as']}"
            })
    
    # 保存不一致样本分析
    inconsistent_analysis = {
        "analysis_time": pd.Timestamp.now().isoformat(),
        "total_inconsistent_samples": len(inconsistent_samples),
        "inconsistency_rate": len(inconsistent_samples) / len(inconsistent_samples) * 100,
        "samples_for_audioset_analysis": analysis_samples[:50]  # 取前50个样本进行AudioSet分析
    }
    
    with open('inconsistent_samples_analysis.json', 'w', encoding='utf-8') as f:
        json.dump(inconsistent_analysis, f, ensure_ascii=False, indent=2)
    
    print(f"\n已生成 {len(analysis_samples[:50])} 个不一致样本供AudioSet分析")
    print("文件保存为: inconsistent_samples_analysis.json")
    
    return inconsistent_analysis

def main():
    """主函数"""
    print("开始AE vs AS预测结果比较分析...")
    
    # 加载预测结果
    ae_df, as_df = load_prediction_results("prediction_results_AE.csv", "prediction_results_AS.csv")
    
    if ae_df is None or as_df is None:
        print("无法加载预测结果文件")
        return
    
    # 找出不一致样本
    inconsistent_samples, merged_df = find_inconsistent_samples(ae_df, as_df)
    
    if len(inconsistent_samples) == 0:
        print("没有发现不一致的样本")
        return
    
    # 分析不一致模式
    true_label_analysis, inconsistent_patterns = analyze_inconsistent_patterns(inconsistent_samples)
    
    # 生成AudioSet分析用的不一致样本文件
    inconsistent_analysis = generate_inconsistent_samples_for_audioset(inconsistent_samples)
    
    # 保存详细的不一致样本数据
    inconsistent_samples.to_csv('detailed_inconsistent_samples.csv', index=False)
    print("详细不一致样本数据已保存为: detailed_inconsistent_samples.csv")
    
    print("\n比较分析完成！")
    print("不一致样本分析文件已准备好供AudioSet模型使用。")

if __name__ == "__main__":
    main()
