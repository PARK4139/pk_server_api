try:
    from pkg_py.pk_core import pk_cd, assist_to_change_d
    import traceback
    from pkg_py.pk_core_constants import D_PROJECT, UNDERLINE, STAMP_TRY_GUIDE, STAMP_PYTHON_DEBUGGING_NOTE, STAMP_EXCEPTION_DISCOVERED
    from pkg_py.pk_core import pk_deprecated_get_d_current_n_like_person, get_f_current_n, pk_copy
    from pkg_py.pk_colorful_cli_util import pk_print
    from colorama import init as pk_colorama_init

    pk_colorama_init(autoreset=True)

    assist_to_change_d()

except Exception as e:
    f_current_n = get_f_current_n()
    d_current_n = pk_deprecated_get_d_current_n_like_person()

    traceback_format_exc_list = traceback.format_exc().split("\n")
    pk_print(working_str=f'{UNDERLINE}', print_color='red')
    for traceback_format_exc_str in traceback_format_exc_list:
        pk_print(working_str=f'{STAMP_EXCEPTION_DISCOVERED} {traceback_format_exc_str}', print_color='red')
    pk_print(working_str=f'{UNDERLINE}', print_color='red')

    pk_print(working_str=f'{UNDERLINE}', print_color="yellow")
    pk_print(working_str=f'{STAMP_PYTHON_DEBUGGING_NOTE} f_current={f_current_n} d_current={d_current_n}', print_color="yellow")
    pk_print(working_str=f'{UNDERLINE}', print_color="yellow")

finally:
    script_to_run_python_program_in_venv = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
    print(f'\n')
    pk_copy(working_str=script_to_run_python_program_in_venv)
    pk_print(working_str=f'{UNDERLINE}')
    pk_print(working_str=f'{STAMP_TRY_GUIDE} {script_to_run_python_program_in_venv}')
    pk_print(working_str=f'{UNDERLINE}')
