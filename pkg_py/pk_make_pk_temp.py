__author__ = 'pk == junghoon.park'

if __name__ == "__main__":
    try:

        import traceback

        from colorama import init as pk_colorama_init

        from pkg_py.pk_core import pk_copy, cmd_to_os, is_os_windows, kill_self_pk_program, LTA
        from pkg_py.pk_core_constants import UNDERLINE, STAMP_TRY_GUIDE, D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
        from pkg_py.pk_colorful_cli_util import pk_print

        pk_colorama_init(autoreset=True)

        if is_os_windows():
            cmd_to_os(cmd='mkdir %USERPROFILE%\Downloads\pk_working\pk_temp')

        if not LTA:
            kill_self_pk_program(self_f=__file__)

    except:
        traceback_format_exc_list = traceback.format_exc().split("\n")
        pk_print(working_str=f'{UNDERLINE}', print_color='red')
        for traceback_format_exc_str in traceback_format_exc_list:
            # pk_print(working_str=f'{STAMP_EXCEPTION_DISCOVERED} {traceback_format_exc_str}', print_color='red')
            pk_print(working_str=f'{STAMP_UNIT_TEST_EXCEPTION_DISCOVERED} {traceback_format_exc_str}', print_color='red')
        pk_print(working_str=f'{UNDERLINE}', print_color='red')

    finally:
        script_to_run_python_program_in_venv = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
        pk_print(working_str=f'{UNDERLINE}')
        pk_print(working_str=f'{STAMP_TRY_GUIDE} {script_to_run_python_program_in_venv}')
        pk_print(working_str=f'{UNDERLINE}')
