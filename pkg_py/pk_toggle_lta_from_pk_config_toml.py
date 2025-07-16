from pkg_py.pk_core import is_os_windows


if __name__ == "__main__":
    try:
        import traceback
        from pkg_py.pk_core import pk_copy, LTA, pk_toggle_pk_config_key, get_nx, pk_kill_process_by_window_title_seg, get_pnx_os_style, get_list_that_element_applyed_via_func, kill_self_pk_program
        from pkg_py.pk_core_constants import D_PROJECT, UNDERLINE, STAMP_TRY_GUIDE, STAMP_EXCEPTION_DISCOVERED, D_PKG_PY
        from pkg_py.pk_colorful_cli_util import pk_print
        from colorama import init as pk_colorama_init

        pk_colorama_init(autoreset=True)

        pk_toggle_pk_config_key('LOCAL_TEST_ACTIVATE')

        if is_os_windows():
            kill_self_pk_program(self_f=__file__)

    except:
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
