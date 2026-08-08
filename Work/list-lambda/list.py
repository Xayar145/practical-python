'''
列表表达式练习：
列表表达式    [ 返回值  for a in A  条件 ]  

问题： 如果list推导式未闭合，检查是否是条件，即if
'''

tasks = [
    {"id": 1, "title": "学习Python", "status": "完成", "priority": 3},
    {"id": 2, "title": "学习C#", "status": "进行中", "priority": 2},
    {"id": 3, "title": "刷算法题", "status": "完成", "priority": 1},
    {"id": 4, "title": "写项目", "status": "未开始", "priority": 3},
]

result = [task['title'] for task in tasks if task['status'] == '完成']
print(result)

students = [
    {"name":"Tom","score":85},
    {"name":"Jack","score":60},
    {"name":"Mary","score":92},
    {"name":"Bob","score":45}
]

result = [
        task['name']
        for task in students
        if task['score']>60
]
print(result)

numbers = [1,2,3,4,5,6,7,8,9,10]

result = [
        number*number
        for number in numbers
        if not number%2
]
print(result)




products = [
    {
        "name":"电脑",
        "price":8000,
        "stock":5
    },
    {
        "name":"鼠标",
        "price":100,
        "stock":0
    },
    {
        "name":"键盘",
        "price":500,
        "stock":10
    }
]

result = sorted([
        task
        for task in products
        if task['stock'] > 0
],key= lambda x : x['price'],reverse=True)
print(result)


