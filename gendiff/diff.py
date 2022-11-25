def _form_list(first, second, key):
    if isinstance(first.get(key), dict) and isinstance(second.get(key), dict):
        return
      
    if key not in first:
        return ('added', key, second.get(key))
    elif key not in second:
        return ('deleted', key, first.get(key))
    elif first.get(key) == second.get(key):
        return ('unchanged', key, first.get(key))
    else: 
        return ('changed', key, (first.get(key), second.get(key)))


def get_diff_list(first, second):
    diff_data = []
    keys = first.keys() | second.keys()
    for key in sorted(keys):
        first_value = first.get(key)
        second_value = second.get(key)
        if isinstance(first_value, dict) and isinstance(second_value, dict):
            nested_dictionary = get_diff_list(first_value, second_value)
            diff_data.append(('dictionary', key, nested_dictionary))
        else:
            diff_data.append(_form_list(first, second, key))
    return diff_data


def get_diff_dict(file1, file2):
    keys1, keys2 = file1.keys(), file2.keys()
    keys = sorted(keys1 | keys2)
    tree = []
    for key in keys:
        if key not in keys1:
            children = {
                'status': 'added',
                'key': key,
                'value': file2[key]
            }
        elif key not in keys2:
            children = {
                'status': 'deleted',
                'key': key,
                'value': file1[key]
            }
        elif file1[key] == file2[key]:
            children = {
                'status': 'unchanged',
                'key': key,
                'value': file1[key]
            }
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            children = {
                'status': 'nested',
                'key': key,
                'value': get_diff_dict(file1[key], file2[key])
            }
        else:
            children = {
                'status': 'changed',
                'key': key,
                'value': [file1[key], file2[key]]
            }
        tree.append(children)
    return tree