import yaml
import json


FORMATS = {
    'json': 'JSON',
    'yaml': 'YAML',
    'yml': 'YAML'
}


def to_read(filename):
    format_file = FORMATS[filename.split('.')[-1]]
    with open(filename, 'r') as rf:
        if format_file == 'JSON':
            files_data = json.load(rf)
        elif format_file == 'YAML':
            files_data = yaml.load((rf), Loader=yaml.SafeLoader)
        return files_data
