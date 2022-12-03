import pytest
from gendiff.engine import generate_diff
from tests.fixtures import expected_test


@pytest.mark.parametrize(
    "json_1, json_2, expected1,",
    [
        pytest.param(
            'tests/fixtures/flat_json_1.json',
            'tests/fixtures/flat_json_2.json',
            expected_test.JSON_FLAT_CORRECT,
        ),
    ],
)
def test_json_flat(json_1, json_2, expected1):
    assert generate_diff(json_1, json_2) == expected1


@pytest.mark.parametrize(
    "yaml_1, yaml_2, expected2",
    [
        pytest.param(
            'tests/fixtures/flat_yaml_1.yml',
            'tests/fixtures/flat_yaml_2.yml',
            expected_test.YML_FLAT_CORRECT,
        ),
    ],
)
def test_yaml_flat(yaml_1, yaml_2, expected2):
    assert generate_diff(yaml_1, yaml_2) == expected2


@pytest.mark.parametrize(
    "json_1, json_2, expected3",
    [
        pytest.param(
            'tests/fixtures/nested_json_1.json',
            'tests/fixtures/nested_json_2.json',
            expected_test.NESTED_CORRECT,
        ),
    ],
)
def test_json_nested(json_1, json_2, expected3):
    assert generate_diff(json_1, json_2) == expected3


@pytest.mark.parametrize(
    "yaml_1, yaml_2, expected4",
    [
        pytest.param(
            'tests/fixtures/nested_yaml_1.yml',
            'tests/fixtures/nested_yaml_2.yml',
            expected_test.NESTED_CORRECT,
        ),
    ],
)
def test_yaml_nested(yaml_1, yaml_2, expected4):
    assert generate_diff(yaml_1, yaml_2) == expected4


@pytest.mark.parametrize(
    "json_1, json_2, expected5",
    [
        pytest.param(
            'tests/fixtures/nested_json_1.json',
            'tests/fixtures/nested_json_2.json',
            expected_test.PLAIN_FORMAT,
        ),
    ],
)
def test_json_plain_format(json_1, json_2, expected5):
    assert generate_diff(json_1, json_2, 'plain') == expected5


@pytest.mark.parametrize(
    "json_1, json_2, expected6",
    [
        pytest.param(
            'tests/fixtures/nested_json_1.json',
            'tests/fixtures/nested_json_2.json',
            expected_test.JSON_FORMAT,
        ),
    ],
)
def test_json_format(json_1, json_2, expected6):
    assert generate_diff(json_1, json_2, 'json') == expected6
