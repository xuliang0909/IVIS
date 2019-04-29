import csv
import pandas as pd
import matplotlib.pyplot as plt

# 求导,输入两列数据，返回导数列表
def getDerivatives(dataset, t_var):
    derivatives = [(dataset[i+1]-dataset[i])/t_var[i+1] for i in range(len(dataset)-1)]
    return derivatives
# 传入列表路径+name >>> 返回data（数据集）, a_wide（横加）, a_long（纵加）, a_long_der（纵加导）
def dataExtraction(filename):
    datalist = []
    lis = [1, 2, 5, 4, 3]
    for i in lis:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            column = [row[i] for row in reader]
            datalist.append(column)
    print(datalist[0][:19])
    # 删除表头
    data = []
    for arr in datalist:
        del (arr[0])
        arr = list(map(float, arr))  # 数值转换为float型
        data.append(arr)
    # 计算1.时间变化量2.位移变化量>>>3.横向速度>>>4.横向速度变化量>>>5.横向加速度
    t_var, velocity, a_wide = [], [], []
    for i in range(len(data[1])-1):
        t_var.append((data[1][i+1]-data[1][i])/100)     # 时间变化量列表
        velocity.append(((data[2][i+1]-data[2][i])/1000)/((data[1][i+1]-data[1][i])/100)) # 横向速度
        # velocity = getDerivatives(data[2], )

    for i in range(len(velocity)-1):
        a_wide.append((velocity[i+1]-velocity[i])/t_var[i+1]) # 横向加速度
    speed_var = [data[4][i+1]-data[4][i] for i in range(len(data[4])-1)]
    a_long = getDerivatives(speed_var, t_var)   # 纵加(速度一阶导）
    a_long_der = getDerivatives(a_long, t_var[1:])      # 速度二阶导（加速度的导数值）
    return data, a_wide, a_long, a_long_der
# 导入数据
name = ['10.csv', '20.csv', '35.csv', '40.csv', '50.csv', '55.csv', '60.csv']
filename = 'E:/PythonData/Data/tripdata/'
for number in name:
    data = dataExtraction(filename+number)[0]
    a_lateral = ['', ''] + dataExtraction(filename+number)[1]
    a_long = ['', ''] + dataExtraction(filename+number)[2]
    a_long_der = ['', '', ''] + dataExtraction(filename+number)[3]
    # 存储数据
    data_show = [[data[0][i], data[1][i], a_lateral[i], a_long[i], a_long_der[i]] for i in range(len(a_long))]
    name = ['ID', 'Time', 'a_lateral', 'a_long', 'a_long_der']
    test = pd.DataFrame(columns=name, data=data_show)
    test.to_csv(filename+'data'+number, encoding='gbk')

'''
# 画图
import matplotlib.pyplot as plt
# ########################################################
# 速度-纵向加速度
x_values = data[3]
y_values = data[2]
plt.scatter(x_values, y_values, s=5)
plt.title("Speed-Longitudinal")
plt.xlabel("Speed")
plt.ylabel("Longitudinal")
plt.show()
# ########################################################
# 速度-横向加速度
x_values = data[3][2:]
y_values = a_long
plt.scatter(x_values, y_values, s=5)
plt.title("Speed-Lateral")
plt.xlabel("Speed")
plt.ylabel("Lateral")
plt.show()
# ########################################################
# 横向加速度-纵向加速度
x_values = a_long
y_values = data[2][2:]
plt.scatter(x_values, y_values, s=5)
plt.title("Lateral-Longitudinal")
plt.xlabel("Lateral")
plt.ylabel("Longitudinal")
plt.show()
'''