# import os
# import string
# from datetime import datetime
# from typing import List
#
# from PySide6.QtCore import Signal, QThread
#
# from pk_core_constants import PROJECT_D
#
# directory_abspath = PROJECT_D
#
# # delete_db_toml()
#
# # create_db_toml()
#
# current_directory_state: any = get_directory_state(directory_abspath=directory_abspath)
# current_directory_state = "\n".join([f"{key}: {value}" for key, value in current_directory_state.items()])  # dict to str (개행을 시킨)
# current_directory_state = get_replace_from_special_characters_to_replacement(target=current_directory_state, replacement="")  # 특수문자 제거 시킨
# current_directory_state = current_directory_state.split("\n")  # str to list (개행을 시킨)
# # print(rf'type(current_directory_state) : {type(current_directory_state)}')
# # print(rf'len(current_directory_state) : {len(current_directory_state)}')
#
#
# previous_directory_state = select_db_toml(key=get_db_toml_key(directory_abspath))
# if previous_directory_state is None:
#     insert_db_toml(key=get_db_toml_key(directory_abspath), value=current_directory_state)  # 50000 줄의 str 다루는 것보다 50000 개의 list 다루는 것이 속도성능에 대하여 효율적이다.
#     previous_directory_state = select_db_toml(key=get_db_toml_key(directory_abspath))
#
#
# # print(rf'type(previous_directory_state) : {type(previous_directory_state)}')
# # print(rf'len(previous_directory_state) : {len(previous_directory_state)}')
#
#

#
#
# if is_two_lists_equal(current_directory_state, previous_directory_state):
#     print("디렉토리가 변경되지 않았습니다")
# else:
#     print("디렉토리가 변경되었습니다")
#
# # update_db_toml(key=get_db_toml_key(directory_abspath), value=current_directory_state)
# # explorer(DB_TOML)
