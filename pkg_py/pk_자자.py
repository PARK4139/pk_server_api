if __name__ == "__main__":
    try:
        import traceback
        from pkg_py.pk_core import pk_back_up_pnx, kill_os, is_office_pc, is_internet_connected, save_power_as_s3, pk_kill_process_as_async, pk_run_process_as_async, restart_f_list_with_new_window_as_async
        from pkg_py.pk_core import pk_back_up_pnx_without_venv_and_idea
        from pkg_py.pk_core import pk_copy, is_day
        from pkg_py.pk_core import assist_to_upload_pnx_to_git, get_time_as_, get_pk_token
        from pkg_py.pk_colorful_cli_util import pk_print
        from pkg_py.pk_core_constants import D_ARCHIVED, D_PKG_PY
        from colorama import init as pk_colorama_init

        from pkg_py.pk_core import pk_deprecated_get_d_current_n_like_person, get_f_current_n, pk_copy, assist_to_upload_pnx_to_git, get_time_as_, get_pk_token, ensure_input_preprocessed, ensure_d_size_stable, push_pnx_to_github, LTA
        from pkg_py.pk_colorful_cli_util import pk_print
        from pkg_py.pk_core_constants import D_PROJECT, UNDERLINE, STAMP_TRY_GUIDE, STAMP_PYTHON_DEBUGGING_NOTE, STAMP_EXCEPTION_DISCOVERED, D_PKG_TOML
        from pkg_py.pk_core_constants import D_PROJECT
        from pkg_py.pk_core_constants import UNDERLINE, STAMP_TRY_GUIDE, STAMP_EXCEPTION_DISCOVERED, D_PKG_TOML

        # backup to local
        pnx_working = D_PROJECT
        pk_back_up_pnx_without_venv_and_idea(pnx_working=pnx_working, d_dst=D_ARCHIVED, with_timestamp=1)
        if is_day(dd=15):
            pk_back_up_pnx(pnx_working=pnx_working, d_dst=D_ARCHIVED)

        # 2. puload to github
        if is_internet_connected():
            pk_colorama_init(autoreset=True)
            git_repo_url = get_pk_token(f_token=rf"{D_PKG_TOML}/pk_token_pk_server_fastapi_github_repo_url.toml", initial_str="")
            commit_msg = ensure_input_preprocessed(working_str=f"commit_msg=", upper_seconds_limit=30, return_default=f"feat: auto pushed by pk_server_fastapi at {get_time_as_("%Y-%m-%d %H:%M")}")
            push_pnx_to_github(d_working=D_PROJECT, git_repo_url=git_repo_url, commit_msg=commit_msg, branch_n='dev')

        # 3 kill or lock os
        if is_office_pc():
            kill_os()
        else:
            # make_os_power_saving_mode_as_s3()
            f_py_list = [
                rf"{D_PKG_PY}/pk_assist_to_lock_os.py",
            ]
            restart_f_list_with_new_window_as_async(f_py_list)


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
