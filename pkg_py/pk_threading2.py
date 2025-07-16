# -*- coding: utf-8 -*-



if __name__ == '__main__':
    from pk_core import pk_deprecated_get_d_current_n_like_person, get_f_current_n, chcp_65001, get_os_n, close_window_duplicated_list, get_window_opened_list, get_pnx_os_style, cmd_to_os
    from pkg_py.pk_colorful_cli_util import pk_print, print_yellow
    from pkg_py.pk_core_constants import UNDERLINE, D_PKG_CMD
    import threading
    import time

    try:
        if get_os_n() == 'windows':
            chcp_65001()

        # 전역 플래그를 사용해 루프 재exec  제어
        flag_to_detect_enter = 0


        def listen_enter():
            global flag_to_detect_enter
            while 1:
                input()
                flag_to_detect_enter = 1


        def main_loop():
            global flag_to_detect_enter
            while 1:
                # liost

                # todo
                print("todo")

                # sleep
                sleep_seconds = 3
                for _ in range(sleep_seconds):
                    if flag_to_detect_enter:
                        pk_print("Enter detected Restarting loop...", print_color="blue")

                        # todo
                        print("todo")

                        flag_to_detect_enter = 0
                        pk_print(f"wait for enter %%%FOO%%%", print_color='white')
                        break
                    time.sleep(1)

        # thread run ( in background )
        thread = threading.Thread(target=listen_enter, daemon=True)
        thread.start()

        # main loop run 
        main_loop()

    except Exception as e:
        f_current_n= get_f_current_n()
        d_current_n=pk_deprecated_get_d_current_n_like_person()
        script_to_run_python_program_in_venv = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
        traceback_format_exc_list = traceback.format_exc().split("\n")

        pk_print(working_str=f'{UNDERLINE}', print_color='red')
        for traceback_format_exc_str in traceback_format_exc_list:
            pk_print(working_str=f'{STAMP_EXCEPTION_OCCURED} {traceback_format_exc_str}', print_color='red')
        pk_print(working_str=f'{UNDERLINE}', print_color='red')

        

        pk_print(working_str=f'{UNDERLINE}')
        pk_print(working_str=f'{STAMP_TRY_GUIDE} {script_to_run_python_program_in_venv}')
        pk_print(working_str=f'{UNDERLINE}')





