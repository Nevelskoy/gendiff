import pytest
from gendiff.engine import generate_diff
from tests import expected_test


@pytest.mark.parametrize(
    "input1, input2, expected1,",
    [
        pytest.param(
        'tests/fixtures/1_flat.json',
        'tests/fixtures/2_flat.json',
        expected_test.JSON_CORRECT,
        ),
    ],
)
def test_json_generate_diff(input1, input2, expected1):
        assert generate_diff(input1, input2) == expected1


@pytest.mark.parametrize(
    "input3, input4, expected2",
    [
        pytest.param(
        'tests/fixtures/3_flat.yml',
        'tests/fixtures/4_flat.yml',
        expected_test.YML_CORRECT,
        ),
    ],
)
def test_yaml_generate_diff(input3, input4, expected2):
        assert generate_diff(input3, input4) == expected2
