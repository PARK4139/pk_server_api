if __name__ == "__main__":
    try:
        import traceback

        from colorama import init as pk_colorama_init

        from pkg_py.pk_core import pk_deprecated_get_d_current_n_like_person, get_f_current_n, pk_copy, assist_to_upload_pnx_to_git, get_time_as_, get_pk_token, kill_os, does_pnx_exist, LTA, get_pk_input
        from pkg_py.pk_colorful_cli_util import pk_print
        from pkg_py.pk_core_constants import D_PROJECT, UNDERLINE, STAMP_TRY_GUIDE, STAMP_PYTHON_DEBUGGING_NOTE, STAMP_EXCEPTION_DISCOVERED, D_PKG_TOML, D_PK_MEMO
        from pkg_py.pk_core_constants import D_ARCHIVED
        from pkg_py.pk_core import pk_back_up_pnx_without_venv_and_idea
        from pkg_py.pk_core import pk_copy, pk_back_up_pnx, is_day
        from pkg_py.pk_core import pk_back_up_pnx
        from pkg_py.pk_core_constants import D_PROJECT, D_DOWNLOADS

        pk_colorama_init(autoreset=True)

        # 백업 정책
        # .venv 데이터 특성은 용량 큼, 자주 바뀌지 않음.-> uv + pyproject.toml + uv.lock 으로 대체
        # ; half_month : 매월 15일마다 저빈도로 백업을 수행한다.

        pnx_working = get_pk_input(message='pnx_working=', answer_options=[D_PROJECT, D_PK_MEMO])

        # 로컬백업
        f = pk_back_up_pnx_without_venv_and_idea(pnx_working=pnx_working, d_dst=D_ARCHIVED, with_timestamp=1)
        if not does_pnx_exist(f):
            pk_print(f'''데일리 로컬백업 {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        elif does_pnx_exist(f):
            pk_print(f'''데일리 로컬백업 {'%%%FOO%%%' if LTA else ''}''', print_color='green')

        # 로컬백업
        # if is_day(dd=15):
        #     f = pk_back_up_pnx(pnx_working=pnx_working, d_dst=D_ARCHIVED)
        #     if not does_pnx_exist(f):
        #         pk_print(f'''15일 전체 로컬백업 {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        #     elif does_pnx_exist(f):
        #         pk_print(f'''15일 전체 로컬백업 {'%%%FOO%%%' if LTA else ''}''', print_color='green')

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
