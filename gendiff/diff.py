def _get_diff_list(first, second, key):
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


def get_diff_data(first, second):
    result = []
    keys = first.keys() | second.keys()
    for key in sorted(keys):
        first_value = first.get(key)
        second_value = second.get(key)
        if isinstance(first_value, dict) and isinstance(second_value, dict):
            nested_dictionary = get_diff_data(first_value, second_value)
            result.append(('dictionary', key, nested_dictionary))
        else:
            result.append(_get_diff_list(first, second, key))
    return result
