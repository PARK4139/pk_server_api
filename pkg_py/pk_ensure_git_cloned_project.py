# !/usr/bin/env python   # shebang
# -*- coding: utf-8 -*- # encoding declaration
__author__ = 'junghoon.park'

import traceback

from colorama import init as pk_colorama_init

from pkg_py.pk_colorful_cli_util import pk_print, print_red
from pkg_py.pk_core import cmd_to_os, ensure_pnx_made, get_pk_input, get_values_from_pk_db, get_pk_list, get_n
from pkg_py.pk_core_class import PkStateFromDB
from pkg_py.pk_core_constants import UNDERLINE, STAMP_TRY_GUIDE, D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED, D_PKG_TXT
from project_database.project_database_utils import pk_sleep

pk_colorama_init(autoreset=True)
if __name__ == "__main__":
    try:

        f_historical = rf'{D_PKG_TXT}/historical_{get_n(__file__)}.txt'
        ensure_pnx_made(pnx=f_historical, mode='f')
        pk_db = PkStateFromDB()



        db_id = 'historical_git_repo_urls'
        historical_git_repo_urls = get_values_from_pk_db(db_id=db_id, pk_db=pk_db, f_historical=f_historical)

        git_repo_url = get_pk_input(message='git_repo_url=', answer_options=historical_git_repo_urls)

        historical_git_repo_urls = get_pk_list(origin_list=historical_git_repo_urls, plus_list=git_repo_url)
        pk_db.set(db_id, historical_git_repo_urls)




        db_id = 'historical_branch_names'
        historical_branch_names = get_values_from_pk_db(db_id=db_id, pk_db=pk_db, f_historical=f_historical)

        branch_name = get_pk_input(message='branch_name=', answer_options=historical_branch_names)

        historical_branch_names = get_pk_list(origin_list=historical_branch_names, plus_list=branch_name)
        pk_db.set(db_id, historical_branch_names)





        db_id = 'historical_d_workings'
        historical_d_workings = get_values_from_pk_db(db_id=db_id, pk_db=pk_db, f_historical=f_historical)

        d_working = get_pk_input(message='d_working=', answer_options=historical_d_workings)

        historical_d_workings = get_pk_list(origin_list=historical_d_workings, plus_list=d_working)
        pk_db.set(db_id, historical_d_workings)

        # TBD 한번에 받는 것도 방법이다.
        std_list = cmd_to_os(f'git clone -b {branch_name} {git_repo_url} {d_working}')




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
