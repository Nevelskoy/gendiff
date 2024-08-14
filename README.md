# Gendiff

<a href="https://codeclimate.com/github/Nevelskoy/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/3df40b3004da949f1cda/maintainability" /></a>
<a href="https://codeclimate.com/github/Nevelskoy/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/3df40b3004da949f1cda/test_coverage" /></a>

Gendiff is a CLI utility for finding differences between configuration files.

## Features

- Suppported formats: YAML, JSON
- Report generation as plain text, structured text or JSON
- Can be used as CLI tool or external library

## Usage

### As external library

```python
from gendiff import generate_diff

diff = generate_diff(first_filepath1, second_filepath)
```

### As CLI tool

```
> gendiff --help
usage: gendiff [-h] [-f FORMAT] first_file second_file

Generate diff

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
```
