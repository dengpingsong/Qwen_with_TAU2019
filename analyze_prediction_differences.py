import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

def load_prediction_results(ae_path, as_path):
    """加载AE和AS预测结果文件"""
    try:
        ae_df = pd.read_csv(ae_path)
        as_df = pd.read_csv(as_path)
        
        print(f"AE预测结果: {len(ae_df)} 条记录")
        print(f"AS预测结果: {len(as_df)} 条记录")
        
        return ae_df, as_df
    except Exception as e:
        print(f"加载文件时出错: {e}")
        return None, None

def extract_base_filename(filename):
    """从文件名中提取基础文件名（去除aAE.npy或aAS.npy后缀）"""
    if filename.endswith('-aAE.npy'):
        return filename.replace('-aAE.npy', '')
    elif filename.endswith('-aAS.npy'):
        return filename.replace('-aAS.npy', '')
    else:
        return filename.replace('.npy', '')

def align_predictions(ae_df, as_df):
    """对齐AE和AS的预测结果，基于相同的音频文件"""
    
    # 提取基础文件名
    ae_df['base_filename'] = ae_df['file_name'].apply(extract_base_filename)
    as_df['base_filename'] = as_df['file_name'].apply(extract_base_filename)
    
    # 找到共同的文件
    common_files = set(ae_df['base_filename']) & set(as_df['base_filename'])
    print(f"共同的音频文件数量: {len(common_files)}")
    
    # 筛选出共同文件的预测结果
    ae_common = ae_df[ae_df['base_filename'].isin(common_files)].copy()
    as_common = as_df[as_df['base_filename'].isin(common_files)].copy()
    
    # 按base_filename排序以确保对应
    ae_common = ae_common.sort_values('base_filename').reset_index(drop=True)
    as_common = as_common.sort_values('base_filename').reset_index(drop=True)
    
    return ae_common, as_common, common_files

def analyze_prediction_differences(ae_df, as_df):
    """分析预测差异"""
    
    print("="*80)
    print("AE vs AS 预测结果差异分析")
    print("="*80)
    
    # 计算预测一致性
    same_predictions = (ae_df['predicted_label'] == as_df['predicted_label']).sum()
    different_predictions = len(ae_df) - same_predictions
    consistency_rate = same_predictions / len(ae_df)
    
    print(f"\n1. 预测一致性分析:")
    print(f"   - 预测一致的样本: {same_predictions}")
    print(f"   - 预测不一致的样本: {different_predictions}")
    print(f"   - 预测一致率: {consistency_rate:.4f} ({consistency_rate*100:.2f}%)")
    
    # 分析正确性
    ae_correct = (ae_df['true_label'] == ae_df['predicted_label']).sum()
    as_correct = (as_df['true_label'] == as_df['predicted_label']).sum()
    
    print(f"\n2. 模型准确性比较:")
    print(f"   - AE模型正确预测: {ae_correct}/{len(ae_df)} ({ae_correct/len(ae_df)*100:.2f}%)")
    print(f"   - AS模型正确预测: {as_correct}/{len(as_df)} ({as_correct/len(as_df)*100:.2f}%)")
    
    # 分析不一致的预测
    different_mask = ae_df['predicted_label'] != as_df['predicted_label']
    different_df = pd.DataFrame({
        'base_filename': ae_df.loc[different_mask, 'base_filename'],
        'true_label': ae_df.loc[different_mask, 'true_label'],
        'ae_predicted': ae_df.loc[different_mask, 'predicted_label'],
        'as_predicted': as_df.loc[different_mask, 'predicted_label'],
        'ae_correct': ae_df.loc[different_mask, 'true_label'] == ae_df.loc[different_mask, 'predicted_label'],
        'as_correct': as_df.loc[different_mask, 'true_label'] == as_df.loc[different_mask, 'predicted_label']
    }).reset_index(drop=True)
    
    print(f"\n3. 预测差异详细分析:")
    print(f"   - 仅AE正确的样本: {(different_df['ae_correct'] & ~different_df['as_correct']).sum()}")
    print(f"   - 仅AS正确的样本: {(~different_df['ae_correct'] & different_df['as_correct']).sum()}")
    print(f"   - 两者都错误的样本: {(~different_df['ae_correct'] & ~different_df['as_correct']).sum()}")
    
    return different_df, consistency_rate

def analyze_class_level_differences(ae_df, as_df, different_df):
    """分析各类别的预测差异"""
    
    print(f"\n4. 各类别预测差异分析:")
    print("-" * 60)
    
    # 获取所有类别
    all_classes = sorted(set(ae_df['true_label'].unique()) | set(as_df['true_label'].unique()))
    
    class_analysis = []
    
    for class_name in all_classes:
        # 该类别的总样本数
        class_mask = ae_df['true_label'] == class_name
        total_samples = class_mask.sum()
        
        if total_samples == 0:
            continue
            
        # 该类别中预测不一致的样本数
        class_different_mask = (ae_df['true_label'] == class_name) & (ae_df['predicted_label'] != as_df['predicted_label'])
        different_samples = class_different_mask.sum()
        
        # 该类别的准确率
        ae_class_correct = ((ae_df['true_label'] == class_name) & (ae_df['predicted_label'] == class_name)).sum()
        as_class_correct = ((as_df['true_label'] == class_name) & (as_df['predicted_label'] == class_name)).sum()
        
        ae_class_accuracy = ae_class_correct / total_samples
        as_class_accuracy = as_class_correct / total_samples
        
        # 该类别中仅AE或仅AS正确的情况
        class_ae_only_correct = ((ae_df['true_label'] == class_name) & 
                                (ae_df['predicted_label'] == class_name) & 
                                (as_df['predicted_label'] != class_name)).sum()
        
        class_as_only_correct = ((as_df['true_label'] == class_name) & 
                                (as_df['predicted_label'] == class_name) & 
                                (ae_df['predicted_label'] != class_name)).sum()
        
        class_analysis.append({
            'class': class_name,
            'total_samples': total_samples,
            'different_predictions': different_samples,
            'difference_rate': different_samples / total_samples,
            'ae_accuracy': ae_class_accuracy,
            'as_accuracy': as_class_accuracy,
            'accuracy_diff': ae_class_accuracy - as_class_accuracy,
            'ae_only_correct': class_ae_only_correct,
            'as_only_correct': class_as_only_correct
        })
        
        print(f"{class_name:<18}: 总样本={total_samples:>4}, 预测差异={different_samples:>4} ({different_samples/total_samples*100:>5.1f}%), "
              f"AE准确率={ae_class_accuracy:.3f}, AS准确率={as_class_accuracy:.3f}, 差异={ae_class_accuracy-as_class_accuracy:>+.3f}")
    
    return pd.DataFrame(class_analysis)

def analyze_confusion_patterns(different_df):
    """分析混淆模式"""
    
    print(f"\n5. 主要混淆模式分析:")
    print("-" * 60)
    
    # AE和AS的主要混淆对
    ae_confusions = different_df.groupby(['true_label', 'ae_predicted']).size().sort_values(ascending=False)
    as_confusions = different_df.groupby(['true_label', 'as_predicted']).size().sort_values(ascending=False)
    
    print("AE模型主要混淆对 (真实标签 -> 预测标签):")
    for (true_label, pred_label), count in ae_confusions.head(10).items():
        print(f"  {true_label} -> {pred_label}: {count} 次")
    
    print("\nAS模型主要混淆对 (真实标签 -> 预测标签):")
    for (true_label, pred_label), count in as_confusions.head(10).items():
        print(f"  {true_label} -> {pred_label}: {count} 次")
    
    # 分析预测转换模式 (AE预测 -> AS预测)
    prediction_transitions = different_df.groupby(['ae_predicted', 'as_predicted']).size().sort_values(ascending=False)
    
    print(f"\n主要预测转换模式 (AE预测 -> AS预测):")
    for (ae_pred, as_pred), count in prediction_transitions.head(10).items():
        print(f"  {ae_pred} -> {as_pred}: {count} 次")

def create_visualizations(ae_df, as_df, different_df, class_analysis, consistency_rate):
    """创建可视化图表"""
    
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False
    
    fig = plt.figure(figsize=(20, 15))
    
    # 1. 预测一致性饼图
    plt.subplot(2, 4, 1)
    consistent = len(ae_df) - len(different_df)
    inconsistent = len(different_df)
    plt.pie([consistent, inconsistent], 
            labels=[f'一致预测\n{consistent}', f'不一致预测\n{inconsistent}'],
            autopct='%1.1f%%', 
            colors=['lightgreen', 'lightcoral'])
    plt.title(f'预测一致性\n(一致率: {consistency_rate:.1%})')
    
    # 2. 各类别差异率
    plt.subplot(2, 4, 2)
    class_analysis_sorted = class_analysis.sort_values('difference_rate', ascending=True)
    plt.barh(range(len(class_analysis_sorted)), class_analysis_sorted['difference_rate'])
    plt.yticks(range(len(class_analysis_sorted)), class_analysis_sorted['class'])
    plt.xlabel('预测差异率')
    plt.title('各类别预测差异率')
    plt.grid(True, alpha=0.3)
    
    # 3. 各类别准确率对比
    plt.subplot(2, 4, 3)
    x = np.arange(len(class_analysis))
    width = 0.35
    plt.bar(x - width/2, class_analysis['ae_accuracy'], width, label='AE', alpha=0.8)
    plt.bar(x + width/2, class_analysis['as_accuracy'], width, label='AS', alpha=0.8)
    plt.xlabel('类别')
    plt.ylabel('准确率')
    plt.title('各类别准确率对比')
    plt.xticks(x, class_analysis['class'], rotation=45, ha='right')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # 4. 准确率差异
    plt.subplot(2, 4, 4)
    colors = ['red' if x < 0 else 'blue' for x in class_analysis['accuracy_diff']]
    plt.bar(range(len(class_analysis)), class_analysis['accuracy_diff'], color=colors, alpha=0.7)
    plt.xlabel('类别')
    plt.ylabel('准确率差异 (AE - AS)')
    plt.title('各类别准确率差异')
    plt.xticks(range(len(class_analysis)), class_analysis['class'], rotation=45, ha='right')
    plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)
    plt.grid(True, alpha=0.3)
    
    # 5. 仅AE正确 vs 仅AS正确
    plt.subplot(2, 4, 5)
    x = np.arange(len(class_analysis))
    plt.bar(x - width/2, class_analysis['ae_only_correct'], width, label='仅AE正确', alpha=0.8)
    plt.bar(x + width/2, class_analysis['as_only_correct'], width, label='仅AS正确', alpha=0.8)
    plt.xlabel('类别')
    plt.ylabel('样本数量')
    plt.title('各类别独有正确预测数量')
    plt.xticks(x, class_analysis['class'], rotation=45, ha='right')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # 6. 预测差异热力图 - AE模型混淆
    plt.subplot(2, 4, 6)
    ae_confusion_matrix = pd.crosstab(different_df['true_label'], different_df['ae_predicted'])
    sns.heatmap(ae_confusion_matrix, annot=True, fmt='d', cmap='Reds', square=True)
    plt.title('AE模型混淆模式\n(仅差异样本)')
    plt.xlabel('AE预测')
    plt.ylabel('真实标签')
    
    # 7. 预测差异热力图 - AS模型混淆
    plt.subplot(2, 4, 7)
    as_confusion_matrix = pd.crosstab(different_df['true_label'], different_df['as_predicted'])
    sns.heatmap(as_confusion_matrix, annot=True, fmt='d', cmap='Blues', square=True)
    plt.title('AS模型混淆模式\n(仅差异样本)')
    plt.xlabel('AS预测')
    plt.ylabel('真实标签')
    
    # 8. 预测转换热力图
    plt.subplot(2, 4, 8)
    transition_matrix = pd.crosstab(different_df['ae_predicted'], different_df['as_predicted'])
    sns.heatmap(transition_matrix, annot=True, fmt='d', cmap='Greens', square=True)
    plt.title('预测转换模式\n(AE → AS)')
    plt.xlabel('AS预测')
    plt.ylabel('AE预测')
    
    plt.tight_layout()
    plt.savefig('prediction_differences_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\n可视化图表已保存: prediction_differences_analysis.png")

def save_detailed_analysis(different_df, class_analysis):
    """保存详细分析结果"""
    
    # 保存预测差异的详细信息
    different_df.to_csv('prediction_differences_detailed.csv', index=False)
    
    # 保存类别级别的分析
    class_analysis.to_csv('class_level_differences_analysis.csv', index=False)
    
    # 保存一些关键样本
    ae_only_correct = different_df[different_df['ae_correct'] & ~different_df['as_correct']]
    as_only_correct = different_df[~different_df['ae_correct'] & different_df['as_correct']]
    both_wrong = different_df[~different_df['ae_correct'] & ~different_df['as_correct']]
    
    ae_only_correct.to_csv('ae_only_correct_samples.csv', index=False)
    as_only_correct.to_csv('as_only_correct_samples.csv', index=False)
    both_wrong.to_csv('both_models_wrong_samples.csv', index=False)
    
    print(f"\n详细分析文件已保存:")
    print(f"- prediction_differences_detailed.csv: 所有预测差异详情")
    print(f"- class_level_differences_analysis.csv: 类别级别差异分析")
    print(f"- ae_only_correct_samples.csv: 仅AE正确的样本 ({len(ae_only_correct)} 个)")
    print(f"- as_only_correct_samples.csv: 仅AS正确的样本 ({len(as_only_correct)} 个)")
    print(f"- both_models_wrong_samples.csv: 两模型都错误的样本 ({len(both_wrong)} 个)")

def generate_summary_report(ae_df, as_df, different_df, class_analysis, consistency_rate):
    """生成总结报告"""
    
    summary = []
    summary.append("="*80)
    summary.append("AE vs AS 预测结果差异分析总结报告")
    summary.append("="*80)
    summary.append(f"分析时间: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}")
    summary.append("")
    
    summary.append("1. 基本统计信息:")
    summary.append(f"   - 总样本数: {len(ae_df)}")
    summary.append(f"   - 预测一致样本: {len(ae_df) - len(different_df)}")
    summary.append(f"   - 预测差异样本: {len(different_df)}")
    summary.append(f"   - 预测一致率: {consistency_rate:.4f} ({consistency_rate*100:.2f}%)")
    summary.append("")
    
    # 整体准确率
    ae_accuracy = (ae_df['true_label'] == ae_df['predicted_label']).mean()
    as_accuracy = (as_df['true_label'] == as_df['predicted_label']).mean()
    summary.append("2. 整体准确率:")
    summary.append(f"   - AE模型: {ae_accuracy:.4f} ({ae_accuracy*100:.2f}%)")
    summary.append(f"   - AS模型: {as_accuracy:.4f} ({as_accuracy*100:.2f}%)")
    summary.append(f"   - 差异: {ae_accuracy-as_accuracy:+.4f}")
    summary.append("")
    
    # 差异最大的类别
    summary.append("3. 预测差异最大的类别:")
    top_diff_classes = class_analysis.nlargest(5, 'difference_rate')
    for _, row in top_diff_classes.iterrows():
        summary.append(f"   - {row['class']}: {row['difference_rate']:.3f} ({row['different_predictions']}/{row['total_samples']})")
    summary.append("")
    
    # 各模型优势类别
    ae_advantage = class_analysis[class_analysis['accuracy_diff'] > 0.01].nlargest(3, 'accuracy_diff')
    as_advantage = class_analysis[class_analysis['accuracy_diff'] < -0.01].nsmallest(3, 'accuracy_diff')
    
    summary.append("4. AE模型优势类别:")
    for _, row in ae_advantage.iterrows():
        summary.append(f"   - {row['class']}: AE={row['ae_accuracy']:.3f}, AS={row['as_accuracy']:.3f}, 差异=+{row['accuracy_diff']:.3f}")
    
    summary.append("\n5. AS模型优势类别:")
    for _, row in as_advantage.iterrows():
        summary.append(f"   - {row['class']}: AE={row['ae_accuracy']:.3f}, AS={row['as_accuracy']:.3f}, 差异={row['accuracy_diff']:.3f}")
    summary.append("")
    
    # 关键发现
    summary.append("6. 关键发现:")
    if ae_accuracy > as_accuracy:
        summary.append(f"   - AE模型整体表现更好，准确率高出{(ae_accuracy-as_accuracy)*100:.2f}%")
    else:
        summary.append(f"   - AS模型整体表现更好，准确率高出{(as_accuracy-ae_accuracy)*100:.2f}%")
    
    summary.append(f"   - 约{(1-consistency_rate)*100:.1f}%的样本两模型预测不一致")
    summary.append(f"   - 仅AE正确的样本: {(different_df['ae_correct'] & ~different_df['as_correct']).sum()}")
    summary.append(f"   - 仅AS正确的样本: {(~different_df['ae_correct'] & different_df['as_correct']).sum()}")
    
    # 保存报告
    with open('prediction_differences_summary.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(summary))
    
    print('\n'.join(summary))

def main():
    """主函数"""
    print("开始分析AE和AS预测结果差异...")
    
    # 加载数据
    ae_df, as_df = load_prediction_results('prediction_results_AE.csv', 'prediction_results_AS.csv')
    
    if ae_df is None or as_df is None:
        print("无法加载预测结果文件")
        return
    
    # 对齐预测结果
    ae_aligned, as_aligned, common_files = align_predictions(ae_df, as_df)
    
    if len(common_files) == 0:
        print("没有找到共同的音频文件")
        return
    
    # 分析预测差异
    different_df, consistency_rate = analyze_prediction_differences(ae_aligned, as_aligned)
    
    # 分析各类别差异
    class_analysis = analyze_class_level_differences(ae_aligned, as_aligned, different_df)
    
    # 分析混淆模式
    analyze_confusion_patterns(different_df)
    
    # 创建可视化
    create_visualizations(ae_aligned, as_aligned, different_df, class_analysis, consistency_rate)
    
    # 保存详细分析
    save_detailed_analysis(different_df, class_analysis)
    
    # 生成总结报告
    generate_summary_report(ae_aligned, as_aligned, different_df, class_analysis, consistency_rate)
    
    print("\n预测差异分析完成！")

if __name__ == "__main__":
    main()
