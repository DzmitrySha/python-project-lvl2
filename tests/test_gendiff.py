import pytest
from gendiff import generate_diff


@pytest.fixture
def file_path1():
	return "tests/fixtures/file1.json"


@pytest.fixture
def file_path2():
	return "tests/fixtures/file2.json"


@pytest.fixture
def result_json():
	with open("tests/fixtures/result_json") as file:
		result_json = file.read()
	return result_json


def test_generate_diff(file_path1, file_path2, result_json):
	result = str(generate_diff(file_path1, file_path2))
	assert result == result_json
