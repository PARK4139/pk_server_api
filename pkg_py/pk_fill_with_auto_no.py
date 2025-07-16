



if __name__ == '__main__':
    try:
        from pk_colorful_cli_util import pk_print
        from pkg_py.pk_core_constants import UNDERLINE, D_PROJECT
        from pk_core import replace_with_auto_no
        import constants
        from pkg_py.pk_core_constants import D_PROJECT, UNDERLINE, STAMP_TRY_GUIDE, STAMP_PYTHON_DEBUGGING_NOTE, STAMP_EXCEPTION_DISCOVERED, UNDERLINE, STAMP_TRY_GUIDE, STAMP_PYTHON_DEBUGGING_NOTE, STAMP_EXCEPTION_DISCOVERED, D_PKG_PY
        from pk_core import get_f_current_n, pk_deprecated_get_d_current_n_like_person, get_list_from_f, does_pnx_exist, get_str_from_list, print_highlighted
        from pkg_py.pk_colorful_cli_util import pk_print
        import traceback
        from pkg_py.pk_core import get_str_from_f, pk_input_validated

        # todo
        #   chore : rename f_n with suffix as _converted

        # [OPTION]
        # f = input_validated(prompt='f=')
        # f = rf'{PKG_PY}/'

        # [OPTION]
        # template_str = get_str_f_temp() # todo    with open     f_obj    notepad.exe
        # template_str = get_list_f_temp() # todo
        # template_str = get_str_from_f(f=f)

        pk_print(working_str=rf'''{UNDERLINE} %%%FOO%%%''')
        result = replace_with_auto_no(template_str=template_str, word_monitored='%%%FOO%%%', auto_cnt_starting_no=0)
        pk_print(result)
        pk_print(working_str=rf'''{UNDERLINE} %%%FOO%%%''')


    except:
        pk_print("202312071431")

