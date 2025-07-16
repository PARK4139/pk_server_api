import constants
from pk_core import get_f_current_n, get_d_current_n_like_person, should_i_search_to_google, get_txt_dragged, print_txt_dragged_changed, should_i_search_to_chatGPT
from pkg_py.pk_colorful_cli_util import pk_print



if __name__ == "__main__":
    try:
        # todo
        while 1:
            should_i_search_to_chatGPT()
            print()
            print()
            print()
            print()

        # print_txt_dragged_changed()

    except:
        f_current_n= get_f_current_n()
        d_current_n=get_d_current_n_like_person()
        script_to_run_python_program_in_venv = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
        traceback_format_exc_list = traceback.format_exc().split("\n")
        
        pk_print(working_str=f'{UNDERLINE}', print_color='red')
        for traceback_format_exc_str in traceback_format_exc_list:
            pk_print(working_str=f'{STAMP_EXCEPTION_OCCURED} {traceback_format_exc_str}', print_color='red')
        pk_print(working_str=f'{UNDERLINE}', print_color='red')

        pk_print(working_str=f'{UNDERLINE}\n', print_color="yellow")
        pk_print(working_str=f'{STAMP_PYTHON_DEBUGGING_NOTE} f_current={f_current_n}\nd_current={d_current_n}\n', print_color="yellow")
        pk_print(working_str=f'{UNDERLINE}\n', print_color="yellow")

        pk_print(working_str=f'{UNDERLINE}')
        pk_print(working_str=f'{STAMP_TRY_GUIDE} {script_to_run_python_program_in_venv}')
        pk_print(working_str=f'{UNDERLINE}')




