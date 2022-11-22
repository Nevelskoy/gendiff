from gendiff.read_file import to_read
from gendiff.diff import get_diff_data
from gendiff.formaters.format_data import output_data
#from gendiff.formatter import style

#TODO: add formatter
def generate_diff(first_file, second_file, format='stylish'):
    '''compare two files'''
    first_files_data = to_read(first_file)
    second_files_data = to_read(second_file)
    diff_list = get_diff_data(first_files_data, second_files_data)
    return output_data(diff_list, format)

