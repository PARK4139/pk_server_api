__author__ = 'pk == junghoon.park'

if __name__ == "__main__":
    try:
        import traceback
        from pkg_py.pk_core import pk_assist_to_ensure_f_list_organized_by_x, pk_copy
        from pkg_py.pk_core_constants import UNDERLINE, STAMP_TRY_GUIDE, D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
        from pkg_py.pk_colorful_cli_util import pk_print
        from colorama import init as pk_colorama_init

        pk_colorama_init(autoreset=True)

        pk_assist_to_ensure_f_list_organized_by_x()

        # kill_pk_program_self(self_f=__file__)
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
