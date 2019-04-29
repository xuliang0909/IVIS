import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 计算置信区间
def confidenceinterval(data):#求置信区间
    StandardDeviation_sum=0
    #返回样本数量
    Sizeofdata=len(data)
    data=np.array(data)
    Sumdata=sum(data)
    #计算平均值
    Meanvalue=Sumdata/Sizeofdata
    #计算标准差
    for index in data:
        StandardDeviation_sum=StandardDeviation_sum+(index-Meanvalue)**2
    StandardDeviation_sum=StandardDeviation_sum/Sizeofdata
    StandardDeviationOfData=StandardDeviation_sum**0.5
    #计算置信区间
    LowerLimitingValue = Meanvalue-1.64*StandardDeviationOfData
    UpperLimitingValue = Meanvalue+1.64*StandardDeviationOfData
    return (LowerLimitingValue, UpperLimitingValue)

# 计算置信区间，异常点分类,k=1:纵向找异常；  k=2：横向找异常
def get_normal_abnormal_point(data_div, k):
    '''
    :param data_div: 按速度区间分组的数据列表，形式为：data_div=[[(,,,,,),(),...,()], ..., [(),(),...,()]]
    :param k: k=1:纵向找异常；  k=2：横向找异常
    :return: 返回正常点与异常点的列表，形式为：normal_abnormal = [[(正常点),(),.....], [(异常点),(),.....]]
    '''
    normal_abnormal = [[], []]
    for data_v_a in data_div:
        acc = [e[k] for e in data_v_a]
        lower_upper = confidenceinterval(acc)
        # print(lower_upper)
        for i in range(len(data_v_a)):
            if data_v_a[i][k]>=lower_upper[0] and data_v_a[i][k]<=lower_upper[1]:
                normal_abnormal[0].append(data_v_a[i])
            else:
                normal_abnormal[1].append(data_v_a[i])
    print('正常数据量：', len(normal_abnormal[0]), '异常数据量：', len(normal_abnormal[1]))
    return normal_abnormal

# 画图    k=1:纵向异常；  k=2：横向异常
def drawing(normal_abnormal, k):
    '''
    :param normal_abnormal: list, 形式为：[[(),(),(),...], [(),(),(),...]]
    :param k: int, k=1:纵向异常；k=2：横向异常
    :return:
    '''
    ylabelName = ["Longitudinal Acceleration(m/s2)", "Lateral Acceleration(m/s2)"]
    x1, y1, z1, *rest = [*zip(*normal_abnormal[0])]    # 正常点
    nor = [y1, z1]
    x2, y2, z2, *rest = [*zip(*normal_abnormal[1])]    # 异常点
    abnor = [y2, z2]
    plt.scatter(x1, nor[k-1], s=10, c='r', marker='o')
    plt.scatter(x2, abnor[k-1], s=10, c='b', marker='o')
    plt.xlabel("speed(m)")
    plt.ylabel(ylabelName[k-1])
    plt.show()

def saveCSV(normal_abnormal, filename, k):
    '''
    :param normal_abnormal: 正常点与异常点的列表，形式为：normal_abnormal = [[(正常点),(),.....], [(异常点),(),.....]]
    :param filename: str, 存储路径
    :return:
    '''
    data_dump = [[v[6], v[3], v[4], v[5], v[0], v[1], v[2]] for v in normal_abnormal[k]]
    data_dump.sort()
    name = ['ID', 'VehicleId', 'TripId', 'Time', 'Speed', 'LongtiAcc', 'a_la']
    test = pd.DataFrame(columns=name, data=data_dump)
    test.to_csv(filename, encoding='gbk')

# #########################################################################################################
datalist = []
for e in range(10):
    with open("data_fill_0.csv") as f:
        next(f)
        reader = csv.reader(f)
        datalist.append([row[e] for row in reader])
# 数值类型转换
data = []
for arr in datalist:
    arr = list(map(float, arr))
    data.append(arr)
# zip打包[(speed, longAcc)]
datapack = list(zip(data[4], data[5], data[7], data[1], data[2], data[3], data[0]))
datapack.sort()

# ##############  数据按速度区间分组：data_div = [[(,,,,,),(),...,()], ..., [(),(),...,()]]  ##############
data_div = [[] for i in range(91)]
mul = 0
for i in range(len(datapack)):
    # print('a:', a)
    if datapack[i][0] < 0.1+0.5*mul:
        data_div[mul].append(datapack[i])
    else:
        data_div[mul].append(datapack[i])
        mul += 1
# ###########################################################################################

print('纵向加速度异常点:')
normal_abnormal_longti = get_normal_abnormal_point(data_div, 1)
print('横向加速度异常点:')
normal_abnormal_lati = get_normal_abnormal_point(data_div, 2)
'''
# 画纵向异常图
drawing(normal_abnormal_longti, 1)
# 画横向异常图
# drawing(normal_abnormal_lati, 2)
'''
# print('保存数据')
# saveCSV(normal_abnormal_longti, "Longitudinal abnormal point.csv", 1)
# saveCSV(normal_abnormal_lati, "Lateral abnormal point.csv", 1)
# print('存储完成')
print('保存数据')
saveCSV(normal_abnormal_longti, "Longitudinal normal point.csv", 0)
saveCSV(normal_abnormal_lati, "Lateral normal point.csv", 0)
print('存储完成')

'''
# 按单个速度给数据分组
data_div = []
d = {}
for i in datapack:
    d.setdefault(i[0],[]).append(i)
data_div = list(d.values())

i = 0
while i <= len(datapack):
   lis = [datapack[i]]
   for j in range(i+1, len(datapack)):
       if j<len(datapack) and datapack[j][0] == lis[0][0]:
           lis.append(datapack[j])
           new_index = j
   data_div.append(lis)
   i = new_index

print('按速度分为', len(data_div), '组')
a = 0
for i in data_div:
    a += len(i)
print('分组后数据长度', a)
'''