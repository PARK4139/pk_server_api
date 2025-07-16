if __name__ == "__main__":
    try:
        import traceback

        from colorama import init as pk_colorama_init

        from pkg_py.pk_core import pk_deprecated_get_d_current_n_like_person, get_f_current_n, pk_copy, assist_to_upload_pnx_to_git, get_time_as_, get_pk_token
        from pkg_py.pk_colorful_cli_util import pk_print
        from pkg_py.pk_core_constants import D_PROJECT, UNDERLINE, STAMP_TRY_GUIDE, STAMP_PYTHON_DEBUGGING_NOTE, STAMP_EXCEPTION_DISCOVERED, D_PKG_TOML

        pk_colorama_init(autoreset=True)

        git_repo_url = get_pk_token(f_token=rf"{D_PKG_TOML}/pk_token_pk_system_github_repo_url.toml", initial_str="")
        d_working = D_PROJECT
        branch_n = 'dev'
        assist_to_upload_pnx_to_git(d_working=d_working, git_repo_url=git_repo_url,branch_n=branch_n)

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
