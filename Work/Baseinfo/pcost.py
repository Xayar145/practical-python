# pcost.py
#
# Exercise 1.27




with open("Data/portfolio.csv","rt") as f:
    header = next(f).split(',')
    sum =0
    for line in f:
        row = line.split(',')
        row[1] = int(row[1])
        row[2] = float(row[2])
        sum += row[2]*row[1]
    
    print(f"Total cost {sum}")


