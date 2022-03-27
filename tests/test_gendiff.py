import pytest
from gendiff import generate_diff
from tests.fixtures.test_results import RESULT_JSON, RESULT_YML


@pytest.fixture
def paths():
	paths = {
		"json1": "tests/fixtures/file1.json",
		"json2": "tests/fixtures/file2.json",
		"yml1": "tests/fixtures/file1.yml",
		"yml2": "tests/fixtures/file2.yml",
	}
	return paths


def test_generate_diff(paths):
	result_diff_json = str(generate_diff(paths["json1"], paths["json2"]))
	result_diff_yml = str(generate_diff(paths["yml1"], paths["yml2"]))
	assert result_diff_json == RESULT_JSON
	assert result_diff_yml == RESULT_YML
