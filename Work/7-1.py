

def avg(x,*more):
    return float(x+sum(more))/(1+len(more))

print(avg(10,11))


print(avg(10,11,12))
          
print(avg(1,2,3,4,5))


data = ('GOOG',100,490.1)
