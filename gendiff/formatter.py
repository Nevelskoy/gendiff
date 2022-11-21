def format_value(pretty_diff_value):
    if isinstance(pretty_diff_value, bool):
        return 'true' if pretty_diff_value else 'false'
    if pretty_diff_value is None:
        return 'null'
    return str(pretty_diff_value)


def pretty_stylish(state, key, value):       
    buffer_dict = {}
    if state == 'deleted':
        buffer_dict[f'- {key}'] = value
    elif state == 'changed':
         buffer_dict[f'- {key}'] = value[0]
         buffer_dict[f'+ {key}'] = value[1]
    elif state == 'added':
         buffer_dict[f'+ {key}'] = value
    else:
         buffer_dict[f'{key}'] = value
    return buffer_dict