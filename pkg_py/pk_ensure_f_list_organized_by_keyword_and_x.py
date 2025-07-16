# -*- coding: utf-8 -*-
if __name__ == '__main__':
    try:
        from pk_core import (
            pk_deprecated_get_d_current_n_like_person,
            get_f_current_n, chcp_65001, get_os_n,
            pk_ensure_f_list_organized_by_keyword_and_x
        )
        from pkg_py.pk_core_constants import UNDERLINE, D_PROJECT
        from pkg_py.pk_colorful_cli_util import pk_print, print_yellow

        if get_os_n() == 'windows':
            chcp_65001()

        pk_ensure_f_list_organized_by_keyword_and_x()
    except Exception as e:
        import traceback

        pk_print(working_str=f'{UNDERLINE}예외발생 s\n\n', print_color='red')
        pk_print(f'''{traceback.format_exc()} %%%FOO%%%''', print_color='red')
        pk_print(working_str=f'{UNDERLINE}예외발생 e\n\n', print_color='red')

        pk_print(working_str=f'{UNDERLINE}[Debugging Note] s\n', print_color="yellow")
        f_current = get_f_current_n()
        d_current = pk_deprecated_get_d_current_n_like_person()
        print_yellow(prompt=f'f_current={f_current}\nd_current={d_current}\n')
        pk_print(working_str=f'{UNDERLINE}[Debugging Note] e\n', print_color="yellow")
        script_to_run_python_program_in_venv = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
        pk_print(script_to_run_python_program_in_venv)
