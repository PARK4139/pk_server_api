import traceback

from colorama import init as pk_colorama_init

from pkg_py.pk_core import get_pk_input, pk_deprecated_get_d_current_n_like_person, get_f_current_n, pk_copy, get_time_as_, get_pk_token, ensure_input_preprocessed, push_pnx_to_github
from pkg_py.pk_core_constants import D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED, UNDERLINE, STAMP_TRY_GUIDE, STAMP_PYTHON_DEBUGGING_NOTE, STAMP_EXCEPTION_DISCOVERED, D_PKG_TOML
from pkg_py.pk_colorful_cli_util import pk_print, print_red

if __name__ == "__main__":
    try:
        pk_colorama_init(autoreset=True)
        git_repo_url = get_pk_token(f_token=rf"{D_PKG_TOML}/pk_token_pk_server_fastapi_github_repo_url.toml", initial_str="")
        commit_msg = get_pk_input(message='commit_msg=', answer_options=[f"feat: auto pushed by pk_server_fastapi at {get_time_as_("%Y-%m-%d %H:%M")}"])
        # TBD branch_name
        # TBD git_repo_url
        push_pnx_to_github(d_working=D_PROJECT, git_repo_url=git_repo_url, commit_msg=commit_msg, branch_n='dev')

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