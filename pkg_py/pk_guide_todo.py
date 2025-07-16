if __name__ == "__main__":
    import constants
    from pk_core import get_d_current_n_like_person, get_f_current_n, guide_todo
    from pkg_py.pk_colorful_cli_util import pk_print

    try:
        import constants
        from pk_core import get_d_current_n_like_person, get_f_current_n, add_todo, guide_todo
        from pkg_py.pk_colorful_cli_util import pk_print

        guide_todo()

    except:
        f_current_n= get_f_current_n()
        d_current_n=get_d_current_n_like_person()
        script_to_run_python_program_in_venv = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
        traceback_format_exc_list = traceback.format_exc().split("\n")
        
        pk_print(working_str=f'{UNDERLINE}', print_color='red')
        for traceback_format_exc_str in traceback_format_exc_list:
            pk_print(working_str=f'{STAMP_EXCEPTION_OCCURED} {traceback_format_exc_str}', print_color='red')
        pk_print(working_str=f'{UNDERLINE}', print_color='red')

        pk_print(working_str=f'{UNDERLINE}\n', print_color="yellow")
        pk_print(working_str=f'{STAMP_PYTHON_DEBUGGING_NOTE} f_current={f_current_n}\nd_current={d_current_n}\n', print_color="yellow")
        pk_print(working_str=f'{UNDERLINE}\n', print_color="yellow")

        pk_print(working_str=f'{UNDERLINE}')
        pk_print(working_str=f'{STAMP_TRY_GUIDE} {script_to_run_python_program_in_venv}')
        pk_print(working_str=f'{UNDERLINE}')