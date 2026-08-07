#最大的问题：对象和字典混用

class Task:
    def __init__(self,id,title,status,priority,tags:list):
        self.id = id
        self.title = title 
        self.status = status
        self.priority = priority
        self.tags = tags

    def __str__(self):
        return (
            f"id={self.id}, "
            f"title={self.title}, "
            f"status={self.status}, "
            f"priority={self.priority}, "
            f"tags={self.tags}"
        )
    
    def __repr__(self):
        return self.__str__()

    def Updata_task_status(self,status):
        self.status = status

    def Updata_task_priority(self,priority):
        self.priority = priority

    def Updata_task_tags(self,gas,tags):
        if(gas == 1):
            self.tags.append(tags)
        else:
            self.tags.remove(tags)

class Task_manage:
    def __init__(self):
        self.task_list = []

    def Add_task(self,title,status = '未开始' ,priority= '低',tags =None):
        if tags ==None:
            tags = []

        new_task = Task(
            id= len(self.task_list)+1,
            title= title,
            status= status,
            priority=priority,
            tags= tags
        )

        self.task_list.append(new_task)   #此时放入task_list的是一个Task对象
    
    def Del_task(self,task):
        self.task_list.remove(task)
        print("删除成功！")


    def Find_task(self,keywords):
        result = []
        for task in self.task_list:
            if keywords in task.title or keywords in task.tags:    #
                result.append(task)
        return result

    def find_by_id(self,task_id):
        for task in self.task_list:
            if task.id == task_id:
                return task
        
        return None

    def find_by_title(self,task_title):
        for task in self.task_list:
            if task.title == task_title:
                return task
        
        return None
    def find_meth(self, query):
        if query.isdigit():
            return self.find_by_id(int(query))

        return self.find_by_title(query)

    def filter_by_status(self,status):
        '''
        列表表达式    [ 返回值  for a in A  条件 ]  
        '''
        return [
            task
            for task in self.task_list 
            if task.status == status
            ]

    def sort_by_priority(self):
        '''
        lambda表达式：python的lambda表达式是匿名函数，通常只有一行
         Key=lambda 参数: 返回值
         相当于   函数名(参数)
                    返回值
                Key = 函数()
        常用与排序，此案例需背诵
        '''
        priority_order = {
            '高' : 1,
            '中' : 2,
            '低' : 3
        }
        return sorted(
            self.task_list,
            key = lambda task:priority_order[task.priority]
        )
    def count_by_status(self):
        '''
        定义一个字典，然后遍历字典，有就加一，无就设为一
        传入是self.list
        需要一个字典，然后找到字典的status，当作key，对每一个元素进行处理
        需要的数据结构是
        {
             "未开始": 3,
             "进行中": 1,
             "已完成": 2
        }
        '''
        result = {}

        for task in self.task_list:
            status = task.status

            if status not in result:
                result[status] = 1
            else:
                result[status] += 1 
        return result

def main():
    manager = Task_manage()

    while (True):
        print("1. 添加任务")
        print("2. 查看任务")
        print("3. 修改任务")
        print("4. 删除任务")
        print("5. 查找任务")
        print("0. 退出")

        choice = input("请选择：")

        if choice == "1":
            title = input("任务标题：")
            manager.Add_task(title = title)

        elif choice == "2":
            for task in manager.task_list:
                print(task)

        elif choice == "3":
            '''
            思路2：
            同样的，user 给出修改的任务id或者title，然后给出具体的修改主题和内容
            中间层需要把用户输入的内容，先找到对应的task，然后传入Task类，调用Task类方法即可
            函数只管修改，但是此修改的方法在，Task类里，只接受Task类的调用
            '''
            query = input("输入要修改任务的id/title：")
            task = manager.find_task(query)

            task = manager.find_by_id(int(query))
            print("title,status,priority,tags")
            task_key = input("输入要修改任务的主题:")
            task_value = input("输入要修改任务的内容:")
            if task_key == "title":
                task.title = task_value
            elif task_key == "status":
                task.Updata_task_status(task_value)
            elif task_key == "priority":
                task.Updata_task_priority(task_value)
            elif task_key == "tags":
                task.Updata_task_tags(1, task_value)
            '''
                    不对，写到这里，我本来是要调用tasker的方法的，但是我发现除非一个一个写
                    不然是没办法调用update_task_ status/priority/tags

                    而且最关键的是，我都依旧找到他的key了，我可以直接让value= task，那之前的思路就乱了，我觉得之前的还是好的，应该是我的函数写的思路有问题
                    然后就是我发现用户输入id/title这个可以写一个函数封装起来，进行复用，区别是参数不一样id和string，因为python没有重载
                    所以可能用到*args / **kwargs，但是这个只是一个参数，只是有两种数据类型。
            '''

        elif choice == "4":
            '''
            思路1：
            按照id删除，或者按照 title删除
            删除函数不管删除的内容，只管删除
            而用户不管是怎么删除的，只在意输入的id和tile
            中间层负责把用户输入的id或者title，转换成删除函数所需要的task。
            '''
            query = input("输入删除任务的id/title：")
            task = manager.find_task(query)
            if task is None:
                print("没有找到这个任务。")
            else:
                manager.Del_task(task)


        elif choice == '5':
            keyword = input("输入查找内容：")
            result = manager.Find_task(keyword)
            if not result:     #result == None不适合判断空列表  应该使用if not result:
                print("为找到结果")
            else:
                for task in result:
                    print(task)

        elif choice == "0":
            break

        else:
            print("输入无效。")

if __name__ == "__main__":
    main()