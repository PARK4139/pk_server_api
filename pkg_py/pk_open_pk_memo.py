import sys

if __name__ == "__main__":
    try:
        import traceback

        from colorama import init as pk_colorama_init

        from pkg_py.pk_core import get_pnx_os_style, cmd_to_os
        from pkg_py.pk_core import pk_copy
        from pkg_py.pk_core_constants import STAMP_EXCEPTION_DISCOVERED, F_MEMO_HOW_PK, F_MEMO_WORK_PK
        from pkg_py.pk_core_constants import UNDERLINE, STAMP_TRY_GUIDE, D_PROJECT
        from pkg_py.pk_colorful_cli_util import pk_print

        pk_colorama_init(autoreset=True)

        f_list = [
            F_MEMO_HOW_PK,
            F_MEMO_WORK_PK,
        ]
        for f in f_list:
            f = get_pnx_os_style(f)
            cmd_to_os(cmd=f'code {f}')

        state = True
    except:
        traceback_format_exc_list = traceback.format_exc().split("\n")
        pk_print(working_str=f'{UNDERLINE}', print_color='red')
        for traceback_format_exc_str in traceback_format_exc_list:
            pk_print(working_str=f'{STAMP_EXCEPTION_DISCOVERED} {traceback_format_exc_str}', print_color='red')
        pk_print(working_str=f'{UNDERLINE}', print_color='red')

        # finally:
        #     script_to_run_python_program_in_venv = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
        #     pk_print(working_str=f'{UNDERLINE}')
        #     pk_print(working_str=f'{STAMP_TRY_GUIDE} {script_to_run_python_program_in_venv}')
        #     pk_print(working_str=f'{UNDERLINE}')

        #     if is_os_linux() and state:
        #         cmd_to_os('exit')
        sys.exit()
