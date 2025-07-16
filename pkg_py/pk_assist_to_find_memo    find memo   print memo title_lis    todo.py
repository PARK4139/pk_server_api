from pk_core import pk_deprecated_get_d_current_n_like_person, get_f_current_n, chcp_65001, get_os_n, print_memo_titles, ensure_f_list_change_stable
from pkg_py.pk_core_constants import D_PROJECT, UNDERLINE, STAMP_TRY_GUIDE, STAMP_PYTHON_DEBUGGING_NOTE, STAMP_EXCEPTION_DISCOVERED
from pkg_py.pk_colorful_cli_util import pk_print


def main():
    if get_os_n() == 'windows':
        chcp_65001()

    f = rf'{D_PROJECT}\memo_how.toml'
    # f_pnx = rf'{PROJECT_D}\todo.toml'
    # if not does_pnx_exist(f_pnx):
    #     pk_print(f'''{f_pnx} does not exist %%%FOO%%%''', print_color='red')
    #     return
    # line_list = get_list_from_f_pnx(f_pnx=f_pnx)
    # line_list = get_str_from_list(item_list=line_list)
    # line_str = line_list
    # pk_print(f'''len(line_list)={len(line_list)} %%%FOO%%%''')
    # pk_print(f'''len(line_str)={len(line_str)} %%%FOO%%%''')
    # data = line_str
    # txt_highlighted = [
    #     "%%%FOO%%%",
    #     'mkr_',
    #     "mkr_________________________________________________________________________",
    # ]
    # print_with_highlighted(txt_whole=data, txt_highlighted_list=txt_highlighted)

    # txt_str = input("Press Enter to continue...")
    # write_str_to_f_pnx(txt_str=txt_str, f_pnx=f_pnx)

    f_monitored_list = [
        f
    ]
    while 1:
        if ensure_f_list_change_stable(f_list=f_monitored_list, limit_seconds=30):
            print_memo_titles(f=f)


if __name__ == "__main__":
    try:
        # todo
        main()

    except:
        f_current_n = get_f_current_n()
        d_current_n = pk_deprecated_get_d_current_n_like_person()
        script_to_run_python_program_in_venv = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
        traceback_format_exc_list = traceback.format_exc().split("\n")

        pk_print(f'{UNDERLINE}', print_color='red')
        for traceback_format_exc_str in traceback_format_exc_list:
            pk_print(f'{STAMP_EXCEPTION_DISCOVERED} {traceback_format_exc_str}', print_color='red')
        pk_print(f'{UNDERLINE}', print_color='red')

        pk_print(f'{UNDERLINE}\n', print_color="yellow")
        pk_print(f'{STAMP_PYTHON_DEBUGGING_NOTE} f_current={f_current_n}\nd_current={d_current_n}\n', print_color="yellow")
        pk_print(f'{UNDERLINE}\n', print_color="yellow")

        pk_print(f'{UNDERLINE}')
        pk_print(f'{STAMP_TRY_GUIDE} {script_to_run_python_program_in_venv}')
        pk_print(f'{UNDERLINE}')
