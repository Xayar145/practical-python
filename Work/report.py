# report.py
#
# Exercise 2.4
# pcost.py


import csv

def read_portfolio(filename):
    List = []
#读取到一个元组列表中
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            List.append
            ({'name':'row[0]',
            'shares':'int(row[1])',
            'price':'float(row[2]'
            })
    return List

portfolio = read_portfolio('Data/portfolio.csv')
print(portfolio)
print(portfolio[1])
total = 0
for s in portfolio:
    total += s[1]+s[2]
print(total)


total = 0
for name, shares, price in portfolio:
            total += shares*price

print(total)

