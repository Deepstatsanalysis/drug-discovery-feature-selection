'''
Train and test 3 classifiers using expanded herbal Indonesia dataset (manual docking result):
1. SVM with all features
2. SVM with WM-GA feature selection mask (output of 02-feature-selection-wm.py)
3. SVM with SVM-RE feature selection mask (output of 02-feature-selection-svm-rfe.py)

Result:
SVM + RFE Accuracy: 0.9727 in 0.0 s
SVM + WM Accuracy: 0.9727 in 0.0 s
SVM Accuracy: 0.9700 in 0.0 s

Execution Time (Core i7 5500U, 8 GB, SSD):
real    0m4.454s
user    0m2.374s
sys     0m1.228s

@author yohanes.gultom@gmail.com
'''
import matplotlib.pyplot as plt
from evaluate_performance import evaluate

evaluate(
    '../dataset/dataset_test_expanded.csv', # herbal db manual docking
    '03-evaluate-4_result.csv',
    '03-evaluate-4_roc_chart.png',
    'ROC on Herbal DB Dataset manual docking',
    'As both train and test data',
    '03-evaluate-4_scores_chart.png',
    'Performance Comparison on Herbal DB manual docking',
    'As training and testing data'
)

# show plots
plt.show()
