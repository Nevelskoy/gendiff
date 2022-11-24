from gendiff.read_file import to_read
from gendiff.diff import get_diff_data
from gendiff.formaters.stylish import stringify_stylish
from gendiff.formaters.plain import stringify_plain


def _output_data(data, format_name):
    if format_name == "plain":
        return stringify_plain(data)
   # elif format_name == "json":
   #     return stringify_json(data)
   # else:
    return stringify_stylish(data)


def generate_diff(first_file, second_file, format="stylish"):
    '''compare two files'''
    first_files_data = to_read(first_file)
    second_files_data = to_read(second_file)
    diff_list = get_diff_data(first_files_data, second_files_data)
    return _output_data(diff_list, format)

