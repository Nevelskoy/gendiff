DUMMY = '[complex value]'


def set_value_format(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return f"'{value}'"
    return str(value)


def _put_dummy(value):
    if isinstance(value, dict):
        return DUMMY
    elif isinstance(value, tuple):
        new_value = [value[0], value[1]]
        if isinstance(value[0], dict):
            new_value[0] = DUMMY
        else:
            new_value[0] = set_value_format(value[0])
            
        if isinstance(value[1], dict):
            new_value[1] = DUMMY
        else:
            new_value[1] = set_value_format(value[1])
            
        return tuple(new_value)
    return set_value_format(value)


def _plain_format(state, pipline, value):
    value = _put_dummy(value)
    buffer_plain = ''
    if state == 'added':
        buffer_plain = f"Property '{pipline}' was added with value: {value}\n"
    elif state == 'deleted':
        buffer_plain = f"Property '{pipline}' was removed\n"
    elif state == 'changed':
        buffer_plain = f"Property '{pipline}' was updated. From {value[0]} to {value[1]}\n"

    return buffer_plain


def stringify_plain(data):

    def inner(pipline, value_data):
        result = []
        for tuple in value_data:
            state, key, value = tuple
            key = f'{pipline}{key}'
            if state != 'dictionary':            
                result.append(_plain_format(state, key, value))
            else:
                path_key = f'{key}.'
                result.append(inner(path_key, value))               
        return ''.join(result)
    return inner('', data)