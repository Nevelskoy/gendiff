from gendiff.read_file import to_read
from gendiff.diff import get_diff_data
from gendiff.diff import stringify_diff
#from gendiff.formatter import style

#TODO: add formatter
def generate_diff(first_file, second_file):
    '''compare two files'''
    first_files_data = to_read(first_file)
    second_files_data = to_read(second_file)
    diff_list = get_diff_data(first_files_data, second_files_data)
    return stringify_diff(diff_list)

