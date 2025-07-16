import threading
import time

from pk_core import pk_press
from pkg_py.pk_colorful_cli_util import pk_print


if __name__ == "__main__":
    # ref
    import keyboard
    import pyautogui
    pk_print(f'''detect hotkey %%%FOO%%%''',print_color="blue")
    while 1:
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('alt') and keyboard.is_pressed('`'):
            pyautogui.alert("백스페이스와 1이 눌렸습니다!")  # 예제 동작: 알림창 표시
        # 종료 키
        if keyboard.is_pressed('esc'):
            print("프로그램 종료")
            break

    # ref
    # pk_print(f'''detect hotkey %%%FOO%%%''', print_color="blue")
    # while 1:
    #     if keyboard.is_pressed('ctrl') and keyboard.is_pressed('scroll lock'):
    #         can_i_search_contents_dragged_to_google()
    #     # if keyboard.is_pressed('esc'):
    #     #     print("프로그램 종료")
    #     #     break