import pytest
from gendiff.engine import generate_diff
from tests.expected_test import STRING_CORRECT


@pytest.mark.parametrize(
    "input1, input2, expected",
    [
        pytest.param(
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json',
        STRING_CORRECT,
        ),
    ],
)
def test_generate_diff(input1, input2, expected):
        assert generate_diff(input1, input2) == expected




  