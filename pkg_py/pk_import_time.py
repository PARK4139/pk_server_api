import traceback

import ipdb

from pk_core import get_f_current_n, pk_deprecated_get_d_current_n_like_person
from pkg_py.pk_colorful_cli_util import pk_print, print_red
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


def test_module_import_time_via_time():
    modules = [
        # 기본 라이브러리
        "asyncio", "datetime", "inspect", "json", "os", "platform", "random", "re", "shutil", "string", "subprocess", "sys", "threading", "time", "traceback", "urllib", "webbrowser", "zipfile", "collections.Counter", "functools.partial", "typing.TypeVar", "typing.List", "urllib.parse.quote", "urllib.parse.urlparse", "zipfile.BadZipFile",

        # 외부 라이브러리
        "chardet", "clipboard", "cv2", "easyocr", "ipdb", "keyboard", "mutagen", "numpy as np", "pandas as pd", "psutil", "pyaudio", "pyautogui", "pygetwindow", "pyglet", "pywintypes", "requests", "selenium.webdriver as webdriver", "send2trash", "speech_recognition as sr", "tqdm", "win32con", "win32gui", "win32process", "PIL.Image", "PIL.ImageFont", "PIL.ImageDraw", "PIL.ImageFilter",
        "playwright.sync_api as sync_playwright", "bs4.BeautifulSoup", "bs4.ResultSet", "dirsync.sync", "fastapi.HTTPException", "gtts.gTTS", "moviepy.VideoFileClip", "pynput.mouse", "pytube.Playlist", "selenium.webdriver.chrome.options as Options", "selenium.webdriver.common.by as By",

        # 사용자 정의 모듈
        "legacy.CustomErrorUtil", "legacy.DataStructureUtil", "pkg_py.interface_cmd_line.pk_print", "pkg_py.interface_cmd_line.print_light_black", "pkg_py.interface_cmd_line.print_cyan", "pkg_py.interface_cmd_line.print_with_underline", "pkg_py.interface_cmd_line.print_red", "pkg_py.interface_cmd_line.print_magenta", "pkg_py.interface_cmd_line.print_light_white", "pkg_py.interface_cmd_line.ColoramaUtil", "pkg_py.interface_cmd_line.print_ment_via_colorama",
        "pkg_py.interface_cmd_line.print_success", "pkg_py.interface_cmd_line.print_light_yellow", "pkg_py.interface_cmd_line.print_yellow",
        "pkg_py.constants.USERPROFILE", "pkg_py.constants.HOSTNAME", "pkg_py.constants.UNDERLINE",
        "pkg_py.constants.BLANK", "pkg_py.constants.BIGGEST_PNXS", "pkg_py.constants.SMALLEST_PNXS",
        "pkg_py.constants.PLAYING_SOUNDS", "pkg_py.constants.COUNTS_FOR_GUIDE_TO_SLEEP",
        "pkg_py.constants.[]", "pkg_py.constants.VIDEO_IDS_ALLOWED",
        "pkg_py.constants.AUDIO_IDS_ALLOWED", "pkg_py.constants.STORAGE_VIDEOES_MERGED",
        "pkg_py.constants.PROJECT_PARENTS_DIRECTORY", "pkg_py.constants.DESKTOP",
        "pkg_py.constants.DOWNLOADS", "pkg_py.constants.PKG_PNG", "pkg_py.constants.PKG_DPL",
        "pkg_py.constants.PKG_TXT", "pkg_py.constants.CLASSIFYING", "pkg_py.constants.RECYCLE_BIN",
        "pkg_py.constants.LOCAL_PKG_CACHE_FILE", "pkg_py.constants.SUCCESS_LOG", "pkg_py.constants.SCHECLUER_YAML", "pkg_py.constants.YT_DLP_CMD",
        "pkg_py.constants.JQ_WIN64_EXE", "pkg_py.constants.FFMPEG_EXE", "pkg_py.constants.DB_YAML",
        "pkg_py.constants.USELESS_FILE_NAMES_TXT", "pkg_py.constants.SILENT_MP3",
        "pkg_py.constants.PKG_SOUND_POTPLAYER64_DPL", "pkg_py.constants.PKG_VIDEO_POTPLAYER64_DPL",
        "pkg_py.constants.MERGED_EXCEL_FILE", "pkg_py.constants.PROJECT_D",
        "pkg_py.constants.YES", "pkg_py.constants.NO", "pkg_py.constants.NOT_PREPARED_YET",
        "pkg_py.gui.GuiUtil", "pkg_py.gui.get_display_info", "times.get_time_as_"
    ]
    import time
    test_result_list = []
    for module in modules:
        start_time = time.time()
        try:
            exec(f"import {module}")
            test_result_list.append(f"in {time.time() - start_time:.4f} seconds  {module:60s} imported")
        except Exception as e:
            test_result_list.append(f"in {time.time() - start_time:.4f} seconds  {module:60s} FAILED ({e})")

    test_result_list = sorted(test_result_list)
    print("\n".join(test_result_list))


def function_to_test():
    
    pass


def test_function_exec_time_via_cprofile():
    import cProfile
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    pk_print(working_str=rf'''{UNDERLINE}{func_name}() s %%%FOO%%%''', print_color='blue')
    cProfile.run('function_to_test()')
    pk_print(working_str=rf'''{UNDERLINE}{func_name}() e %%%FOO%%%''', print_color='blue')


def test_function_exec_time_via_time():
    import time
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    pk_print(working_str=rf'''{UNDERLINE}{func_name}() s %%%FOO%%%''', print_color='blue')
    debug_mode = True
    total_start = time.time()
    try:
        start = time.time()
        function_to_test()
        print(f"function_to_test() took {time.time() - start:.2f} seconds")
    except Exception as e:
        print(f"Exception occurred: {e}")
    print(f"Total execution time: {time.time() - total_start:.2f} seconds")
    pk_print(working_str=rf'''{UNDERLINE}{func_name}() e %%%FOO%%%''', print_color='blue')


if __name__ == '__main__':
    debug_mode = True
    try:
        # todo
        # ipdb.set_trace()
        test_function_exec_time_via_time()
        test_function_exec_time_via_cprofile()
        test_module_import_time_via_time()

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