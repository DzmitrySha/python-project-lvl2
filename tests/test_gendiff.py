import pytest
from gendiff import generate_diff


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
        "RESULT_PLAIN": "tests/fixtures/RESULT_PLAIN.txt",
        "RESULT_TREE": "tests/fixtures/RESULT_TREE.txt",
        "RESULT_STAT": "tests/fixtures/RESULT_STAT.txt",
        "RESULT_JSON": "tests/fixtures/RESULT_JSON.txt",
    }
    return paths


@pytest.fixture
def format_name():
    format_name = {
        "stylish": "stylish",
        "plain": "plain",
        "json": "json",
    }
    return format_name


def get_result(path):
    with open(path) as file:
        result = file.read()
    return result


def test_generate_diff(paths, format_name):
    result_diff_json = generate_diff(
        paths["json1"],
        paths["json2"],
        format_name["stylish"],
    )
    result_diff_yml = generate_diff(
        paths["yml1"],
        paths["yml2"],
        format_name["stylish"],
    )
    result_diff_json_tree = generate_diff(
        paths["tree_json1"],
        paths["tree_json2"],
        format_name["stylish"],
    )
    result_diff_yml_tree = generate_diff(
        paths["tree_yml1"],
        paths["tree_yml2"],
        format_name["stylish"],
    )
    result_diff_json_tree_stat = generate_diff(
        paths["tree_json1"],
        paths["tree_json2"],
        format_name["plain"],
    )
    result_diff_yml_tree_stat = generate_diff(
        paths["tree_yml1"],
        paths["tree_yml2"],
        format_name["plain"],
    )
    result_diff_json_view = generate_diff(
        paths["tree_json1"],
        paths["tree_json2"],
        format_name["json"],
    )
    assert result_diff_json == get_result(paths["RESULT_PLAIN"])
    assert result_diff_yml == get_result(paths["RESULT_PLAIN"])
    assert result_diff_json_tree == get_result(paths["RESULT_TREE"])
    assert result_diff_yml_tree == get_result(paths["RESULT_TREE"])
    assert result_diff_json_tree_stat == get_result(paths["RESULT_STAT"])
    assert result_diff_yml_tree_stat == get_result(paths["RESULT_STAT"])
    assert result_diff_json_view == get_result(paths["RESULT_JSON"])
