from collections import Counter

def analyzer_count(file_list):
    result = []
    result = Counter(task['endname']for task in file_list)
    return result

def analyzer_size(file_list):
    '''
    result = [{
            endname:total_size
    }]
    '''
    result = {}
    for file in file_list:
        extension = file["endname"]
        if extension not in result:
            result[extension] = file["size"]
        else:
            result[extension] += file["size"]

    return result


def sort_file(file_list):
    return sorted(file_list,key = lambda s : s['size'],reverse= True)

def select_file(file_list,select_end):
    return  [file
             for file in file_list
             if file['endname'] == select_end]



