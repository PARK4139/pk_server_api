

if __name__ == "__main__":
    try:
        import traceback

        from pk_core import pk_deprecated_get_d_current_n_like_person, get_f_current_n, add_todo, guide_todo
        from pkg_py.pk_core_constants import UNDERLINE, D_PROJECT, STAMP_TRY_GUIDE, STAMP_PYTHON_DEBUGGING_NOTE, STAMP_EXCEPTION_DISCOVERED
        from pkg_py.pk_colorful_cli_util import pk_print

        add_todo()

    except:
        f_current_n= get_f_current_n()
        d_current_n=pk_deprecated_get_d_current_n_like_person()
        script_to_run_python_program_in_venv = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
        traceback_format_exc_list = traceback.format_exc().split("\n")
        
        pk_print(f'{UNDERLINE}', print_color='red')
        for traceback_format_exc_str in traceback_format_exc_list:
            pk_print(f'{STAMP_EXCEPTION_DISCOVERED} {traceback_format_exc_str}', print_color='red')
        pk_print(f'{UNDERLINE}', print_color='red')

        pk_print(f'{UNDERLINE}\n', print_color="yellow")
        pk_print(f'{STAMP_PYTHON_DEBUGGING_NOTE} f_current={f_current_n}\nd_current={d_current_n}\n', print_color="yellow")
        pk_print(f'{UNDERLINE}\n', print_color="yellow")

        pk_print(f'{UNDERLINE}')
        pk_print(f'{STAMP_TRY_GUIDE} {script_to_run_python_program_in_venv}')
        pk_print(f'{UNDERLINE}')