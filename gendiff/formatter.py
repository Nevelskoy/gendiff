def diff_dict(state, key, value):
    buffer_dict = {}
    if state == 'deleted':
        buffer_dict[f'- {key}'] = value
    elif state == 'changed':
         buffer_dict[f'- {key}'] = value[0]
         buffer_dict[f'+ {key}'] = value[1]
    elif state == 'added':
         buffer_dict[f'+ {key}'] = value
    elif state == 'unchanged':
         buffer_dict[f'  {key}'] = value
    else:
         buffer_dict[f'{key}'] = value
    return buffer_dict