'''
lambda表达式练习：
lambda表达式：python的lambda表达式是匿名函数，通常只有一行
         Key=lambda 参数: 返回值
         相当于   函数名(参数)
                    返回值
                Key = 函数()
'''


tasks = [
    {"id": 1, "title": "学习Python", "status": "完成", "priority": 3},
    {"id": 2, "title": "学习C#", "status": "进行中", "priority": 2},
    {"id": 3, "title": "刷算法题", "status": "完成", "priority": 1},
    {"id": 4, "title": "写项目", "status": "未开始", "priority": 3},
]

result = sorted(tasks, key=lambda x: x["priority"], reverse=True)
print(result)



students = [
    {"name":"Tom","score":85},
    {"name":"Jack","score":60},
    {"name":"Mary","score":92},
    {"name":"Bob","score":45}
]

result = sorted(students, key = lambda n: n['score'],reverse = True)
print(result)

files = [
    {
        "name":"test.py",
        "size":300
    },
    {
        "name":"main.py",
        "size":100
    },
    {
        "name":"data.json",
        "size":500
    }
]


result = sorted (files , key = lambda s : s['size'],reverse =False)
for task in result:
    print(task['name'])

employees = [
    {"name":"Tom","age":25,"salary":5000},
    {"name":"Jack","age":30,"salary":8000},
    {"name":"Mary","age":25,"salary":9000},
    {"name":"Bob","age":30,"salary":6000}
]

result = sorted(employees,key = lambda x:(x['age'],-x['salary']))
print(result)


numbers = [10,15,20,25,30,35]

result = list(filter(lambda x: x > 20 and x % 5 == 0, numbers))
print(result)
