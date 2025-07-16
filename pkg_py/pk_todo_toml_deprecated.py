#
#
#
#
#
#
# def add_data_to_f_toml(f_toml, data_new):
#     import toml
#     """
#     TOML 파일에 데이터를 추가하거나 수정하는 함수.
#
#     Args:
#         file_path (str): TOML 파일 경로.
#         new_data (dict): 추가할 데이터.
#     """
#     # TOML 파일 읽기
#     with open(f_toml, "r", encoding="utf-8") as f:
#         toml_data = toml.load(f)
#
#     # 새로운 데이터 추가
#     for key, value in data_new.items():
#         if key in toml_data:
#             # 기존 데이터와 병합
#             toml_data[key].update(value)
#         else:
#             # 새로운 키 추가
#             toml_data[key] = value
#
#     # TOML 파일 다시 저장
#     with open(f_toml, "w", encoding="utf-8") as f:
#         toml.dump(toml_data, f)
#
#
# def get_data_from_f_toml(f_toml):
#     import toml
#     with open(f_toml, "r", encoding="utf-8") as f:
#         data = toml.load(f)
#     return data
#
#
# def get_format_structured(data, indent=0):
#     """
#     데이터를 계층적으로 문자열로 포맷팅하는 함수.
#
#     Args:
#         data (dict or list): 출력할 데이터.
#         indent (int): 현재 들여쓰기 수준.
#
#     Returns:
#         str: 계층적으로 포맷된 문자열.
#     """
#     result = []
#     indent_str = " " * (indent * 4)  # 들여쓰기 설정 (4칸 공백)
#
#     if isinstance(data, dict):
#         for key, value in data.items():
#             result.append(f"{indent_str}{key}:")
#             if isinstance(value, (dict, list)):
#                 result.append(get_format_structured(value, indent + 1))
#             else:
#                 result.append(f"{indent_str}   {value}")
#     elif isinstance(data, list):
#         for item in data:
#             if isinstance(item, (dict, list)):
#                 result.append(get_format_structured(item, indent + 1))
#             else:
#                 result.append(f"{indent_str}   {item}")
#     else:
#         result.append(f"{indent_str}{data}")
#
#     return "\n".join(result)
#
#
# def main():
#     # todo : 기억전혀 안난다.
#     # f_pnx = rf'{PROJECT_D}\memo_how.toml'
#     f_pnx = rf'{D_PROJECT}\todo.toml'
#     if not does_pnx_exist(f_pnx):
#         pk_print(f'''{f_pnx} does not exist %%%FOO%%%''', print_color='red')
#         user_input = input(":(enter)")
#         if user_input == "":
#             with open(f_pnx, 'w') as f:
#                 f.write(user_input)
#     line_list = get_list_from_f(f=f_pnx)
#     line_list = get_str_from_list(working_list=line_list)
#     line_str = line_list
#     pk_print(f'''len(line_list)={len(line_list)} %%%FOO%%%''')
#     pk_print(f'''len(line_str)={len(line_str)} %%%FOO%%%''')
#     data = line_str
#     highlight_config_dict = {
#         "bright_red": [
#             "%%%FOO%%%",
#             'mkr_',
#             "mkr_________________________________________________________________________",
#         ],
#     }
#     print_highlighted(txt_whole=data, highlight_config_dict=highlight_config_dict)
#     data_new = {
#         "todo": {
#             "test": {
#                 "test1": {
#                     "test1-2": "foo2"
#                 }
#             }
#         }
#     }
#     add_data_to_f_toml(f_toml=f_pnx, data_new=data_new)
#
#     data = get_data_from_f_toml(f_toml=f_pnx)
#     data = get_format_structured(data=data)
#     highlight_config_dict = {
#         "bright_red": [
#             "%%%FOO%%%",
#         ],
#     }
#     print_highlighted(txt_whole=data, highlight_config_dict=highlight_config_dict)
#
#
# if __name__ == "__main__":
#     try:
#         import pk_core_constants
#         from pkg_py.pk_core_constants import D_PROJECT, UNDERLINE, STAMP_TRY_GUIDE, STAMP_PYTHON_DEBUGGING_NOTE, STAMP_EXCEPTION_DISCOVERED, UNDERLINE, STAMP_TRY_GUIDE, STAMP_PYTHON_DEBUGGING_NOTE, STAMP_EXCEPTION_DISCOVERED
#         from pk_core import get_f_current_n, pk_deprecated_get_d_current_n_like_person, get_list_from_f, does_pnx_exist, get_str_from_list, print_highlighted
#         from pkg_py.pk_colorful_cli_util import pk_print
#         import traceback
#
#         main()
#
#     except:
#         f_current_n= get_f_current_n()
#         d_current_n=pk_deprecated_get_d_current_n_like_person()
#         script_to_run_python_program_in_venv = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
#         traceback_format_exc_list = traceback.format_exc().split("\n")
#
#         pk_print(f'{UNDERLINE}', print_color='red')
#         for traceback_format_exc_str in traceback_format_exc_list:
#             pk_print(f'{STAMP_EXCEPTION_DISCOVERED} {traceback_format_exc_str}', print_color='red')
#         pk_print(f'{UNDERLINE}', print_color='red')
#
#         pk_print(f'{UNDERLINE}', print_color="yellow")
#         pk_print(f'{STAMP_PYTHON_DEBUGGING_NOTE} f_current={f_current_n} d_current={d_current_n}', print_color="yellow")
#         pk_print(f'{UNDERLINE}', print_color="yellow")
#
#         pk_print(f'{UNDERLINE}')
#         pk_print(f'{STAMP_TRY_GUIDE} {script_to_run_python_program_in_venv}')
#         pk_print(f'{UNDERLINE}')
