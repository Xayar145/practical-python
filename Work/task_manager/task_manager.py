import csv
import json
import os

class Task_manage:
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)

class Task:
    def __init__(self,id:int,title:str,status:str,priority:str,tags:list):
        '''
        初始化属性，定义task列表，获取基本数据结构。
        '''
        ## 问题1：__init__()同时接收“单个任务的信息”和“创建任务列表”，职责混乱。
        ## 问题2： 初始字典使用了大写键名，而后面的字典使用了小写键名。
        self.id = id
        self.title = title
        self.status = status
        self.priority = priority
        self.tags = tags
    
    def add_task(self,id:int,title:str,status:str,priority:str,tags:list):
        '''
        添加任务。使用初始化task_list
        '''
        ##问题1： id由外部传入，容易重复
        ##问题2： 初始任务的键名和新增任务的键名不一致。
        ##问题3： 生成id编码/status内容是要自己定义的，需要考虑这个问题，第一次写的时候没有考虑此内容
        ##问题4： 没有返回新的list数组，这个数组是一个临时的列表，如果不return，会消失的
        new_list ={
            'ID': len(self.task_list) + 1,
            'Title': title,
            'Status': status,
            'Priority': priority,
            'Tags': tags,
        }
        self.task_list.append(new_list)

        print("任务添加成功！")
        print(f"当前任务数量：{len(self.task_list)}")
        print(f"{new_list}")
        return new_list

    def replace_task(self):
        '''
        首先把序号和键放入新的字典，然后通过用户选择的数字和序号进行对比，来索引到正确的key，对其value进行修改。
        '''
        ###问题1：
        ###问题2：ID - 1直接作为列表索引，依赖 id 和索引永远一致。
        task_id = int(input("选择你要修改的任务 id："))
    
        for task in self.task_list:
            if task['id'] == task_id:
                print(task)
                task["title"] = input("新的标题：")
                task["status"] = input("新的状态：")
                task["priority"] = input("新的优先级：")

                print("任务修改成功！")
                return 
        print("没有找到这个任务")

    def del_task(self):
        '''
        直接使用del索引task列表的索引值，进行删除
        '''
        ##问题：把任务 id 当成列表索引。删除任务后，后面的任务 id 和索引可能不一致。
        ##如果中间删一个任务，任务id不变，但是索引值发生了改变，就不准了
        task_id = int(input("选择你要删除的任务 id："))

        for index,task in enumerate(self.task_list):
            if task['id'] == task_id:
                del self.task_list[index]
                print("任务删除成功")
                return
        return("没有找到这个任务")

    def find(self):
        '''
        用户输入一个任务id/主题，然后通过用户输入的内容，对列表的字典的键值进行遍历，并返回对应的任务字典内容
        '''
        ##2.user_input是字符串，任务id通常是整数，不能直接比较。
        ##3.self.task_list[i]错误，因为i是一个任务字典，不是整数索引。
        keyword =input("输入任务 id 或标题关键词：").strip()
        result =[]

        for task in self.task_list:
            if keyword == str(task['id']) or keyword  in task['title']:
                result.append(task)

    def search_by_keywork(self,keyword):
        '''
        直接接受外部的关键词参数，然后定义结果列表，对其Title和Tags进行遍历。
        '''
        result = []
        for task in self.task_list:
            if keyword in task['Title'] or keyword in task['Tags']:
                result.append(task)
        return result

    def filter_by_status(self,target_status):
        '''
        和关键字搜索一样，
        '''
        result = []
        for task in self.task_list:
            if task['status'] == target_status:
                result.append(task)
        return result

    def count_task(self):
        return len(self.task_list)


    def load_file(self,filename = 'task.csv'):
        '''
        
        '''
        if not os.path.exists(filename):
            print(f'提示：文件 {filename} 不存在，返回空列表。')
            return []

        self.task_list = []

        with open(filename,'rt',encoding='utf-8') as f:
            reader =csv.DictReader(f)

            for row in reader:
                task = {
                        'id': int(row['id']),  # 字符串转回整数
                        'title': row['title'],
                        'status': row['status'],
                        'priority': row['priority'],
                        'tags': json.loads(row['tags']),  # 将 JSON 字符串还原为 Python 列表
                        }
                self.task_list.append(task)
        print(f'成功：已从 {filename} 加载 {len(self.task_list)} 条任务数据')
        return self.task_list

    def save_file(self,filename = 'save_file.csv'):
        if not os.path.exists(filename):
            os.makedirs(filename)
        
        fieldnames = ['Id', 'Title', 'Status', 'Priority', 'Tags']

        with open (filename,'rt',encoding='utf-8') as f:
            writer = csv.DictWriter(f,filename = filename)

        writer.writeheader()

        for task in self.task_list:
            row = task.copy()
            row['Tags'] = json.dumps(task['Tags'],ensure_ascii=False)

        writer.writerow(row)

        print(f'成功：数据已保存至 {filename}')

def main():
    manager = Task_manage()

    while True:
        print("1. 添加任务")
        print("2. 查看任务")
        print("3. 修改任务")
        print("4. 删除任务")
        print("0. 退出")

        choice = input("请选择：")

        if choice == "1":
            title = input("任务标题：")
            manager.add_task(title)
        elif choice == "2":
            for task in manager.task_list:
                print(task)
        elif choice == "3":
            manager.replace_task()
        elif choice == "4":
            manager.del_task()
        elif choice == "0":
            break
        else:
            print("输入无效。")

if __name__ == "__main__":
    main()
