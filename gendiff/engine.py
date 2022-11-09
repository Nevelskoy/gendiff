import json

def generate_diff(first_file, second_file):
    '''compare two files'''   
    first_files_data = json.load(open(first_file))
    second_files_data = json.load(open(second_file))
    return matching_data(first_files_data, second_files_data)


def matching_data(data1, data2):
    keys = data1.keys() | data2.keys()
    result = '{\n'
    for key in sorted(keys):
        if key not in data2:
            result += f'  - {key}: {data1[key]}\n'
        elif key in data2 and key in data1:
            if data1[key] != data2[key]:
                result += f'  - {key}: {data1[key]}\n'
                result += f'  + {key}: {data2[key]}\n'
            else:
                result += f'    {key}: {data1[key]}\n'
        else: 
            result += f'  + {key}: {data2[key]}\n'
    return result + '}'
