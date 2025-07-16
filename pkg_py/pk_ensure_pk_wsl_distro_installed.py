#!/usr/bin/env python   # shebang
# -*- coding: utf-8 -*- # encoding declaration
__author__ = 'pk == junghoon.park'

import sys
import traceback

from colorama import init as pk_colorama_init

from pkg_py.pk_core import ensure_pk_wsl_distro_installed
from pkg_py.pk_core_constants import UNDERLINE, STAMP_TRY_GUIDE, D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.pk_colorful_cli_util import pk_print, print_red

pk_colorama_init(autoreset=True)

if __name__ == "__main__":
    try:
        if not ensure_pk_wsl_distro_installed():
            raise RuntimeError("WSL 배포판 설치/이름 변경에 실패했습니다.")
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
