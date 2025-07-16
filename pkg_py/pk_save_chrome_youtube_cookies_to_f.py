import os
import sys
import traceback

# pkg_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
# if pkg_path not in sys.path:
#     sys.path.append(pkg_path)

from pk_colorful_cli_util import pk_print
from pkg_py.pk_core_constants import UNDERLINE, D_PROJECT 
from pk_core import pk_deprecated_get_d_current_n_like_person, get_f_current_n, pk_sleep
from pkg_py.pk_core import save_chrome_youtube_cookies_to_f

if __name__ == "__main__":
    try:
        save_chrome_youtube_cookies_to_f()

        while 1:
            pk_sleep(hours=24)
    except Exception as e:
        traceback.print_exc()
        # 예외 처리
        pk_print(working_str=f'{UNDERLINE}예외발생 s\n\n', print_color='red')
        pk_print(working_str=f'{traceback.format_exc()}\n', print_color='red')
        pk_print(working_str=f'{UNDERLINE}예외발생 e\n\n', print_color='red')

        # 디버깅 노트 출력
        f_current= get_f_current_n()
        d_current=pk_deprecated_get_d_current_n_like_person()
        pk_print(working_str=f'{UNDERLINE}[Debugging Note] s\n', print_color="yellow")
        pk_print(working_str=f'f_current={f_current}\nd_current={d_current}\n', print_color="yellow")
        pk_print(working_str=f'{UNDERLINE}[Debugging Note] e\n', print_color="yellow")
        script_to_run_python_program_in_venv = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
        pk_print(script_to_run_python_program_in_venv)
