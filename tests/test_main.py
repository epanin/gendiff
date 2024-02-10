from gendiff import generate_diff
import pytest
from pathlib import Path

@pytest.fixture
def expected_result():
    with open('tests/fixtures/expected_result.txt') as f:
        return f.read()

def test_generate_diff_json(expected_result):
    result = generate_diff(Path('tests/fixtures/file1.json'), 
                           Path('tests/fixtures/file2.json'))
    assert result == expected_result

def test_generate_diff_yaml(expected_result):
    result = generate_diff(Path('tests/fixtures/yaml1.yml'),
                           Path('tests/fixtures/yaml2.yml'))
    assert result == expected_result
