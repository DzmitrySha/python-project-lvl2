import pytest
from gendiff import generate_diff
from tests.fixtures.test_results import RESULT_PLAIN, RESULT_TREE


@pytest.fixture
def paths():
    paths = {
        "json1": "tests/fixtures/file1.json",
        "json2": "tests/fixtures/file2.json",
        "yml1": "tests/fixtures/file1.yml",
        "yml2": "tests/fixtures/file2.yml",
        "tree_json1": "tests/fixtures/file_tree1.json",
        "tree_json2": "tests/fixtures/file_tree2.json",
        "tree_yml1": "tests/fixtures/file_tree1.yml",
        "tree_yml2": "tests/fixtures/file_tree2.yml",
    }
    return paths


def test_generate_diff(paths):
    result_diff_json = str(generate_diff(paths["json1"], paths["json2"]))
    result_diff_yml = str(generate_diff(paths["yml1"], paths["yml2"]))
    result_diff_json_tree = str(generate_diff(paths["tree_json1"],
                                              paths["tree_json2"]))
    result_diff_yml_tree = str(generate_diff(paths["tree_yml1"],
                                             paths["tree_yml2"]))
    assert result_diff_json == RESULT_PLAIN
    assert result_diff_yml == RESULT_PLAIN
    assert result_diff_json_tree == RESULT_TREE
    assert result_diff_yml_tree == RESULT_TREE
