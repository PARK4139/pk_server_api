import traceback

from pkg_py.pk_core import pk_copy, kill_cmd_exe, cmd_to_os
from pkg_py.pk_colorful_cli_util import pk_print
from pkg_py.pk_core_constants import D_PROJECT
from pkg_py.pk_core_constants import UNDERLINE, STAMP_TRY_GUIDE, STAMP_EXCEPTION_DISCOVERED

if __name__ == "__main__":
    try:
        img_name = 'cmd.exe'
        cmd_to_os(f'taskkill /f /im "{img_name}"')
        cmd_to_os(f'wmic process where name="{img_name}" delete ')
        kill_cmd_exe()


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
