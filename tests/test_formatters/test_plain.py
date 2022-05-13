# # test plain formatter (for tree structure)
#
# import pytest
# from gendiff import generate_diff
#
# FORMATTER = 'plain'
#
#
# @pytest.mark.asyncio
# async def test_json_plain(file_tree1_json_path,
#                           file_tree2_json_path,
#                           result_render):
#     assert result_render == generate_diff(file_tree1_json_path,
#                                           file_tree2_json_path)
#
#
# @pytest.mark.asyncio
# async def test_yml_plain(file_tree1_yml_path,
#                          file_tree2_yml_path,
#                          result_render):
#     assert result_render == generate_diff(file_tree1_yml_path,
#                                           file_tree2_yml_path)
