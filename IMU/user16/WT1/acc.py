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
plt.figure(figsize=(10, 4))
plt.plot(df['时间'], acc_total, color='purple', linewidth=2)

# plt.xlabel('时间')
# plt.ylabel('合加速度 (g)')
# plt.title('三轴合加速度随时间变化')
# plt.grid(True)
# plt.legend()
plt.tight_layout()
plt.show()
