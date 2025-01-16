import pandas as pd
import matplotlib.pyplot as plt

# 读取xls表格数据
xls = pd.ExcelFile('./metric_test_imgs_SuperFusion.xlsx')
method_names = []
metric_names = []
metrics = {}
statistical = {}
for sheet_name in xls.sheet_names:
    if sheet_name == "Sheet":
        continue
    df = pd.read_excel(xls, sheet_name=sheet_name)
    if len(method_names) == 0:
        for column in df.columns:
            if column == "Unnamed: 0":
                continue
            method_names.append(column)
    metric_names.append(sheet_name)
    metrics[sheet_name] = {}
    statistical[sheet_name] = {}
    metrics[sheet_name][column], statistical[sheet_name][column] = df[column].values[:-2], df[column].values[-2:]


num_metrics = len(metric_names)
fig, axs = plt.subplots(num_metrics, 1, figsize=(10, num_metrics * 5))  # 根据指标数量决定图的大小

if num_metrics == 1:  # 如果只有一个指标，确保axs可迭代
    axs = [axs]

# 遍历每个指标，绘制其对应的所有方法的数据
for ax, metric in zip(axs, metric_names):
    for method in method_names:
        df = pd.DataFrame(metrics[metric][method], columns=['Scores'])
        # 计算每个分数以下的学生百分比
        percentages = df['Scores'].apply(lambda x: (df['Scores'] < x).mean())
        # 将百分比乘以100转换为百分比格式
        df['Percentages'] = percentages * 100
        # 去重并排序
        df = df.drop_duplicates().sort_values(by='Scores')
        ax.plot(df['Percentages'], df['Scores'], marker='o', label=f"{method} mean: {statistical[metric][method][0]} std: {statistical[metric][method][1]}")
    ax.set_title(f'Performance Metrics for {metric}')
    ax.set_xlabel('Percentage')
    ax.set_ylabel(metric)
    ax.legend()
    ax.grid(True)

plt.tight_layout()
plt.savefig('figures/summary.png')
