
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    try:
        import traceback

        from pk_core import chcp_65001, assist_to_perform_to_ensure_vpc_condition
        from pk_core import is_os_windows
        from pkg_py.pk_core import pk_deprecated_get_d_current_n_like_person, get_f_current_n, pk_copy
        from pkg_py.pk_core_constants import D_PROJECT, UNDERLINE, STAMP_TRY_GUIDE, STAMP_EXCEPTION_DISCOVERED
        from pkg_py.pk_colorful_cli_util import pk_print

        if is_os_windows():
            chcp_65001()

        assist_to_perform_to_ensure_vpc_condition()

    except Exception as e:
        f_current_n = get_f_current_n()
        d_current_n = pk_deprecated_get_d_current_n_like_person()

        traceback_format_exc_list = traceback.format_exc().split("\n")
        pk_print(working_str=f'{UNDERLINE}', print_color='red')
        for traceback_format_exc_str in traceback_format_exc_list:
            pk_print(working_str=f'{STAMP_EXCEPTION_DISCOVERED} {traceback_format_exc_str}', print_color='red')
        pk_print(working_str=f'{UNDERLINE}', print_color='red')


    finally:
        script_to_run_python_program_in_venv = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
        pk_print(working_str=f'{UNDERLINE}')
        pk_print(working_str=f'{STAMP_TRY_GUIDE} {script_to_run_python_program_in_venv}')
        pk_print(working_str=f'{UNDERLINE}')
