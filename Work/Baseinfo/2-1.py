
row = ['AA', '100', '32.20']
t = (row[0],int(row[1]),float(row[2]))
cost = t[1]*t[2]
print(f'{cost:0.2f}')



d = {
        'name' : row[0],
        'shares' : int(row[1]),
        'price'  : float(row[2])
    }
print(d)
cost = d['shares']*d['price']
print(cost)
d['shares'] = 56
print(d)