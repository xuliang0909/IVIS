import csv

datalist = []
for e in range(10):
    with open("data_fill_0.csv") as f:
        next(f)
        reader = csv.reader(f)
        datalist.append([row[e] for row in reader])
data = []
for arr in datalist:
    arr = list(map(float, arr))  # 数值转换为float型
    data.append(arr)
print('分组前数据长度：', len(data[0]))

# 画图
print('正在画图中，请稍后：')
import matplotlib.pyplot as plt
# ########################################################
# 速度-横向加速度
x_values = data[4]
y_values = data[7]
plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45])
plt.scatter(x_values, y_values, s=5)
plt.title("Speed--Lateral Acceleration")
plt.xlabel("Speed(m)")
plt.ylabel("Lateral Acceleration(m/s2)")
plt.show()
# ########################################################
# 横向加速度-纵向加速度
x_values = data[7]
y_values = data[5]
plt.scatter(x_values, y_values, s=5)
plt.title("Lateral Acceleration--Longitudinal Acceleration")
plt.xlabel("Lateral Acceleration(m/s2)")
plt.ylabel("Longitudinal Acceleration(m/s2)")
plt.show()
# ########################################################
# 速度-纵向加速度
x_values = data[4]
y_values = data[5]
plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45])
plt.scatter(x_values, y_values, s=5)
plt.title("Speed--Longitudinal Acceleration")
plt.xlabel("Speed(m)")
plt.ylabel("Longitudinal Acceleration(m/s2)")
plt.show()
# ########################################################
# 速度-速度一阶导
x_values = data[4]
y_values = data[8]
plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45])
plt.scatter(x_values, y_values, s=5)
plt.title("Speed--speed_der")
plt.xlabel("Speed(m)")
plt.ylabel("speed_der(m/s2)")
plt.show()