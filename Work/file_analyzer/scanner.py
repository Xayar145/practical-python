import os
import csv

'''
负责扫描文件夹中的文件，读取为list套dict的格式
task = [
        {
        "filename" =
        "endname" =
        "size" =
        "path" = 
        ""
        }
]
需要使用os的内容

'''

def load_path(mkdirpath):
    '''
    使用os来获取文件夹中的内容， os.walk
    '''
    target_dirpath = mkdirpath
    result = []
    if not os.path.exists(target_dirpath):
        print("文件夹不存在")
        return result
    
    for root, dirs,files in os.walk(target_dirpath):
        for file in files:
            full_path = os.path.join(root,file)
            file_name,extension = os.path.splitext(file)
            file_size = os.path.getsize(full_path)
            result.append ({
                        "filename" : file_name,
                        "endname" :extension,
                        "size" :file_size/1024,
                        "path" : full_path
            })
    return result





