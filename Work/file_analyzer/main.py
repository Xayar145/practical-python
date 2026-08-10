'''
E:\Code\Python\Agent\Model\Python\practical-python\Work\file_analyzer\
├── models.py
├── scanner.py
├── analyzer.py
├── reporter.py
└── main.py
项目只读取文件，不移动、不删除文件，也不做 UI 和 AI。
项目目标
输入一个目录后，程序完成：
扫描目录中的文件；
获取文件名、后缀、路径、大小；
按文件后缀统计数量；
统计不同类型文件的总大小；
按文件大小排序；
筛选指定后缀；
输出终端报告；
保存 JSON 报告。
'''

from scanner import load_path
from analyzer import analyzer_count, analyzer_size,sort_file,select_file
from reporter import build_report

def main():
    path = input("输入要分析的目录：")

    file_list = load_path(path)
    report = build_report(file_list)

    print(report)

if __name__ == "__main__":
    main()