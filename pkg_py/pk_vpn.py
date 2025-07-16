import sys

import constants
from pk_core import search_f_list_contains_search_key, pk_deprecated_get_d_current_n_like_person, get_f_current_n
from gui import should_i_do
from pkg_py.pk_colorful_cli_util import pk_print
from pkg_py.pk_core_constants import UNDERLINE

# def try_to_access_to_url_via_vpn():
#     import subprocess
#     def connect_nordvpn(country):
#         try:
#             subprocess.run(["nordvpn", "connect", country], check=True)
#         except subprocess.CalledProcessError as e:
#             print(f"Failed to connect to NordVPN: {e}")
#
#     # NordVPN 연결
#     connect_nordvpn("South Korea")
#     # https://free-proxy-list.net/
#     # proxy = "https://3.37.125.76:3128"
#     # proxy = "https://43.202.154.212:80"
#     # driver = friday.get_driver_selenium(browser_debug_mode=True, proxy=proxy)
#     driver = friday.get_driver_selenium(browser_debug_mode=True)
#     url = 'https://~~~~'
#     try:
#         driver.get(url)
#         ipdb.set_trace()
#     except Exception as e:
#         print(f"Error: {e}")
#     finally:
#         driver.quit()


if __name__ == '__main__':
    debug_mode = True
    try:
        # todo
        # ipdb.set_trace()
        import ipdb
        ipdb.set_trace()


    except Exception as e:
        # red
        import traceback

        pk_print(working_str=f'{UNDERLINE}예외발생 s\n\n', print_color='red')
        pk_print(working_str=f'{traceback.format_exc()}\n', print_color='red')
        pk_print(working_str=f'{UNDERLINE}예외발생 e\n\n', print_color='red')

        # yellow
        f_current= get_f_current_n()
        d_current=pk_deprecated_get_d_current_n_like_person()
        pk_print(working_str=f'{UNDERLINE}[Debugging Note] s\n', print_color="yellow")
        pk_print(working_str=f'f_current={f_current}\nd_current={d_current}\n', print_color="yellow")
        pk_print(working_str=f'{UNDERLINE}[Debugging Note] e\n', print_color="yellow")
        script_to_run_python_program_in_venv = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
        pk_print(script_to_run_python_program_in_venv)

        # debug
        import ipdb
        ipdb.set_trace()
