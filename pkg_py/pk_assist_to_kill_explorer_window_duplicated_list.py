# -*- coding: utf-8 -*-

if __name__ == '__main__':
    try:
        import traceback

        from pkg_py.pk_core_constants import D_PROJECT, UNDERLINE, STAMP_TRY_GUIDE, STAMP_PYTHON_DEBUGGING_NOTE, STAMP_EXCEPTION_DISCOVERED
        from pkg_py.pk_core import chcp_65001, get_os_n, pk_deprecated_get_d_current_n_like_person, get_f_current_n, assist_to_kill_window_duplicated_list, is_os_windows
        from pkg_py.pk_colorful_cli_util import pk_print

        if is_os_windows():
            chcp_65001()

        assist_to_kill_window_duplicated_list()

    except Exception as e:
        f_current_n = get_f_current_n()
        d_current_n = pk_deprecated_get_d_current_n_like_person()

        traceback_format_exc_list = traceback.format_exc().split("\n")
        pk_print(f'{UNDERLINE}', print_color='red')
        for traceback_format_exc_str in traceback_format_exc_list:
            pk_print(f'{STAMP_EXCEPTION_DISCOVERED} {traceback_format_exc_str}', print_color='red')
        pk_print(f'{UNDERLINE}', print_color='red')

        pk_print(f'{UNDERLINE}', print_color="yellow")
        pk_print(f'{STAMP_PYTHON_DEBUGGING_NOTE} f_current={f_current_n} d_current={d_current_n}', print_color="yellow")
        pk_print(f'{UNDERLINE}', print_color="yellow")

    finally:
        script_to_run_python_program_in_venv = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
        print(f'\n')
        pk_print(f'{UNDERLINE}')
        pk_print(f'{STAMP_TRY_GUIDE} {script_to_run_python_program_in_venv}')
        pk_print(f'{UNDERLINE}')
