from gendiff.formaters.stylish import stringify_stylish


def output_data(data, format_name):
   # if format_name == "plain":
   #     return stringify_plain(data)
   # elif format_name == "json":
   #     return stringify_json(data)
   # else:
    return stringify_stylish(data)