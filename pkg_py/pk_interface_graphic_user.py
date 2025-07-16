import inspect
import os
import platform
import sys
import time
import traceback
from functools import partial
from typing import Callable, TypeVar

import clipboard
import pyautogui
import pynput
from BlurWindow.blurWindow import GlobalBlur
from PySide6 import QtWidgets
from PySide6.QtCore import QCoreApplication
from PySide6.QtCore import QEvent
from PySide6.QtCore import QThread
from PySide6.QtCore import QTimer
from PySide6.QtCore import Qt
from PySide6.QtCore import Signal
from PySide6.QtGui import QCursor
from PySide6.QtGui import QFontDatabase, QFont
from PySide6.QtGui import QIcon, QGuiApplication
from PySide6.QtGui import QKeySequence
from PySide6.QtGui import QScreen
from PySide6.QtGui import QShortcut
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QDialog
from PySide6.QtWidgets import QGridLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QScrollArea, QTextBrowser
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget
from screeninfo import get_monitors



T = TypeVar('T')  # todo : ref : 타입 힌팅 설정

from pkg_py.pk_colorful_cli_util import pk_print, print_light_black, print_cyan, print_success, print_red
from pkg_py.pk_core_constants import UNDERLINE, F_MACRO_LOG, F_POP_SOUND_POP_SOUND_WAV, D_PROJECT, F_RUBIKDOODLESHADOW_REGULAR_TTF, F_ICON_PNG, F_GMARKETSANSTTFLIGHT_TTF


def get_windows_opened_via_win32gui(debug_mode=True):
    window_titles = []

    def enum_windows_callback(hwnd, lparam):
        if win32gui.IsWindowVisible(hwnd):
            # 창의 제목을 가져와서 리스트에 추가
            window_title = win32gui.GetWindowText(hwnd)
            if window_title:  # 제목이 비어있지 않은 창만 추가
                window_titles.append(window_title)

    import win32gui # pywin32
    win32gui.EnumWindows(enum_windows_callback, None)

    if debug_mode == True:
        pk_print(f'''window_titles = "{window_titles}" %%%FOO%%%''')
    return window_titles


def get_windows_opened(debug_mode=True):
    # return get_windows_opened_via_psutil()
    # return get_windows_opened_via_pygetwindow()
    return get_windows_opened_via_win32gui(debug_mode=debug_mode)


def get_list_removed_element_none(items, debug_mode=True):
    func_n = inspect.currentframe().f_code.co_name
    if debug_mode == False:
        pk_print(working_str=rf'''%%%FOO%%%''')
    if items is not None:
        return [x for x in items if x is not None]
    return None


def is_window_open(window_title_seg, debug_mode=True):
    func_n = inspect.currentframe().f_code.co_name
    if debug_mode == True:
        pk_print(working_str=rf'''%%%FOO%%%''')

    windows_titles_opened = get_windows_opened(debug_mode=debug_mode)
    windows_titles_opened = get_list_removed_element_none(items=windows_titles_opened)

    for windows_title_opened in windows_titles_opened:
        if debug_mode == True:
            pk_print(working_str=rf'''windows_title_opened="{windows_title_opened}" %%%FOO%%%''')
        if window_title_seg in windows_title_opened:
            if debug_mode == True:
                pk_print(f'''"{windows_title_opened}" 창이 열려 있습니다''')
            return True
    if debug_mode == True:
        pk_print(f'''"{window_title_seg}" 창이 닫혀 있습니다''')
    return False


def get_front_window_title():
    try:
        import pygetwindow
        active_window = pygetwindow.getActiveWindow()
        if active_window:
            return active_window.title
        else:
            return None  # 활성화된 창이 없다면 None 반환
    except Exception as e:
        return f"Error: {str(e)}"


def is_front_window_title(window_title_seg, debug_mode=True):
    front_window_title = get_front_window_title()
    if not front_window_title is None:
        if debug_mode == True:
            pk_print(f'''window_title_seg = "{window_title_seg}"''')
            pk_print(f'''front_window_title = "{front_window_title}"''')
        if window_title_seg in front_window_title:
            return True
    return False



# async def move_window_to_front_via_async(window_title_seg=None, pid=None, debug_mode=True):
#     import psutil
#     func_n = inspect.currentframe().f_code.co_name
#     if debug_mode == True:
#         pk_print(str_working=rf'''%%%FOO%%%''')
#         if window_title_seg is not None or pid is not None:
#             pk_print(rf"{func_n}() 동작 조건 충족")
#         else:
#             pk_print(rf"{func_n}() 동작 조건 불충족")
#             return
#         if window_title_seg is not None:
#             pk_print(f'''window_title_seg = "{window_title_seg}" %%%FOO%%%''')
#         if pid is not None:
#             pk_print(f'''pid = "{pid}" %%%FOO%%%''')
#
#     if window_title_seg is not None:
#         while 1:
#             if is_window_open(window_title_seg=window_title_seg, debug_mode=debug_mode):
#                 if not is_front_window_title(window_title_seg=window_title_seg):
#                     move_window_to_front_v_1_0_0(window_title_seg, debug_mode=debug_mode)
#                 if is_front_window_title(window_title_seg=window_title_seg):
#                     pk_print(f'''"{window_title_seg} 창을 앞으로 이동했습니다"''', print_color='blue')
#                     break
#             else:
#                 return
#     if pid is not None:
#         # PID가 숫자인지 확인
#         if not str(pid).isdigit():
#             if debug_mode:
#                 pk_print(f"PID 분석 결과 숫자가 아닌 것으로 판단: {pid} %%%FOO%%%", print_color='red')
#             return
#
#         pid = int(pid)  # PID를 정수로 변환
#
#         try:
#             # PID에 해당하는 프로세스 객체 가져오기
#             process = psutil.Process(pid)
#
#             if process.is_running() and process.status() != psutil.STATUS_ZOMBIE:
#                 import win32gui # pywin32
#                 hwnd = win32gui.FindWindow(None, None)  # 첫 번째 창 핸들을 가져옴
#
#                 # PID와 연결된 창 핸들을 검색
#                 while hwnd:
#                     import win32process
#                     _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
#
#                     # 검색된 창의 PID가 입력 PID와 일치하면 창 활성화
#                     if found_pid == pid:
#                         try:
#                             win32gui.SetForegroundWindow(hwnd)  # 창 활성화
#                             if debug_mode:
#                                 pk_print(f"PID {pid}의 창을 활성화했습니다.", print_color='blue')
#                             break
#                         except Exception as e:
#                             if debug_mode:
#                                 pk_print(f"창 활성화 실패: {e}", print_color='red')
#
#                     # 다음 창 핸들 검색
#                     import win32gui # pywin32
#                     hwnd = win32gui.FindWindowEx(None, hwnd, None, None)
#                 else:
#                     if debug_mode:
#                         pk_print(f"PID {pid}에 해당하는 창 핸들을 찾을 수 없습니다.", print_color='yellow')
#             else:
#                 print_cyan(f"{UNDERLINE}프로세스가 exec  중이지 않거나 좀비 상태입니다.")
#         except psutil.NoSuchProcess:
#             print_cyan(f"{UNDERLINE}유효하지 않은 PID입니다.")
#         except Exception as e:
#             pk_print(f"알 수 없는 오류 발생: {e}", print_color='red')


class GuiUtil:
    class CustomQdialog(QDialog):
        """순환참조 를 회피하기 위해서 객체를 복제했다."""

        def update_txt_clicked(self, text_of_clicked_button):
            func_n = inspect.currentframe().f_code.co_name
            pk_print(working_str=rf'''%%%FOO%%%''')
            self.txt_clicked = text_of_clicked_button

        def update_txt_clicked_and_close(self, text_of_clicked_button):
            func_n = inspect.currentframe().f_code.co_name
            pk_print(working_str=rf'''%%%FOO%%%''')
            from pk_core import play_wav_f
            play_wav_f(f=F_POP_SOUND_POP_SOUND_WAV)
            self.txt_clicked = text_of_clicked_button
            self.close()

        def set_shortcut(self, key_plus_key: str, function):
            func_n = inspect.currentframe().f_code.co_name
            pk_print(working_str=rf'''%%%FOO%%%''')
            self.shortcut = QShortcut(QKeySequence(key_plus_key), self)
            self.shortcut.activated.connect(function)

        # 스택 마우스 제작 참고용
        # def eventFilter(self, obj, event):

        #     # 드래그 가능한 레이블의 이벤트 구현
        #     if isinstance(obj, DraggableLabel) and event.type() == QEvent.MouseButtonPress:
        #         obj.mousePressEvent(event)
        #         return True
        #     elif isinstance(obj, DraggableLabel) and event.type() == QEvent.MouseMove:
        #         obj.mouseMoveEvent(event)
        #         return True
        #
        #     return super().eventFilter(obj, event)

        def __init__(self, prompt: str, btn_list=None, parent=None, input_box_mode=False, input_box_text_default="", title="", auto_click_negative_btn_after_seconds: int = None, auto_click_positive_btn_after_seconds: int = None):
            func_n = inspect.currentframe().f_code.co_name

            # log _________ class_name.function()
            class_name = self.__class__.__name__
            pk_print(working_str=rf'''{UNDERLINE}class_name="{class_name}/{func_n}()" %%%FOO%%%''')

            try:
                super().__init__(parent)
                f = F_POP_SOUND_POP_SOUND_WAV
                if os.path.exists(f):
                    from pk_core import play_wav_f
                    play_wav_f(f=f)
                self.input_text_default = input_box_text_default
                self.context = prompt
                self.title = title
                if self.title == "":
                    self.setWindowTitle(".")
                else:
                    self.setWindowTitle(self.title)
                self.is_input_text_box = input_box_mode
                self.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: white;")  # 메시지박스창 스타일시트 적용 설정
                self.setWindowIcon(QIcon(F_ICON_PNG))  # 메시지박스창 아이콘 설정
                self.setAttribute(Qt.WA_TranslucentBackground)  # 메시지박스창 블러 설정
                # self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # 메시지박스창 최상단 프레임레스 설정
                GlobalBlur(self.winId(), hexColor=False, Acrylic=False, Dark=True, QWidget=self)
                # self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint)  # 메시지박스창 최대화 최소화 버튼숨기기
                # self.setWindowFlag(Qt.WindowCloseButtonHint, False)  # 메시지박스창 닫기 버튼 disable
                # self.setWindowFlag(Qt.WindowStaysOnTopHint)  # 모든 창들 중 가장 앞에 메시지박스창 위치하도록 설정
                # self.setStyleSheet("background-color: rgba(0, 0, 0, 0)")  # 메시지박스창 스타일시트 적용 설정

                self.display_width = get_display_info()['width'],
                self.display_height = get_display_info()['height'],
                # self.pop_up_window_width_default = int(int(self.display_width[0]) * 0.4)
                # self.pop_up_window_height_default = int(int(self.display_height[0]) * 0.4)
                # self.resize(self.pop_up_window_width_default, self.pop_up_window_height_default)
                if len(prompt.split("\n")) < 20:
                    # self.resize(500, 250)
                    self.resize(int(self.display_width[0] * 0.3), int(self.display_height[0] * 0.2))
                else:
                    # self.resize(int(500 * 2.5), 250 * 2)
                    # self.resize(int(self.display_width[0] * 0.8), int(self.display_height[0] * 0.6))
                    self.resize(int(self.display_width[0] * 0.4), int(self.display_height[0] * 0.6))
                    # self.resize(int(self.display_width[0] * 0.9), int(self.display_height[0] * 0.6))

                # 창을 화면의 상단가운데로 이동
                screen = QGuiApplication.primaryScreen()
                screen_geometry = screen.availableGeometry()
                center_point = screen_geometry.center()
                self.move(center_point.x() - self.width() / 2, screen_geometry.top() + (center_point.y() * 0.1))

                # pyside6 표준버튼 설정
                # self.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
                # self.setButtonText(QMessageBox.StandardButton.Ok, "확인", )
                # self.setButton.setStyleSheet("background-color: rgba(0, 0, 0, 0);  color: white;")
                # self.setButtonText(QMessageBox.StandardButton.Cancel, "취소")
                self.txt_clicked = None
                self.layout_horizontal = None
                self.btn_positive = None
                self.btn_negative = None
                self.btn_third = None

                # 스크롤지역 설정
                self.scroll_area = None

                # 버튼 설정
                btn_to_copy = QPushButton(prompt)
                btn_to_copy.setStyleSheet("background-color: rgba(0, 0, 0, 0);  color: white;")
                btn_to_copy.setFocusPolicy(Qt.NoFocus)
                btn_to_copy.clicked.connect(self.copy_label_text_to_clipboard)
                # pk_print(context=len(contents.strip()))
                if 30 < len(prompt.strip()):
                    # btn_to_copy.setStyleSheet("text-align: left; font-size: 8px")
                    btn_to_copy.setStyleSheet("text-align: left; font-size: 16px")
                else:
                    btn_to_copy.setStyleSheet("text-align: center; font-size: 20px")
                f = F_GMARKETSANSTTFLIGHT_TTF
                if os.path.exists(f):
                    btn_to_copy.setFont(Pyside6Util.get_font_for_pyside6(font_path=f))

                self.set_shortcut(function=self.copy_label_text_to_clipboard, key_plus_key="alt+C")  # 단축키 설정

                self.scroll_area = QScrollArea()
                # self.scroll_area.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                self.scroll_area.setWidget(btn_to_copy)
                self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
                self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
                self.scroll_area.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                self.scroll_area.setStyleSheet(" border: none;")
                # if 100 < len(contents):
                # self.scroll_area.setStyleSheet("text-align: center; border: none;")
                # else:
                # self.scroll_area.setStyleSheet("text-align: left; border: none; ")
                self.scroll_area.setFocusPolicy(Qt.NoFocus)  # focus 가 필요 없는 부분에는 이렇게 설정을 해두어야 원하는 곳으로 처음 창이 열렸을 때 focus 되도록 유도할 수 있었다
                # self.scroll_area.setMaximumSize(3000, 1000)

                # 입력 텍스트 박스 설정
                if self.is_input_text_box == True:
                    self.input_box = QLineEdit()
                    self.input_box.setText(self.input_text_default)
                    self.input_box.setFocusPolicy(Qt.StrongFocus)
                    self.input_box.setFocus()  # 창이 나타났을 때 focus 가 다른데 말고 입력 텍스트 박스에 있도록

                if btn_list is not None:
                    self.btns = btn_list

                else:
                    self.btns = [""]
                self.btns_etc = [None] * (len(self.btns) - 3)
                try:
                    # 버튼 설정 / 단축키 설정
                    # f = FONTS.RUBIKDOODLESHADOW_REGULAR_TTF
                    f = F_GMARKETSANSTTFLIGHT_TTF
                    # if self.btns[0]:
                    #     self.btn_positive = QPushButton(f'{self.btns[0]} (F1)')
                    #     self.btn_positive.setStyleSheet("background-color: rgba(0, 0, 0, 0);  color: white;")
                    #     self.btn_positive.clicked.connect(partial(self.update_txt_clicked_and_close, self.btns[0]))
                    #     if os.path.exists(pnx=f):
                    #         self.btn_positive.setFont(Pyside6Util.get_font_for_pyside6(font_path=f))
                    #     # self.set_shortcut(function=partial(self.update_txt_clicked_and_close, self.btns[0]), key_plus_key="alt+y")  # 단축키 설정
                    #     self.set_shortcut(function=partial(self.update_txt_clicked_and_close, self.btns[0]), key_plus_key="F1")  # 단축키 설정
                    # if self.btns[1]:
                    #     self.btn_negative = QPushButton(f'{self.btns[1]} (F2)')
                    #     self.btn_negative.setStyleSheet("background-color: rgba(0, 0, 0, 0);  color: white;")
                    #     self.btn_negative.clicked.connect(partial(self.update_txt_clicked_and_close, self.btns[1]))
                    #     if os.path.exists(pnx=f):
                    #         self.btn_negative.setFont(Pyside6Util.get_font_for_pyside6(font_path=f))
                    #     self.set_shortcut(function=partial(self.update_txt_clicked_and_close, self.btns[1]), key_plus_key="F2")  # 단축키 설정
                    # if self.btns[2]:
                    #     self.btn_third = QPushButton(f'{self.btns[2]} (F3)')
                    #     self.btn_third.setStyleSheet("background-color: rgba(0, 0, 0, 0);  color: white;")
                    #     self.btn_third.clicked.connect(partial(self.update_txt_clicked_and_close, self.btns[2]))
                    #     if os.path.exists(pnx=f):
                    #         self.btn_third.setFont(Pyside6Util.get_font_for_pyside6(font_path=f))
                    #     self.set_shortcut(function=partial(self.update_txt_clicked_and_close, self.btns[2]), key_plus_key="F3")  # 단축키 설정
                    #
                    # for n, item in enumerate(iterable=self.btns[3:]):
                    #     # 여기서 Unexpected type(s): (int, QPushButton | QPushButton) Possible type(s): (SupportsIndex, None) (slice, Iterable[None]) 이 메세지가
                    #     # self.btns_etc[n]  에서 나타났는데  결국 원인을 찾지 못하였고, n 에 대한 노란밑줄을 무시처리했다.
                    #     self.btns_etc[n] = QPushButton(f'{self.btns[3:][n]}')  # noqa
                    #     self.btns_etc[n].setStyleSheet("background-color: rgba(0, 0, 0, 0);  color: white;")  # noqa
                    #     self.btns_etc[n].clicked.connect(partial(self.update_txt_clicked_and_close, self.btns[3:][n]))  # noqa
                    #     self.btns_etc[n].setFont(Pyside6Util.get_font_for_pyside6(font_path=GMARKETSANSTTFLIGHT_TTF))  # noqa
                    if len(self.btns) > 0 and self.btns[0]:
                        self.btn_positive = QPushButton(f'{self.btns[0]} (F1)')
                        self.btn_positive.setStyleSheet("background-color: rgba(0, 0, 0, 0);  color: white;")
                        self.btn_positive.clicked.connect(partial(self.update_txt_clicked_and_close, self.btns[0]))
                        if os.path.exists(f):
                            self.btn_positive.setFont(Pyside6Util.get_font_for_pyside6(font_path=f))
                        self.set_shortcut(function=partial(self.update_txt_clicked_and_close, self.btns[0]),
                                          key_plus_key="F1")  # 단축키 설정

                    if len(self.btns) > 1 and self.btns[1]:
                        self.btn_negative = QPushButton(f'{self.btns[1]} (F2)')
                        self.btn_negative.setStyleSheet("background-color: rgba(0, 0, 0, 0);  color: white;")
                        self.btn_negative.clicked.connect(partial(self.update_txt_clicked_and_close, self.btns[1]))
                        if os.path.exists(f):
                            self.btn_negative.setFont(Pyside6Util.get_font_for_pyside6(font_path=f))
                        self.set_shortcut(function=partial(self.update_txt_clicked_and_close, self.btns[1]),
                                          key_plus_key="F2")  # 단축키 설정

                    if len(self.btns) > 2 and self.btns[2]:
                        self.btn_third = QPushButton(f'{self.btns[2]} (F3)')
                        self.btn_third.setStyleSheet("background-color: rgba(0, 0, 0, 0);  color: white;")
                        self.btn_third.clicked.connect(partial(self.update_txt_clicked_and_close, self.btns[2]))
                        if os.path.exists(f):
                            self.btn_third.setFont(Pyside6Util.get_font_for_pyside6(font_path=f))
                        self.set_shortcut(function=partial(self.update_txt_clicked_and_close, self.btns[2]),
                                          key_plus_key="F3")  # 단축키 설정

                    for n, item in enumerate(self.btns[3:]):
                        self.btns_etc[n] = QPushButton(f'{item}')
                        self.btns_etc[n].setStyleSheet("background-color: rgba(0, 0, 0, 0);  color: white;")
                        self.btns_etc[n].clicked.connect(partial(self.update_txt_clicked_and_close, item))
                        self.btns_etc[n].setFont(
                            Pyside6Util.get_font_for_pyside6(font_path=F_GMARKETSANSTTFLIGHT_TTF))

                except:

                    print_light_black(f"{traceback.format_exc()}")

                # except IndexError:
                #     # btns=[]의 index 를 초과하거나 부족한 경우
                #     pass
                # except TypeError:
                #     # btns=None 인 경우
                #     pass

                # 타이머에 의한 자동 버튼 클릭 설정
                if auto_click_negative_btn_after_seconds is not None:
                    self.seconds_remaining_until_auto_click = auto_click_negative_btn_after_seconds
                    self.is_closing_timer = True
                else:
                    self.is_closing_timer = False
                if auto_click_positive_btn_after_seconds is not None:
                    self.seconds_remaining_until_auto_click = auto_click_positive_btn_after_seconds
                    self.is_starting_timer = True
                else:
                    self.is_starting_timer = False
                # print(rf'self.is_closing_timer : {self.is_closing_timer}')
                # print(rf'auto_closing_seconds : {auto_click_negative_btn_after_seconds}')
                # print(rf'self.is_starting_timer : {self.is_starting_timer}')
                # print(rf'auto_starting_seconds : {auto_click_positive_btn_after_seconds}')
                if self.is_closing_timer == True and self.is_starting_timer == True:
                    print_as_gui("closing_timer 와 starting_timer 는 동시에 설정 할 수 없습니다")
                    return

                if self.is_closing_timer == True or self.is_starting_timer == True:
                    self.auto_choice_timer = QTimer()
                    if auto_click_negative_btn_after_seconds is not None:
                        self.auto_choice_timer.timeout.connect(self.countdown_and_click_negative_btn)  # noqa
                    elif auto_click_positive_btn_after_seconds is not None:
                        self.auto_choice_timer.timeout.connect(self.countdown_and_click_positive_btn)  # noqa
                    self.auto_choice_timer.start(1000)

                # 레이아웃 설정
                self.layout_horizontal = QGridLayout()
                pk_print(working_str=rf'''self.btns="{self.btns}" %%%FOO%%%''')
                pk_print(working_str=rf'''len(self.btns)="{len(self.btns)}" %%%FOO%%%''')
                try:
                    if len(self.btns) > 0 and self.btns[0]:  # btns 리스트의 길이가 0보다 크고, 첫 번째 요소가 True인 경우
                        self.layout_horizontal.addWidget(self.btn_positive, 0, 0)
                    if len(self.btns) > 1 and self.btns[1]:  # btns 리스트의 길이가 1보다 크고, 두 번째 요소가 True인 경우
                        self.layout_horizontal.addWidget(self.btn_negative, 0, 1)
                    if len(self.btns) > 2 and self.btns[2]:  # btns 리스트의 길이가 2보다 크고, 세 번째 요소가 True인 경우
                        self.layout_horizontal.addWidget(self.btn_third, 0, 2)
                    try:
                        for n, item in enumerate(iterable=self.btns_etc):
                            self.layout_horizontal.addWidget(self.btns_etc[n], 0, n + 3)
                    except:
                        print_light_black(f"{traceback.format_exc()}")
                except:
                    print_light_black(f"{traceback.format_exc()}")

                layout_vertical = QVBoxLayout()
                # if len(contents.split("\n")) < 10:
                #     layout_vertical.addWidget(self.label)
                # else:
                layout_vertical.addWidget(self.scroll_area)
                if input_box_mode:
                    layout_vertical.addWidget(self.input_box)
                layout_vertical.addLayout(self.layout_horizontal)
                self.setLayout(layout_vertical)

                self.bring_this_window()
            except:
                print_light_black(f"{traceback.format_exc()}")

        # deprecating test
        # def centerOnScreen(self):
        #     # 현재 화면의 가운데 좌표를 계산
        #     screen_geometry = QScreen().geometry()
        #     x = (screen_geometry.width() - self.width()) // 2
        #     y = (screen_geometry.height() - self.height()) // 2
        #     self.move(x, y)

        def copy_label_text_to_clipboard(self):
            clipboard.copy(self.context)
            f = F_POP_SOUND_POP_SOUND_WAV
            if os.path.exists(f):
                from pk_core import play_wav_f
                play_wav_f(F_POP_SOUND_POP_SOUND_WAV)

        def countdown_and_click_positive_btn(self):
            from pk_core import get_minuites_and_remaining_secs
            mins, secs_remaining = get_minuites_and_remaining_secs(seconds=self.seconds_remaining_until_auto_click)
            if secs_remaining != 0:
                secs_remaining_with_unit = f"{secs_remaining}초"
            else:
                secs_remaining_with_unit = ""
            if mins != 0:
                mins_with_unit = f"{mins}분"
            else:
                mins_with_unit = ""
            self.btn_positive.setText(f"{self.btns[0]} ({mins_with_unit} {secs_remaining_with_unit} 뒤 자동클릭)")

            if self.seconds_remaining_until_auto_click == 0:
                if self.btns[0]:
                    self.update_txt_clicked_and_close(self.btns[0])
            self.seconds_remaining_until_auto_click = self.seconds_remaining_until_auto_click - 1

        def countdown_and_click_negative_btn(self):
            from pk_core import get_minuites_and_remaining_secs
            mins, secs_remaining = get_minuites_and_remaining_secs(seconds=self.seconds_remaining_until_auto_click)
            if secs_remaining != 0:
                secs_remaining_with_unit = f"{secs_remaining}초"
            else:
                secs_remaining_with_unit = ""
            if mins != 0:
                mins_with_unit = f"{mins}분"
            else:
                mins_with_unit = ""
            self.btn_negative.setText(f"{self.btns[1]} ({mins_with_unit} {secs_remaining_with_unit} 뒤 자동클릭)")

            if self.seconds_remaining_until_auto_click == 0:
                if self.btns[1]:
                    self.update_txt_clicked_and_close(self.btns[1])
            self.seconds_remaining_until_auto_click = self.seconds_remaining_until_auto_click - 1

        def bring_this_window(self):
            # self.activateWindow() 와 self.show() 의 위치는 서로 바뀌면 의도된대로 동작을 하지 않는다
            self.show()
            self.activateWindow()
            # active_window = win32gui.GetForegroundWindow()
            # win32gui.SetForegroundWindow(active_window)

    class CustomDialog():
        def __init__(self, q_application: QApplication, q_wiget: QWidget, is_app_instance_mode=False, is_exec_mode=True):
            func_n = inspect.currentframe().f_code.co_name
            pk_print(working_str=rf'''%%%FOO%%%''')
            """
            이 함수는 특별한 사용요구사항이 있습니다
            pyside6 앱 내에서 해당 함수를 호출할때는 is_app_instance_mode 를 파라미터에 넣지 않고 쓰는 것을 default 로 디자인했습니다.
            pyside6 앱 밖에서 해당 함수를 호출할때는 is_app_instance_mode 를 True 로 설정하고 쓰십시오.

            해당 사용요구사항이 생기게 된 이유는 다음과 같습니다
            pyside6 는 app을 singletone으로 instance를 구현합니다. 즉, instance는 반드시 pyside6 app 내에서 하나여야 합니다.
            pyside6의 QApplication()이 앱 내/외에서도 호출이 될 수 있도록 디자인했습니다.
            앱 내에서 호출 시에는 is_app_instance_mode 파라미터를 따로 설정하지 않아도 되도록 디자인되어 있습니다.
            앱 외에서 호출 시에는 is_app_instance_mode 파라미터를 True 로 설정해야 동작하도록 디자인되어 있습니다.
            앱 외에서 호출 시에는 반드시 CustomDialog() 인스턴스로 close()를 호출해 pyside6 app instance 를 종료 해야 합니다.
            """
            # 테스트 해보니, QApplication가 먼저 생성된 뒤에 QDialog 는 instance 가 생성되어야 하는 것같다.
            # 그래서 QDialog instance 를 CustomDialog 생성자의 파라미터로 못받는 것 같다.
            # 다른 Qwiget 을 받을 생각 이었는데...
            # 갑자기 든 생각인데. QApplication 도 같이 넘겨주면 되지 않을까?
            # 된다! 내 생각이 맞은 것 같다. QApplicaion() QDialog() 인스턴스의 생성순서만 바꿨는데 동작하지 않는다. 아무튼 QDialog 를 instance 인자로 받을 수 있다.
            f = F_POP_SOUND_POP_SOUND_WAV
            if os.path.exists(f):
                from pk_core import play_wav_f
                play_wav_f(f=F_POP_SOUND_POP_SOUND_WAV)

            self.is_app_instance_mode = is_app_instance_mode
            if is_app_instance_mode == True:
                self.app_instance = q_application
            # if is_exec_mode == False:
            #     global dialog
            dialog = q_wiget
            if is_exec_mode == True:
                dialog.exec()  # noqa
            self.txt_clicked = dialog.txt_clicked  # noqa

        def close(self):
            if self.is_app_instance_mode == True:
                if isinstance(self.app_instance, QApplication):
                    self.app_instance.exec()
            if self.is_app_instance_mode == True:
                # self.app_instance.quit()  # QApplication 인스턴스 quit 시도 : fail
                self.app_instance.shutdown()  # QApplication 인스턴스 shutdown 시도 : success  # 성공요인은 app.shutdown()이 호출이 되면서 메모리를 해제까지 수행해주기 때문
                # del self.app_instance  # QApplication 인스턴스 del 시도 : fail
                # self.app_instance.deleteLater()  # QApplication delete later 시도 : fail
                # self.app_instance = None  # QApplication 인스턴스 None 시도 : fail
                # sys.exit()

    class RpaProgramMainWindow(QWidget):

        # class RpaProgramMainWindow(QDialog):
        # class RpaProgramMainWindow(QMainWindow):
        # def __init__(self, shared_obj): # shared_obj 는 창간 통신용 공유객체 이다. pyside6 app 의 상태관리
        def __init__(self, q_application):

            func_n = inspect.currentframe().f_code.co_name
            pk_print(working_str=rf'''%%%FOO%%%''')

            f = F_POP_SOUND_POP_SOUND_WAV
            if os.path.exists(f):
                from pk_core import play_wav_f
                play_wav_f(f=f)
            super().__init__()
            self.app = q_application

            # deprecated test started at 2023 12 23 01 28
            # self.prompt_window = None
            # self.sub_window = None
            # self.question = None

            #  앱 전역 변수 설정
            self.text = "text"
            self.pw = "`"
            self.id = "`"
            # self.is_window_maximized = False
            self.display_width = get_display_info()['width'],
            self.display_height = get_display_info()['height'],
            # self.display_width_default = int(int(self.display_width[0]) * 0.106)
            # self.display_width_default = int(int(self.display_width[0]) * 0.045)
            # self.display_width_default = int(int(self.display_width[0]) * 0.02)
            self.display_width_default = int(int(self.display_width[0]) * 0.01)
            self.display_height_default = int(int(self.display_height[0]) * 0.2)

            #  메인창 설정
            self.setWindowTitle('.')
            icon_png = rf"{D_PROJECT}\pkg_png\icon.PNG"
            self.setWindowIcon(QIcon(icon_png))  # 메인창 아이콘 설정
            # self.setAttribute(Qt.WA_TranslucentBackground) # 메인창 블러 설정
            # self.setWindowFlags(Qt.WindowType.FramelessWindowHint) # 메인창 최상단 프레임레스 설정
            GlobalBlur(self.winId(), hexColor=False, Acrylic=False, Dark=True, QWidget=self)
            self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint)  # 최대화 최소화 버튼 숨기기
            self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 모든 창 앞에 위치하도록 설정
            self.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
            # self.setStyleSheet(pyqt6css.qss)
            # self.setAttribute(Qt.WA_TranslucentBackground)
            # blur(self.winId())
            # self.scale = 1/1
            # self.scale = 1/2
            # self.scale = 1/3
            # self.scale = 1 / 4
            # self.scale = 1 / 10
            # self.setGeometry(0, 0, int(self.display_width_default * self.scale), int(self.display_height_default * self.scale))
            # self.setGeometry(0, 0,self.display_width_default, self.display_height_default)
            # self.resize(self.display_width_default, self.display_height_default)

            # self.setGeometry(0, 0, int(self.display_width_default * self.scale), int(self.display_height[0]))
            self.windows_size_mode = 1  # 창크기 모드 설정  #0 ~ 3
            QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # 고해상도 스케일링을 활성화합니다.
            self.screens = QGuiApplication.screens()  # 사용 가능한 모든 화면을 가져옵니다.

            # inputbox 설정
            # self.inputbox = QLineEdit(self)
            # self.inputbox.setStyleSheet("color: rgba(255,255,255, 0.9);")
            # self.inputbox.setText("0,0")
            # self.inputbox.setFixedWidth(120)
            # # self.inputbox.setStyleSheet("text-shadow: 1px 1px 7px rgba(1, 1, 1, 1);") #텍스트에 그림자 넣고 싶었는데 안된다.
            # self.inputbox.textChanged.connect(self.inputbox_changed)
            # self.inputbox.editingFinished.connect(self.inputbox_edit_finished)
            # self.inputbox.returnPressed.connect(self.inputbox_return_pressed)

            # 이벤트 가 많으면 프로그램이 늦어지는 것 같아보였다

            # monitor_mouse_position 이벤트 설정
            # self.listener = pynput.mouse.Listener(on_move=self.monitor_mouse_position) # 아주 빠르게 마우스 움직임 감지
            # self.listener.start()

            # monitor_mouse_position_per_second 이벤트 설정 (마우스 멈춤 감지 이벤트/ 5초간 마우스 중지 시 메인화면 자동 숨김 이벤트)
            self.mouse_positions = []
            self.previous_position = None
            self.current_position = None
            self.timer = QTimer()
            self.timer.timeout.connect(self.monitor_mouse_position_per_second)  # noqa
            self.timer.start(1000)

            # mkr_단축키 설정
            self.available_shortcut_list = {
                # 버튼있는 SHORCUT #단축키 설정 #CODE RELATIONAL AREA 1/5
                'HIDE': 'Esc',  # GHOST MODE?
                'EXIT': 'Q',
                'BACK UP TARGET': 'S',
                'ASK AI QUESTION': 'A',
                'SHOOT SCREENSHOT FULL': 'F',
                'SHOOT SCREENSHOT CUSTOM': 'C',
                'SHOOT SCREENSHOT FOR RPA': '4',
                'ANI': '5',  # nyaa.si
                'EXPLORER': 'O',
                'SYNC SERVICES': '`',
                'TEST': '1',
                'BACKUP SERVICES': '2',  # BACK UP TARGET 인데, 버튼 지우게 되면 이걸로
                'PROJECT DIRECTORY': 'P',
                "CLASSIFY SPECIAL FILES": "F2",
                "GATHER EMPTY DIRECTORY": "F3",
                "GATHER SPECIAL FILES": "F4",
                "GATHER USELESS FILES": "F5",
                "MERGE DIRECTORIES": "F6",
                "CONVERT MKV TO WAV": "F7",
                'DOWNLOAD YOUTUBE(webm)': 'F8',
                'DOWNLOAD YOUTUBE(webm)_': 'F9',
                'DOWNLOAD VIDEO FROM WEB1': 'Alt+F1',
                'DOWNLOAD VIDEO FROM WEB2': 'Alt+F2',
                'ROTATE WINDOW MODE': 'Alt+W',
                'SYSTEM REBOOT': 'Alt+9',
                'SYSTEM SHUTDOWN': 'Alt+]',
                'SYSTEM POWER SAVING MODE': 'Alt+[',
                # 'LOGIN': 'Alt+F7',
                'EMPTY RECYCLE BIN': 'Alt+E',
                # 'RUN CMD.EXE AS ADMIN': 'Alt+C',
                'NAVER MAP': 'Alt+N',
                # 'WEB CRAWL HREF': "`+F1", # fail
                'WEB CRAWL HREF': "Ctrl+F1",
                'WEB CRAWL YOUTUBE VIDEO TITLE AND URL': "Ctrl+F2",
                'WEB CRAWL YOUTUBE VIDEO PLAYLIST': "Ctrl+F3",
                'rdp-82106': 'R+1',
                # 'DOWNLOAD YOUTUBE(wav)': 'S',
                # 'DOWNLOAD YOUTUBE(webm) ONLY SOUND': 'Alt+S',

            }

            # 버튼없는 SHORCUT #단축키 설정 #shortcut #mkr2024
            self.set_shortcut('TEST', self.should_i_start_test)
            self.set_shortcut('BACK UP TARGET', self.should_i_back_up_target)

            # 버튼있는 버튼
            # self.btn_to_open_PROJECT_D = self.get_btn(self.get_btn_name_promised('PROJECT DIRECTORY'), self.open_PROJECT_D)

            # 버튼있는 단축키
            # self.btn_to_open_PROJECT_D_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('PROJECT DIRECTORY'), function=self.open_PROJECT_D)
            # self.btn_to_back_up_target_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('BACK UP TARGET'), function=self.should_i_back_up_target)

            print(f'{UNDERLINE}단축키')
            temp = ''
            for key in self.available_shortcut_list:
                value = self.available_shortcut_list[key]
                print(f'{value}         {key}')
                temp = temp + '\n' + f'{value}         {key}'

            # 레이블로 설정
            html = f"<html><body><h1 style='color: white;'>{temp}</h1></body></html>"
            text_browser = QTextBrowser()
            text_browser.setHtml(html)
            text_browser.resize(800, 600)

            text_browser2 = QTextBrowser()
            text_browser2.setHtml(html)
            text_browser2.resize(800, 600)

            text_browser3 = QTextBrowser()
            text_browser3.setHtml(html)
            text_browser3.resize(800, 600)

            text_browser4 = QTextBrowser()
            text_browser4.setHtml(html)
            # text_browser4.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: white;")  # 메시지박스창 스타일시트 적용 설정
            text_browser4.resize(800, 600)

            # btns 설정 5/5
            btns = [
                # [text_browser, text_browser2],  # BLANK #여백
                # [text_browser3, text_browser4], #BLANK #여백
                # [self.btn_to_should_i_exit_this_program, self.btn_to_should_i_exit_this_program_only_shortcut_name],
                # [self.btn_to_toogle_rpa_window, self.btn_to_toogle_rpa_window_only_shorcut_name],
                # [self.btn_to_rotate_window_size_mode, self.btn_to_rotate_window_size_mode_only_shortcut_name],
                # [self.btn_to_should_i_empty_trash_can, self.btn_to_should_i_empty_trash_can_only_shortcut_name],
                # [self.btn_to_should_i_enter_to_power_saving_mode, self.btn_to_should_i_enter_to_power_saving_mode_only_shortcut_name],
                # [self.btn_to_classify_special_files, self.btn_to_classify_special_files_only_shortcut_name],
                # [self.btn_to_gather_empty_directory, self.btn_to_gather_empty_directory_only_shortcut_name],
                # [self.btn_to_merge_directories, self.btn_to_merge_directories_only_shortcut_name],
            ]

            # GRID SETTING
            grid = QtWidgets.QGridLayout(self)

            # GRID COORDINATION REFERENCE (ROW, COLUMN)
            #        0,0  0,1  0,2
            #        1,0  1,1  1,2
            #        2,0  2,1  2,2

            # spaver

            # GRID_COLUMN 1 폭 조절용 policy
            # size_policy = QSizePolicy()
            # grid.setHorizontalPolicy(QSizePolicy.Minimum)  # 그리드의 열의 폭을 최소로 설정합니다.
            grid.setVerticalSpacing(9)
            grid.setHorizontalSpacing(5)
            grid.setColumnMinimumWidth(1, 125)
            grid.setColumnMinimumWidth(2, 45)

            btns_grid = btns
            line_no = 0
            for btn in btns_grid:
                grid.addWidget(btn[0], line_no, 0)  # GRID_COLUMN 0 설정
                grid.addWidget(btn[1], line_no, 2)  # GRID_COLUMN 1 설정
                line_no = line_no + 1

            # 화면exec 
            def do_once():
                self.rotate_window_size_mode()
                self.timer2.stop()

            self.timer2 = QTimer()
            self.timer2.timeout.connect(do_once)  # noqa
            # self.timer2.start(500)
            self.timer2.start(50)

            # TEST
            # self.inputbox = QPlainTextEdit(self)
            # self.inputbox = QTextEdit(self)
            # self.ta1 = QTableWidget(self)
            # self.ta1.resize(500, 500)
            # self.ta1.setColumnCount(3)
            # self.ta1.setStyleSheet("color: rgba(255,255,255, 0.9);")
            # self.ta1.setStyleSheet("background-color: rgba(255,255,255, 0.9);")
            # table_column = ["첫번째 열", "두번째 열", "Third 열"]
            # self.ta1.setHorizontalHeaderLabels(table_column)

            # # 행 2개 추가
            # self.ta1.setRowCount(2)

            # # 추가된 행에 데이터 채워넣음
            # self.ta1.setItem(0, 0, QTableWidgetItem("(0,0)"))
            # self.ta1.setItem(0, 1, QTableWidgetItem("(0,1)"))
            # self.ta1.setItem(1, 0, QTableWidgetItem("(1,0)"))
            # self.ta1.setItem(1, 1, QTableWidgetItem("(1,1)"))

            # 마지막에 행 1개추가
            # self.ta1.insertRow(2)
            # self.ta1.setItem(2, 0, QTableWidgetItem("New Data"))

            # 셀의 텍스트 변경
            # self.ta1.item(1, 1).setText("데이터 변경")

            # 셀에 있는 텍스트 출력
            # print(self.ta1.item(0, 1).text())

            # 테이블 데이터 전부 삭제
            # self.ta1.clear()

            # 테이블 행전부 삭제
            # self.ta1.setRowCount(0)

            self.scroll_area = QScrollArea()
            self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            self.scroll_area.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
            self.scroll_area.setStyleSheet(f" border: none; width: {self.display_width_default}px; height: {self.display_height_default}px")
            self.scroll_area.setLayout(grid)

            # 레이아웃 설정
            layout = QVBoxLayout(self)
            layout.addWidget(self.scroll_area)

            self.setMouseTracking(True)  # pyside6 창 밖에서도 마우스 추적 가능 설정 # 마우스 움직임 이벤트 감지 허용 설정
            # self.toogle_rpa_window()
            # press("alt", "w")

            self.move_pyside6_window_to_front()

            self.txt_clicked = "foo"

            # self.event_loop = QEventLoop()
            # self.event_loop.exec()

            # self.exec()

        def monitor_mouse_position_per_second(self):

            """마우스 움직임 감지 함수"""
            x, y = pyautogui.position()  # 현재 마우스 위치 ( 이게 내가 원하던 수치 )
            # print(x, y)
            self.current_position = QCursor.pos()  # 현재 마우스 커서 위치 ( 이건 내가 원하는 수치는 아닌데... 뭘 의미하는 거지? )
            # print(self.current_position)
            if self.previous_position is not None and self.previous_position == self.current_position:
                # print("마우스가 멈췄습니다")
                # print(f"self.mouse_positions : {self.mouse_positions}") # 마우스 위치 리스트
                if 10 <= len(self.mouse_positions):
                    # 10번 연속 mouse 중지 감지
                    # self.mouse_positions 에 등록된 모든 self.current_position 가 동일하면 10번 연속으로 움직이지 않은 것으로 판단
                    if len(self.mouse_positions) == 10:
                        # 동일한 10개 원소를 갖는 리스트 내에서 요소의 중복을 제거하면 중복이 제거된 리스트의 요소의 수는 1개가 나올 것을 기대
                        mouse_positions_removed_duplicatd_elements = list(set(self.mouse_positions))  # orderless way
                        if len(mouse_positions_removed_duplicatd_elements) == 1:
                            # print("10번 연속 중지 감지")
                            self.hide()
                            pass

                if 5 <= len(self.mouse_positions):
                    self.mouse_positions = []  # 감지값들이 5개 이상이면 감지값목록 초기화

                elif len(self.mouse_positions) < 5:
                    self.mouse_positions.append(self.current_position)
                pass
            else:
                pass
                # print("마우스가 움직였습니다")

                # mkr_우측하단 꼭지점 부근 네비게이션
                # if 3440 - 25 <= x and 1440 - 25 <= y:
                #     press("win", "d", interval=0.15)

                # 우측 네비게이션
                # if 3440 - 50 <= x <= 3440 and 300 <= y <= 1440:
                #     try:
                #         open_pnx(PYCHARM64_EXE)
                #     except:
                #         print_light_black(f"{traceback.format_exc()}")
                #         pass

                # 좌측 네비게이션
                # elif 0 <= x <= 15 and 0 <= y <= 1440:
                #     self.toogle_rpa_window()
                #     pass

                # else:
                #     pass
            self.previous_position = self.current_position

        def monitor_mouse_position(self, x, y):
            # 상단 네비게이션
            if 0 <= x <= 3440 and 0 <= y <= 25:
                pass
            else:
                pass

        @staticmethod
        # def rpa_program_method_decorator(function):
        def rpa_program_method_decorator(function: Callable[[T], None]):
            def wrapper(self):
                f = F_POP_SOUND_POP_SOUND_WAV
                if os.path.exists(f):
                    from pk_core import play_wav_f
                    play_wav_f(f=f)
                self.hide()  # 비동기 전까지는 사용자가 다른 명령을 하지 못하도록 이 코드를 사용
                function(self)
                self.move_pyside6_window_to_front()

            return wrapper

        def eventFilter(self, obj, event):
            # if event.type() == QEvent.MouseMove:
            #     x = event.globalX()
            #     y = event.globalY()
            #     print(f"마우스 이동 - X: {x}, Y: {y}")
            # return super().eventFilter(obj, event)
            if event.type() == QEvent.MouseButtonPress and not self.rect().contains(event.pos()):
                print("pyside6 창 외부 클릭 되었습니다")
            return super().eventFilter(obj, event)

        def mousePressEvent(self, e):
            if e.button() == Qt.LeftButton:  # 왼쪽 버튼 클릭 시 동작
                # print(f"mouse press event monitor: LeftButton pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
                pass
            elif e.button() == Qt.RightButton:
                print(f"mouse press event monitor: RightButton pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.BackButton:
                print(f"mouse press event monitor: BackButton pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton1:
                print(f"mouse press event monitor: ExtraButton1 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton10:
                print(f"mouse press event monitor: ExtraButton10 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton11:
                print(f"mouse press event monitor: ExtraButton11 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton12:
                print(f"mouse press event monitor: ExtraButton12 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton13:
                print(f"mouse press event monitor: ExtraButton13 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton14:
                print(f"mouse press event monitor: ExtraButton14 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton15:
                print(f"mouse press event monitor: ExtraButton15 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton16:
                print(f"mouse press event monitor: ExtraButton16 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton17:
                print(f"mouse press event monitor: ExtraButton17 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton18:
                print(f"mouse press event monitor: ExtraButton18 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton19:
                print(f"mouse press event monitor: ExtraButton19 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton2:
                print(f"mouse press event monitor: ExtraButton2 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton20:
                print(f"mouse press event monitor: ExtraButton20 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton21:
                print(f"mouse press event monitor: ExtraButton21 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton22:
                print(f"mouse press event monitor: ExtraButton22 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton23:
                print(f"mouse press event monitor: ExtraButton23 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton24:
                print(f"mouse press event monitor: ExtraButton24 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton3:
                print(f"mouse press event monitor: ExtraButton3 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton4:
                print(f"mouse press event monitor: ExtraButton4 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton5:
                print(f"mouse press event monitor: ExtraButton5 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton6:
                print(f"mouse press event monitor: ExtraButton6 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton7:
                print(f"mouse press event monitor: ExtraButton7 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton8:
                print(f"mouse press event monitor: ExtraButton8 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton9:
                print(f"mouse press event monitor: ExtraButton9 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ForwardButton:
                print(f"mouse press event monitor: ForwardButton pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.LeftButton:
                print(f"mouse press event monitor: LeftButton pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.MiddleButton:
                print(f"mouse press event monitor: MiddleButton pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.NoButton:
                print(f"mouse press event monitor: NoButton pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.TaskButton:
                print(f"mouse press event monitor: TaskButton pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.XButton1:
                print(f"mouse press event monitor: XButton1 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.XButton2:
                print(f"mouse press event monitor: XButton2 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")

        # def mouseReleaseEvent(self, e):
        #     self.label10.setText(f"event monitor:\nmouseReleaseEvent : {str(e.pos().x())} ,{str(e.pos().y())} ")
        #
        # def mouseDoubleClickEvent(self, e):
        #     self.label10.setText(f"event monitor:\nmouseDoubleClickEvent : {str(e.pos().x())} ,{str(e.pos().y())} ")

        def keyPressEvent(self, e):
            self.mouse_positions = []  # 키보드가 눌리면 사용자가 사용중인 것으로 간주하고 마우스 위치 값 목록 초기화

        # def keyPressEvent(self, e):
        #     # these keys refered from https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html
        #     # 테스트 결과 한/영, 한자 인식안됨.
        #     if e.key() == Qt.Key_Return:
        #         self.label11.setText(f"keyboard event monitor:\nKey_Return : Key_Return ")
        #         self.showMinimized()
        #         press("space")
        #         self.showMaximized()
        #     elif e.key() == Qt.Key_0:
        #         self.label11.setText(f"keyboard event monitor:\nKey_0 : Key_0 ")
        # deprecated test
        # def inputbox_changed(self):
        #     pk_print("inputbox 텍스트 change event 감지 되었습니다")
        #     print(self.inputbox.ment())
        #
        # def inputbox_edit_finished(self):
        #     pk_print("inputbox edit finish event 감지 되었습니다")
        #
        # def inputbox_return_pressed(self):
        #     pk_print("inputbox return pressed event 감지 되었습니다")

        def get_btn_name_with_shortcut_name(self, button_name_without_shortcut):
            # 버튼명과 shourtcut 명을 을 적당한 간격으로 띄워서 string 으로 반환하는 코드, 폰트 가 고정폭폰트 가 아니면 무용지물인 함수
            numbers = []
            for key, value in self.available_shortcut_list.items():
                numbers.append(len(value) + len(key))
            max_len_value = max(numbers)
            button_name_with_short_cut = ""
            for key, value in self.available_shortcut_list.items():
                if key == button_name_without_shortcut:
                    space_between = " " * (max_len_value - len(key) - len(value) + 1)
                    # space_between = "\t"
                    # button_name_with_short_cut = button_name_with_short_cut + f"{key}{space_between}{value}".strip()
                    # button_name_with_short_cut = button_name_with_short_cut + f"{key}{space_between}( {value} )".strip()
                    button_name_with_short_cut = button_name_with_short_cut + f"{value}{space_between}( {key} )".strip()
            print(button_name_with_short_cut)
            return button_name_with_short_cut

        def get_btn_name_promised(self, button_name_without_shortcut):
            button_name_with_short_cut = ""
            for key, value in self.available_shortcut_list.items():
                if key == button_name_without_shortcut:
                    button_name_with_short_cut = button_name_with_short_cut + f"{key}".strip()
            return button_name_with_short_cut

        def get_shortcut_name_promised(self, button_name_without_shortcut):
            button_name_with_short_cut = ""
            for key, value in self.available_shortcut_list.items():
                if key == button_name_without_shortcut:
                    button_name_with_short_cut = button_name_with_short_cut + f"{value}".strip()
            return button_name_with_short_cut

        # def show_available_shortcut_list(self):
        #     # global max
        #     # global 을 설정하면, 이 변수는 함수의 exec 이 끝난 다음에도 없어지지 않는다.
        #     # 이 값을 나중에 함수 끝나고도 또 쓸려면 이렇게 쓰면 되겠다. @staticmethod 의 경우에는 변수 간의 값에 간섭이 되지 않도록 굳이 쓰지 않는 것이 좋겠다.
        #     # global 많이 쓰면 이는 변수가 전역화 되니까 메모리의 성능이 저하되는 것이 아닐까?
        #     # 그렇다면 함수 내에서만 전역적으로 변수를 쓰는 경우에, global 을 쓰지 않는 것이 성능을 위해서는 좋은 선택이겠다. 굳이 함수가 끝난 뒤에 밖에서 써야한다면 global 을 써야 겠지만, 나는 무척이나 이게 헷갈릴 것 같다
        #     # 그동안의 경험으로는 코드 맥락 상, global 선언을 하지 않아도 전역변수 처럼 작동 되는 것 같아 보인다.... 아니다 이게 global max 를 선언하지 않았다고 가정하면 max 는 show_available_shortcut_list() 가 종료되면 max 는 사라진다. 그런데 global max를 선언하면 max 는 유지된다!
        #     # 혹시 객체의 인스턴스 같은 것을 global 을 통해서 변수에 저장하고 쓰면 싱글톤 처럼 쓸 수 있는 것일까? 메모리 효율은 많이 나빠질까?
        #
        #     numbers = []
        #     for key_shortcut, value in self.available_shortcut_list.items():
        #         numbers.append(len(value))
        #     max_no: int
        #     max_no = max(numbers)
        #     for key_shortcut, value in self.available_shortcut_list.items():
        #         print(f"{{0: <{max_no}}} : {key_shortcut}".format(value))

        def rotate_window_size_mode(self):
            if self.windows_size_mode == 0:
                self.resize(self.display_width_default, self.display_height_default)
                self.move_window_to_center()  # 불필요 하면 주석하는 게 나쁘지 않겠다
                self.windows_size_mode = self.windows_size_mode + 1
            elif self.windows_size_mode == 1:
                self.setGeometry(0, 0, int(self.display_width_default), int(self.display_height[0]))
                # self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 모든 창 앞에 위치하도록 설정
                self.windows_size_mode = self.windows_size_mode + 1
            elif self.windows_size_mode == 2:
                self.showMaximized()
                self.windows_size_mode = self.windows_size_mode + 1
            elif self.windows_size_mode == 3:
                self.setGeometry(1600 - int(self.display_width_default), 0, int(self.display_width_default), int(self.display_height[0]))
                self.windows_size_mode = 0

        def set_shortcut(self, shortcut_key_promised, function):
            # self.shortcut = QShortcut(QKeySequence(self.available_shortcut_list[btn_name_promised]), self)  # ctrl+1 2개 키들의 조합 설정
            self.shortcut = QShortcut(self.available_shortcut_list[shortcut_key_promised], self)  # ctrl+n+d 3개 키들의 조합 설정 시도
            self.shortcut.activated.connect(function)
            pass

        def get_btn(self, btn_name, function, btn_text_align="left"):
            button = QPushButton(btn_name, self)  # alt f4 로 가이드 해도 되겠다. 이건 그냥 설정 되어 있는 부분.
            button.clicked.connect(function)

            # 2023년 12월 14일 (목) 16:28:15
            # 결론, fixed width font로 시도해볼 수 있다 자릿 수를 맞출 수 있다.
            # non-fixed width font 이슈 JAVA 에서도 구현했을 때 마딱드렸던 내용인데,
            # 분명히 문장 전체 길이를 단어 사이의 공백의 수를 결정짓는 함수를 테스트 했음에도 자릿수가 맞지 않았는데
            # 이는 고정 폭이 아님이기 때문이었다 따라서 고정 폭 폰트로 출력되는 콘솔에서는 정상, 비고정 폭 폰트로 출력되는 콘솔에서는 비정상,
            # 이 경우에는 콘솔이 아니라 pyside6 로 만든 UI 에서 나타났다.
            # 새벽에 이 문제를 만나서 잠깐 넋나갔는데 아침에 다시보니 그때 경험이 떠올라서 실험해보니 잘 해결되었다. 덕분에 pyside6에서 위젯에 폰트 적용하는 법도 터득

            # pyside6 버튼 내장폰트 설정
            # pyside6 built in fixed width font
            # font = QFont("Monospace")
            # font = QFont("Ubuntu Mono")
            # font = QFont("Inconsolata")
            # font = QFont("Monaco")
            # font = QFont("Courier")
            # font = QFont("Courier 10 Pitch")
            # font = QFont("Courier Prime")
            # font = QFont("Droid Sans Mono")
            # font = QFont("Fira Mono")
            # font = QFont("Hack")
            # font = QFont("Menlo")
            # font = QFont("Monofur")
            # font = QFont("Noto Mono")
            # font = QFont("PT Mono")
            # font = QFont("Roboto Mono")
            # font = QFont("Source Code Pro")
            # font = QFont("Victor Mono")
            # font = QFont("Courier New")
            # font = QFont("Liberation Mono")
            # font = QFont("DejaVu Sans Mono")
            # font = QFont("Consolas")  # 그나마 가장 마음에 드는 폰트

            # pyside6 버튼 외부폰트 설정
            button.setFont(Pyside6Util.get_font_for_pyside6(font_path=F_GMARKETSANSTTFLIGHT_TTF))
            if btn_text_align == "right":
                # button.setStyleSheet("QPushButton { text-align: right; color: rgba(255,255,255, 0.9); height: 20px; font-size: 8px}")
                # button.setStyleSheet("QPushButton { text-align: right; color: rgba(255,255,255, 0.9);               font-size: 8px}")
                button.setStyleSheet("QPushButton { text-align: right; color: rgba(255,255,255, 0.9);               font-size: 13px}")
                # button.setStyleSheet("QPushButton { text-align: right; color: rgba(255,255,255, 0.9); height: 20px; font-size: 13px}")
                button.setFixedWidth(65)
                # button.setMinimumWidth(button.sizeHint().width())
            else:
                # button.setStyleSheet("QPushButton { text-align: left; color: rgba(255,255,255, 0.9); height: 20px; font-size: 8px}")
                # button.setStyleSheet("QPushButton { text-align: left; color: rgba(255,255,255, 0.9);                 font-size: 8px}")
                button.setStyleSheet("QPushButton { text-align: left; color: rgba(255,255,255, 0.9);                 font-size: 13px}")
                # button.setStyleSheet("QPushButton { text-align: left; color: rgba(255,255,255, 0.9); height: 20px; font-size: 13px}")
                button.setFixedWidth(225)
                # button.setMinimumWidth(button.sizeHint().width())
            return button

        def move_window_to_center(self):
            center = QScreen.availableGeometry(self.app.primaryScreen()).center()
            geo = self.frameGeometry()
            geo.moveCenter(center)
            self.move(geo.topLeft())
            # if self.screens:
            #     primary_screen = self.screens[0]  # 첫 번째 화면을 기본 화면으로 설정합니다.
            #     center = primary_screen.availableGeometry().center()  # 기본 화면의 중앙 좌표를 가져옵니다.
            #     # 화면을 가운데로 이동시키는 코드를 작성하세요.
            #     # 예시로 윈도우를 생성하고 중앙 좌표를 이용하여 위치를 설정합니다.
            #     self.setGeometry(100, 100, 500, 300)  # 윈도우의 초기 위치와 크기를 설정합니다.
            #     self.move(center - self.rect().center())  # 윈도우를 화면 중앙으로 이동시킵니다.

        # @rpa_program_method_decorator
        # def run_no_paste_memo(self):
        #     speak_that_service_is_in_preparing()

        # @rpa_program_method_decorator
        # def should_i_reboot_this_computer(self):
        #     func_n = inspect.currentframe().f_code.co_name
        #     pk_print(str_working=rf'''%%%FOO%%%''')
        #     should_i_reboot_this_computer()

        # @QtCore.Slot()
        # def login(self):
        #     speak_that_service_is_in_preparing()

        # @rpa_program_method_decorator
        # def should_i_show_animation_information_from_web(self):
        #     func_n = inspect.currentframe().f_code.co_name
        #     pk_print(str_working=rf'''%%%FOO%%%''')
        #     should_i_show_animation_information_from_web()

        # @rpa_program_method_decorator
        # def should_i_exit_this_program(self):
        #     func_n = inspect.currentframe().f_code.co_name
        #     pk_print(str_working=rf'''%%%FOO%%%''')
        #     should_i_exit_this_program()

        # @rpa_program_method_decorator
        # def should_i_find_direction_via_naver_map(self):
        #     func_n = inspect.currentframe().f_code.co_name
        #     pk_print(str_working=rf'''%%%FOO%%%''')
        #     should_i_find_direction_via_naver_map()

        # @rpa_program_method_decorator
        # def download_youtube_as_wav(self):
        #     speak_that_service_is_in_preparing()

        # @rpa_program_method_decorator
        # def should_i_download_youtube_as_webm(self):
        #     func_n = inspect.currentframe().f_code.co_name
        #     pk_print(str_working=rf'''%%%FOO%%%''')
        #     should_i_download_youtube_as_webm()

        # @rpa_program_method_decorator
        # def should_i_download_youtube_as_webm_alt(self):
        #     func_n = inspect.currentframe().f_code.co_name
        #     pk_print(str_working=rf'''%%%FOO%%%''')
        #     should_i_download_youtube_as_webm_alt()

        # @rpa_program_method_decorator
        # def download_youtube_as_webm_only_sound(self):
        #     speak_that_service_is_in_preparing()
        # 
        # # @rpa_program_method_decorator
        # # def should_i_shutdown_this_computer(self):
        # #     func_n = inspect.currentframe().f_code.co_name
        # #     pk_print(str_working=rf'''%%%FOO%%%''')
        # #     should_i_shutdown_this_computer()
        # 
        # @rpa_program_method_decorator
        # def shoot_screenshot_custom(self):
        #     while 1:
        #         asyncio.run(shoot_custom_screenshot_via_asyncio())
        #         break
        # 
        # @rpa_program_method_decorator
        # def shoot_screenshot_full(self):
        #     while 1:
        #         collect_img_for_autogui()
        #         break
        # 
        # # @rpa_program_method_decorator
        # # def should_i_back_up_target(self):
        # #     func_n = inspect.currentframe().f_code.co_name
        # #     pk_print(str_working=rf'''%%%FOO%%%''')
        # #     should_i_back_up_target()
        # 
        # # @rpa_program_method_decorator
        # # def should_i_start_test(self):
        # #     func_n = inspect.currentframe().f_code.co_name
        # #     pk_print(str_working=rf'''%%%FOO%%%''')
        # #     should_i_start_test_core()
        # 
        # @rpa_program_method_decorator
        # def open_PROJECT_D(self):
        #     PROJECT_D = str(PROJECT_D)
        #     open_pnx(pnx=PROJECT_D, debug_mode=True)

        # @rpa_program_method_decorator
        # def should_i_enter_to_power_saving_mode(self):
        #     func_n = inspect.currentframe().f_code.co_name
        #     pk_print(str_working=rf'''%%%FOO%%%''')
        #     should_i_enter_to_power_saving_mode()
        #
        # @rpa_program_method_decorator
        # def should_i_translate_eng_to_kor(self):
        #     func_n = inspect.currentframe().f_code.co_name
        #     pk_print(str_working=rf'''%%%FOO%%%''')
        #     should_i_translate_eng_to_kor()
        #
        # @rpa_program_method_decorator
        # def should_i_translate_kor_to_eng(self):
        #     func_n = inspect.currentframe().f_code.co_name
        #     pk_print(str_working=rf'''%%%FOO%%%''')
        #     should_i_translate_kor_to_eng()

        # @rpa_program_method_decorator
        # def should_i_empty_trash_can(self):
        #     func_n = inspect.currentframe().f_code.co_name
        #     pk_print(str_working=rf'''%%%FOO%%%''')
        #     should_i_do(string="쓰레기통을 비울까요?", function=empty_recycle_bin, auto_click_negative_btn_after_seconds=10)

        # @rpa_program_method_decorator
        # def run_cmd_exe_as_admin(self):
        #     run_cmd_exe_as_admin()
        # 
        # @rpa_program_method_decorator
        # def ask_something_to_ai(self):
        #     ask_something_to_ai()
        # 
        # # @rpa_program_method_decorator
        # # def should_i_connect_to_rdp1(self):
        # #     func_n = inspect.currentframe().f_code.co_name
        # #     pk_print(str_working=rf'''%%%FOO%%%''')
        # #     mstsc()
        # #
        # # @rpa_program_method_decorator
        # # def should_i_record_macro(self):
        # #     func_n = inspect.currentframe().f_code.co_name
        # #     pk_print(str_working=rf'''%%%FOO%%%''')
        # #     should_i_record_macro()
        # #
        # # @rpa_program_method_decorator
        # # def should_i_classify_special_files(self):
        # #     func_n = inspect.currentframe().f_code.co_name
        # #     pk_print(str_working=rf'''%%%FOO%%%''')
        # #     should_i_classify_special_files()
        # #
        # # @rpa_program_method_decorator
        # # def should_i_gather_empty_directory(self):
        # #     func_n = inspect.currentframe().f_code.co_name
        # #     pk_print(str_working=rf'''%%%FOO%%%''')
        # #     should_i_gather_empty_directory()
        # 
        # # @rpa_program_method_decorator
        # # def should_i_gather_useless_files(self):
        # #     func_n = inspect.currentframe().f_code.co_name
        # #     pk_print(str_working=rf'''%%%FOO%%%''')
        # #     should_i_gather_pnxs_useless()
        # 
        # # @rpa_program_method_decorator
        # # def should_i_merge_directories(self):
        # #     func_n = inspect.currentframe().f_code.co_name
        # #     pk_print(str_working=rf'''%%%FOO%%%''')
        # #     should_i_merge_directories()
        # #
        # # @rpa_program_method_decorator
        # # def should_i_convert_mkv_to_wav(self):
        # #     func_n = inspect.currentframe().f_code.co_name
        # #     pk_print(str_working=rf'''%%%FOO%%%''')
        # #     should_i_convert_mkv_to_wav()
        # 
        # @rpa_program_method_decorator
        # def should_i_crawl_a_tag_href(self):
        #     func_n = inspect.currentframe().f_code.co_name
        #     pk_print(str_working=rf'''%%%FOO%%%''')
        #     should_i_crawl_a_tag_href()
        # 
        # @rpa_program_method_decorator
        # def should_i_crawl_youtube_video_title_and_url(self):
        #     func_n = inspect.currentframe().f_code.co_name
        #     pk_print(str_working=rf'''%%%FOO%%%''')
        #     should_i_crawl_youtube_video_title_and_url()
        # 
        # @rpa_program_method_decorator
        # def should_i_crawl_youtube_playlist(self):
        #     func_n = inspect.currentframe().f_code.co_name
        #     pk_print(str_working=rf'''%%%FOO%%%''')
        #     should_i_crawl_youtube_playlist()
        # 
        # @rpa_program_method_decorator
        # def should_i_explorer(self):
        #     func_n = inspect.currentframe().f_code.co_name
        #     pk_print(str_working=rf'''%%%FOO%%%''')
        #     should_i_explorer()
        # 
        # @rpa_program_method_decorator
        # def should_i_sync(self):
        #     func_n = inspect.currentframe().f_code.co_name
        #     pk_print(str_working=rf'''%%%FOO%%%''')
        #     should_i_sync()
        # 
        # @rpa_program_method_decorator
        # def download_video_from_web1(self):
        #     download_video_from_web1()
        # 
        # @rpa_program_method_decorator
        # def download_video_from_web2(self):
        #     download_video_from_web2()
        # 
        # def toogle_rpa_window(self):
        #     # pk_print(f"def {inspect.currentframe().f_code.co_name}() is called...")
        #     if self.isHidden() and not self.isVisible():
        #         # console_blurred 프로그램 창 활성화
        #         self.move_pyside6_window_to_front()
        #     else:
        #         self.hide()
        # 
        def move_pyside6_window_to_front(self):
            # self.activateWindow() 와 self.show() 의 위치는 서로 바뀌면 의도된대로 동작을 하지 않는다
            self.show()
            self.activateWindow()
            # active_window = win32gui.GetForegroundWindow()
            # win32gui.SetForegroundWindow(active_window)

    class MacroWindow(QDialog):
        # class MacroWindow(QWidget):
        def __init__(self):

            super().__init__()
            f = F_POP_SOUND_POP_SOUND_WAV
            if os.path.exists(f):
                from pk_core import play_wav_f
                play_wav_f(f=F_POP_SOUND_POP_SOUND_WAV)

            #  매크로 창 전역 변수 설정
            self.previus_pressed_keys = []
            self.display_width = get_display_info()['width'],
            self.display_height = get_display_info()['height'],
            # self.display_width_default = int(int(self.display_width[0]) * 0.106)
            self.display_width_default = int(int(self.display_width[0]) * 0.06)
            self.display_height_default = int(int(self.display_height[0]) * 0.2)

            # 마우스 위치, 클릭 정보, 시간 정보를 저장할 리스트
            # self.positions = []

            # 녹화 시작 시간
            self.time_recording_start = time.time()
            # self.time_recording_start_rel = 0.0
            self.elapsed_full_recording_time = 0.0
            self.previous_time = time.time()
            self.time_recording_end = 0.0
            #  메인창 설정
            self.setWindowTitle('.')
            self.setWindowIcon(QIcon(F_ICON_PNG))  # 메인창 아이콘 설정
            # self.setAttribute(Qt.WA_TranslucentBackground) # 메인창 블러 설정
            # self.setWindowFlags(Qt.WindowType.FramelessWindowHint) # 메인창 최상단 프레임레스 설정
            GlobalBlur(self.winId(), hexColor=False, Acrylic=False, Dark=True, QWidget=self)
            self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint)  # 최대화 최소화 버튼 숨기기
            self.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
            self.scale = 1 / 10
            self.windows_size_mode = 0  # 창크기 모드 설정  #0 ~ 3

            QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # 고해상도 스케일링을 활성화합니다.
            self.screens = QGuiApplication.screens()  # 사용 가능한 모든 화면을 가져옵니다.
            self.rotate_window_size_mode()

            # label 설정
            self.label = QLabel(self)
            self.label.setStyleSheet("color: rgba(255,255,255, 0.9);")
            self.label.setText(f"녹화 중...\n녹화경과시간: None\n")

            # 단축키 설정
            self.available_shortcut_list = {
                'MACRO EXCUTE': 'Ctrl+E',
                'MACRO EXIT': 'Ctrl+Q',
            }
            # self.set_shortcut('MACRO RECORD',self.record_macro)
            self.set_shortcut('MACRO EXCUTE', self.excute_macro)
            self.set_shortcut('MACRO EXIT', self.exit_macro)

            # 버튼 설정
            btn_to_excute_macro = self.get_btn(self.get_btn_name_with_shortcut_name('MACRO EXCUTE'), self.excute_macro)
            btn_to_exit_macro = self.get_btn(self.get_btn_name_with_shortcut_name('MACRO EXIT'), self.exit_macro)

            # GRID SETTING
            grid = QtWidgets.QGridLayout(self)
            btns = [
                self.label,
                btn_to_excute_macro,
                btn_to_exit_macro
            ]
            cnt = 0
            for i in btns:
                grid.addWidget(i, cnt, 0)
                cnt = cnt + 1

            # 레이아웃 설정
            layout = QGridLayout(self)
            layout.addLayout(grid, 0, 0)

            # 단일 단축키가 같이 눌리는 문제 ( ctrl + v 를 누르면   ctrl + v 에 바인딩된 함수만 호출되길 기대하는데, ctrl 에 바인딩된 함수도 호출되는 문제 )
            # 이벤트를 나누어 만들어 하나의 이벤트가 호출되면 다른 하나의 이벤트는 호출되지 않도록 설정 시도
            self.is_processing_event = False

            # Condition 객체 생성
            # self.condition = threading.Condition()

            # 이벤트 우선순위 설정
            # self.is_event_shortcut_3_processing = False # highest priority
            # self.is_event_shortcut_1_processing = False

            # 마우스 이동 이벤트 핸들러 설정
            listener = pynput.mouse.Listener(on_move=self.on_mouse_move)
            listener.start()

            # 마우스 버튼 클릭 이벤트 핸들러 설정
            listener2 = pynput.mouse.Listener(on_click=self.on_mouse_btn_clicked)
            listener2.start()

            # 키보드 이벤트 핸들러 설정 ( 3개 조합 단축키 , 2개 조합 단축키 , 단일 단축키 모두가능)
            self.keyboard_main_listener = pynput.keyboard.Listener(on_press=self.on_keys_down, on_release=self.on_keys_up)
            self.keyboard_main_listener.start()
            # 충돌이 문제가 아니고 두 이벤트가 중복이 되면 안되고 이벤트에 우선순위를 더 두어서 두 이벤트 호출 시 우선순위가 높은 이벤트만 exec 되도록

            # self.is_processing_event = False

            # 이벤트 핸들러 스레드 생성
            # event1_thread = threading.Thread(target=self.listener3)
            # event2_thread = threading.Thread(target=self.listner_2_combination_shorcuts)

            # 이벤트 핸들러 스레드 시작
            # event1_thread.start()
            # event2_thread.start()

            # 키보드 이벤트 핸들러 설정 ( 단일 단축키 )
            # self.listener3 = pynput.keyboard.Listener(on_press=self.on_keboard_press, suppress=True)
            # self.listener3.start()

            # 모니터링 이벤트 설정
            # self.mouse_positions = []
            # self.previous_position = None
            # self.current_position = None
            # self.timer = QTimer()
            # self.timer.timeout.connect(self.on_left_mouse_btn_clicked)
            # self.timer.start(900)

            # 녹화 경과시간 업데이트
            self.timer2 = QTimer()
            self.timer2.timeout.connect(self.update_label)  # noqa # 해당 검사에 대해서는 예외 목록에 "connect"를 넣는 것을 권장합니다. jetbrain 오류로 다년간 지속된 것으로 생각 중이다,
            self.timer2.start(1000)

            print("매크로녹화를 시작합니다")

            # 매크로녹화시작 로깅
            log_title = "매크로녹화시작"
            from pk_core import get_time_as_
            contents = f"{UNDERLINE}{get_time_as_('%Y-%m-%d_%H:%M:%S')}{log_title}"
            print_cyan(contents)
            self.save_macro_log(contents=contents)

            self.bring_this_window()

            # event_loop = QEventLoop()
            # event_loop.exec()

        def on_mouse_move(self, x, y):  # 아주 빠르게 감지
            # 이방식으로 매크로 중지를 할까?
            # print(f"마우스 이동 - X: {x}, Y: {y}")
            # print("마우스가 움직였습니다")
            # 상단 네비게이션
            if 0 <= x <= 3440 and 0 <= y <= 25:
                self.rotate_window_size_mode()
            else:
                pass

        def eventFilter(self, obj, event):
            if event.type() == QEvent.MouseMove:
                x = event.globalX()
                y = event.globalY()
                print(f"pyside6 창 외부 마우스 이동 감지 시도 - X: {x}, Y: {y}")
            return super().eventFilter(obj, event)

            # if event.type() == QEvent.MouseButtonPress and not self.rect().contains(event.pos()):
            #     print("pyside6 창 외부 클릭 되었습니다")
            # return super().eventFilter(obj, event)

        def get_btn_name_with_shortcut_name(self, button_name_without_shortcut):
            numbers = []
            for key, value in self.available_shortcut_list.items():
                numbers.append(len(value) + len(key))
            max_len_value = max(numbers)
            # print(max_len_value)

            button_name_with_short_cut = ""
            for key, value in self.available_shortcut_list.items():
                # print(key == button_name_without_shortcut)
                # print(key)
                # print(button_name_without_shortcut)

                if key == button_name_without_shortcut:
                    space_between = " " * (max_len_value - len(key) - len(value) + 1)
                    # space_between = " "
                    # space_between = str(max_len_value - len(key) - len(value) + 1)
                    # button_name_with_short_cut = button_name_with_short_cut + f"{key}{space_between}{value}\n"
                    button_name_with_short_cut = button_name_with_short_cut + f"{key}{space_between}{value}".strip()
            print(button_name_with_short_cut)
            return button_name_with_short_cut

        def rotate_window_size_mode(self):
            if self.windows_size_mode == 0:
                self.bring_this_window()
                self.setGeometry(0, 0, int(self.display_width_default / 2), int(self.display_height[0] / 5))
                self.move_window_to_center()
                self.windows_size_mode = self.windows_size_mode + 1
            elif self.windows_size_mode == 1:
                self.showMinimized()
                self.windows_size_mode = 0

        def set_shortcut(self, btn_name_promised, function):
            self.shortcut = QShortcut(self.available_shortcut_list[btn_name_promised], self)  # ctrl+n+d 3개 키들의 조합 설정 시도
            self.shortcut.activated.connect(function)
            pass

        def get_btn(self, btn_name, function):
            button = QPushButton(btn_name, self)
            button.clicked.connect(function)

            # 폰트 설정
            button.setFont(Pyside6Util.get_font_for_pyside6(font_path=F_RUBIKDOODLESHADOW_REGULAR_TTF))  # 입체감있는 귀여운 영어 폰트
            button.setStyleSheet("QPushButton { text-align: left; color: rgba(255,255,255, 0.9); height: 20px ; font-size: 10px}")
            # button.setLayoutDirection(QtCore.Qt.)
            return button

        def move_window_to_center(self):
            # center = QScreen.availableGeometry(app.primaryScreen()).center()
            # geo = self.frameGeometry()
            # geo.moveCenter(center)
            # self.move(geo.topLeft())
            if self.screens:
                primary_screen = self.screens[0]  # 첫 번째 화면을 기본 화면으로 설정합니다.
                center = primary_screen.availableGeometry().center()  # 기본 화면의 중앙 좌표를 가져옵니다.
                # 화면을 가운데로 이동시키는 코드를 작성하세요.
                # 예시로 윈도우를 생성하고 중앙 좌표를 이용하여 위치를 설정합니다.
                self.setGeometry(100, 100, 500, 300)  # 윈도우의 초기 위치와 크기를 설정합니다.
                self.move(center - self.rect().center())  # 윈도우를 화면 중앙으로 이동시킵니다.

                # self.show()

        def excute_macro(self):
            pass

        def exit_macro(self):
            from pk_core import get_time_as_
            # 매크로녹화종료 로깅
            log_title = "매크로녹화종료"
            self.time_recording_end = self.elapsed_full_recording_time
            contents = f"{UNDERLINE}{get_time_as_('%Y-%m-%d_%H:%M:%S')}{log_title}"
            print_cyan(contents)
            self.save_macro_log(contents=contents)

            # 매크로 로그 확인
            print("저장된 매크로 로그를 확인합니다")

            os.system(f'explorer "{F_MACRO_LOG}" ')

        # @Slot() # 최신 버전의 PySide6에서는 @Slot() 데코레이터를 사용하지 않고도 Slot 메서드를 정의할 수 있습니다. 이렇게 되면 자동으로 Slot으로 인식됩니다. 즉 최신버전 pyside6 에서는 쓸 필요 없다.
        def update_label(self):

            try:
                self.elapsed_full_recording_time = int(time.time() - self.time_recording_start)
                self.label.setText(f"녹화 중...\n녹화경과시간: {self.elapsed_full_recording_time} secs \n")
            except:
                traceback.print_exc(file=sys.stdout)

        def on_mouse_btn_clicked(self, x, y, button, pressed):
            from pk_core import get_time_as_
            # 현재 시간과 녹화 시작 시간의 차이 계산
            current_time = time.time()
            elapsed_time = int((current_time - self.previous_time) * 1000)
            # print(f"current_time : {current_time}")
            # print(f"self.previous_time : {self.previous_time}")

            # x, y = pyautogui.position() # parameter 에서 오는 값과 동일하므로 대안으로 남겨둠.
            if button == pynput.mouse.Button.left and pressed:
                info = f"sleep({elapsed_time})   %%%FOO%%%    click_mouse_left_btn(abs_x={x},abs_y={y}) "
                print_cyan(info)
                self.save_macro_log(contents=f"{get_time_as_('%Y-%m-%d_%H:%M:%S')} {info}")
            elif button == pynput.mouse.Button.right and pressed:
                info = f"sleep({elapsed_time})   %%%FOO%%%    click_mouse_right_btn(abs_x={x},abs_y={y}) "
                print_cyan(info)
                self.save_macro_log(contents=f"{get_time_as_('%Y-%m-%d_%H:%M:%S')} {info}")

            # 현재시간을 이전시간에 저장
            self.previous_time = current_time

        def save_macro_log(self, contents: str):
            macro_log = F_MACRO_LOG
            os.makedirs(os.path.dirname(F_MACRO_LOG))
            with open(macro_log, "a", encoding="utf-8") as f:
                f.write(f"{contents}\n")

        def on_keboard_press(self, key):
            # global is_processing_event
            # if self.is_processing_event != False:
            print(f'키보드 입력: {key}')

            # isinstance()
            # all(list) # (iterable) 객체의 모든 요소가 참(True)인지 확인
            # all(dict) # (iterable) 객체의 모든 요소가 참(True)인지 확인
            # all(tuple) # (iterable) 객체의 모든 요소가 참(True)인지 확인

        def on_keys_down(self, key):
            # 현재 시간과 녹화 시작 시간의 차이 계산
            current_time = time.time()
            elapsed_time = int((current_time - self.previous_time) * 1000)

            # for hotkey in self.HOTKEYS:
            #     hotkey.release(self.keyboard_listener1.canonical(key))
            #     print(f"key : {key}")

            # 키이름 여러 형식으로 출력
            # try:
            #     print(key)
            #     print(key.value)
            #     print(key.value.vk)
            # except:
            #     print(key)
            #     pass

            # 키이름 전처리
            key: str = str(key)
            key: str = key.lower()
            key: str = key.replace("\'", "")
            key: str = key.replace("\"", "")
            key: str = key.replace("key.", "")
            key: str = key.replace("<25>", "한자 or ctrl_r")
            key: str = key.replace("<21>", "한영 or alt_r")
            key: str = key.replace("12", "텐키 5")  # 텐키
            key: str = key.replace("cmd", "win")
            key: str = key.replace("page", "pg")
            key: str = key.replace("down", "dn")
            if key != "num_lock":
                key: str = key.replace("_l", "")
            key: str = key.replace("_r", "")

            key: str = key.replace(" ", "")
            key: str = key.replace("<", "")
            key: str = key.replace(">", "")
            # key: str = key.replace("_", "")

            # 전처리 후 출력
            # print(str(key))

            # if key == "ctrl+alt":
            log_title = "키보드인풋"
            info = f"sleep({elapsed_time})\nkeyDown('{key}') "
            print_cyan(info)
            from pk_core import get_time_as_
            self.save_macro_log(contents=f"{get_time_as_('%Y-%m-%d_%H:%M:%S')}{log_title} {info}")

            # 현재시간을 이전시간에 저장
            self.previous_time = current_time

            # if self.store = []
            # global is_processing_event
            # if self.is_processing_event == False:
            # self.is_processing_event = True
            # self.is_processing_event = False

            # pynput.keyboard.Listener()는 다시 self.listener3.start() 할 수 없다.
            # 새로 만들어야 한다
            # if self.listener3.is_alive():
            #     self.listener3.stop()
            # else:

            # self.listener3 = pynput.keyboard.Listener(on_press=self.on_keboard_press)
            # self.listener3.start()

            # self.condition.notify()  # event1에게 동작 신호 보내기

        def on_single_key_pressed(self, key):

            # 현재 시간과 녹화 시작 시간의 차이 계산
            current_time = time.time()
            elapsed_time = int((current_time - self.previous_time) * 1000)

            # print(str(key))
            if pynput.keyboard.GlobalHotKeys.name == "<ctrl>":
                log_title = "키보드단일키인풋"
                info = f"  sleep({elapsed_time})   %%%FOO%%%    press({str(key)}) "
                print_cyan(info)
                from pk_core import get_time_as_
                self.save_macro_log(contents=f"{get_time_as_('%Y-%m-%d_%H:%M:%S')}{log_title} {info}")

            # 현재시간을 이전시간에 저장
            self.previous_time = current_time

            # try:
            #     # alphanumeric key
            #     print('{0}'.format(key.char))
            # except AttributeError:
            #     # special key
            #     print('{0}'.format(key.char))

        def on_keys_up(self, key):
            # 현재 시간과 녹화 시작 시간의 차이 계산
            current_time = time.time()
            elapsed_time = int((current_time - self.previous_time) * 1000)

            # for hotkey in self.HOTKEYS:
            #     if hotkey
            #     hotkey.press(self.keyboard_listener1.canonical(key))
            #     print(f"key : {key}")

            # 키이름 전처리
            key: str = str(key)
            key: str = key.lower()
            key: str = key.replace("\'", "")
            key: str = key.replace("\"", "")
            key: str = key.replace("key.", "")
            key: str = key.replace("<25>", "한자 or ctrl_r")
            key: str = key.replace("<21>", "한영 or alt_r")
            key: str = key.replace("12", "텐키 5")  # 텐키
            key: str = key.replace("cmd", "win")
            key: str = key.replace("page", "pg")
            key: str = key.replace("down", "dn")
            if key != "num_lock":
                key: str = key.replace("_l", "")
            key: str = key.replace("_r", "")

            key: str = key.replace(" ", "")
            key: str = key.replace("<", "")
            key: str = key.replace(">", "")
            # key: str = key.replace("_", "")

            # 전처리 후 출력
            # print(str(key))

            log_title = "키보드릴리즈"
            info = f"sleep({elapsed_time})\nkeyUp('{key}') "
            print_cyan(info)
            from pk_core import get_time_as_
            self.save_macro_log(contents=f"{get_time_as_('%Y-%m-%d_%H:%M:%S')}{log_title} {info}")

            # 현재시간을 이전시간에 저장
            self.previous_time = current_time
            pass

        def bring_this_window(self):
            self.show()
            self.activateWindow()
            # active_window = win32gui.GetForegroundWindow()
            # win32gui.SetForegroundWindow(active_window)

    class CustomQthread(QThread):
        finished = Signal()  # run()의 성공 신호를 보내기 위해 필요, run() 은 상속된 QThread 객체의 run()을 통해서 오버라이딩 되는 것 보인다.

        def __init__(self, q_application):  # 이 생성자는 q_application 를 받기 위해서 내가 작성 q_application 가 필요없는 void method QThread 이용 시 그냥 없애면 되는 생성자.
            super().__init__()
            self.q_application = q_application

        def run(self):
            # QThread 동작 테스트 코드
            print("QThread 초기화 시작")
            for i in range(10):
                print(i)
                self.msleep(30)

            def tmp2(q_application: QApplication):
                global dialog2
                dialog2 = GuiUtil.CustomDialog(q_application=q_application, q_wiget=GuiUtil.CustomQdialog(prompt="테스트", btn_list=["exec ", "exec 하지 않기"]), is_app_instance_mode=False)
                if dialog2.txt_clicked == "exec ":
                    print("정상적으로 동작합니다")

            def tmp(string: str):
                print(string)
                # global tmpc
                # dialog = CustomDialog(q_application=q_application, q_wiget=RpaProgramMainWindow(), is_app_instance_mode=True, is_exec_mode=True)
                # global dialog
                # dialog = UiUtil.CustomQdialog(context="테스트", buttons=["확인"], is_input_text_box=True, input_text_default="???")
                # dialog.show()
                # dialog = CustomDialog(q_application=q_application, q_wiget=UiUtil.CustomQdialog(context="테스트", buttons=["exec ", "exec 하지 않기"], starting_timer=True, closing_timer=False), is_app_instance_mode=True)

            # 프로그램 외 단축키 이벤트 설정
            shortcut_keys_up_promised = {
                # "<ctrl>+<cmd>": self.close, #success
                # "<ctrl>+T": partial(tmp, "test"), #success
                # "<ctrl>+Q": partial(tmp2, self.q_application), #fail
                # "<ctrl>+h": partial(q_wiget.toogle_rpa_window, "<ctrl>+h"), #fail
            }
            keyboard_main_listener = pynput.keyboard.GlobalHotKeys(hotkeys=shortcut_keys_up_promised)
            keyboard_main_listener.start()

            self.finished.emit()  # 작업이 성공되었음을 신호로 알림 # flutter 상태관리와 비슷
            print("QThread exec  증...")

    # class SharedObject(QObject):
    #     """pyside6 app 전용 공유객체 (pyside6 app 상태관리용)"""
    #     dataChanged = Signal(str)  # 데이터 변경을 알리는 시그널
    #
    #     def __init__(self):
    #         super().__init__()
    #         self._data = ""
    #         self.answer = ""
    #         self.question = ""
    #         self.rpa_program_main_window = None
    #
    #     #  /////////////////////////////////////////////// SharedObject.data
    #     @property
    #     def data(self):
    #         return self._data
    #
    #     @data.setter
    #     def data(self, value):
    #         self._data = value
    #         self.dataChanged.emit(self._data)  # 데이터 변경 시 시그널 발생
    #
    #     #  /////////////////////////////////////////////// 공유객체 SharedObject.answer
    #     @property
    #     def data(self):
    #         return self.answer
    #
    #     @data.setter
    #     def data(self, value):
    #         self.answer = value
    #         self.dataChanged.emit(self.answer)
    #
    #     #  SharedObject.question
    #     @property
    #     def data(self):
    #         return self.question
    #
    #     @data.setter
    #     def data(self, value):
    #         self.question = value
    #         self.dataChanged.emit(self.question)
    #
    #     #  SharedObject.rpa_program_main_window ....이래도 되나 모르겠네... 성능 이슈 있을 수도...
    #     @property
    #     def data(self):
    #         return self.rpa_program_main_window
    #
    #     @data.setter
    #     def data(self, value):
    #         self.rpa_program_main_window = value
    #         self.dataChanged.emit(self.rpa_program_main_window)

    @staticmethod
    def pop_up_as_complete(title: str, ment: str, auto_click_positive_btn_after_seconds: int, input_text_default="", btn_list=None):
        # should_i_do 가 앱 안과 밖에서도 잘 된다면 deprecated 하자
        if btn_list is None:
            btn_list = ["확인"]
        if platform.system() == 'Windows':
            func_n = inspect.currentframe().f_code.co_name
            pk_print(working_str=rf'''%%%FOO%%%''')
            f = F_POP_SOUND_POP_SOUND_WAV
            if os.path.exists(f):
                from pk_core import play_wav_f
                play_wav_f(f=f)

            app_foo = None

            # QApplication 인스턴스 확인
            app = QApplication.instance()
            if app is None:
                app_foo = QApplication()
            if input_text_default == "":
                is_input_text_box = False
            else:
                is_input_text_box = True

            dialog = GuiUtil.CustomQdialog(title=title, prompt=ment, btn_list=btn_list, input_box_mode=is_input_text_box, input_box_text_default=input_text_default, auto_click_positive_btn_after_seconds=auto_click_positive_btn_after_seconds)
            dialog.exec()
            txt_clicked = dialog.txt_clicked

            if txt_clicked == "":
                print_cyan(f'버튼 입니다 {txt_clicked}')
            if app == True:  # .....app 은 bool 이 아닌데. 동작 되고있는데..
                print_cyan("여기는 좀 확인을 해야하는데. 호출 안되면 좋겠는데1")
                if isinstance(app_foo, QApplication):
                    print_cyan("여기는 좀 확인을 해야하는데. 호출 안되면 좋겠는데2")
                    app_foo.exec()
            if app == True:
                # app_foo.quit()# QApplication 인스턴스 제거시도 : fail
                # app_foo.deleteLater()# QApplication 인스턴스 파괴시도 : fail
                # del app_foo # QApplication 인스턴스 파괴시도 : fail
                # app_foo = None # QApplication 인스턴스 파괴시도 : fail
                print_cyan("여기는 좀 확인을 해야하는데. 호출 안되면 좋겠는데3")
                app_foo.shutdown()  # QApplication 인스턴스 파괴시도 : success  # 성공요인은 app.shutdown()이 호출이 되면서 메모리를 해제까지 수행해주기 때문
                # sys.exit()
        else:
            print_success(f"{ment}")


class Pyside6Util:
    @staticmethod
    def get_font_for_pyside6(font_path):
        font_id = QFontDatabase.addApplicationFont(font_path)
        font_name = QFontDatabase.applicationFontFamilies(font_id)[0]
        font = QFont(font_name)
        font.setFixedPitch(True)
        return font


def should_i_do(prompt: str, function: Callable = None, auto_click_negative_btn_after_seconds: int = None, auto_click_positive_btn_after_seconds: int = None, input_box_text_default="", btn_list=None, title="%%%FOO%%%", input_box_mode=False):
    from pkg_py.pk_core_class import PkMents2025
    if not btn_list:
        btn_list=[PkMents2025.POSITIVE, PkMents2025.NEGATIVE]
    func_n = inspect.currentframe().f_code.co_name
    pk_print(working_str=rf'''%%%FOO%%%''')

    # gui pop sound
    f = F_POP_SOUND_POP_SOUND_WAV
    if os.path.exists(f):
        from pk_core import play_wav_f
        play_wav_f(f=f)

    # make QApplication
    app_foo = None
    app = QApplication.instance()
    if app is None:
        app_foo = QApplication()

    dialog = GuiUtil.CustomQdialog(
        title=title,
        prompt=prompt,
        btn_list=btn_list,
        input_box_mode=input_box_mode,
        input_box_text_default=input_box_text_default,
        auto_click_positive_btn_after_seconds=auto_click_positive_btn_after_seconds,
        auto_click_negative_btn_after_seconds=auto_click_negative_btn_after_seconds
    )
    from pk_core import ensure_window_to_front
    ensure_window_to_front(window_title_seg=title)
    # move_window_to_front_via_async(window_title_seg=title)
    # await move_window_to_front_via_async(window_title_seg=title)
    # todo : chore : minimize another windows
    dialog.exec()
    txt_clicked = dialog.txt_clicked
    txt_written = None
    if not input_box_mode == False:
        if not dialog.input_box.text() is None:
            txt_written = dialog.input_box.text()
    return (txt_clicked, function, txt_written)


# def should_i_back_up_target():  # please_type_abspath_to_back_up
#     func_n = inspect.currentframe().f_code.co_name
#     pk_print(str_working=rf'''%%%FOO%%%''')
#     loop_cnt = 0
#     while 1:
#         if loop_cnt == 0:
#             previous_input = PROJECT_PARENTS_DIRECTORY
#         else:
#             previous_input = clipboard.paste()
#         previous_input = previous_input.strip()
#         dialog = GuiUtil.CustomQdialog(string="백업할 pnx를 입력하세요", btns=["입력", "입력하지 않기"], input_box_mode=True, input_box_text_default=previous_input)
#         dialog.exec()
#         txt_clicked = dialog.txt_clicked
#         print_cyan(txt_clicked)
#         loop_cnt = + 1
#         if txt_clicked == "입력":
#             compress_pnx_via_bz(dialog.input_box.text())
#         else:
#             break
#
#
# def should_i_start_test_core():
#     func_n = inspect.currentframe().f_code.co_name
#     pk_print(str_working=rf'''%%%FOO%%%''')
#     while 1:
#         dialog = GuiUtil.CustomQdialog(string="테스트를 시작할까요?", btns=["시작하기", "시작하지 않기"])
#         dialog.exec()
#         txt_clicked = dialog.txt_clicked
#         if txt_clicked == "시작하기":
#             print_cyan("아무 테스트도 정의되지 않았습니다.")
#             pass
#         else:
#             break
#
#
# def should_i_enter_to_power_saving_mode():
#     func_n = inspect.currentframe().f_code.co_name
#     pk_print(str_working=rf'''%%%FOO%%%''')
#     txt_clicked, function, txt_written = should_i_do(
#         string="절전모드로 진입할까요?",
#         btns=["진입", "아니,"                  " 그냥 닫아", "10분 뒤 진입", "20분 뒤 진입", "30분 뒤 진입", "1시간 뒤 진입", "진입취소해줘"],
#         function=change_os_to_power_saving_mode,
#         auto_click_negative_btn_after_seconds=30,
#         title="Undefined Title",
#         return_mode=True,
#     )
#     print_cyan(txt_clicked)
#     if function is not None:
#         if txt_clicked == "진입":
#             function()
#         if txt_clicked == "아니, 그냥 닫아":
#             return
#         elif txt_clicked == "10분 뒤 진입":
#             GuiUtil.pop_up_as_complete(title_="작업중간보고", ment="10분 뒤 절전모드 진입을 시도합니다", input_text_default="", auto_click_positive_btn_after_seconds=3)
#             sleep(minutes=10)
#             function()
#         elif txt_clicked == "20분 뒤 진입":
#             GuiUtil.pop_up_as_complete(title_="작업중간보고", ment="20분 뒤 절전모드 진입을 시도합니다", input_text_default="", auto_click_positive_btn_after_seconds=3)
#             sleep(minutes=20)
#             function()
#         elif txt_clicked == "30분 뒤 진입":
#             GuiUtil.pop_up_as_complete(title_="작업중간보고", ment="30분 뒤 절전모드 진입을 시도합니다", input_text_default="", auto_click_positive_btn_after_seconds=3)
#             sleep(minutes=30)
#             function()
#         elif txt_clicked == "1시간 뒤 진입":
#             GuiUtil.pop_up_as_complete(title_="작업중간보고", ment="1시간 뒤 절전모드 진입을 시도합니다", input_text_default="", auto_click_positive_btn_after_seconds=3)
#             sleep(minutes=60)
#             function()
#         elif txt_clicked == "진입취소해줘":
#             change_os_to_shutdown(cancel_mode=True)
#
#
# def should_i_translate_eng_to_kor():
#     func_n = inspect.currentframe().f_code.co_name
#     pk_print(str_working=rf'''%%%FOO%%%''')
#     while 1:
#         dialog = GuiUtil.CustomQdialog(string="WRITE SOMETHING YOU WANT TO TRANSLATE", btns=["Translate this to Korean", "Don't"], input_box_mode=True)
#         dialog.exec()
#         txt_clicked = dialog.txt_clicked
#         print_cyan(txt_clicked)
#         if txt_clicked == "Translate this to Korean":
#             translate_eng_to_kor(dialog.input_box.text())
#         else:
#             break
#
#
# def should_i_translate_kor_to_eng():
#     func_n = inspect.currentframe().f_code.co_name
#     pk_print(str_working=rf'''%%%FOO%%%''')
#     while 1:
#         dialog = GuiUtil.CustomQdialog(string='번역하고 싶은 내용을 입력하세요', btns=["영어로 번역", "번역하지 않기"], input_box_mode=True)
#         dialog.exec()
#         txt_clicked = dialog.txt_clicked
#         print_cyan(txt_clicked)
#         if txt_clicked == "영어로 번역":
#             translate_kor_to_eng(dialog.input_box.text())
#         else:
#             break
#
#
# def should_i_exit_this_program():
#     func_n = inspect.currentframe().f_code.co_name
#     pk_print(str_working=rf'''%%%FOO%%%''')
#     while 1:
#         # dialog = GuiUtil.CustomQdialog(context="앱을 종료할까요?", buttons=["종료", "종료하지 않기"])
#         dialog = GuiUtil.CustomQdialog(string="프로그램을 종료할까요?", btns=["종료", "종료하지 않기"])
#         dialog.exec()
#         txt_clicked = dialog.txt_clicked
#         print_cyan(txt_clicked)
#         if txt_clicked == "종료":
#             # app.quit()
#             # taskkill("python.exe")
#             # self.close()
#             sys.exit()
#             # break
#         else:
#             break
#
#
# def should_i_find_direction_via_naver_map():
#     func_n = inspect.currentframe().f_code.co_name
#     pk_print(str_working=rf'''%%%FOO%%%''')
#     while 1:
#         dialog = GuiUtil.CustomQdialog(string="어디로 길을 찾아드릴까요?", btns=["찾아줘", "찾아주지 않아도 되"], input_box_mode=True)
#         dialog.exec()
#         txt_clicked = dialog.txt_clicked
#         print_cyan(txt_clicked)
#         if txt_clicked == "찾아줘":
#             find_direction_via_naver_map(dialog.input_box.text())
#         else:
#             print("네, 알겠습니다", comma_delay=0.98)
#             break
#
#
# def should_i_connect_to_rdp1():
#     func_n = inspect.currentframe().f_code.co_name
#     pk_print(str_working=rf'''%%%FOO%%%''')
#     while 1:
#         dialog = GuiUtil.CustomQdialog(string='rdp1에 원격접속할까요?', btns=[YES, NO])
#         dialog.exec()
#         txt_clicked = dialog.txt_clicked
#         print_cyan(txt_clicked)
#         if txt_clicked == YES:
#             # run_rdp_client()
#             pass
#         else:
#             break
#
#
# def should_i_record_macro():
#     func_n = inspect.currentframe().f_code.co_name
#     pk_print(str_working=rf'''%%%FOO%%%''')
#     while 1:
#         dialog = GuiUtil.CustomQdialog(string="매크로 레코드를 어떻게 시작할까요?", btns=["새로 시작하기", "이어서 시작하기", "시작하지 않기"])
#         dialog.exec()
#         txt_clicked = dialog.txt_clicked
#         if txt_clicked == "새로 시작하기":
#             if os.path.exists(MACRO_LOG):
#                 move_pnx_to_trash_bin(MACRO_LOG)
#             make_pnx(MACRO_LOG, mode="f")
#             open_pnx(pnx=MACRO_LOG, debug_mode=True)
#         elif txt_clicked == "이어서 시작하기":
#             if os.path.exists(MACRO_LOG):
#                 make_pnx(MACRO_LOG, mode="f")
#                 open_pnx(pnx=MACRO_LOG, debug_mode=True)
#         elif txt_clicked == "시작하지 않기":
#             break
#         macro_window = GuiUtil.MacroWindow()
#         macro_window.show()
#         macro_window.activateWindow()
#         break
#
#
# def should_i_download_youtube_as_webm():
#     func_n = inspect.currentframe().f_code.co_name
#     pk_print(str_working=rf'''%%%FOO%%%''')
#     text_previous_from_clipboard = None
#     while 1:
#         if text_previous_from_clipboard != clipboard.paste():
#             text_previous_from_clipboard = clipboard.paste()
#         else:
#             text_previous_from_clipboard = ""
#         dialog = GuiUtil.CustomQdialog(string="다운로드하고 싶은 URL을 입력해주세요", btns=["입력", "입력하지 않기"], input_box_mode=True, input_box_text_default=text_previous_from_clipboard)
#         dialog.exec()
#         if dialog.txt_clicked == "입력":
#             download_from_youtube_to_webm(urls=dialog.input_box.text())
#         else:
#             break
#
#
# def should_i_merge_directories():
#     func_n = inspect.currentframe().f_code.co_name
#     pk_print(str_working=rf'''%%%FOO%%%''')
#     previous_text = ""
#     while 1:
#         previous_text = clipboard.paste()
#         dialog = GuiUtil.CustomQdialog(string="머지할 pnx들을 입력하세요", btns=["입력", "입력하지 않기"], input_box_mode=True, input_box_text_default=previous_text, auto_click_negative_btn_after_seconds=10)
#         dialog.exec()
#         directory_pnxs = dialog.input_box.text()
#         if dialog.txt_clicked == "입력":
#             directory_pnxs = directory_pnxs.strip()
#             directory_pnxs = directory_pnxs.strip("\t")
#             directory_pnxs_: List[str] = directory_pnxs.split("\n")
#             merge_directories(directory_pnxs=directory_pnxs_)
#             break
#         else:
#             break
#
#
# def should_i_convert_mkv_to_wav():
#     func_n = inspect.currentframe().f_code.co_name
#     pk_print(str_working=rf'''%%%FOO%%%''')
#     while 1:
#         dialog = GuiUtil.CustomQdialog(string="convert 할 MKV파일경로를 입력하세요", btns=["입력", "입력하지 않기"], input_box_mode=True, auto_click_negative_btn_after_seconds=10)
#         dialog.exec()
#         txt_clicked = dialog.txt_clicked
#         file_mkv = dialog.input_box.text()
#         if txt_clicked == "입력":
#             convert_mkv_to_wav(file_mkv=file_mkv)
#             break
#         else:
#             break
#
#
# def should_i_gather_empty_directory():
#     func_n = inspect.currentframe().f_code.co_name
#     pk_print(str_working=rf'''%%%FOO%%%''')
#     while 1:
#         dialog = GuiUtil.CustomQdialog(string="빈폴더를 순회하며 수집할 pnx를 입력하세요", btns=["입력", "입력하지 않기"], input_box_mode=True)
#         dialog.exec()
#         txt_clicked = dialog.txt_clicked
#         if txt_clicked == "입력":
#             pnx = dialog.input_box.text()
#             pnx = pnx.strip()
#             pnx = pnx.replace("\"", "")
#             pnx = pnx.replace("\'", "")
#             connected_drives = []
#             for drive_letter in string.ascii_uppercase:
#                 drive_path = drive_letter + ":\\"
#                 if os.path.exists(drive_path):
#                     connected_drives.append(drive_path)
#                     if pnx == drive_path:
#                         print("입력된 pnx는 너무 광범위하여 진행할 수 없도록 설정되어 있습니다", comma_delay=0.98)
#                         break
#             if not os.path.exists(pnx):
#                 print("입력된 pnx가 존재하지 않습니다", comma_delay=0.98)
#                 continue
#             if pnx == "":
#                 continue
#
#             gather_pnxs_empty(pnx)
#             print_success(string=rf"pnx를 순회하며 빈폴더를 모았습니다")
#             # speak_ments("pnx를 순회하며 빈폴더를 약속된 폴더로 모았습니다", sleep_after_play=0.65) # 시끄러웠다,
#             GuiUtil.pop_up_as_complete(title_="작업성공보고", ment=f"pnx를 순회하며 빈폴더를 모았습니다", auto_click_positive_btn_after_seconds=2)
#         else:
#             break
#
#
# def should_i_gather_pnxs_useless():
#     func_n = inspect.currentframe().f_code.co_name
#     pk_print(str_working=rf'''%%%FOO%%%''')
#     try:
#         txt_clicked, function, txt_written = should_i_do(
#             string="pnx를 순회하며 텍스트파일에 정의된 불필요한 파일을 약속된 pnx로 모을까요?",
#             btns=["모으기", "모으지 않기"],
#             function=change_os_to_power_saving_mode, auto_click_negative_btn_after_seconds=30,
#             title=f"{func_n}()",
#             return_mode=True,
#             input_box_mode=True,
#         )
#         if txt_clicked == "모으기":
#             pnx = txt_written
#             pnx = pnx.strip()
#             pnx = pnx.replace("\"", "")
#             pnx = pnx.replace("\'", "")
#             pk_print(f'''pnxs={pnx} %%%FOO%%%''')
#             if pnx == "":
#                 pk_print(f'''pnx가 입력되지 않았습니다 %%%FOO%%%''')
#                 return
#             connected_drives = []
#             for drive_letter in string.ascii_uppercase:
#                 drive_path = drive_letter + ":\\"
#                 if os.path.exists(drive_path):
#                     connected_drives.append(drive_path)
#                     if pnx == drive_path:
#                         pk_print(f'''입력된 pnx는 너무 광범위하여 진행할 수 없도록 설정되어 있습니다 %%%FOO%%%''')
#                         return
#             if not os.path.exists(pnx):
#                 pk_print(f'''입력된 pnx가 존재하지 않습니다 %%%FOO%%%''')
#                 return
#             gather_pnxs_useless(src=pnx)
#         return
#     except:
#         print_light_black(f"{traceback.format_exc()}")
#
#
# def should_i_gather_special_files():
#     func_n = inspect.currentframe().f_code.co_name
#     pk_print(str_working=rf'''%%%FOO%%%''')
#     """분류되지 않은 하나의 폴더로 모음"""
#     # while 1:
#     #     dialog = GuiUtil.CustomQdialog(ment="pnx를 순회하며 특별한 파일을 약속된 폴더로 모을까요?", buttons=["모으기", "모으지 않기"], is_input_text_box=True)
#     #     dialog.exec()
#     #     txt_clicked = dialog.txt_clicked
#     #     if txt_clicked == "모으기":
#     #         pnx_todo = dialog.input_box.text()
#     #         pnx_todo = pnx_todo.strip()
#     #         pnx_todo = pnx_todo.replace("\"", "")
#     #         pnx_todo = pnx_todo.replace("\'", "")
#     #         connected_drives = []
#     #         for drive_letter in string.ascii_uppercase:
#     #             drive_path = drive_letter + ":\\"
#     #             if os.path.exists(drive_path):
#     #                 connected_drives.append(drive_path)
#     #                 if pnx_todo == drive_path:
#     #                     speak_ments("입력된 pnx는 너무 광범위하여 진행할 수 없도록 설정되어 있습니다", sleep_after_play=0.65)
#     #                     break
#     #         if not os.path.exists(pnx_todo):
#     #             speak_ments("입력된 pnx가 존재하지 않습니다", sleep_after_play=0.65)
#     #             continue
#     #         if pnx_todo == "":
#     #             continue
#     #         special_files = [
#     #             "[subplease]",
#     #         ]
#     #         dst = rf"D:\[noe] [8TB] [ext]\$special_files"
#     #         make_d_leaf(dst)
#     #         isSpoken = False
#     #         if os.path.isdir(pnx_todo):
#     #             for root, dirs, files in os.walk(pnx_todo, topdown=False):  # os.walk()는 with walking 으로 동작한다
#     #                 for file in files:
#     #                     file_path = os.path.join(root, file)
#     #                     for special_file in special_files:
#     #                         if special_file in os.path.basename(file_path):
#     #                             # print(rf'file_path : {file_path}')
#     #                             print(rf"special file : {file_path}")
#     #                             move_pnx_without_overwrite(pnx_todo=file_path, dst=dst)
#     #                             if isSpoken == False:
#     #                                 speak_ments("pnx를 순회하며 특별한 파일을 약속된 폴더로 모았습니다", sleep_after_play=0.65)
#     #                                 isSpoken = True
#     #     else:
#     #         break
#     pass
#
#
# def should_i_classify_special_files():
#     func_n = inspect.currentframe().f_code.co_name
#     pk_print(str_working=rf'''%%%FOO%%%''')
#     """분류된 여러 폴더로 모음"""
#     is_nested_loop_broken = False
#     previous_abspath = ""
#     while 1:
#         while 1:
#             dialog1 = GuiUtil.CustomQdialog(string="파일분류를 위해 순회할 디렉토리의 pnx를 입력해주세요", btns=["제출", "제출하지 않기"], input_box_mode=True, input_box_text_default=previous_abspath)
#             dialog1.exec()
#
#             txt_clicked = dialog1.txt_clicked
#             if txt_clicked == "제출하지 않기":
#                 is_nested_loop_broken = True
#                 break
#             if txt_clicked == "제출":
#                 pnx_todo = dialog1.input_box.text()
#                 pnx_todo = pnx_todo.strip()
#                 pnx_todo = pnx_todo.replace("\"", "")
#                 pnx_todo = pnx_todo.replace("\'", "")
#                 previous_abspath = pnx_todo
#                 connected_drives = []
#                 for drive_letter in string.ascii_uppercase:
#                     drive_path = drive_letter + ":\\"
#                     if os.path.exists(drive_path):
#                         connected_drives.append(drive_path)
#                         if pnx_todo == drive_path:
#                             pk_print(str_working="입력된 pnx는 너무 광범위하여 진행할 수 없도록 설정되어 있습니다")
#                             is_nested_loop_broken = True
#                             break
#                 if not os.path.exists(pnx_todo):
#                     # print("입력된 pnx가 존재하지 않습니다", comma_delay=0.98)
#                     continue
#                 if pnx_todo == "":
#                     continue
#                 special_dirs_promised = [
#                     # "blahblahblah_boom_boom_boom",
#                 ]
#                 previous_keyword = clipboard.paste()
#                 if previous_keyword == pnx_todo:
#                     previous_keyword = ""
#
#                 dialog2 = GuiUtil.CustomQdialog(string="분류할 파일에 포함되어 있을 키워드를 입력해주세요", btns=["제출", "제출하지 않기"], input_box_mode=True, input_box_text_default=previous_keyword)
#                 dialog2.exec()
#                 txt_clicked2 = dialog2.txt_clicked
#                 if txt_clicked2 == "제출":
#                     file_path = dialog2.input_box.text()
#                     file_path = file_path.strip()
#                     if file_path == "":
#                         print("입력된 pnx가 존재하지 않습니다", comma_delay=0.98)
#                         break
#                     if "\n" in file_path:
#                         file_paths = file_path.split("\n")
#                         print(f"{len(file_paths)}개의 키워드들이 입력되었습니다, 파일분류를 시작합니다", comma_delay=0.98)
#                     else:
#                         file_paths = [file_path]
#                     for file_path in file_paths:
#                         file_path = file_path.strip()
#                         if file_path != "":
#                             special_dirs_promised.append(file_path)
#                         # destination_directory_of_files_classified = SPECIAL_DIRECTORY # e: drive 에 저장
#                         dst_dir_of_files_classified = rf"{pnx_todo}\`"  # 입력된 pnx에 ` 폴더를 만들어 저장
#                         for special_file in special_dirs_promised:
#                             make_pnx(rf"{dst_dir_of_files_classified}\{special_file}", mode="d")
#                         # make_d_leaf(destination_directory_of_files_classified)
#                         file_abspaths_searched = []
#                         if os.path.isdir(pnx_todo):
#                             for root, dirs, files in os.walk(pnx_todo, topdown=False):  # os.walk()는 with walking 으로 동작한다
#                                 for file in files:
#                                     file_abspath = os.path.join(root, file)
#                                     for file_path in special_dirs_promised:
#                                         if file_path in os.path.basename(file_abspath):
#                                             file_abspaths_searched.append(file_abspath)
#                         file_abspaths_searched_for_print = "\n".join(file_abspaths_searched)  # [str] to str with 개행
#
#                         # dialog3 = GuiUtil.CustomQdialog(ment=f"<검색된 파일 목록>\n\n검색된 파일 개수 : {len(file_abspaths_searched)}\n{file_abspaths_searched_for_print}\n\n 검색된 내용대로 계속진행을 할까요?", btns=[YES, NO], auto_click_positive_btn_after_seconds=0)
#                         # dialog3.exec()
#                         # if dialog3.txt_clicked == NO:
#                         #     break
#                         # if dialog3.txt_clicked == YES:
#                         #     for index, special_dir in enumerate(special_dirs_promised):
#                         #         for file_abspath_searched in file_abspaths_searched:
#                         #             if special_dir in os.path.basename(file_abspath_searched):
#                         #                 # GuiUtil.pop_up_as_complete(title="디버깅", ment=f"index : {index} \n special_dir: {special_dir}", auto_click_positive_btn_after_seconds=600)
#                         #                 move_pnx_without_overwrite(pnx_todo=file_abspath_searched, dst=rf"{dst_dir_of_files_classified}\{special_dirs_promised[index]}")
#                         # special_dirs_promised = []
#
#                         print_cyan(string=f"#검색된 파일 개수 : {len(file_abspaths_searched)}")
#                         print_cyan(string=f"#검색된 파일 목록 : {file_abspaths_searched_for_print}")
#                         for index, special_dir in enumerate(special_dirs_promised):
#                             for file_abspath_searched in file_abspaths_searched:
#                                 if special_dir in os.path.basename(file_abspath_searched):
#                                     # GuiUtil.pop_up_as_complete(title="디버깅", ment=f"index : {index} \n special_dir: {special_dir}", auto_click_positive_btn_after_seconds=600)
#                                     move_pnx_without_overwrite(src=file_abspath_searched, dst=rf"{dst_dir_of_files_classified}\{special_dirs_promised[index]}")
#                         special_dirs_promised = []
#
#         if is_nested_loop_broken == True:
#             break


def print_as_gui(ment: str, input_text_default="", auto_click_positive_btn_after_seconds=3, btn_list=None):
    if not btn_list:
        btn_list=["확인"]
    func_n = inspect.currentframe().f_code.co_name
    pk_print(working_str=rf'''%%%FOO%%%''')
    """
    이 함수는 특별한 사용요구사항이 있습니다
    pyside6 앱 내에서 해당 함수를 호출할때는 is_app_instance_mode 를 파라미터에 넣지 않고 쓰는 것을 default 로 디자인했습니다.
    pyside6 앱 밖에서 해당 함수를 호출할때는 is_app_instance_mode 를 True 로 설정하고 쓰십시오.

    사용 요구사항이 생기게 된 이유는 다음과 같습니다
    pyside6 는 app을 singletone으로 instance를 구현합니다. 즉, instance는 반드시 pyside6 app 내에서 하나여야 합니다.
    pyside6의 QApplication()이 앱 내/외에서도 호출이 될 수 있도록 디자인했습니다.
    앱 내에서 호출 시에는 is_app_instance_mode 파라미터를 따로 설정하지 않아도 되도록 디자인되어 있습니다.
    앱 외에서 호출 시에는 is_app_instance_mode 파라미터를 True 로 설정해야 동작하도록 디자인되어 있습니다.
    """
    # app_foo: QApplication = None
    # if is_app_instance_mode == True:
    #     app_foo: QApplication = QApplication()
    # if input_text_default == "":
    #     pk_print(f"{inspect.currentframe().f_code.co_name}()")
    #     is_input_text_box = False
    # else:
    #     is_input_text_box = True
    # dialog = GuiUtil.CustomQdialog(ment=f"{context}", buttons=["확인"], is_input_box=is_input_text_box, input_box_text_default=input_text_default)
    # pk_print(f"{inspect.currentframe().f_code.co_name}()")
    # dialog.exec()
    # txt_clicked = dialog.txt_clicked
    # if txt_clicked == "":
    #     print_ment_magenta()(f'누르신 버튼은 {txt_clicked} 입니다')
    # if is_app_instance_mode == True:
    #     if isinstance(app_foo, QApplication):
    #         app_foo.exec()
    # if is_app_instance_mode == True:
    #     # app_foo.quit()# QApplication 인스턴스 제거시도 : fail
    #     # app_foo.deleteLater()# QApplication 인스턴스 파괴시도 : fail
    #     # del app_foo # QApplication 인스턴스 파괴시도 : fail
    #     # app_foo = None # QApplication 인스턴스 파괴시도 : fail
    #     app_foo.shutdown()  # QApplication 인스턴스 파괴시도 : success  # 성공요인은 app.shutdown()이 호출이 되면서 메모리를 해제까지 수행해주기 때문
    #     # sys.exit()
    # # return app_foo
    try:
        return GuiUtil.pop_up_as_complete(title="디버깅결과보고", ment=ment, input_text_default=input_text_default, auto_click_positive_btn_after_seconds=auto_click_positive_btn_after_seconds, btn_list=btn_list)
    except:
        print_red(traceback.print_exc())
        return None


# THIS IS BAD FUNCTION... I SHOULD CHECK TYPE, WHEN I MADE THIS
def get_display_info():
    func_n = inspect.currentframe().f_code.co_name
    pk_print(working_str=rf'''%%%FOO%%%''')
    # 디스플레이 정보 가져오기  # pyautogui.size?() 로 대체할것.
    global height, width
    for infos in get_monitors():
        for info in str(infos).split(','):
            if 'width=' in info.strip():
                width = info.split('=')[1]
            elif 'height=' in info.strip():
                height = info.split('=')[1]
    display_setting = {
        'height': int(height),  # todo : chore : ,(comma) 실수로 써놨는데 런타임에서 발견못한 문제
        'width': int(width)
    }
    return display_setting


def get_display_setting():
    func_n = inspect.currentframe().f_code.co_name
    pk_print(working_str=rf'''%%%FOO%%%''')
    height = ''
    width = ''
    for monitor_info in get_monitors():
        for info in str(monitor_info).split(','):
            if 'width=' in info.strip():
                width = info.split('=')[1]
            elif 'height=' in info.strip():
                height = info.split('=')[1]
    display_setting = {
        'height': int(height),
        'width': int(width)
    }
    return display_setting
