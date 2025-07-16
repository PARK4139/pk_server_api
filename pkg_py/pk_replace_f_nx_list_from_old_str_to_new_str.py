
__author__ = 'pk == junghoon.park'

if __name__ == "__main__":
    try:
        import traceback

        from colorama import init as pk_colorama_init

        from pk_core import pk_replace_f_nx_list_from_old_str_to_new_str, pk_input, get_pnx_validated
        from pkg_py.pk_core import pk_copy, get_no_blank_working_str_validated, get_nx_validated
        from pkg_py.pk_core_constants import UNDERLINE, STAMP_TRY_GUIDE, D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED, D_WORKING
        from pkg_py.pk_colorful_cli_util import pk_print

        pk_colorama_init(autoreset=True)

        d_working = pk_input(working_str=rf'd_working=', limit_seconds=60, return_default=D_WORKING, get_input_validated=get_pnx_validated)
        while 1:
            old_str = pk_input(working_str="old_str=", limit_seconds=60, return_default='%%%OLD_STR%%%', get_input_validated=get_nx_validated)
            old_str = get_no_blank_working_str_validated(old_str)
            new_str = pk_input(working_str="new_str=", limit_seconds=60, return_default='%%%NEW_STR%%%', get_input_validated=get_nx_validated)
            new_str = get_no_blank_working_str_validated(new_str)
            pk_replace_f_nx_list_from_old_str_to_new_str(d_working=d_working, old_str=old_str, new_str=new_str)

    except:
        from pkg_py.pk_colorful_cli_util import print_red

        traceback_format_exc_list = traceback.format_exc().split("\n")
        print_red(UNDERLINE)
        for line in traceback_format_exc_list:
            print_red(f'{STAMP_UNIT_TEST_EXCEPTION_DISCOVERED} {line}')
        print_red(UNDERLINE)

    finally:
        script_to_run_python_program_in_venv = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
        pk_print(working_str=f'{UNDERLINE}')
        pk_print(working_str=f'{STAMP_TRY_GUIDE} {script_to_run_python_program_in_venv}')
        pk_print(working_str=f'{UNDERLINE}')
