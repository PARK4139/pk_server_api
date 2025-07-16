import traceback

from colorama import init as pk_colorama_init

from pk_core import load_magnet_set_to_bittorrent, collect_magnet_set, get_f_current_n, pk_deprecated_get_d_current_n_like_person
from pkg_py.pk_core_constants import D_PROJECT, UNDERLINE, STAMP_TRY_GUIDE, STAMP_EXCEPTION_DISCOVERED
from pkg_py.pk_colorful_cli_util import pk_print

if __name__ == '__main__':
    try:

        pk_colorama_init(autoreset=True)

        collect_magnet_set()
        # load_magnet_set_to_bittorrent()

    except Exception as e:
        f_current_n = get_f_current_n()
        d_current_n = pk_deprecated_get_d_current_n_like_person()
        script_to_run_python_program_in_venv = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
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
