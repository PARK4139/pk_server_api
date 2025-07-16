import traceback

from colorama import init as pk_colorama_init

from pkg_py.pk_colorful_cli_util import pk_print, print_red
from pkg_py.pk_core import cmd_to_os, pk_sleep
from pkg_py.pk_core_constants import D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED, UNDERLINE, STAMP_TRY_GUIDE, D_PROJECT_PARENTS


if __name__ == "__main__":
    try:
        pk_colorama_init(autoreset=True)
        f_bat = f'call "{D_PROJECT_PARENTS}\pk_server_fastapi\pk_push_project_to_github.bat"'
        std_list = cmd_to_os(f_bat)

        f_bat = f'call "{D_PROJECT_PARENTS}\pk_memo\pk_push_project_to_github.bat"'
        std_list = cmd_to_os(f_bat)

    except Exception as ex:
        print_red(UNDERLINE)
        for line in traceback.format_exception_only(type(ex), ex):
            print_red(f"{STAMP_UNIT_TEST_EXCEPTION_DISCOVERED} {line.strip()}")
        print_red(UNDERLINE)
        # sys.exit(1)
    finally:
        script_to_run = rf"{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate"
        pk_print(working_str=UNDERLINE)
        pk_print(working_str=f"{STAMP_TRY_GUIDE} {script_to_run}")
        pk_print(working_str=UNDERLINE)
