#!/usr/bin/env python   # shebang
# -*- coding: utf-8 -*- # encoding declaration
__author__ = 'pk == junghoon.park'

import os
import traceback

from colorama import init as pk_colorama_init

from pkg_py.pk_core import ensure_tmux_pk_session_removed, get_nx, get_pk_input, get_pk_wsl_mount_d, get_pnx_list, is_os_linux, pk_sleep, pk_speak
from pkg_py.pk_core_constants import D_PKG_PY, UNDERLINE, STAMP_TRY_GUIDE, D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.pk_colorful_cli_util import pk_print, print_red

pk_colorama_init(autoreset=True)

if __name__ == "__main__":
    try:

        # d_working = get_pnx_from_fzf()
        windows_path = get_pk_input(message="windows_path=", answer_options=[])
        # path_to_mount = get_pk_input_via_tab(message="path_to_mount=", tab_completer_iterable=available_ip_without_localhost_list)
        d_pk_wsl_mount = get_pk_wsl_mount_d(windows_path=windows_path, path_to_mount='Downloads/pk_working')
        # d_pk_wsl_mount = get_pk_wsl_mount_d(windows_path=d_working, path_to_mount=path_to_mount)
        
        pk_sleep(100000)
        if is_os_linux():
            # cmd_to_os('exit')
            # available_pk_python_program_pnx = get_pnx_from_fzf(D_PKG_PY)
            available_pk_python_program_pnx = None
            pnx_list = get_pnx_list(d_working=D_PKG_PY, mode="f", with_walking=0)
            for pnx in pnx_list:
                if __file__ not in pnx:
                    continue
                available_pk_python_program_pnx = pnx
            tmux_session = get_nx(available_pk_python_program_pnx).replace(".", "_")
            ensure_tmux_pk_session_removed(tmux_session)

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
