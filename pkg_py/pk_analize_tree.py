# -*- coding: utf-8 -*-



from pk_core import pk_deprecated_get_d_current_n_like_person, get_f_current_n, pk_sleep, chcp_65001, get_os_n, analize_tree
from pkg_py.pk_colorful_cli_util import pk_print, print_red, print_yellow
from pkg_py.pk_core_constants import UNDERLINE

pass

if __name__ == '__main__':
    try:
        # ___________________________________________________________________________
        if get_os_n() == 'windows':
            chcp_65001()

        while 1:
            analize_tree(d_src=rf"D:\pk_classifying")
            pk_sleep(hours=3)
        # ___________________________________________________________________________
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
