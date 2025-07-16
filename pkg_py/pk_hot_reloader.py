# -*- coding: utf-8 -*-
if __name__ == '__main__':
    try:
        import asyncio
        import os
        import traceback

        from pk_core import pk_deprecated_get_d_current_n_like_person, get_f_current_n, chcp_65001, get_os_n, pk_kill_process_as_async, cmd_to_remote_os_with_pubkey, ensure_remote_os_as_nopasswd, ensure_ssh_public_key_to_remote_os, get_pnx_wsl_unix_style, get_wsl_pw, get_wsl_user_n, get_wsl_ip, \
    ensure_and_get_wsl_port, print_iterable_as_vertical, pk_here, pk_run_process_as_async, LTA, pk_run_process, get_n, get_nx, cmd_to_os, ensure_f_list_change_stable, pk_kill_process, get_window_opened_list, get_pk_input, pk_sleep
        from pkg_py.pk_core_constants import STAMP_TRY_GUIDE, STAMP_PYTHON_DEBUGGING_NOTE, STAMP_EXCEPTION_DISCOVERED
        from pkg_py.pk_core_constants import UNDERLINE, D_PKG_PY, D_PROJECT, D_PROJECT_FASTAPI, STAMP_REMOTE_DEBUG, STAMP_REMOTE_ERROR, D_PROJECT_CMAKE
        from pkg_py.pk_core import pk_copy, get_pnx_os_style, pk_kill_process_by_window_title_seg, is_process_killed, get_set_from_list
        from pkg_py.pk_colorful_cli_util import pk_print

        if get_os_n() == 'windows':
            chcp_65001()

        # f.py
        # pnx_monitored_list = [
        #     # D_PROJECT,
        #     # rf"{__file__}",
        #     # rf"{D_PKG_PY}/test_monitor_process_cpu.py",
        #     # rf"{D_PROJECT}/pkg_friday/__init__.py",
        #     # rf"{D_PKG_PY}/pk_test.py",cmake
        # ]
        # pnx_to_excute_list = [
        #     rf"{D_PKG_PY}/test_build_and_exec_cmake_project.py",
        # ]
        # # monitoring_interval_seconds = 0.1
        # monitoring_interval_seconds = 1
        # while 1:
        #     if does_f_changed(pnx_list=pnx_monitored_list, monitoring_interval_seconds=monitoring_interval_seconds, pnx_changed_cnt_limit=1):
        #         # cmd_f_in_cmd_exe_like_person(cmd_prefix='python',  f=rf"{f_test_py}")
        #         for f in pnx_to_excute_list:
        #             asyncio.run(pk_kill_process_as_async(f=f))
        #         for f in pnx_to_excute_list:
        #             asyncio.run(pk_run_process_as_async(f=f))

        # f.cpp
        # pnx_monitored_list = [
        #     rf"{D_PKG_PY}/pk_hot_reloader.py",
        #     rf"{D_PKG_PY}/pk_build_and_exec_cmake_project.py",
        #     # rf"{PKG_CMAKE_PROJECT}/src/.vscode",
        #     rf"{D_PKG_CMAKE_PROJECT}/CMakeLists.txt",
        #     rf"{D_PKG_CMAKE_PROJECT}/src/config.yaml",
        #     rf"{D_PKG_CMAKE_PROJECT}/src/core.cpp",
        #     rf"{D_PKG_CMAKE_PROJECT}/src/core.h",
        #     rf"{D_PKG_CMAKE_PROJECT}/src/main.cpp",
        # ]
        # pnx_to_excute_list = [
        #     rf"{D_PKG_PY}/pk_build_and_exec_cmake_project.py",
        # ]
        # # monitoring_interval_seconds = 0.1
        # # monitoring_interval_seconds = 5
        # monitoring_interval_seconds = 1
        # while 1:
        #     if does_f_changed(pnx_list=pnx_monitored_list, monitoring_interval_seconds=monitoring_interval_seconds, pnx_changed_cnt_limit=1):
        #         # cmd_f_in_cmd_exe_like_person(cmd_prefix='python',  f=rf"{f_test_py}")
        #         for f in pnx_to_excute_list:
        #             asyncio.run(kill_process_as_async(f=f))
        #         for f in pnx_to_excute_list:
        #             asyncio.run(pk_run_process_as_async(f=f))

        # project_streamlit
        # pnx_monitored_list = [
        #     rf"{D_PKG_PY}/pk_hot_reloader.py",
        #     rf"{D_PROJECT_STREAMLIT}",
        # ]
        # pnx_to_excute_list = [
        #     rf"{D_PROJECT_STREAMLIT}/main.py",
        # ]
        # monitoring_interval_seconds = 1
        # while 1:
        #     if does_f_changed(pnx_list=pnx_monitored_list, monitoring_interval_seconds=monitoring_interval_seconds, pnx_changed_cnt_limit=1):
        #         for f in pnx_to_excute_list:
        #             asyncio.run(pk_kill_process_as_async(f=f))
        #         for f in pnx_to_excute_list:
        #             cmd = f'start "" streamlit run {f}'
        #             cmd_to_os(cmd=cmd, mode='a')

        # project_fastapi
        # wsl_distro_n = 'Ubuntu-24.04'
        # config_remote_os = {
        #     'port': ensure_and_get_wsl_port(wsl_distro_n),
        #     'ip': get_wsl_ip(wsl_distro_n),
        #     'user_n': get_wsl_user_n(wsl_distro_n),
        #     'pw': get_wsl_pw(wsl_distro_n),
        #     'local_ssh_public_key': os.path.join(os.environ["USERPROFILE"], ".ssh", "id_ed25519.pub"),
        #     'local_private_key': os.path.expanduser("~/.ssh/id_ed25519"),
        # }
        # ip = config_remote_os['ip']
        # pw = config_remote_os['pw']
        # port = config_remote_os['port']
        # user_n = config_remote_os['user_n']
        # local_ssh_public_key = config_remote_os['local_ssh_public_key']
        # local_private_key = config_remote_os['local_private_key']
        # project_pnx = get_pnx_unix_style_for_wsl(pnx=D_PROJECT_CMAKE)
        # if LTA:
        #     pk_print(f'''{STAMP_TRY_GUIDE} ssh -p {port} {user_n}@{ip} {'%%%FOO%%%' if LTA else ''}''')
        #
        # ensure_ssh_public_key_to_remote_os(ip=ip, port=port, user_n=user_n, pw=pw, local_ssh_public_key=local_ssh_public_key)
        # ensure_remote_os_as_nopasswd(ip=ip, port=port, user_n=user_n, pw=pw, local_private_key=local_private_key)
        #
        # pnx_monitored_list = [
        #     rf"{D_PKG_PY}/pk_hot_reloader.py",
        #     rf"{D_PROJECT_FASTAPI}",
        #     rf"{D_PROJECT}/project_fastapi.Dockerfile",
        #     rf"{D_PROJECT}/requirements.txt",
        # ]
        # pnx_to_excute_list = [
        #     rf"{D_PROJECT}/project_fastapi.Dockerfile",
        # ]
        # monitoring_interval_seconds = 1
        # while 1:
        #     if does_f_changed(pnx_list=pnx_monitored_list, monitoring_interval_seconds=monitoring_interval_seconds, pnx_changed_cnt_limit=1):
        #         for f in pnx_to_excute_list:
        #             asyncio.run(pk_kill_process_as_async(f=f))
        #         for f in pnx_to_excute_list:
        #             f = get_pnx_unix_style_for_wsl(f)
        #             cmd = f'docker build -t image_project_fastapi -f "{f}" .'
        #             pk_print(f'''cmd={cmd} %%%FOO%%%''')
        #             std_out_list, std_err_list = cmd_to_remote_os_with_pubkey(ip=ip, port=port, user_n=user_n, local_private_key=local_private_key, cmd=cmd)
        #             print_iterable_as_vertical(item_iterable=std_out_list, item_iterable_n="std_out_list")
        #             print_iterable_as_vertical(item_iterable=std_err_list, item_iterable_n="std_err_list")
        #             # build_and_run_docker_image(f=rf'{D_PROJECT}/test.Dockerfile')

        # f.py with pk_test.py
        # pnx_monitored_list = [
        #     rf"{D_PKG_PY}/pk_test.py",
        # ]
        # pnx_to_excute_list = [
        #     rf"{D_PKG_PY}/pk_test.py",
        # ]
        # # monitoring_interval_seconds = 0.1
        # monitoring_interval_seconds = 1
        # while 1:
        #     if does_f_changed(pnx_list=pnx_monitored_list, monitoring_interval_seconds=monitoring_interval_seconds, pnx_changed_cnt_limit=1):
        #         # cmd_f_in_cmd_exe_like_person(cmd_prefix='python',  f=rf"{f_test_py}")
        #         for f in pnx_to_excute_list:
        #             asyncio.run(pk_kill_process_as_async(f=f))
        #         for f in pnx_to_excute_list:
        #             asyncio.run(pk_run_process_as_async(f=f))

        # f.py with pk_test.py way 2
        window_opened_list = get_window_opened_list()
        window_opened_set = get_set_from_list(window_opened_list)
        window_title_to_kill = None
        f_monitored_list = [
            rf"{D_PKG_PY}/pk_test.py",
            rf"{D_PKG_PY}/pk_core.py",
        ]
        pnx_to_execute_list = [
            rf"{D_PKG_PY}/pk_test.py",
        ]
        loop_cnt = 1
        # limit_seconds = 4
        limit_seconds = 1
        while 1:
            if loop_cnt == 1:
                # if window_title_to_kill is None:
                #     window_title_to_kill = get_pk_input_via_tab(message='window_title_to_kill=', tab_completer_iterable=window_opened_set)
                for f in pnx_to_execute_list:
                    window_opened_set.add(get_nx(f))
                    pk_run_process(pk_program_n_seg=get_nx(f))
                    window_title_to_kill = get_nx(f)
                loop_cnt = loop_cnt + 1
                continue
            if not ensure_f_list_change_stable(f_list=f_monitored_list, limit_seconds=limit_seconds):
                pk_print("step 1", print_color='green')
                if ensure_f_list_change_stable(f_list=f_monitored_list, limit_seconds=limit_seconds):
                    pk_print("step 2", print_color='green')
                    # window_tilte_to_kill_list = []
                    for f in pnx_to_execute_list:
                        pk_print("step 3", print_color='green')
                        pk_kill_process(window_title=window_title_to_kill)
                        if not is_process_killed(window_title_seg=get_nx(f)):
                            pk_print("step 4", print_color='green')
                            pk_kill_process(window_title=window_title_to_kill)
                            # break
                        else:
                            pk_print("step 5", print_color='green')
                            # break
                        pk_run_process(pk_program_n_seg=get_nx(f))
            else:
                pk_print("step 6", print_color='green')
                continue

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
