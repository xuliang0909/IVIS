import csv
import pandas as pd
# 导入数据
filename = "15-ALL.csv"
# filename = "11.csv"
datalist = []
lis = [i for i in range(7)]
for i in range(len(lis)):
    with open(filename) as f:
        next(f)
        reader = csv.reader(f)      # 或者：reader = f.readlines()[1:]
        datalist.append([row[i] for row in reader])
# for i in datalist:
#     print(len(i), i[:30])
data = [[] for i in range(7)]
length = 1
# 删除时间不连续的数据（低于50条的删除）
num = 0
for i in range(len(datalist[0])-2):
    if int(datalist[3][i+1])-int(datalist[3][i]) == 100:
        length += 1
    else:
        if length >= 50:
            for j in range(7):
                lis = datalist[j][i-length+1:i+1]
                data[j] += lis
            num += 1
        length = 1
for i in data:
    print(i[:20])
print('删除不必要数据后的数据长度为', len(data[0]))
print('数据按时间分为', num, '组')
# 存储数据
# data_dump = [[data[0][i], data[1][i], data[2][i], data[3][i], data[4][i],
#               data[5][i], data[6][i], data[7][i]] for i in range(len(data[0]))]
# name = ['ID', 'VehicleId', 'TripId', 'Time', 'Speed', 'LongtiAcc', '车道线宽度', '测量概率']
# test = pd.DataFrame(columns=name, data=data_dump)
# test.to_csv("time_filter_1.csv", encoding='gbk')
