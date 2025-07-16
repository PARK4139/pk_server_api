#!/usr/bin/env python   # shebang
# -*- coding: utf-8 -*- # encoding declaration
__author__ = 'pk == junghoon.park'

import sys
import traceback

from colorama import init as pk_colorama_init

from pkg_py.pk_core import collect_magnet_set_from_nyaa_si_p1, get_historical_list, ensure_pnx_made, get_driver_selenium
from pkg_py.pk_core_constants import UNDERLINE, STAMP_TRY_GUIDE, D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.pk_colorful_cli_util import pk_print, print_red

pk_colorama_init(autoreset=True)

if __name__ == "__main__":
    try:
        driver = get_driver_selenium(browser_debug_mode=False)
        # collect_magnet_set_from_nyaa_si(via_f_txt=True, driver=driver)

        import inspect

        func_n = inspect.currentframe().f_code.co_name
        ensure_pnx_made(pnx=rf'historical_{func_n}.txt', mode='f')
        historical_search_keyword_list = get_historical_list(f=rf'historical_{func_n}.txt')
        # tab_completer_iterable = ['', '1080 [Batch]'] + historical_search_keyword_list
        # search_keyword = get_pk_input_via_tab(message='search_keyword=', tab_completer_iterable=tab_completer_iterable).strip()
        # nyaa_si_supplier = get_pk_input_via_tab(message='nyaa_si_supplier=', tab_completer_iterable=['SubsPlease', '', 'Erai-raws'])
        search_keyword = ''  # pk_test
        nyaa_si_supplier = 'SubsPlease'  # pk_test
        collect_magnet_set_from_nyaa_si_p1(nyaa_si_supplier=nyaa_si_supplier, search_keyword=search_keyword, driver=driver)


    except Exception as ex:
        print_red(UNDERLINE)
        for line in traceback.format_exception_only(type(ex), ex):
            print_red(f"{STAMP_UNIT_TEST_EXCEPTION_DISCOVERED} {line.strip()}")
        print_red(UNDERLINE)
        sys.exit(1)
    finally:
        script_to_run = rf"{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate"
        pk_print(working_str=UNDERLINE)
        pk_print(working_str=f"{STAMP_TRY_GUIDE} {script_to_run}")
        pk_print(working_str=UNDERLINE)
