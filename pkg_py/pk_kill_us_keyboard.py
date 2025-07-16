# -*- coding: utf-8 -*-



import traceback

if __name__ == '__main__':
    from pk_core import pk_deprecated_get_d_current_n_like_person, get_f_current_n, kill_us_keyboard
    from pkg_py.pk_colorful_cli_util import pk_print
    from pkg_py.pk_core_constants import UNDERLINE, STAMP_TRY_GUIDE, STAMP_PYTHON_DEBUGGING_NOTE, STAMP_EXCEPTION_DISCOVERED, D_PROJECT

    try:
        kill_us_keyboard()
    except Exception as e:
        f_current_n = get_f_current_n()
        d_current_n = pk_deprecated_get_d_current_n_like_person()
        script_to_run_python_program_in_venv = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
        traceback_format_exc_list = traceback.format_exc().split("\n")

        pk_print(working_str=f'{UNDERLINE}', print_color='red')
        for traceback_format_exc_str in traceback_format_exc_list:
            pk_print(working_str=f'{STAMP_EXCEPTION_DISCOVERED} {traceback_format_exc_str}', print_color='red')
        pk_print(working_str=f'{UNDERLINE}', print_color='red')

        

        pk_print(working_str=f'{UNDERLINE}')
        pk_print(working_str=f'{STAMP_TRY_GUIDE} {script_to_run_python_program_in_venv}')
        pk_print(working_str=f'{UNDERLINE}')
