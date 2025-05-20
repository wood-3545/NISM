import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 读取 CSV 文件（替换为你的实际路径）
df = pd.read_csv('./5_WT1.csv')  # 替换为你的 CSV 路径

# 提取加速度列（单位是 g）
acc_x = df['加速度X(g)']
acc_y = df['加速度Y(g)']
acc_z = df['加速度Z(g)']

# 计算合加速度（欧几里得范数）
# acc_total = np.sqrt(acc_x**2 + acc_y**2 + acc_z**2)
acc_total = acc_x
# 将时间列转为 datetime 格式
df['时间'] = pd.to_datetime(df['时间'])

# 绘图
plt.figure(figsize=(12, 6))
a = 600
plt.plot(df['时间'][a:], -acc_total[a:], color='purple', linewidth=2)

plt.xticks([])
plt.yticks([])

# 获取当前坐标轴范围，用于计算居中位置
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# 在顶部居中显示标题
center_x = xlim[1] - (xlim[1] - xlim[0]) * 0.15
top_y = ylim[1] - (ylim[1] - ylim[0]) * 0.15  # 顶部稍微留点空间
plt.text(center_x, top_y, 'IMU', fontsize=35, ha='center', va='bottom')


# plt.xlabel('时间')
# plt.ylabel('合加速度 (g)')
# plt.title('IMU', fontsize=14)
# plt.grid(True)
# plt.legend()
plt.tight_layout()
plt.show()
