import csv
import pandas as pd

with open("Lateral normal point.csv") as f:
    next(f)
    data = list(csv.reader(f))
    print(len(data), data[:10])
# 删除时间不连续的数据（低于5条的删除）
dataset = []
num = 0
length = 0
for i in range(len(data)-2):
    if int(data[i+1][3])-int(data[i][3]) == 100:
        length += 1
    else:
        if length >= 5:
            dataset += data[i-length:i+1]
            num += 1
        length = 0

print('异常数据长度为：', len(dataset), ';', '共', num, '个场景')
# 存储数据
data_dump = dataset
name = ['ID', 'VehicleId', 'TripId', 'Time', 'Speed', 'LongtiAcc', 'a_la']
test = pd.DataFrame(columns=name, data=data_dump)
test.to_csv("Lateral-normal-point-del.csv", encoding='gbk')