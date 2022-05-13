# test stylish formatter

import pytest
from gendiff import generate_diff

FORMATTER = 'plain'


@pytest.mark.asyncio
async def test_json_plain(file1_json_path, file2_json_path, result_render):
    assert result_render == generate_diff(file1_json_path, file2_json_path)


@pytest.mark.asyncio
async def test_yml_plain(file1_yml_path, file2_yml_path, result_render):
    assert result_render == generate_diff(file1_yml_path, file2_yml_path)
