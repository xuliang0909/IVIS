import csv
import pandas as pd

# 求导,输入两列数据，返回导数列表
def getDerivatives(dataset, t_var):
    '''
    :param dataset: 因变量（速度，距离）
    :param t_var:  list，时间变化量
    :return: 导数的列表，length-1
    '''
    derivatives = [(dataset[i+1]-dataset[i])/t_var[i] for i in range(len(dataset)-1)]
    return derivatives
# 输入一段时间的数据集合，返回关于横加、纵加、纵加'的列表
def get_Derlists(data):
    # 时间，距离单位转换
    t_list = list(map(lambda e: e/100, data[3]))
    s_list = list(map(lambda e: e/1000, data[6]))
    t_var = [t_list[i+1]-t_list[i] for i in range(len(t_list)-1)]
    v_la = getDerivatives(s_list, t_var)    # 横向速度
    a_la = getDerivatives(v_la, t_var[1:])  # 横向加速度
    speed_der = getDerivatives(data[4], t_var)  # 纵向加速度
    speed_der_der = getDerivatives(speed_der, t_var[1:])  # 纵向加速度的一阶导数
    return a_la, speed_der, speed_der_der

# 导入数据
datalist = []
for e in range(7):
    with open("data.csv") as f:
        next(f)
        reader = csv.reader(f)
        datalist.append([row[e] for row in reader])
data = []
for arr in datalist:
    arr = list(map(float, arr))  # 数值转换为float型
    data.append(arr)
print('分组前数据长度：', len(data[0]))
# 数据按时间分组
dataset = []
length = 1
num = 0
for i in range(len(data[0])-1):
    if data[3][i+1]-data[3][i] == 100:
        length += 1
    else:
        if length >= 50:
            asd = []
            for j in range(7):
                lis = data[j][i-length+1:i+1]
                asd.append(lis)
            dataset.append(asd)
            # print(i)
            # print(data[3][i]) # 每个时间分组的最后一个时间
        length = 1
num = sum(list(map(lambda e: len(e[0]), dataset)))
surplus = [[data[i][num:] for i in range(7)]]
dataset += list(surplus)
print('按时间分为', len(dataset), '组')
length = 0
for e in dataset:
    length += len(e[0])
print('分组后数据长度：', length)
# dataset[]的形式：[[[...], [...], [...], [...], [...], [...], [...]] for i in range(按时间的分组数)]
# 计算1.横向加速度 2.纵向加速度 3纵向加速度一阶导
data = data + [[], [], []]
for values in dataset:
    a_la = [0, 0]+get_Derlists(values)[0]
    speed_der = [0]+get_Derlists(values)[1]
    speed_der_der = [0, 0]+get_Derlists(values)[2]
    data[-3] += a_la
    data[-2] += speed_der
    data[-1] += speed_der_der

# 存储数据
data_dump = [[data[0][i], data[1][i], data[2][i], data[3][i], data[4][i],
            data[5][i], data[6][i], data[7][i], data[8][i], data[9][i]] for i in range(213540)]
name = ['ID', 'VehicleId', 'TripId', 'Time', 'Speed', 'LongtiAcc', '车道线宽度', 'a_la', 'speed_der', 'speed_der_der']
test = pd.DataFrame(columns=name, data=data_dump)
test.to_csv("test_213540.csv", encoding='gbk')

'''
# 存储数据
data_dump = [[data[0][i], data[1][i], data[2][i], data[3][i], data[4][i],
            data[5][i], data[6][i], data[7][i], data[8][i], data[9][i]] for i in range(len(data[0]))]
name = ['ID', 'VehicleId', 'TripId', 'Time', 'Speed', 'LongtiAcc', '车道线宽度', 'a_la', 'speed_der', 'speed_der_der']
test = pd.DataFrame(columns=name, data=data_dump)
test.to_csv("C:/Users/lqj/Desktop/data_fill_0.csv", encoding='gbk')
'''
'''
# 画图
print('正在画图中，请稍后：')
import matplotlib.pyplot as plt
# ########################################################
# 速度-横向加速度
x_values = data[4]
y_values = data[7]
plt.scatter(x_values, y_values, s=5)
plt.title("Speed--Longitudinal")
plt.xlabel("Speed(mph)")
plt.ylabel("Longitudinal Acceleration(ft/s2)")
plt.show()
# ########################################################
# 横向加速度-纵向加速度
x_values = data[7]
y_values = data[5]
plt.scatter(x_values, y_values, s=5)
plt.title("Lateral--Longitudinal")
plt.xlabel("Lateral Acceleration(ft/s2)")
plt.ylabel("Longitudinal Acceleration(ft/s2)")
plt.show()
# ########################################################
# 速度-纵向加速度
x_values = data[4]
y_values = data[5]
plt.scatter(x_values, y_values, s=5)
plt.title("Speed--Longitudinal")
plt.xlabel("Speed(mph)")
plt.ylabel("Longitudinal Acceleration(ft/s2)")
plt.show()
# ########################################################
# 速度-速度一阶导
x_values = data[4]
y_values = data[8]
plt.scatter(x_values, y_values, s=5)
plt.title("Speed--speed_der")
plt.xlabel("Speed(mph)")
plt.ylabel("speed_der(ft/s2)")
plt.show()
'''