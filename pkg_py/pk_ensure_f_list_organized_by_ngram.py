if __name__ == "__main__":
    try:
        import os
        from pkg_py.pk_core import pk_copy, pk_ensure_f_list_organized_by_ngram, get_pk_input
        from pkg_py.pk_core_constants import UNDERLINE, STAMP_TRY_GUIDE, D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
        from pkg_py.pk_colorful_cli_util import pk_print
        from pkg_py.pk_core_constants import D_DOWNLOADS, D_PROJECT, D_WORKING

        d_working = get_pk_input(message='d_working=', answer_options=[os.getcwd(), D_WORKING, D_PROJECT, D_DOWNLOADS])
        token_splitter_pattern = get_pk_input(message='token_splitter_pattern=', answer_options=[
            r"\s+",  # 공백 기준으로 나눔
            r"[_]",  # 언더바(_) 기준으로 나눔
            r"[-]",  # 하이픈(-) 기준으로 나눔
            r"[ _\-]+",  # 공백, 언더바(_), 하이픈(-) 중 하나 이상이 연속되면 분리
            r"[ _\-]+",  # 공백, 언더바, 하이픈
            r"[\[\]_\\-]+",  # 대괄호([, ]), 언더바(_), 하이픈(-) 중 하나 이상 기준 (기호까지 포함)
            r"[\W_]+",  # 영문자/숫자 외 모든 문자(기호 포함) 및 언더바(_) 기준으로 분리
            r"\.",  # 마침표(.) 기준으로 분리 (확장자나 버전 구분에 유용)
        ])
        while 1:
            pk_ensure_f_list_organized_by_ngram(token_splitter_pattern, d_working)

    except:
        import traceback

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
