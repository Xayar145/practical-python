import csv
import json
import os

class Task_manage:
    def __init__(self):
        self.task_list = []



class Task:
    def __init__(self,id:int,title:str,status:str,priority:str,tags:list):
        '''
        初始化属性，定义task列表，获取基本数据结构。
        '''

        self.id = id
        self.title = title
        self.status = status
        self.priority = priority
        self.tags = tags

        self.task_list = [{
            'ID' : self.id,
            'Title' : self.title,
            'Status'  :self.status,
            'priority' : self.priority,
            'Tags' : self.tags,
        }]
    
    def add_task(self,id:int,title:str,status:str,priority:str,tags:list):
        '''
        添加任务。使用初始化task_list
        '''

        new_list ={
            'ID': id,
            'Title': title,
            'Status': status,
            'Priority': priority,
            'Tags': tags,
        }
        self.task_list.append(new_list)

        print("任务添加成功！")
        print(f"当前任务数量：{len(self.task_list)}")
        print(f"{new_list}")

    def replace_task(self):
        '''
        首先把序号和键放入新的字典，然后通过用户选择的数字和序号进行对比，来索引到正确的key，对其value进行修改。
        '''
        ###问题1：
        ###问题2：ID - 1直接作为列表索引，依赖 id 和索引永远一致。
        print(f"{self.task_list}")
        ID = int(input("选择你要修改的任务ID："))
        print(f'{self.task_list[ID-1]}')
        print("输入你要修改的内容编号：(ID不可修改)")
        for i,k in enumerate(self.task_list[0].keys()):
            selet_list = {}
            selet_list[i] = k
            print(f'{selet_list}')

        rep_id = int(input("输入数字："))
        text = input('请输入修改的内容：')

        for rep_id in selet_list.keys():
            if (rep_id == selet_list.keys() and rep_id != 5):
                self.task_list[rep_id-1]['sec_id.Value()'] = text
            elif (rep_id == 5):
                print("输入你要修改的方式：")
                print("1.添加  2.替换")
                sec_id = int(input("输入数字："))
                if(sec_id==2):
                    self.task_list[rep_id-1]['Tags'].clear().append(text)
                else:
                    self.task_list[rep_id-1]["Tags"].append(text)
            else:
                continue

    def del_task(self):
        '''
        直接使用del索引task列表的索引值，进行删除
        '''
        print(f"{self.task_list}")
        ID = int(input("选择你要删除的任务ID："))

        del self.task_list[ID-1]

    def find(self):
        '''
        用户输入一个任务id/主题，然后通过用户输入的内容，对列表的字典的键值进行遍历，并返回对应的任务字典内容
        '''

        user_input = input("选择你要查找的任务(ID/Title)：")

        if(user_input.isdigit()):
            for i in self.task_list:
                if(i['Id'] == user_input):
                    print(self.task_list[i])
                else:
                    continue
        else:
            for i in self.task_list:
                if(i['Title']==user_input):
                    print(self.task_list[i])

                else:
                    continue

    def serch_by_keywork(self,keyword):
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
            if target_status in task['Status']:
                result.append(task)
        return result

    def count_task(self):
        return [len(self.task_list)]


    def load_file(self,filename = 'tast.csv'):
        
        if not os.path.exist(filename):
            print(f'提示：文件 {filename} 不存在，返回空列表。')
            return []

        result = []
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
        if not os.path.exist(filename):
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

