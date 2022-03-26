import pytest
from gendiff import generate_diff
from gendiff.parser import parser


@pytest.fixture
def file_path1():
	return "tests/fixtures/file1.json"


@pytest.fixture
def file_path2():
	return "tests/fixtures/file2.json"


@pytest.fixture
def result():
	with open("tests/fixtures/result") as file:
		result = file.read()
	return result


def test_generate_diff(file_path1, file_path2, result):
	result_diff = str(generate_diff(file_path1, file_path2))
	assert result_diff == result
