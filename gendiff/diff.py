import itertools
from gendiff.formatter import pretty_stylish, format_value


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


def _from_diff_list_to_dict(diff):
    result_dict = {}
    for tuple in diff:
        state, key, value = tuple
        if state == 'dictionary':
            nested = _from_diff_list_to_dict(value)
            result_dict.update(pretty_stylish(state, key, nested))
        else:
            result_dict.update(pretty_stylish(state, key, value))
    return result_dict


def stringify_diff(value, replacer=' ', spaces_count=4):
    result_dict = _from_diff_list_to_dict(value)
    def inner(current_value, depth):
        if not isinstance(current_value, dict):
            return format_value(current_value)
            
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