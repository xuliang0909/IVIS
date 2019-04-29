import csv
import sys
import pandas as pd
# 输入数据list(单列数据),筛选删除空白较多的数据
def data_filter(data, dataset):
    '''
    :param data: 整个数据
    :param dataset: 单列数据
    :return: 返回删除较多空白行之后的数据
    '''
    for i in range(len(dataset)-1):
        # sum_num = 0
        # for e in dataset:
        #     if e != None:
        #         sum_num += float(e)
        # average_value = sum_num/len(dataset)
        if dataset[i] == ' ' and i < (len(dataset)-11):
            # dataset[i] = average_value
            t = 0
            for e in range(i, i+10):
                if dataset[e] == ' ':
                    t += 1
            if t >= 5:
                for datalist in data:
                    del(datalist[i:i+10])
        if i >= len(data[0])-1:
            break
    return data

# 导入数据
filename = "15_del.csv"
# filename = "11.csv"
data = []
lis = [i for i in range(8)]
for i in range(len(lis)):
    with open(filename) as f:
        next(f)
        reader = csv.reader(f)      # 或者：reader = f.readlines()[1:]
        data.append([row[i] for row in reader])
print(len(data[0]), data[6][50:100])
# 删除、补全空白行
for i in range(3):
    data = data_filter(data, data[6])
    data = data_filter(data, data[4])
    data = data_filter(data, data[5])

# data = data_filter(data, data[6])
print(len(data[0]))

# 存储数据
data_dump = [[data[0][i], data[1][i], data[2][i], data[3][i], data[4][i],
              data[5][i], data[6][i], data[7][i]] for i in range(len(data[0]))]
name = ['ID', 'VehicleId', 'TripId', 'Time', 'Speed', 'LongtiAcc', '车道线宽度', '测量概率']
test = pd.DataFrame(columns=name, data=data_dump)
test.to_csv("del_blank.csv", encoding='gbk')
