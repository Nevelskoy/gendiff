import itertools


def _format_value(pretty_diff_value):
    if isinstance(pretty_diff_value, bool):
        return 'true' if pretty_diff_value else 'false'
    if pretty_diff_value is None:
        return 'null'
    return str(pretty_diff_value)


def _dict_stylish(state, key, value):       
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


def _from_diff_list_to_dict(diff):
    result_dict = {}
    for tuple in diff:
        state, key, value = tuple
        if state == 'dictionary':
            nested = _from_diff_list_to_dict(value)
            result_dict.update(_dict_stylish(state, key, nested))
        else:
            result_dict.update(_dict_stylish(state, key, value))
    return result_dict


def stringify_stylish(value, replacer=' ', spaces_count=4):
    result_dict = _from_diff_list_to_dict(value)
    def inner(current_value, depth):
        if not isinstance(current_value, dict):
            return _format_value(current_value)
            
        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []      
        for key, val in current_value.items():
            if key[0] == '+' or key[0] == '-':
                sign_indent = replacer * (deep_indent_size - 2)
                lines.append(f'{sign_indent}{key}: {inner(val, deep_indent_size)}')
            else:
                lines.append(f'{deep_indent}{key}: {inner(val, deep_indent_size)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    return inner(result_dict, 0)