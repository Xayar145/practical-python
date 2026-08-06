import time
import functools
from collections import Counter

def timethis(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        r = func(*args,**kwargs)
        end = time.time()
        print('%s.%s:%f'% (func.__module__,func.__name__,end - start))
        return r
    return wrapper

@timethis
def countdown(n):
    while n > 0:
        n -= 1

fruits = ["苹果","香蕉","西瓜","苹果","西瓜","西瓜","番茄"]

fruit_count = {}

for fruit in fruits:
    if fruit in fruit_count:
        fruit_count[fruit] += 1
    else:
        fruit_count[fruit] = 1
print(fruit_count)

for fruit in fruits:
    fruit_count[fruit] = fruit_count.get(fruit, 0) + 1
print(fruit_count)

fruit_count = Counter(fruits)
print(dict(fruit_count))