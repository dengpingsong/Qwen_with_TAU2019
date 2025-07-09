#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
实验批量运行器
用于批量运行多种特征提取和分类实验
Created on 2025-07-03
"""

import argparse
import subprocess
import sys
import time
from pathlib import Path
from typing import List, Dict, Any, Optional
import json
import logging
from datetime import datetime

from experiment_config import ExperimentConfig, get_feature_types, get_classifier_types


class ExperimentRunner:
    """实验批量运行器"""
    
    def __init__(self, config: Optional[ExperimentConfig] = None):
        """初始化实验运行器"""
        self.config = config or ExperimentConfig()
        self.setup_logging()
        
    def setup_logging(self):
        """设置日志"""
        log_dir = Path("./logs")
        log_dir.mkdir(exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = log_dir / f"experiment_runner_{timestamp}.log"
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file, encoding='utf-8'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def run_feature_extraction(self, 
                             feature_type: str,
                             audio_folder: Optional[str] = None,
                             output_folder: Optional[str] = None,
                             batch_size: Optional[int] = None) -> bool:
        """运行特征提取"""
        
        # 获取配置
        extraction_config = self.config.get_extraction_config()
        data_paths = self.config.get_data_paths()
        
        audio_folder = audio_folder or data_paths.get('audio_folder')
        output_folder = output_folder or data_paths.get('feature_folder')
        batch_size = batch_size or extraction_config.get('batch_size', 1000)
        
        cmd = [
            sys.executable, "qwen_feature_extractor.py",
            "--mode", feature_type,
            "--audio_folder", audio_folder,
            "--output_folder", output_folder,
            "--batch_size", str(batch_size)
        ]
        
        self.logger.info(f"开始提取 {feature_type} 特征...")
        self.logger.info(f"命令: {' '.join(cmd)}")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
            
            if result.returncode == 0:
                self.logger.info(f"{feature_type} 特征提取成功完成")
                if result.stdout:
                    self.logger.info(f"输出: {result.stdout}")
                return True
            else:
                self.logger.error(f"{feature_type} 特征提取失败")
                if result.stderr:
                    self.logger.error(f"错误: {result.stderr}")
                return False
                
        except Exception as e:
            self.logger.error(f"运行特征提取时出错: {e}")
            return False
    
    def run_classification(self,
                          feature_type: str,
                          classifier_type: str,
                          data_dir: Optional[str] = None,
                          csv_path: Optional[str] = None,
                          output_dir: Optional[str] = None,
                          training_size: Optional[int] = None) -> bool:
        """运行分类训练"""
        
        # 获取配置
        classification_config = self.config.get_classification_config()
        data_paths = self.config.get_data_paths()
        
        data_dir = data_dir or data_paths.get('feature_folder')
        csv_path = csv_path or data_paths.get('meta_csv')
        output_dir = output_dir or f"./experiment_results/Qwen_{feature_type}_{classifier_type}_Classification"
        training_size = training_size or classification_config.get('training_sample_size', 2000)
        
        cmd = [
            sys.executable, "audio_scene_classifier.py",
            "--feature_type", feature_type,
            "--classifier", classifier_type,
            "--data_dir", data_dir,
            "--csv_path", csv_path,
            "--output_dir", output_dir,
            "--training_size", str(training_size),
            "--save_model"
        ]
        
        self.logger.info(f"开始训练 {feature_type}+{classifier_type} 分类器...")
        self.logger.info(f"命令: {' '.join(cmd)}")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
            
            if result.returncode == 0:
                self.logger.info(f"{feature_type}+{classifier_type} 分类训练成功完成")
                if result.stdout:
                    self.logger.info(f"输出: {result.stdout}")
                return True
            else:
                self.logger.error(f"{feature_type}+{classifier_type} 分类训练失败")
                if result.stderr:
                    self.logger.error(f"错误: {result.stderr}")
                return False
                
        except Exception as e:
            self.logger.error(f"运行分类训练时出错: {e}")
            return False
    
    def run_full_experiment(self,
                           feature_type: str,
                           classifier_type: str,
                           extract_features: bool = True,
                           train_classifier: bool = True) -> Dict[str, bool]:
        """运行完整实验（特征提取+分类训练）"""
        
        results = {
            'feature_extraction': True,
            'classification': True
        }
        
        self.logger.info(f"开始完整实验: {feature_type} + {classifier_type}")
        
        # 特征提取
        if extract_features:
            self.logger.info("=" * 50)
            self.logger.info("阶段 1: 特征提取")
            self.logger.info("=" * 50)
            results['feature_extraction'] = self.run_feature_extraction(feature_type)
            
            if not results['feature_extraction']:
                self.logger.error("特征提取失败，跳过分类训练")
                results['classification'] = False
                return results
        
        # 分类训练
        if train_classifier:
            self.logger.info("=" * 50)
            self.logger.info("阶段 2: 分类训练")
            self.logger.info("=" * 50)
            results['classification'] = self.run_classification(feature_type, classifier_type)
        
        # 总结
        self.logger.info("=" * 50)
        self.logger.info("实验完成总结")
        self.logger.info("=" * 50)
        self.logger.info(f"特征类型: {feature_type}")
        self.logger.info(f"分类器类型: {classifier_type}")
        self.logger.info(f"特征提取: {'成功' if results['feature_extraction'] else '失败'}")
        self.logger.info(f"分类训练: {'成功' if results['classification'] else '失败'}")
        
        return results
    
    def run_batch_experiments(self,
                             feature_types: List[str],
                             classifier_types: List[str],
                             extract_features: bool = True,
                             train_classifiers: bool = True,
                             continue_on_error: bool = True) -> Dict[str, Dict[str, bool]]:
        """批量运行多个实验"""
        
        all_results = {}
        total_experiments = len(feature_types) * len(classifier_types)
        current_experiment = 0
        
        self.logger.info(f"开始批量实验运行")
        self.logger.info(f"特征类型: {feature_types}")
        self.logger.info(f"分类器类型: {classifier_types}")
        self.logger.info(f"总实验数: {total_experiments}")
        
        start_time = time.time()
        
        for feature_type in feature_types:
            for classifier_type in classifier_types:
                current_experiment += 1
                experiment_name = f"{feature_type}_{classifier_type}"
                
                self.logger.info("\\n" + "=" * 80)
                self.logger.info(f"实验 {current_experiment}/{total_experiments}: {experiment_name}")
                self.logger.info("=" * 80)
                
                try:
                    # 对于特征提取，只在第一个分类器时运行
                    should_extract = extract_features and (classifier_types.index(classifier_type) == 0)
                    
                    results = self.run_full_experiment(
                        feature_type=feature_type,
                        classifier_type=classifier_type,
                        extract_features=should_extract,
                        train_classifier=train_classifiers
                    )
                    
                    all_results[experiment_name] = results
                    
                except Exception as e:
                    self.logger.error(f"实验 {experiment_name} 出错: {e}")
                    all_results[experiment_name] = {
                        'feature_extraction': False,
                        'classification': False,
                        'error': str(e)
                    }
                    
                    if not continue_on_error:
                        self.logger.error("停止批量实验")
                        break
        
        # 总结所有实验
        end_time = time.time()
        total_time = end_time - start_time
        
        self.logger.info("\\n" + "=" * 80)
        self.logger.info("批量实验完成总结")
        self.logger.info("=" * 80)
        self.logger.info(f"总耗时: {total_time:.2f} 秒")
        self.logger.info(f"完成实验数: {len(all_results)}")
        
        success_count = 0
        for exp_name, results in all_results.items():
            is_success = results.get('feature_extraction', False) and results.get('classification', False)
            if is_success:
                success_count += 1
            
            status = "成功" if is_success else "失败"
            self.logger.info(f"{exp_name}: {status}")
        
        self.logger.info(f"成功率: {success_count}/{len(all_results)} ({success_count/len(all_results)*100:.1f}%)")
        
        # 保存结果到JSON
        results_file = Path("./logs") / f"batch_experiment_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(results_file, 'w', encoding='utf-8') as f:
            json.dump(all_results, f, indent=2, ensure_ascii=False)
        
        self.logger.info(f"详细结果已保存到: {results_file}")
        
        return all_results


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="实验批量运行器")
    
    # 运行模式
    parser.add_argument("--mode", type=str, 
                       choices=["extract", "classify", "full", "batch"],
                       default="full",
                       help="运行模式")
    
    # 特征类型
    parser.add_argument("--feature_types", type=str, nargs='+',
                       choices=get_feature_types(),
                       default=["AE"],
                       help="特征类型列表")
    
    # 分类器类型
    parser.add_argument("--classifier_types", type=str, nargs='+',
                       choices=get_classifier_types(),
                       default=["svm"],
                       help="分类器类型列表")
    
    # 其他选项
    parser.add_argument("--config_file", type=str,
                       help="配置文件路径")
    parser.add_argument("--continue_on_error", action="store_true",
                       help="遇到错误时继续运行")
    parser.add_argument("--skip_extraction", action="store_true",
                       help="跳过特征提取")
    parser.add_argument("--skip_classification", action="store_true",
                       help="跳过分类训练")
    
    args = parser.parse_args()
    
    # 加载配置
    config = ExperimentConfig(args.config_file) if args.config_file else ExperimentConfig()
    
    # 创建运行器
    runner = ExperimentRunner(config)
    
    # 根据模式运行
    if args.mode == "extract":
        # 只运行特征提取
        for feature_type in args.feature_types:
            runner.run_feature_extraction(feature_type)
    
    elif args.mode == "classify":
        # 只运行分类训练
        for feature_type in args.feature_types:
            for classifier_type in args.classifier_types:
                runner.run_classification(feature_type, classifier_type)
    
    elif args.mode == "full":
        # 运行完整实验
        feature_type = args.feature_types[0]
        classifier_type = args.classifier_types[0]
        runner.run_full_experiment(
            feature_type=feature_type,
            classifier_type=classifier_type,
            extract_features=not args.skip_extraction,
            train_classifier=not args.skip_classification
        )
    
    elif args.mode == "batch":
        # 批量运行
        runner.run_batch_experiments(
            feature_types=args.feature_types,
            classifier_types=args.classifier_types,
            extract_features=not args.skip_extraction,
            train_classifiers=not args.skip_classification,
            continue_on_error=args.continue_on_error
        )


if __name__ == "__main__":
    main()
