# -*- coding: utf-8 -*-



if __name__ == '__main__':
    try:
        import traceback
        from pk_core import pk_deprecated_get_d_current_n_like_person, get_f_current_n, chcp_65001, get_os_n, organize_tree, gather_empty_d, get_p, organize_d_list_by_stamp
        from pkg_py.pk_core_constants import D_PROJECT, UNDERLINE, STAMP_TRY_GUIDE, STAMP_PYTHON_DEBUGGING_NOTE, STAMP_EXCEPTION_DISCOVERED, D_WORKING
        from pkg_py.pk_colorful_cli_util import pk_print
        from pkg_py.pk_core_constants import UNDERLINE
        import threading
        import time
        
        if get_os_n() == 'windows':
            chcp_65001()

        # [OPTION]
        # while 1:
        #     organize_tree(d_src=rf"D:\pk_classifying")
        #     sleep(hours=3)
        #     pk_print(f'''wait for oraganize tree in loop %%%FOO%%%''', print_color='blue')

        flag_to_detect_enter = 0

        def input_listener():
            global flag_to_detect_enter
            while 1:
                input()
                flag_to_detect_enter = 1


        def run_input_listener_loop():
            global flag_to_detect_enter

            # [OPTION]
            # d_working = rf"D:\[]"
            d_working = D_WORKING

            # [OPTION]
            with_walking = True

            while 1:
                for _ in range(3 * 3600):  # 3시간 (3600초) 동안 1초씩 sleep
                    if flag_to_detect_enter:
                        flag_to_detect_enter = 0
                        pk_print("Enter detected Restarting loop...", print_color="blue")

                        organize_tree(d_working=d_working, with_walking=with_walking)
                        gather_empty_d(d_working=get_p(d_working))
                        # organize_d_list_by_stamp(d=get_p(d_working))
                        gather_empty_d(d_working=d_working)
                        organize_d_list_by_stamp(d=d_working)
                        pk_print(f"wait for enter %%%FOO%%%", print_color='white')
                        break
                    time.sleep(1)

        # thread run ( in background )
        listener_thread = threading.Thread(target=input_listener, daemon=True)
        listener_thread.start()

        run_input_listener_loop()

    except Exception as e:
        f_current_n= get_f_current_n()
        d_current_n=pk_deprecated_get_d_current_n_like_person()
        script_to_run_python_program_in_venv = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
        traceback_format_exc_list = traceback.format_exc().split("\n")

        pk_print(working_str=f'{UNDERLINE}', print_color='red')
        for traceback_format_exc_str in traceback_format_exc_list:
            pk_print(working_str=f'{STAMP_EXCEPTION_DISCOVERED} {traceback_format_exc_str}', print_color='red')
        pk_print(working_str=f'{UNDERLINE}', print_color='red')

        

        pk_print(working_str=f'{UNDERLINE}')
        pk_print(working_str=f'{STAMP_TRY_GUIDE} {script_to_run_python_program_in_venv}')
        pk_print(working_str=f'{UNDERLINE}')
