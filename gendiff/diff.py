

def diff_data(first_data, second_data):
    '''get diff structure'''
    #обход структуры через рекурсию, потому что вложенный json файл имеет рекурсивную природу.



def get_diff(first, second):
    '''get diff dictonary'''
    keys = first.keys() | second.keys()
    result = {}
    for key in sorted(keys):
        if key not in first:
            result[key] = 'added'
        elif key not in second:
            result[key] = 'deleted'
        elif first[key] == second[key]:
            result[key] = 'unchanged'
        else:
            result[key] = 'changed'
    return result

