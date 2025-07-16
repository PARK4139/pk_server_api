#!/usr/bin/env python   # shebang
# -*- coding: utf-8 -*- # encoding declaration
__author__ = 'pk == junghoon.park'

import traceback

from colorama import init as pk_colorama_init

from pkg_py.pk_colorful_cli_util import pk_print, print_red
from pkg_py.pk_core import pk_assist_to_alert_time, pk_speak
from pkg_py.pk_core_constants import UNDERLINE, STAMP_TRY_GUIDE, D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED

pk_colorama_init(autoreset=True)

if __name__ == "__main__":
    try:
        # d : directory
        # f : file
        # n : name
        # p : path
        # x : extension
        # pnx : path name extension
        # nx  : name extension
        # pn : path name
        here


        # o1
        #         func_n = inspect.currentframe().f_code.co_name
        #         f_historical = rf'{D_PKG_TXT}/historical_{func_n}.txt'
        # o2
        #         f_historical = rf'{D_PKG_TXT}/historical_{get_n(__file__)}.txt'


        # o1
        #         db_id = 'historical_d_workings'
        #         historical_d_workings = get_values_from_pk_db(db_id=db_id, pk_db=pk_db, f_historical=f_historical)
        #
        #         d_working = get_pk_input(message='d_working=', answer_options=historical_d_workings)
        #
        #         historical_d_workings = get_pk_list(origin_list=historical_d_workings, plus_list=d_working)
        #         pk_db.set(db_id, historical_d_workings)



        # o1
        # decision = get_pk_input(message='if you want to change branch?', answer_options=[PkMents2025.YES, PkMents2025.NO])
        # if decision == PkMents2025.YES:

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
