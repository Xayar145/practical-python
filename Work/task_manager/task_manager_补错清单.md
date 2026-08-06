# task_manager.py 补错清单与复盘

复盘对象：`task_manager.py`

这份复盘的目标不是把代码改得很高级，而是找出当前代码为什么不稳定，并按照你已经在后半部分逐渐形成的思路，给出下一步可以接受的写法。

## 一、先给整体判断

你现在不是“完全不会写”，而是已经开始从“能写出一段代码”转向“考虑数据结构和函数职责”。这个转变在下面几个函数中已经很明显：

- `serch_by_keywork()` 开始接收参数，而不是所有事情都写死在函数里。
- `filter_by_status()` 开始先得到结果列表，再返回结果。
- `count_task()` 已经想到用 `len()` 统计数量。
- `load_file()` 和 `save_file()` 已经开始考虑 CSV、JSON 以及数据类型恢复。

但是，前半部分的代码仍然采用了“通过索引直接操作列表”的写法，后半部分又开始采用“遍历字典、生成结果、返回结果”的写法。两种思路混在一起，就产生了很多问题。

本次复盘的核心方向是：

```text
统一数据结构
    ↓
通过任务 id 找任务，而不是直接把 id 当列表索引
    ↓
查询函数返回结果
    ↓
修改和删除函数修改任务列表
    ↓
最后再处理 CSV 文件
```

## 二、整体性错误

### 1. 单个任务和任务列表混在了一个类中

当前的 `Task` 类接收了一个任务的 `id`、`title`、`status` 等信息，但随后又在类里面创建了 `task_list`。

这会造成一个问题：创建一个 `Task` 对象时，程序自动产生一个任务。可是从项目角度看，`Task` 应该表示一个任务，`task_list` 应该表示所有任务，二者不是同一层级的东西。

当前阶段不必马上设计多个类。最容易接受的做法是：

- 先保留一个类，暂时把它理解成“任务管理器”；或者
- 直接使用一个 `tasks = []` 和几个函数。

如果继续保留当前类，类名改成 `TaskManager` 会更符合它实际负责的内容，但这不是现在最重要的问题。

### 2. 数据结构没有统一

当前代码中出现了这些不同的键名：

```text
ID、Id、id
Title、title
Status、status
Priority、priority
Tags、tags
```

字典键名必须统一，否则保存、读取、查找时会互相找不到。

建议全程统一使用小写：

```python
{
    "id": 1,
    "title": "练习列表",
    "status": "未开始",
    "priority": "高",
    "tags": []
}
```

### 3. 把任务 id 当成了列表索引

例如：

```python
self.task_list[ID - 1]
```

这只有在任务 id 永远连续，并且删除任务后重新编号的情况下才成立。

如果删除了 id 为 2 的任务，列表索引和任务 id 就不再对应。因此正确思路应该是：遍历每个任务，比较 `task["id"]`，找到真正的任务后再操作。

### 4. 函数职责不统一

前面的函数负责接收参数、修改列表、打印结果；后面的查询函数开始返回结果。函数风格不统一，会导致调用方式混乱。

建议采用这个简单规则：

- 添加、修改、删除：修改 `task_list`，可以打印成功提示。
- 查找、筛选、统计：尽量返回结果，不在函数内部强行打印。
- 主程序负责接收用户输入和显示结果。

这正是你在 `serch_by_keywork()` 和 `filter_by_status()` 中已经开始形成的思路。

### 5. 还没有主程序入口

文件中目前只有类和方法定义，没有：

```python
manager = Task(...)
```

也没有菜单循环。因此直接运行文件时，Python 只会定义这些内容，不会执行任何任务。

后面需要补一个简单的 `main()`，并用：

```python
if __name__ == "__main__":
    main()
```

作为程序入口。

### 6. CSV 和 JSON 加得太早

CSV、JSON 本身不是不能学，而是当前的添加、修改、删除还没有稳定，就同时处理文件读写，会让错误很难定位。

推荐顺序：

```text
内存中的列表和字典
    ↓
添加、查看、修改、删除
    ↓
搜索和筛选
    ↓
CSV 保存
    ↓
CSV 加载
```

## 三、数据结构统一方案

本次复盘中的所有函数都使用以下结构：

```python
task_list = [
    {
        "id": 1,
        "title": "练习列表",
        "status": "未开始",
        "priority": "高",
        "tags": ["列表", "字典"]
    }
]
```

这里的关系是：

- 最外层是列表，保存多个任务。
- 每个任务是一个字典。
- `tags` 是一个列表，保存多个标签。

不要把 `tags` 标注成 `dict`。当前阶段可以先不写类型标注；如果要写，应该接近 `list`，而不是 `dict`。

## 四、逐个函数复盘

## 1. `__init__()`

当前写法的问题：

```python
def __init__(self, id: int, title: str, status: str, priority: str, tags: dict):
```

### 问题

1. 创建管理器时必须先传入一个任务，但一开始任务列表应该可以为空。
2. `__init__()` 同时接收“单个任务的信息”和“创建任务列表”，职责混乱。
3. 初始字典使用了大写键名，而后面的字典使用了小写键名。
4. `tags` 的类型写成了 `dict`，实际应该是列表。

### 当前水平适合的优解

如果暂时保留类，可以让这个类表示“任务管理器”：

```python
class TaskManager:
    def __init__(self):
        self.task_list = []
```

这样创建对象时不会自动添加任务：

```python
manager = TaskManager()
```

这已经足够支撑第一版，不需要马上学习复杂的类设计。

## 2. `add_task()`

### 当前写法的问题

1. `id` 由外部传入，容易重复。
2. 初始任务的键名和新增任务的键名不一致。
3. 函数同时负责添加数据和打印数据，暂时不算严重问题，但后续最好让主程序负责显示。
4. `tags` 的类型标注仍然错误。

### 当前水平适合的优解

先继续使用方法，并让程序自动生成 id：

```python
def add_task(self, title, status="未开始", priority="普通", tags=None):
    if tags is None:
        tags = []

    new_task = {
        "id": len(self.task_list) + 1,
        "title": title,
        "status": status,
        "priority": priority,
        "tags": tags
    }

    self.task_list.append(new_task)
    return new_task
```

这里的 `tags is None` 是为了避免多个任务意外共用同一个列表。

当前阶段可以先接受 `len(self.task_list) + 1` 生成编号。等以后处理删除、保存和加载时，再考虑更稳定的 id 方案。

## 3. `replace_task()`

这是当前问题最多的函数，主要问题不是某一个拼写，而是修改流程没有拆清楚。

### 当前写法的问题

1. `ID - 1` 直接作为列表索引，依赖 id 和索引永远一致。
2. `selet_list` 在循环中反复创建，循环结束后只保留最后一次的内容。
3. `rep_id == selet_list.keys()` 是整数和字典键集合比较，永远不会得到想要的结果。
4. `self.task_list[rep_id-1]['sec_id.Value()']` 不是有效的字典键写法，也没有真正根据用户选择修改字段。
5. `clear().append(text)` 会先清空列表，但 `clear()` 的返回值是 `None`，不能继续调用 `append()`。
6. 没有处理输入的任务 id 不存在的情况。

### 当前水平适合的优解

先不要做复杂的字段编号映射，直接把修改流程写清楚：

```python
def replace_task(self):
    task_id = int(input("选择你要修改的任务 id："))

    for task in self.task_list:
        if task["id"] == task_id:
            print(task)
            task["title"] = input("新的标题：")
            task["status"] = input("新的状态：")
            task["priority"] = input("新的优先级：")

            print("任务修改成功！")
            return

    print("没有找到这个任务。")
```

这版先修改标题、状态和优先级，标签可以后面单独处理。重点是先学会：

```text
遍历任务
    ↓
比较 task["id"]
    ↓
找到后修改字典
    ↓
return 结束函数
```

函数名建议改成 `update_task()`，因为这里不是替换整个任务，而是更新任务字段。

## 4. `del_task()`

### 当前写法的问题

```python
del self.task_list[ID - 1]
```

问题在于把任务 id 当成列表索引。删除任务后，后面的任务 id 和索引可能不一致。

另外，任务不存在时会触发 `IndexError`。

### 当前水平适合的优解

```python
def del_task(self):
    task_id = int(input("选择你要删除的任务 id："))

    for index, task in enumerate(self.task_list):
        if task["id"] == task_id:
            del self.task_list[index]
            print("任务删除成功！")
            return

    print("没有找到这个任务。")
```

这里第一次出现了 `enumerate()`。它只是同时得到“列表位置”和“列表元素”，目前值得掌握，不属于跨度很大的知识。

## 5. `find()`

### 当前写法的问题

1. 使用了 `i['Id']`，但统一后的键应该是 `id`。
2. `user_input` 是字符串，任务 id 通常是整数，不能直接比较。
3. `self.task_list[i]` 错误，因为 `i` 是一个任务字典，不是整数索引。
4. 这个函数只能精确查标题，不能进行关键词查找。

### 当前水平适合的优解

让函数返回结果列表，这和你后面的搜索函数思路一致：

```python
def find(self):
    keyword = input("输入任务 id 或标题关键词：").strip()
    result = []

    for task in self.task_list:
        if keyword == str(task["id"]) or keyword in task["title"]:
            result.append(task)

    return result
```

调用这个函数的地方再负责显示：

```python
result = manager.find()
for task in result:
    print(task)
```

## 6. `serch_by_keywork()`

这个函数是当前代码中思路比较好的部分之一：它接收关键词，创建结果列表，最后返回结果。

### 当前写法的问题

1. 函数名拼写错误：`serch` 应该是 `search`，`keywork` 应该是 `keyword`。
2. `keyword in task['Tags']` 要求标签列表中存在完全相同的标签，不是标签文本中的部分匹配。这不一定是错误，但要明确这是“标签匹配”。
3. 依赖大写键名 `Tags`，和统一数据结构不一致。

### 当前水平适合的优解

```python
def search_by_keyword(self, keyword):
    result = []

    for task in self.task_list:
        if keyword in task["title"] or keyword in task["tags"]:
            result.append(task)

    return result
```

这个函数可以保留你现在的整体思路，不需要重写成复杂的列表推导式。

## 7. `filter_by_status()`

这个函数的结构也是比较好的：接收条件、遍历任务、得到结果、返回结果。

### 当前写法的问题

```python
if target_status in task['Status']:
```

如果状态是一个单独的字符串，通常应该使用 `==`，表示状态完全相等。`in` 更适合判断一个字符串是否包含另一个字符串。

### 当前水平适合的优解

```python
def filter_by_status(self, target_status):
    result = []

    for task in self.task_list:
        if task["status"] == target_status:
            result.append(task)

    return result
```

## 8. `count_task()`

### 当前写法的问题

```python
return [len(self.task_list)]
```

你已经正确想到使用 `len()`，但外面多套了一层列表。统计数量应该返回整数，而不是只包含一个整数的列表。

### 当前水平适合的优解

```python
def count_task(self):
    return len(self.task_list)
```

如果以后要统计不同状态，再单独增加统计函数，不要让这个函数同时承担太多工作。

## 9. `load_file()`

这个函数现在属于“方向正确，但文件细节还没有串起来”。

### 当前写法的问题

1. `os.path.exist()` 拼写错误，应为 `os.path.exists()`。
2. 默认文件名 `tast.csv` 可能是 `task.csv` 的拼写错误。
3. 加载出来的字典键名是小写，但当前任务列表中的字典键名有大写和小写混用。
4. 读取后直接 `append()`，如果重复加载，会把任务重复添加。
5. `row['tags']` 为空或格式错误时，`json.loads()` 会报错。
6. 加载的数量应该是本次读取的数量，不应该直接使用整个 `self.task_list` 的长度。

### 当前水平适合的优解

先使用统一的小写字段：

```python
def load_file(self, filename="tasks.csv"):
    if not os.path.exists(filename):
        print("文件不存在，暂时使用空任务列表。")
        return

    self.task_list = []

    with open(filename, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            task = {
                "id": int(row["id"]),
                "title": row["title"],
                "status": row["status"],
                "priority": row["priority"],
                "tags": json.loads(row["tags"]) if row["tags"] else []
            }
            self.task_list.append(task)

    print(f"成功加载 {len(self.task_list)} 条任务。")
```

这版暂时没有加入复杂的异常处理。等基本读写成功后，再处理坏数据。

## 10. `save_file()`

这是当前文件操作问题最集中的函数。

### 当前写法的问题

1. `os.path.exist()` 拼写错误。
2. 不需要先判断 CSV 文件是否存在，使用写入模式时 Python 会自动创建文件。
3. `os.makedirs(filename)` 会尝试创建一个名为 `save_file.csv` 的文件夹。
4. `open(filename, 'rt')` 使用了读取模式，保存时应该使用 `w`。
5. `csv.DictWriter()` 使用了不存在的 `filename` 参数，应该传入 `fieldnames`。
6. `writer.writeheader()` 在 `with` 代码块外面，文件已经关闭。
7. `writer.writerow(row)` 在循环外面，因此最多只会写入最后一个任务。

### 当前水平适合的优解

```python
def save_file(self, filename="tasks.csv"):
    fieldnames = ["id", "title", "status", "priority", "tags"]

    with open(filename, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for task in self.task_list:
            row = task.copy()
            row["tags"] = json.dumps(task["tags"], ensure_ascii=False)
            writer.writerow(row)

    print(f"成功保存到 {filename}。")
```

这里要特别注意缩进：写表头和写每一行都必须在 `with open()` 内部，`writer.writerow(row)` 必须在 `for` 循环内部。

## 五、建议补上的主程序入口

你现在缺少一个真正运行这些函数的地方。当前阶段不需要复杂菜单，可以先写一个非常简单的入口：

```python
def main():
    manager = TaskManager()

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
```

这段代码不是要求你现在直接复制完成，而是帮助你理解：方法定义之后，还需要一个地方调用方法。

## 六、推荐的实际重写顺序

不要现在继续在原文件上同时修所有问题。建议把当前文件留作草稿，按下面顺序重新写一个基础版：

### 第一步：只保留列表和字典

完成：

- 创建空任务列表；
- 添加任务；
- 显示任务；
- 删除任务；
- 修改任务。

暂时删除或不写：

- `csv`；
- `json`；
- `load_file()`；
- `save_file()`；
- 复杂标签修改。

### 第二步：加入查询

完成：

- `find()`；
- `search_by_keyword()`；
- `filter_by_status()`；
- `count_task()`。

这一阶段重点练习“函数返回结果”，这是你后面几个函数已经开始形成的正确方向。

### 第三步：加入 CSV 保存

只先完成保存，不要马上同时完成加载。先检查 CSV 文件中是否真的有多条记录。

### 第四步：加入 CSV 加载

先实现正常文件的读取，再考虑文件不存在和坏数据。

## 七、完成标准

基础版完成后，至少要通过这些操作：

- 添加 3 个任务；
- 查看全部任务；
- 修改第 2 个任务；
- 删除第 1 个任务；
- 查找一个标题关键词；
- 按状态筛选任务；
- 统计当前任务数量；
- 输入不存在的 id 时，程序不崩溃；
- 关闭程序后重新运行，CSV 能恢复任务。

## 八、这次复盘最需要记住的三件事

1. 任务 id 是数据中的字段，不一定等于列表索引。
2. 查询函数可以返回结果，修改函数才负责改变原列表。
3. 文件读写要最后加入，并且先统一字典键名和数据结构。

