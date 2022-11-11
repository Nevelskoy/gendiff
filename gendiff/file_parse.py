import yaml
import json


FORMATS = {
    'json': 'JSON',
    'yaml': 'YAML',
    'yml': 'YAML'
    }


def read_file(filename):
    format_file = FORMATS[filename.split('.')[-1]]
    if format_file == 'JSON':
        files_data = json.load(open(filename))
    elif format_file == 'YAML':
        files_data = yaml.load(open(filename), Loader=yaml.SafeLoader)
    return files_data
    