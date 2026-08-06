#掌握列表推导式、集合推导式和字典推导式的各种组合用法，在各种数据处理中都非常有用。以下示例展示了如何从 CSV 文件中提取选定的列。

#首先，从 CSV 文件中读取一行标题信息：

import csv
f = open('Data/portfoliodate.csv')
rows = csv.reader(f)
headers = next(rows)
headers


#接下来，定义一个变量来列出你真正关心的列：

select = ['name', 'shares', 'price']
#现在，请在源 CSV 文件中找到上述各列的索引：

indices = [ headers.index(colname) for colname in select ]
indices
[0, 3, 4]

#最后，读取一行数据，并使用字典推导式将其转换为字典：

row = next(rows)
record = { colname: row[index] for colname, index in zip(select, indices) }   # dict-comprehension
record
{'price': '32.20', 'name': 'AA', 'shares': '100'}

#如果您对刚才发生的事情感到满意，请继续阅读文件剩余部分：

portfolio = [ { colname: row[index] for colname, index in zip(select, indices) } for row in rows ]
portfolio
[{'price': '91.10', 'name': 'IBM', 'shares': '50'}, {'price': '83.44', 'name': 'CAT', 'shares': '150'},
  {'price': '51.23', 'name': 'MSFT', 'shares': '200'}, {'price': '40.37', 'name': 'GE', 'shares': '95'},
  {'price': '65.10', 'name': 'MSFT', 'shares': '50'}, {'price': '70.44', 'name': 'IBM', 'shares': '100'}]
