import json
import csv
import os
from analyzer import analyzer_count, analyzer_size


def build_report(file_list):
    count = analyzer_count(file_list)
    size = analyzer_size(file_list)

    report = []

    for extension in count:
        report.append({
            "extension": extension,
            "count": count[extension],
            "size_mb": size[extension]
        })

    return report

def save_json(sava_path,build_file):
    '''
    json的使用需要记一下
    '''
    with open(sava_path, "w", encoding="utf-8") as file:
        json.dump(
            build_file,
            file,
            ensure_ascii=False,
            indent=4
        )

    print(f"JSON 报告已保存到：{sava_path}")


def save_csv(sava_path,build_file):
    if not os.path.exists(sava_path):
        os.makedirs(sava_path)

    fieldnames = ['extension','count','size_mb']
    with open (sava_path,'w',encoding='utf-8') as f:
        writer = csv.DictWriter(f,fieldnames=fieldnames)

        for task in build_file:
            row = {
                'extension':task['extension'],
                'count':task['count'],
                'size_mb':task['size_mb']
            }
            writer.writerow(row)
        print(f'成功：数据已保存至 {sava_path}')

