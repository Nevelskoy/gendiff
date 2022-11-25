from gendiff.read_file import to_read
from gendiff.diff import get_diff_list
from gendiff.diff import get_diff_dict
from gendiff.formaters.stylish import stringify_stylish
from gendiff.formaters.plain import stringify_plain
from gendiff.formaters.json import stringify_json


def _output_data(data, format_name):
    if format_name == "plain":
        return stringify_plain(data)
    elif format_name == "stylish":
        return stringify_stylish(data)
    elif format_name == "json":
        return stringify_json(data)


def generate_diff(first_file, second_file, format_output="stylish"):
    '''compare two files'''
    if not format_output:
        format_output = 'stylish'
    
    first_data = to_read(first_file)
    second_data = to_read(second_file)

    if format_output == "json":
        diff_data = get_diff_dict(first_data, second_data)
    else: 
        diff_data = get_diff_list(first_data, second_data)  
        
    return _output_data(diff_data, format_output)

