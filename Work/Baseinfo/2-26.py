import csv

f = open('Data/dowstocks.csv')
rows = csv.reader(f)
print(rows)
header = next(rows)
print(header)
row = next(rows)
print(row)

#清洗处理数据
type =[str, float, str, str, float, float, float, float, int]
converted = [func(val) for func , val in zip(type,row)]
#创建字典
record = dict(zip(header,converted))
print(record)

