import os
import traceback

from colorama import init as pk_colorama_init

from pkg_py.pk_colorful_cli_util import pk_print
from pkg_py.pk_core import ensure_pnx_made, get_pk_input, get_values_from_pk_db, get_n
from pkg_py.pk_core import pk_ensure_f_list_organized_by_ngram
from pkg_py.pk_core_class import PkStateFromDB
from pkg_py.pk_core_constants import D_DOWNLOADS, D_WORKING
from pkg_py.pk_core_constants import UNDERLINE, STAMP_TRY_GUIDE, D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED, D_PKG_TXT

if __name__ == "__main__":
    try:
        pk_colorama_init(autoreset=True)

        f_historical = rf'{D_PKG_TXT}/historical_{get_n(__file__)}.txt'
        ensure_pnx_made(pnx=f_historical, mode='f')
        pk_db = PkStateFromDB()

        historical_d_workings = get_values_from_pk_db(db_id='historical_d_workings', pk_db=pk_db, f_historical=f_historical)

        d_working = get_pk_input(message='d_working=', answer_options=[os.getcwd(), D_WORKING, D_PROJECT, D_DOWNLOADS])
        token_splitter_pattern = get_pk_input(message='token_splitter_pattern=', answer_options=[
            r"\s+",  # 공백
            r"[_]",  # 언더바(_)만 기준으로 나눔
            r"[-]",  # 하이픈(-)만 기준으로 나눔
            r"[ _\-]+",  # 공백, 언더바(_), 하이픈(-) 중 하나 이상이 연속되면 분리
            r"[ _\-]+",  # 공백, 언더바, 하이픈
            r"[\[\]_\\-]+",  # 대괄호([, ]), 언더바(_), 하이픈(-) 중 하나 이상 기준 (기호까지 포함)
            r"[\W_]+",  # 영문자/숫자 외 모든 문자(기호 포함) 및 언더바(_) 기준으로 분리
            r"\.",  # 마침표(.) 기준으로 분리 (확장자나 버전 구분에 유용)
        ])
        pk_ensure_f_list_organized_by_ngram(token_splitter_pattern, d_working)

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
