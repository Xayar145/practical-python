class Task:
    def __init__(self,id,title,status,priority,tags:list):
        self.id = id
        self.title = title 
        self.status = status
        self.priority = priority
        self.tags = tags

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

    def Add_task(self,title,status = '未开始' ,priority= '低',tags = []):
        new_list = Task(
            id= len(self.task_list)+1,
            title= title,
            status= status,
            priority=priority,
            tags= tags
        )

        self.task_list.append(new_list)
    
    def Del_task(self,tasks):
        self.task_list = [t for t in self.task_list if t!= tasks]
        print("删除成功！")

    def Find_task(self,keywords):
        result = []
        for task in self.task_list:
            if keywords == task['title'] or keywords == task['tags']:
                result.append(task)
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
            print(manager.task_list)
            for task in manager.task_list:
                print(task)

        elif choice == "3":
            '''
            思路2：
            同样的，user 给出修改的任务id或者title，然后给出具体的修改主题和内容
            中间层需要把用户输入的内容，先找到对应的task，然后传入Task类，调用Task类方法即可
            函数只管修改，但是此修改的方法在，Task类里，只接受Task类的调用
            '''
            updatask = input("输入要修改任务的id/title：")
            try:
                num = int(updatask)
                for task in manager.task_list:
                    if task['id'] == num:
                        print(task)
                        tasker = Task(task)
                        task_key = input("输入要修改任务的主题")
                        task_value = input("输入要修改任务的内容")
                        for k,v in task.item():
                            if k.key() == task_key:
                                k.value = task_value
                                '''
                                不对，写到这里，我本来是要调用tasker的方法的，但是我发现除非一个一个写
                                不然是没办法调用update_task_ status/priority/tags

                                而且最关键的是，我都依旧找到他的key了，我可以直接让value= task，那之前的思路就乱了，我觉得之前的还是好的，应该是我的函数写的思路有问题
                                然后就是我发现用户输入id/title这个可以写一个函数封装起来，进行复用，区别是参数不一样id和string，因为python没有重载
                                所以可能用到*args / **kwargs，但是这个只是一个参数，只是有两种数据类型。
                                '''
            except:
                for task in manager.task_list:
                    if task['title'] == updatask:
                        print(task)
                        task_key = input("输入要修改任务的主题")
                        task_value = input("输入要修改任务的内容")
                        for k,v in task.item():
                            if k.key() == task_key:
                                k.value = task_value

        elif choice == "4":
            '''
            思路1：
            按照id删除，或者按照 title删除
            删除函数不管删除的内容，只管删除
            而用户不管是怎么删除的，只在意输入的id和tile
            中间层负责把用户输入的id或者title，转换成删除函数所需要的task。
            '''
            delmeth = input("输入删除任务的id/title：")
            try:
                num = int(delmeth)
                for task in manager.task_list:
                    if task['id'] == num:
                        manager.Del_task(task)
                        break
            except:
                
                for task in manager.task_list:
                    if task['title'] == delmeth:
                        manager.Del_task(task)
                        break

        elif choice == '5':
            keyword = input("输入查找内容：")
            result = manager.Find_task(keyword)
            if result == None:
                print("为找到结果")
            else:
                print(result)

        elif choice == "0":
            break

        else:
            print("输入无效。")

if __name__ == "__main__":
    main()