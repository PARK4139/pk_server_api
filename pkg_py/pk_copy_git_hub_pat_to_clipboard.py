if __name__ == "__main__":
    try:
        import traceback
        from pkg_py.pk_core import pk_copy, run_project_docker_base, LTA, get_pk_token, assist_to_ensure_vpc_bit, get_vpc_data_raw_from_vpc_request, assist_to_perform_to_ensure_vpc_condition
        from pkg_py.pk_colorful_cli_util import pk_print, print_pk_divider
        from pkg_py.pk_core_constants import D_PROJECT, UNDERLINE, STAMP_TRY_GUIDE, STAMP_EXCEPTION_DISCOVERED, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED, D_PKG_TOML

        github_pat = get_pk_token(f_token=f'{D_PKG_TOML}/pk_token_github_pat.toml', initial_str='')
        pk_copy(working_str=github_pat)
    except:
        traceback_format_exc_list = traceback.format_exc().split("\n")
        pk_print(working_str=f'{UNDERLINE}', print_color='red')
        for traceback_format_exc_str in traceback_format_exc_list:
            pk_print(working_str=f'{STAMP_EXCEPTION_DISCOVERED} {traceback_format_exc_str}', print_color='red')
        pk_print(working_str=f'{UNDERLINE}', print_color='red')

    finally:
        # script_to_run_python_program_in_venv = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
        pk_print(working_str=f'{UNDERLINE}')
        # pk_print(working_str=f'{STAMP_TRY_GUIDE} {script_to_run_python_program_in_venv}')
        pk_print(working_str=f'{UNDERLINE}')