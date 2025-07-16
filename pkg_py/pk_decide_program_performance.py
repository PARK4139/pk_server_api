# -*- coding: utf-8 -*-  # todo : ref : python 3.x 하위버전 호환을 위한코드
__author__ = 'pk_system'

import inspect
import os
import time
from typing import TypeVar

from pk_core import get_f_current_n, pk_deprecated_get_d_current_n_like_person, get_tree_depth_level, get_pnx_list_with_mtime_without_f_list_to_exclude, kill_powershell_exe, get_token_from_txt_f, get_hostname, get_d_working, chcp_65001, get_os_n, kill_wsl_exe, LTA, print_function_run_measure_seconds_via_timeit
from pkg_py.pk_core import run_pk_release_server
from pkg_py.pk_colorful_cli_util import pk_print, print_red, print_yellow

from pkg_py.pk_core_constants import UNDERLINE, D_PKG_TXT, D_PROJECT

T = TypeVar('T')  # todo : ref : 타입 힌팅 설정

비교군1_결과 = None
비교군2_결과 = None

# todo control test loop limit
test_loop_limit = 1
is_first_test_lap = 1

@staticmethod
def print_measure_seconds_performance_nth_for_비교군1(function):
    """시간성능 측정용 코드 as 데코레이터"""
    func_n = inspect.currentframe().f_code.co_name

    # todo control wrapper arguments
    # def wrapper(*args, **kwargs):
    def wrapper(**kwargs):  # **kwargs, keyword argument, dictionary 로 parameter 를 받음. named parameter / positional parameter 를 받을 사용가능?
        # def wrapper(*args):# *args, arguments, tuple 로 parameter 를 받음.
        # def wrapper():
        pk_print(working_str=rf'''{UNDERLINE}{func_n}() %%%FOO%%%''', print_color='blue')
        pk_print(working_str=rf'''test_loop_limit="{test_loop_limit}" %%%FOO%%%''', print_color="blue")
        pk_print(working_str=rf'''is_first_test_lap="{is_first_test_lap}" %%%FOO%%%''', print_color="blue")
        if test_loop_limit == 1:
            is_first_test_lap = False
            # speak_ment(ment=ment, after_delay=1) # 너무느려
        seconds = []

        for i in range(0, test_loop_limit):
            pk_print(working_str=rf'''{UNDERLINE}{i} 번째 테스트 %%%FOO%%%''', print_color="blue")
            time_s = time.time()
            try:
                # todo : ref : set argument counts
                # function(*args, **kwargs)
                function(**kwargs)
                # function(*args)
                # function()

                time_e = time.time()
                mesured_seconds = time_e - time_s
                seconds.append(round(mesured_seconds, 2))
            except:
                pk_print(working_str=f'{UNDERLINE}예외발생 s\n\n', print_color="blue")
                pk_print(f'''{traceback.format_exc()} %%%FOO%%%''', print_color='red')
                pk_print(working_str=f'{UNDERLINE}예외발생 e\n\n', print_color="blue")

                pk_print(working_str=f'{UNDERLINE}[Debugging Note] s\n', print_color="blue")
                f_current= get_f_current_n()
                d_current=pk_deprecated_get_d_current_n_like_person()
                print_yellow(prompt=f'f_current={f_current}\n d_current={d_current}\n')
                pk_print(working_str=f'{UNDERLINE}[Debugging Note] e\n', print_color="blue")

                # ment = ment + f'{StateManageUNDERLINE_PROMISED}테스트 진행할 명령어를 입력하세요+++ s'
                # pk_print(ment=ment, print_color='blue')
                # hold_console()  # cmd /k
                ipdb.set_trace()  # 디버깅을 시작할 지점 # 파이썬 환경이 그대로 이어짐

        if len(seconds) == test_loop_limit:
            pk_print(f'''"{UNDERLINE}시간성능측정 테스트 결과 보고"''', print_color="blue")
            pk_print(working_str=rf'''test_loop_limit="{test_loop_limit}" %%%FOO%%%''', print_color="blue")
            pk_print(working_str=rf'''seconds={seconds} %%%FOO%%%''', print_color="blue")
            seconds_average = sum(seconds) / len(seconds)
            pk_print(working_str=rf'''seconds_average="{seconds_average}" %%%FOO%%%''', print_color="blue")
            global 비교군1_결과
            비교군1_결과 = {'test_loop_limit': test_loop_limit, 'seconds_average': seconds_average}
            is_first_test_lap = 1

    return wrapper


@staticmethod
def measure_seconds_performance_nth_for_비교군2(function):
    """시간성능 측정용 코드 as 데코레이터"""
    func_n = inspect.currentframe().f_code.co_name

    # todo : ref : set arguments
    # def wrapper(*args, **kwargs):
    def wrapper(**kwargs):  # **kwargs, keyword argument, dictionary 로 parameter 를 받음. named parameter / positional parameter 를 받을 사용가능?
        # def wrapper(*args):# *args, arguments, tuple 로 parameter 를 받음.
        # def wrapper():
        pk_print(working_str=rf'''{UNDERLINE}{func_n}() %%%FOO%%%''', print_color='blue')
        pk_print(working_str=rf'''test_loop_limit="{test_loop_limit}" %%%FOO%%%''', print_color="blue")
        pk_print(working_str=rf'''StateManageis_first_test_lap="{is_first_test_lap}" %%%FOO%%%''', print_color="blue")
        if is_first_test_lap:
            is_first_test_lap = False
            # speak_ment(ment=ment, after_delay=1) # 너무느려
        seconds = []
        for i in range(0, test_loop_limit):
            pk_print(working_str=rf'''{UNDERLINE}{i} 번째 테스트 %%%FOO%%%''', print_color="blue")
            time_s = time.time()
            try:
                # todo : ref : function argument setting
                # function(*args, **kwargs)
                function(**kwargs)
                # function(*args)
                # function()

                time_e = time.time()
                mesured_seconds = time_e - time_s
                # seconds_performance_test_results.append(f"{round(mesured_seconds, 2)}sec")
                seconds.append(round(mesured_seconds, 2))
            except:
                pk_print(working_str=f'{UNDERLINE}예외발생 s\n\n', print_color="blue")
                pk_print(f'''{traceback.format_exc()} %%%FOO%%%''', print_color='red')
                pk_print(working_str=f'{UNDERLINE}예외발생 e\n\n', print_color="blue")

                pk_print(working_str=f'{UNDERLINE}[Debugging Note] s\n', print_color="blue")
                f_current= get_f_current_n()
                d_current=pk_deprecated_get_d_current_n_like_person()
                print_yellow(prompt=f'f_current={f_current}\n d_current={d_current}\n')
                pk_print(working_str=f'{UNDERLINE}[Debugging Note] e\n', print_color="blue")

                # ment = ment + f'{StateManageUNDERLINE_PROMISED}테스트 진행할 명령어를 입력하세요+++ s'
                # pk_print(ment=ment, print_color='blue')
                # hold_console()  # cmd /k
                ipdb.set_trace()  # 디버깅을 시작할 지점 # 파이썬 환경이 그대로 이어짐

        if len(seconds) == test_loop_limit:
            pk_print(f'''"{UNDERLINE}시간성능측정 테스트 결과 보고"''', print_color="blue")
            pk_print(working_str=rf'''test_loop_limit="{test_loop_limit}" %%%FOO%%%''', print_color="blue")
            pk_print(working_str=rf'''seconds={seconds} %%%FOO%%%''', print_color="blue")
            seconds_average = sum(seconds) / len(seconds)
            pk_print(working_str=rf'''seconds_average="{seconds_average}" %%%FOO%%%''', print_color="blue")
            global 비교군2_결과
            비교군2_결과 = {'test_loop_limit': test_loop_limit, 'seconds_average': seconds_average}
            is_first_test_lap = 1

    return wrapper


@print_measure_seconds_performance_nth_for_비교군1
def run_비교군1():
    if not LTA:
        return

    if LTA:
        pass


@measure_seconds_performance_nth_for_비교군2
def run_비교군2():
    if not LTA:
        return

    if LTA:
        pass

def print_report_compared_functions_exec_time(function1, function2):
    function1()
    function2()
    pk_print(working_str=rf'''{UNDERLINE}비교군 코드 대조 %%%FOO%%%''', print_color='blue')
    pk_print(working_str=rf'''비교군1_결과="{비교군1_결과}" %%%FOO%%%''', print_color="blue")
    pk_print(working_str=rf'''비교군2_결과="{비교군2_결과}" %%%FOO%%%''', print_color="blue")
    # results = [
    #     비교군1_결과['seconds_average'],
    #     비교군2_결과['seconds_average'],
    # ]
    # fastest_time = min(results)
    # slowest_time = max(results)
    # fastest_time_index = results.index(fastest_time)
    # pk_print(string = rf'''slowest_time="{slowest_time}" %%%FOO%%%''', print_color="blue")
    # pk_print(string = rf'''fastest_time="{fastest_time}" %%%FOO%%%''', print_color="blue")
    # pk_print(string = rf'''fastest_time_index="{fastest_time_index}" %%%FOO%%%''', print_color="blue")
    results = {
        "비교군1_결과": 비교군1_결과['seconds_average'],
        "비교군2_결과": 비교군2_결과['seconds_average'],
    }
    fastest = min(results, key=results.get)
    pk_print(working_str=rf'''fastest="{fastest}" %%%FOO%%%''')
    pk_print(working_str=rf'''results[fastest]="{results[fastest]}" %%%FOO%%%''')
    pk_print(f'가장 빠른 시간은 "{fastest}" 입니다', print_color="blue")


def main():
    window_title_seg = rf"관리자: C:\WINDOWS\system32\cmd.exe"
    window_title_seg_for_cmd_as_admin = rf"관리자: C:\WINDOWS\system32\cmd.exe"

    hostname_ras_pi = get_token_from_txt_f(f_token=rf'{D_PKG_TXT}\token_hostname_ras_pi.txt', initial_token="")
    hostname_lg_gram = get_token_from_txt_f(f_token=rf'{D_PKG_TXT}\token_hostname_lg_gram.txt', initial_token="")
    hostname_desktop = get_token_from_txt_f(f_token=rf'{D_PKG_TXT}\token_hostname_desktop.txt', initial_token="")
    hostname_galaxy_book = get_token_from_txt_f(f_token=rf'{D_PKG_TXT}\token_hostname_galaxy_book.txt', initial_token="?????")  # todo
    hostname_xc_front = get_token_from_txt_f(f_token=rf'{D_PKG_TXT}\token_hostname_xc_front.txt', initial_token="")
    hostname_xc_rear = get_token_from_txt_f(f_token=rf'{D_PKG_TXT}\token_hostname_xc_rear.txt', initial_token="")
    hostname_mac = get_token_from_txt_f(f_token=rf'{D_PKG_TXT}\token_hostname_mac.txt', initial_token="")
    users_desktop_wsl = get_token_from_txt_f(f_token=rf'{D_PKG_TXT}\token_user_wsl_24.txt', initial_token="")
    users_desktop = get_token_from_txt_f(f_token=rf'{D_PKG_TXT}\token_users_desktop.txt', initial_token="")
    users_mac = get_token_from_txt_f(f_token=rf'{D_PKG_TXT}\token_users_mac.txt', initial_token="")
    pw_mac = get_token_from_txt_f(f_token=rf'{D_PKG_TXT}\token_pw_mac.txt', initial_token="")
    port_rdp_mac = int(get_token_from_txt_f(f_token=rf'{D_PKG_TXT}\token_port_rdp_mac.txt', initial_token="3390"))
    ip_private_lg_gram = get_token_from_txt_f(f_token=rf'{D_PKG_TXT}\token_ip_private_lg_gram.txt', initial_token="")
    ip_public_desktop = get_token_from_txt_f(f_token=rf'{D_PKG_TXT}\token_ip_public_desktop.txt', initial_token="")
    ip_private_control_pc = get_token_from_txt_f(f_token=rf'{D_PKG_TXT}\token_ip_private_control_pc.txt', initial_token="")
    ip_private_mac = get_token_from_txt_f(f_token=rf'{D_PKG_TXT}\token_ip_private_mac.txt', initial_token="")
    ip_private_acu_front = get_token_from_txt_f(f_token=rf'{D_PKG_TXT}\token_ip_private_xc_front.txt', initial_token="")
    ip_private_acu_rear = get_token_from_txt_f(f_token=rf'{D_PKG_TXT}\token_ip_private_xc_rear.txt', initial_token="")

    # todo : chore : etc
    # run_pk_system_info_collector()
    # monitor_target_edited_and_sync(pnx=)
    # get_comprehensive_weather_information_from_web()
    # print_sub_pnxs(src=rf"D:\#기타\pkg_files")
    # print_from_pnxs_to_semantic_words(pnx = rf"D:\#기타\pkg_files")
    # close_chrome_tab_duplicated()# 중복탭 닫기
    # reconnect_to_qcy_h3_anc_headset_via_bluetooth()
    # reconnect_to_wifi()
    # command_to_os(commands="rundll32.exe user32.dll,LockWorkStation") #화면잠금
    # sleep(min=50, show_mode=True) # console 에  # 카운트다운이 되면서 출력이 되도록 하자.
    # reconnect_to_qcy_h3_anc_headset_via_bluetooth()
    # reconnect_to_wifi()
    # sleep(min=50, show_mode=True) # console 에  #   카운트다운이 되면서 출력이 되도록 하자.
    # ask_to_chat_gpt(question="가 뭐야?") # 질문하기
    # test_string_handling()
    # test_wsl_util() #타겟 제어
    # test_explorer_util() # 타겟 탐색
    # ipdb.set_trace()

    # todo : chore : tool
    # print_as_cli(f'''last_digit = {get_last_digit(search_keyword = "1080 삼시세끼 Light E07")}''') # last digit 파싱
    # organize_duplicated_hashed_texts_via_user_input() # 해시테그 오름차순 정리
    # sum_via_text_file() # 합 연산
    # speak_ment_experimental(ment='제 이름은 알바생입니다', comma_delay=0.43, thread_join_mode=True)
    # speak_ment_experimental(ment=f'{get_time_as_('%H')}시 입니다', comma_delay=0.43, thread_join_mode=True)
    # speak_ment_experimental(ment='내일 너무 피곤할 거에요, 내일 몸이 너무 힘들 수도 있어요', comma_delay=0.43, thread_join_mode=True)
    # speak_ment_experimental(ment='건강을 위해서 자는 것이 좋습니다', comma_delay=0.43, thread_join_mode=True)
    # speak_ment_experimental(ment='후회를 줄이기 위해서는, 그만 자라', comma_delay=0.43, thread_join_mode=True)
    # speak_ment_experimental(ment='스스로를 돌보는일은, 중요한 일일까요?', comma_delay=0.43, thread_join_mode=True)
    # speak_today_time_info()
    # should_i_do(ment="알송을 종료할까요?", function=partial(taskkill, 'ALSong.exe'),  auto_click_negative_btn_after_seconds=15)
    # windows_shutdown(seconds=60)
    # UiUtil.pop_up_as_complete(title_="모니터링감지보고", ment="test", auto_click_positive_btn_after_seconds=3)

    # todo : chore : start
    # 시프티
    # token_shifty
    # should_i_do    하고
    # 토큰 없으면 생성
    # 토큰으로 값이 오늘이면 패스
    # 토큰으로 값이 오늘이면 업데이트

    # todo : chore : 장치 제어
    # ssh(users=users_mac, ip=ip_private_mac, wsl_linux_version=wsl_linux_version, wsl_window_title_seg=f"{users_desktop_wsl}@{HOSTNAME}", pw=pw_mac, exit_mode=False)
    # ping(ip=ip_private_mac)
    # command_to_remote_os(command=rf'sudo reboot', users=users_mac, ip=ip_private_mac, wsl_linux_version=wsl_linux_version, wsl_window_title_seg=f"{users_desktop_wsl}@{HOSTNAME}", pw=pw_mac, exit_mode=False)
    # command_to_remote_os(command=rf'sudo poweroff', users=users_mac, ip=ip_private_mac, wsl_linux_version=wsl_linux_version, wsl_window_title_seg=f"{users_desktop_wsl}@{HOSTNAME}", pw=pw_mac, exit_mode=False)
    # ping(ip=ip_private_mac)
    # mstsc(ip = ip_private_mac, port=port_rdp_mac)
    # remmina(users=users_mac, ip=ip_private_mac, wsl_linux_version=wsl_linux_version, wsl_window_title_seg=f"{users_desktop_wsl}@{HOSTNAME}", pw=pw_mac, exit_mode=False)
    # xfreerdp(users=users_mac, ip=ip_private_mac, wsl_linux_version=wsl_linux_version, wsl_window_title_seg=f"{users_desktop_wsl}@{HOSTNAME}", pw=pw_mac, exit_mode=False)
    # install_chrome_remote_desktop_server_to_remote_os(users=users_mac, ip=ip_private_mac, wsl_linux_version=wsl_linux_version, wsl_window_title_seg=f"{users_desktop_wsl}@{HOSTNAME}", pw=pw_mac, exit_mode=False)
    # install_chrome_remote_desktop_client_to_remote_os(users=users_mac, ip=ip_private_mac, wsl_linux_version=wsl_linux_version, wsl_window_title_seg=f"{users_desktop_wsl}@{HOSTNAME}", pw=pw_mac, exit_mode=False)
    # chrome_remote_desktop(hostname = hostname) # todo GPU 없는 장비는 사용불가, pin 입력 로직 검토필요
    # teamviewer(hostname = hostname) # todo
    # send_pkg_to_house_to_pk_system_release_server() # todo

    # todo : chore : 빌드
    # build_console_blurred() # todo build 시 테스트
    # %%%FOO%%% 부분 autofill dev tool 적용 # todo

    # todo : chore : 업로드
    # token_gitlab_repo_url = get_token_from_text_file(token_file=rf'{PKG_TXT}\token_gitlab_repo_url.txt', initial_token="")
    # commit_ment = "test:initial git push test"
    # commit_ment = "fix: run_release_server() "
    # upload_pnx_to_git(git_repository_url=token_gitlab_repo_url, commit_msg=commit_ment)

    # todo : chore : 퇴근
    # change_os_to_screen_saver()
    # # back_up_pnxs_via_func_n_txt(dst =rf"{DOWNLOADS}\deprecated")
    # make_pkg(dst = rf'{DESKTOP}\pkg')
    # # change_os_to_screen_locked() # 화면 잠금
    # # sleep(hours=1)
    # sleep(minutes=10)
    # change_os_to_power_saving_mode()
    # # change_os_to_shutdown(seconds=60)
    # # change_os_to_shutdown(mins=3)
    # # change_os_to_shutdown(restart_mode=True)
    # # change_os_to_shutdown()
    # should_i_enter_to_power_saving_mode()

    # todo : chore : tool
    # run_pk_release_server(port=9090) # todo with linux/fastapi
    # git_push_via_hard_code()  # todo git push 자동화
    # send_pkg_to_house_to_pk_system_release_server()
    # build_console_blurred() # todo build 자동화
    # shutdown_pnx(process_name="python.exe")
    # shutdown_pnx(process_name="alsong.exe")
    # shutdown_pnx(process_name="cortana.exe")
    # shutdown_pnx(process_name="mysqld.exe")
    # shutdown_pnx(process_name="KakaoTalk.exe")
    # shutdown_pnx(process_name="OfficeClickToRun.exe")
    # shutdown_pnx(process_name="TEWebP.exe")
    # shutdown_pnx(process_name="TEWeb64.exe")
    # shutdown_pnx(process_name="TEWebP64.exe")
    # shutdown_pnx(process_name="AnySign4PC.exe")
    # shutdown_pnx(process_name="alsong.exe")
    # shutdown_pnx(process_name="ALSong.exe")
    # shutdown_pnx(process_name="chrome.exe")
    # shutdown_pnx(process_name="PotPlayer64.exe")
    # shutdown_pnx(process_name="utorrent.exe")
    # shutdown_pnx(process_name="cmd.exe")
    # rerun_pnx(my_name='알송')
    # run_pnxs_via_text_file()
    # run_parrot()
    # run_voice_note()
    pass


if __name__ == '__main__':
    try:
        # ___________________________________________________________________________
        # todo : ref : 평균시간 측정 via timeit
        
        print_function_run_measure_seconds_via_timeit(function=main, repeat=1)

        # todo : ref : 비교군 간 비교
        # function1 = run_비교군1
        # function2 = run_비교군2
        # compare_mean_times(function1=function1, function2=function2)

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


class CustomErrorUtil(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class DataStructureUtil:
    @staticmethod
    def get_list_added_elements_alternatively(list_for_odd, list_for_even):  # from [1, 2, 3] + [ x, y, z] to [1,x,2,y,3,z]
        """
        두 리스트를 더할때 사용하는 함수
        list, ndarray 모두 사용이 가능한 함수이다.

        result = get_list_added_elements_alternatively(list1 = [1, 2, 3], list_to_added_as_even_order = ['x', 'y', 'z'])
        """
        result = []
        for i in range(len(list_for_odd)):
            result.append(list_for_odd[i])
            if i < len(list_for_even):
                result.append(list_for_even[i])
        return result

    @staticmethod
    def print_list_each_two_elements(list: []):  # print(rf'list[index] list[index+1] : {list[index]} {list[index+1]}') without out of index
        for index, item in enumerate(list):  # enumerate 로 리스트의 원소를 2개씩 출력
            if index + 1 < len(list):
                print(rf'list[index] list[index+1] : {list[index]} {list[index + 1]}')

    @staticmethod
    def get_list_each_two_elements_joined(list: []):  # from ["a", "b", "c", "d"] to ["ab", "cd"]
        return [f"{list[i]}{list[i + 1]}" for i in range(0, len(list), 2)]

    @staticmethod
    def get_nested_list_grouped_by_each_two_elements_in_list(list: []):  # from ["a", "b", "c", "d"] to [["a","b"], ["c","d"]]
        result = []
        for i in range(0, len(list), 2):
            if i + 1 < len(list):
                result.append([list[i], list[i + 1]])
        return result

    @staticmethod
    def get_column_of_2_dimension_list(list_2_dimension: [], column_no):  # return 은 list 아니고 ndarray 일 수 있다
        import numpy as np
        arr = np.array(list_2_dimension)
        second_column = arr[:, column_no]
        print(second_column)

    @staticmethod
    def get_nested_list_converted_from_ndarray(ndarray):  # np.ndarray # ndarray 에서 list 로 변환 # ndarray 에서 list 로 변환 # ndarray to nested []  from [[1 2]] to [[1, 2]] # from [ [str str] [str str] ]  to  [ [str, str], [str, str] ]
        return ndarray.tolist()

    @staticmethod
    def get_nested_list_sorted_by_column_index(nested_list: [[str]], column_index: int, decending_order=False):  # tree depth(sample[1]) 에 대한 내림차순 정렬 # list 2차원 배열의 특정 열의 내림차순 정렬 # from [[str, str]] to [[str, str]]
        """
         중첩리스트를 첫 번째 행을 기준으로 내림차순으로 정렬
         from
         [
             [ 1 a z ]
             [ 7 a b ]
             [ 4 a c ]
         ]
         to
         [
             [ 7 a b ]
             [ 4 a c ]
             [ 1 a z ]
         ]
         튜플도 된다
         from
         [
             ( 1 a z )
             ( 7 a b )
             ( 4 a c )
         ]
         to
         [
             ( 7 a b )
             ( 4 a c )
             ( 1 a z )
         ]
        """

        def bubble_sort_nested_list(nested_list, column_index):
            """버블 소팅 테스트"""
            if type(nested_list[0][column_index]) == float:
                column_index = int(column_index)
                n = len(nested_list)
                for i in range(n):
                    for j in range(0, n - i - 1):
                        if decending_order == True:
                            if int(str(nested_list[j][column_index]).replace(".", "")) < int(str(nested_list[j + 1][column_index]).replace(".", "")):
                                nested_list[j], nested_list[j + 1] = nested_list[j + 1], nested_list[j]
                        elif decending_order == False:
                            if int(str(nested_list[j][column_index]).replace(".", "")) > int(str(nested_list[j + 1][column_index]).replace(".", "")):
                                nested_list[j], nested_list[j + 1] = nested_list[j + 1], nested_list[j]
                return nested_list
            elif type(nested_list[0][column_index]) == int or nested_list[0][column_index].isdigit():  # 에고 힘들다. 머리아팠다
                column_index = int(column_index)
                n = len(nested_list)
                for i in range(n):
                    for j in range(0, n - i - 1):
                        if decending_order == True:
                            if int(nested_list[j][column_index]) < int(nested_list[j + 1][column_index]):
                                # print(rf'{nested_list[j][column_index]}>{nested_list[j + 1][column_index]}')
                                # print(rf'nested_list[j][column_index] > nested_list[j+1][column_index] : {int(nested_list[j][column_index]) > int(nested_list[j+1][column_index])}')
                                nested_list[j], nested_list[j + 1] = nested_list[j + 1], nested_list[j]
                        elif decending_order == False:
                            if int(nested_list[j][column_index]) > int(nested_list[j + 1][column_index]):
                                # print(rf'{nested_list[j][column_index]}>{nested_list[j + 1][column_index]}')
                                # print(rf'nested_list[j][column_index] > nested_list[j+1][column_index] : {int(nested_list[j][column_index]) > int(nested_list[j+1][column_index])}')
                                nested_list[j], nested_list[j + 1] = nested_list[j + 1], nested_list[j]
                return nested_list
            elif type(nested_list[0][column_index]) == str:
                column_index = int(column_index)
                n = len(nested_list)
                for i in range(n):
                    for j in range(0, n - i - 1):
                        if decending_order == True:
                            if nested_list[j][column_index] < nested_list[j + 1][column_index]:
                                # print(rf'{nested_list[j][column_index]}>{nested_list[j + 1][column_index]}')
                                # print(rf'nested_list[j][column_index] > nested_list[j+1][column_index] : {int(nested_list[j][column_index]) > int(nested_list[j+1][column_index])}')
                                nested_list[j], nested_list[j + 1] = nested_list[j + 1], nested_list[j]
                        if decending_order == False:
                            if nested_list[j][column_index] > nested_list[j + 1][column_index]:
                                # print(rf'{nested_list[j][column_index]}>{nested_list[j + 1][column_index]}')
                                # print(rf'nested_list[j][column_index] > nested_list[j+1][column_index] : {int(nested_list[j][column_index]) > int(nested_list[j+1][column_index])}')
                                nested_list[j], nested_list[j + 1] = nested_list[j + 1], nested_list[j]
                return nested_list

        return bubble_sort_nested_list(nested_list, column_index)

    @staticmethod
    def get_nested_list_removed_row_that_have_nth_element_dulplicated_by_column_index_for_ndarray(ndarray: [[]], column_index: int):  # 중복된 행 제거하는게 아니고 행의 2번째 요소가 중복되는 것을 제거
        seen = set()
        unique_rows = []
        for row in ndarray:
            if row[column_index] not in seen:
                unique_rows.append(row)
                seen.add(row[column_index])
        return unique_rows

    @staticmethod
    def get_nested_list_removed_row_that_have_nth_element_dulplicated_by_column_index(nested_list: [[]], column_index: int):  # 중복된 행 제거하는게 아니고 행의 2번째 요소가 중복되는 것을 제거
        seen = set()  # 중복된 행의 두 번째 요소를 추적하기 위한 집합(set) 생성
        unique_rows = []
        for row in nested_list:
            if row[column_index] not in seen:
                unique_rows.append(row)  # 중복된 행의 두 번째 요소가 중복되지 않는 행들만 추출하여 unique_rows 리스트에 추가
                seen.add(row[column_index])
        return unique_rows  # 중복된 행의 두 번째 요소가 중복되지 않는 행들만 남게 됩니다.

    @staticmethod
    def get_list_seperated_by_each_elements_in_nested_list(nested_list):
        return [item for sublist in nested_list for item in sublist]

    @staticmethod
    def is_two_lists_equal(list1, list2):
        from pkg_py.pk_core_constants import UNDERLINE, D_PROJECT 
        from pk_colorful_cli_util import pk_print
        func_n = inspect.currentframe().f_code.co_name
        pk_print(working_str=rf'''{UNDERLINE}{func_n}() %%%FOO%%%''')
        # 두 리스트의 요소들이 동일한지만 확인 # 하나라도 발견되면 탐색 중지 # 두 리스트의 동일 인덱스에서 진행하다 달라도 다른거다
        if len(list1) != len(list2):
            print(f"두 리스트의 줄 수가 다릅니다 {len(list1)}, {len(list2)}")
            return False
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                print(f"두 리스트의 같은 인덱스 중 다른 리스트 발견={list1[i]}, {list2[i]}")
                return False
        return True

    @staticmethod
    def get_elements_that_list1_only_have(list1, list2):  # 두 개의 리스트를 비교하여 특정 하나의 리스트 만 가진 요소만 모아서 리스트로 출력
        unique_elements_of_list1 = []
        for element in list1:
            if element not in list2:
                unique_elements_of_list1.append(element)
        return unique_elements_of_list1

    @staticmethod
    def get_different_elements(list1, list2):  # 두 개의 리스트를 비교하여 서로 다른 요소만 모아서 리스트로 출력
        different_elements = []
        # 두 리스트 중 더 긴 리스트의 길이를 구합니다.
        max_length = max(len(list1), len(list2))
        # 범위는 더 긴 리스트의 길이로 설정합니다.
        for i in range(max_length):
            # 리스트의 인덱스가 범위 내에 있는지 확인 후 비교합니다.
            if i < len(list1) and i < len(list2):
                if list1[i] != list2[i]:
                    different_elements.append(list1[i])
            else:
                # 한 리스트는 범위를 벗어났으므로 해당 요소를 추가합니다.
                if i >= len(list1):
                    different_elements.append(list2[i])
                else:
                    different_elements.append(list1[i])
        # 위의 코드는 5 초 경과

        different_elements = []
        # set1 = set(list1)  # list to set
        # set2 = set(list2)
        # different_elements = list(set1.symmetric_difference(set2))
        # 위의 코드는 12 초 경과
        return different_elements

    @staticmethod
    def get_common_elements(list1, list2):  # 두 개의 리스트를 비교하여 서로 동일한 요소만 새로운 리스트로 출력 # 중복값 색출
        common_elements = []
        for element in list1:
            if element in list2:
                common_elements.append(element)
        return common_elements

    @staticmethod
    def add_suffix_to_string_list(string_list, suffix):
        result = []
        for string in string_list:
            result.append(string + suffix)
        return result

    @staticmethod
    def add_prefix_to_string_list(string_list, prefix):
        result = []
        for string in string_list:
            result.append(prefix + string)
        return result


class PkProgramPerformanceOptimizingUtil:
    @staticmethod
    def generate_mp3_file_for_time_performance():  # time performance : 9028 초 /60 /60  =  2.5 시간
        """
        deprecated
        시간에 대한 mp3 파일 미리 만들어 놓음으로 생성시간 저감 기대 > speaks() 메소드 최적화
        """
        for HH in range(24, 0, -1):
            for mm in range(0, 60):
                pk_print(f'{int(HH)}시')
                pk_print(f'{int(mm)}분 입니다')

    @staticmethod
    def gen_dictionary_for_monitor_pnx_edited_and_back_up(directory_pnx):
        r"""
        deprecated
        monitor_target_edited_and_back_up() 성능개량용 코드
        lzw 알고리즘 딕셔너리 생성용 성능개량용 코드 > 이건 추후에 생각해보기로
        딕셔너리 업데이트 필요한 경우에 사용해서 콘솔에 출력된 딕셔너리 초기화용 코드를
        딕셔너리를 코드베이스에 하드코딩하여 사용

        생성된 딕셔너리 코드 예시
        dictionary_based_on_tri_structure = [
            "{PROJECT_D}\pkg_font\Montserrat\static",
            "{PROJECT_D}\pkg_font\Noto_Sans_KR\static",
            "{PROJECT_D}\pkg_font\GmarketSans",
            "{PROJECT_D}\pkg_font\Montserrat",
            "{PROJECT_D}\pkg_font\Noto_Sans_KR",
            "{PROJECT_D}\pkg_font\Poppins",
            "{PROJECT_D}\pkg_yaml",
            "{PROJECT_D}",
        ]
        """
        current_directory_state = get_pnx_list_with_mtime_without_f_list_to_exclude(d_src=directory_pnx)  # str to dict
        current_directory_state = [f"{key}" for key, value in current_directory_state.items()]  # from dict to ["key\n"]   # 이건 함수는 테스트해보고, # noqa 처리 해야할 듯
        print(rf'type(current_directory_state) : {type(current_directory_state)}')
        print(rf'len(current_directory_state) : {len(current_directory_state)}')

        current_pnxs = current_directory_state
        # current_pnxs = current_directory_state[0:100]  # 샘플 100개만 테스트
        dirnames = [os.path.dirname(item) for item in current_pnxs]  # 파일 dirname 목록
        tree_levels = [get_tree_depth_level(item) for item in current_pnxs]  # 파일시스템 트리깊이레벨 목록
        dirnames_and_trees = DataStructureUtil.get_list_added_elements_alternatively(dirnames, tree_levels)  # from [][] to []
        dirnames_and_trees = DataStructureUtil.get_nested_list_grouped_by_each_two_elements_in_list(dirnames_and_trees)
        dirnames_and_trees = DataStructureUtil.get_nested_list_sorted_by_column_index(nested_list=dirnames_and_trees, column_index=1, decending_order=True)  # tree depth를 의미하는 column_index=1 에 대한 내림차순 정렬
        dirnames_and_trees = DataStructureUtil.get_nested_list_removed_row_that_have_nth_element_dulplicated_by_column_index(nested_list=dirnames_and_trees, column_index=0)  # from [[]] to [[]] # from [[1 2]] to [[1, 2]] # from [ [str str] [str str] ]  to  [ [str, str], [str, str]]
        dirnames = [x[0] for x in dirnames_and_trees]  # dirnames_and_trees 의 첫번째 컬럼인 dirname 만 추출
        pk_print("딕셔너리 초기화용 코드 시작")
        print("dictionary_based_on_tri_structure = {")
        [print(rf'    r"{dirname}":"{index}빠릿{index}" ,') for index, dirname in enumerate(dirnames)]
        print("}")
        # print(rf'dirnames : {dirnames}')
        print(rf'type(dirnames) : {type(dirnames)}')
        print(rf'len(dirnames) : {len(dirnames)}')
        pk_print("딕셔너리 초기화용 코드 종료")
        # ipdb.set_trace()

    dictionary_for_monitoring_performance = {
        r"{PROJECT_D}\pkg_font\Montserrat\static": "이거지1",
        r"{PROJECT_D}\pkg_font\Noto_Sans_KR\static": "이거지2",
        r"{PROJECT_D}\pkg_font\GmarketSans": "이거지3",
        r"{PROJECT_D}\pkg_font\Montserrat": "이거지4",
        r"{PROJECT_D}\pkg_font\Noto_Sans_KR": "이거지5",
        r"{PROJECT_D}\pkg_font\Poppins": "이거지6",
        r"{PROJECT_D}\pkg_yaml": "이거지7",
        r"{PROJECT_D}": "이거지8",
    }

    @staticmethod
    def replace_words_based_on_tri_node(text, dictionary):
        """
        # 사용 예시
        dictionary = ["apple", "banana", "orange"]
        text = "I like apple and banana."
        replaced_text = replace_words(text, dictionary)
        print(replaced_text)
        """

        class TrieNode:
            def __init__(self):
                self.children = {}  # 자식 노드를 저장하는 딕셔너리
                self.is_end_of_word = False  # 단어의 끝인지 나타내는 플래그

        class Trie:
            def __init__(self):
                self.root = TrieNode()  # 루트 노드 생성

            def insert(self, word):
                current_node = self.root
                for char in word:
                    if char not in current_node.children:
                        current_node.children[char] = TrieNode()
                    current_node = current_node.children[char]
                current_node.is_end_of_word = True

            def search(self, word):
                current_node = self.root
                for char in word:
                    if char not in current_node.children:
                        return False
                    current_node = current_node.children[char]
                return current_node.is_end_of_word

        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        words = text.split()
        replaced_words = []
        for word in words:
            if trie.search(word):
                replaced_words.append("REPLACED")
            else:
                replaced_words.append(word)

        return " ".join(replaced_words)

# class FastapiUtil:
#
#     # try:
#     # services_directory_pnx = os.path.dirname(os.path.dirname(__file__))
#     # external_pkg_pnx = rf'{services_directory_pnx}\archive_py\pkg_alba'
#     # print(rf'external_pkg_pnx : {external_pkg_pnx}')
#     # os.environ['pkg_alba_pnx'] = rf'{external_pkg_pnx}'
#     # sys.path.append(external_pkg_pnx)
#     # print(rf'sys.path : {sys.path}')
#     # except:
#     #     pass
#     # try:
#     # 대안 global pkg 로 복사하고 쓰고 exec 후에는 프로젝트 내에서 패키지를 삭제한다 > 자동화할것
#     # 의존성을 추가하기 위해서, pkg_alba의 .venv 도 따라 복사한다.
#     # CURRENT_PROJECT_D= os.path.dirname(__file__)
#     # SERVICES_DIRECTORY = os.path.dirname(CURRENT_PROJECT_D)
#     # EXTERNAL_PKG_pnx = rf'{SERVICES_DIRECTORY}\archive_py\pkg_alba'
#     # # VIRTUAL_PKG_pnx = rf'{CURRENT_PROJECT_D}\.venv\Lib\site-packages'
#     # INTERNAL_PKG_pnx = rf'{CURRENT_PROJECT_D}\pkg_alba'
#     # print(rf'VIRTUAL_PKG_pnx : {INTERNAL_PKG_pnx}')
#     # os.system(rf'chcp 65001')
#     # os.system(rf'robocopy "{EXTERNAL_PKG_pnx}" "{INTERNAL_PKG_pnx}" /MIR')
#     # # os.system("pause")
#     # except Exception:
#     #     sys.exit()
#     # try:
#     # 그냥 pkg 내에 집어 넣었다. 가상환경도 동일하게 개발한다.
#     # except:
#     #     pass
#     # pass
#
#     @staticmethod
#     def convert_file_from_cp_949_to_utf_8(f_pnx):
#         # file_pnx_converted = rf"{get_target_as_pn(f_pnx)}_utf_8{get_target_as_x(f_pnx)}"
#         # print(file_pnx_converted)
#         # # 기존 파일을 'utf-8'로 읽어오고, 새로운 파일에 'utf-8'로 저장
#         # with codecs.open(f_pnx, 'r', encoding='cp949') as file_previous:
#         #     contents = file_previous.read()
#         #     with codecs.open(file_pnx_converted, 'w', encoding='utf-8') as new_file:
#         #         new_file.write(contents)
#         pass
#
#     @staticmethod
#     def init_cors_policy(app):
#         # dev
#         # op 에서는 이 함수는 사용하면 않기로 결정, nginx 에서 CORS 설정을 할 것 이므로
#         # CORS 두개 설정하면 multi header 로 인한 Control-Allow-Origin' header contains multiple values '*, https://www.pjh4139.store', but only one is allowed. 에러가 발생할 것이다.
#         app.add_middleware(
#             # success, fastapi CORS allow_origins 동적 할당은 대안 못찾았고, # 초기 origins 값을 와일드카드로 설정
#             CORSMiddleware,  # 노란줄 원인 뭘까? #_noqa 를 적용해야 할지 고민 중
#             allow_credentials=True,  # cookie 포함 여부를 설정. 기본은 False
#             allow_origins=['*'],
#             allow_methods=["*"],  # 허용할 method를 설정할 수 있으며, 기본값은 'GET'이다. OPTIONS request ?
#             allow_headers=["*"],  # 허용할 http header 목록을 설정할 수 있으며 Content-Type, Accept, Accept-Language, Content-Language은 항상 허용된다.
#
#             # try, 보안강화
#             # fastapi CORS allow_origins 정적 할당 # 톳시하나 틀리면 안됨.
#             # allow_origins=[,
#             #     # "http://localhost",  # fail
#             #     # "http://localhost/",  # fail
#             #     # "http://localhost:3000",# success
#             #     "http://localhost:3000/service-dev-diary",
#             #     # "http://127.0.0.1:3000",#
#             #     "https://e-magazine-jung-hoon-parks-projects.vercel.app",
#             #     # "https://e-magazine-jung-hoon-parks-projects.vercel.app/",
#             #     "https://e-magazine-jung-hoon-parks-projects.vercel.app/````````````````````",
#             # ],
#         )
#
#     @staticmethod
#     def init_Logging_via_middleware(app):
#         # 미들웨어를 통한 로깅
#         # @app.middleware("http")
#         # async def log_requests(request: Request, call_next):
#         #     logging.debug(f"요청: {request.method} {request.url}")
#         #     response = await call_next(request)
#         #     logging.debug(f"응답: {response.status_code}")
#         #     return response
#         pass
#
#     @staticmethod
#     def init_domain_address_allowed(app):
#         # 접속허용도메인 주소 제한, 이 서버의 api 를 특정 도메인에서만 호출 가능하도록 설정
#         # @app.middleware("http")
#         # async def domain_middleware(request: Request, call_next):
#         #     allowed_domains = ["example.com", "subdomain.example.com"]
#         #     client_host = request.client.host
#         #     client_domain = client_host.split(":")[0]  # 도메인 추출
#         #     if client_domain not in allowed_domains:
#         #         raise HTTPException(status_code=403, detail="Forbidden")
#         #     response = await call_next(request)
#         #     return response
#         pass
#
#     @staticmethod
#     def init_ip_address_allowed(app):
#         # 접속허용IP 주소 제한
#         # @app.middleware("http")
#         # async def ip_middleware(request: Request, call_next):
#         #     allowed_ips = [
#         #         "127.0.0.1",
#         #         "10.0.0.1",
#         #     ]
#         #     client_ip = request.client.host
#         #     if client_ip not in allowed_ips:
#         #         raise HTTPException(status_code=403, detail="Forbidden")
#         #     response = await call_next(request)
#         #     return response
#         pass
#
#     @staticmethod
#     async def preprocess_after_request(request):
#         # pk_print(f"{str(request.url)} 로 라우팅 시도 중...")
#         pass
#
#     @staticmethod
#     async def preprocess_before_response_return(request, response):
#         # pk_print(f"{str(request.url)} 로 라우팅 되었습니다")
#         pass
#
#     @staticmethod
#     def init_and_update_json_file(json_file, objects=None):
#
#
#
#         if objects is None:
#             objects = []
#         try:
#             make_pnx(pnx=json_file, mode="f")
#             if os.path.exists(json_file):
#                 if is_letters_cnt_zero(pnx=json_file) == True:
#                     write_str_to_f(pnx=json_file, txt_str="[]\n")  # 이러한 형태로 객체를 받을 수 있도록 작성해 두어야 받을 수 있음.
#                 else:
#                     if not os.path.isfile(json_file):
#                         with open(json_file, "w", encoding='utf-8') as f:
#                             # json.dump(objects, f, ensure_ascii=False)  # ensure_ascii=False 는 encoding 을 그대로 유지하는 것 같다. ascii 로 변환하는게 안전할 지도 모르겠다.
#                             json.dump(objects, f)  # ensure_ascii=False 는 encoding 을 그대로 유지하는 것 같다. ascii 로 변환하는게 안전할 지도 모르겠다.
#                     else:
#                         with open(json_file, "r", encoding='utf-8') as f:
#                             # print_ment_via_colorama(f"{BOOKS_FILE} 업로드 되었습니다", colorama_color=ColoramaColorUtil.LIGHTWHITE_EX)
#                             objects = json.load(f)
#                         return objects
#         except IOError as e:
#             print("파일 작업 중 오류가 발생했습니다:", str(e))
#
#     @staticmethod
#     def test_client_post_request():  # test 자동화 용도
#         url = "https://store/api/volatile/items"
#         url = "https://store/api/db-json/items"
#         url = "https://store/api/db-maria/items"
#
#         # 저장할 데이터
#         data = {
#             "name": "John Doe",
#             "email": "johndoe@example.com",
#             "password": "password",
#         }
#         # 데이터를 JSON 문자열로 변환합니다.
#         json_data = json.dumps(data)
#
#         # POST 요청을 생성합니다.
#         headers = {"Content-Type": "application/json"}
#         response = requests.post(url, headers=headers, data=json_data)
#
#         # 응답을 확인합니다.
#         if response.status_code == 201:
#             print("데이터가 성공적으로 저장되었습니다.")
#         else:
#             print("데이터 저장에 실패했습니다.")
#
#     # Pydantic은 Python의 데이터 유효성 검사 및 직렬화를 위한 라이브러리,
#     # BaseModel은 Pydantic에 built in 되어 있다,
#     # 데이터 모델을 정의하고 유효성을 검사하며 직렬화/역직렬화를 수행하는 기능을 제공합니다
#     # auto increment 하고 싶어 pydantic model 로 구현
#     class Board(BaseModel):
#         id: int = uuid4().hex  # 수정대기
#         title: str
#         content: str
#
#         class Config:
#             populate_by_name = True
#
#     @staticmethod
#     def is_board_validated(board: Board) -> bool:
#         # Board(게시물)의 유효성을 검사하는 커스텀 비지니스 로직을 구현, create/update 의 경우에 사용
#         if not board.title:
#             return False
#         if not board.content:
#             return False
#         return True
#
#     class Book(BaseModel):  # BaseModel 를 상속받은 Book 은 일반적인 객체가 아니다. type 을 출력해봐도 pydantic 의 하위 객체를 상속한 것으로 보인다
#         id: Optional[str] = uuid4().hex  # Optional 을 설정하면 nullable 되는 거야? # 여기서 할당을 시키면 put() 동작하며 id가 바뀌어버린다. put()에서 업데이트되도록 따로 설정했다.
#         name: str
#         genre: Literal["러브코메디", "러브픽션", "액션"]  # string literal validation 설정, 이 중 하나만 들어갈 수 있음
#         # price: float
#         price: int
#
#     class TodoItem(BaseModel):
#         id: str
#         title: str
#         completed: bool
#
#     class User(BaseModel):  # 여기에 validation 해두면 docs에서 post request 시 default 값 지정해 둘 수 있음.
#
#
#
#
#         id: str = uuid4().hex + get_time_as_('%Y%m%d%H%M%S%f') + get_random_alphabet()  # 진짜id 는 이렇게 default 로 들어가게하고, 사용자 id 는 e-mail
#         pw: str
#         name: str
#         date_join: str = get_time_as_('%Y-%m-%d %H:%M %S%f')
#         date_logout_last: str
#         address_house: str
#         address_e_mail: str
#         number_phone: str
#
#         # @classmethod
#         @field_validator('id')
#         def validate_id(cls, id):
#             if 53 < len(id) or 53 < len(id):
#                 return {"fail", "id 는 53 자리 이상 이거나 이하 일 수 없습니다"}
#             return id
#
# #         @classmethod
#         @field_validator('pw')
#         def validate_pw(cls, pw):
#             # 다시 작성
#             return pw
#
# #         @classmethod
#         @field_validator('name')
#         def validate_name(cls, name):
#             if 30 < len(name):
#                 return {"fail", "name 은 30 자리 이상 일 수 없습니다"}
#             return name
#
#         @classmethod  # class 간 종속 관계가 있을 때 하위 class 에 붙여 줘야하나?, cls, 파라미터와 함께? , instance를 생성하지 않고 호출 가능해?
#         @field_validator('date_join')
#         def validate_date_join(cls, date_join):
#             # datetime.strptime(date_join, '%Y-%m-%d %H:%M %S%f')
#             # 다시 작성
#             return date_join
#
#         @classmethod
#         @field_validator('address_e_mail')
#         def validate_address_e_mail(cls, address_e_mail):
#             # 다시 작성
#             return address_e_mail
#
#     class LoginForm(BaseModel):
#         id: str
#         pw: str
#
#     class JoinForm(BaseModel):  # 회원가입 유효성검사 설정
#         id: str  # 필수항목
#         pw: str
#         pw2: str
#         name: str
#         pw: str
#         phone_no: str
#         address: str
#         e_mail: str
#         age: str
#         birthday: str
#         date_joined: Optional[str]  # nullable
#         date_canceled: Optional[str]
#         fax_no: Optional[str]
#         business_registration_no: Optional[str]
#         company_name: Optional[str]
#         department: Optional[str]
#         position: Optional[str]
#         company_address: Optional[str]
#
#     class jinja_data(BaseModel):  # 모든 데이터를 수집하고, Optional 로 할당.
#         id: Optional[str]  # nullable
#         pw: Optional[str]
#         prefix_promised: Optional[str]
#         random_bytes: Optional[str]
#         random_str: Optional[str]
#         pw2: Optional[str]
#         name: Optional[str]
#         pw: Optional[str]
#         phone_no: Optional[str]
#         address: Optional[str]
#         e_mail: Optional[str]
#         age: Optional[str]
#         date_joined: Optional[str]
#         date_canceled: Optional[str]
#         fax_no: Optional[str]
#         business_registration_no: Optional[str]
#         company_name: Optional[str]
#         department: Optional[str]
#         position: Optional[str]
#         company_address: Optional[str]
#         birthday: Optional[str]
#
# class UvicornUtil:
#     class Settings:
#         # js 의 destructon 문법처럼 py의 unpacking 을 사용하는 방법이 있으나 변수 새로 생성해야함
#         # 튜플로 데이터가 들어오는 것은 , 를 어딘가 작성했을 수 있다. 이 문법적 오류는 IDE 에서 알려주지 않는다.
#         protocol_type = "http"
#         # protocol_type =  "https"
#         # host =  "0.0.0.0"
#         host = "127.0.0.1"  # localhost
#         port = 8080
#         url = f"{protocol_type}://{host}:{port}"


# class DbTomlUtil:
#     @staticmethod
#     def create_db_toml():
#         try:
#             db_pnx = DB_YAML
#             # db_template =db_template
#             func_n = inspect.currentframe().f_code.co_name
#             pk_print(str_working=rf'''{UNDERLINE}{func_n}() %%%FOO%%%''')
#             if not os.path.exists(os.path.dirname(db_pnx)):
#                 os.makedirs(os.path.dirname(db_pnx))  # 이거 파일도 만들어지나? 테스트 해보니 안만들어짐 디렉토리만 만들어짐
#             # pk_print("db 파일 존재 검사 시도")
#             if not os.path.isfile(db_pnx):
#                 # with open(db_pnx, "w") as f2:
#                 #     toml.dump(db_template, f2)
#                 make_pnx(db_pnx, mode="f")
#                 print_cyan(f"DB를 만들었습니다 {db_pnx}")
#             else:
#                 print_cyan(f"DB가 이미존재합니다 {db_pnx}")
#         except:
#             print_light_black(f"{traceback.format_exc()}")
#
#     @staticmethod
#     def read_db_toml():
#         try:
#             func_n = inspect.currentframe().f_code.co_name
#             pk_print(str_working=rf'''{UNDERLINE}{func_n}() %%%FOO%%%''')
#             print("DB 의 모든 자료를 가져왔습니다")
#             return toml.load(DB_YAML)
#         except:
#             print_light_black(f"{traceback.format_exc()}")
#
#     @staticmethod
#     def get_db_toml_key(unique_id):
#         return get_str_replaced_special_characters(target=unique_id, replacement="_")
#
#     @staticmethod
#     def select_db_toml(key):
#         # pk_print(f"{inspect.currentframe().f_code.co_name}()")
#         try:
#             key = str(key)
#             db_pnx = DB_YAML
#             try:
#                 # return toml.load(DB_TOML)[key]
#                 with open(db_pnx, 'r', encoding='utf-8') as f:
#                     db = toml.load(f)
#                 return db[key]
#
#             except KeyError:
#                 print(f"DB 에 해당키가 존재하지 않습니다 {key}")
#                 return None
#         except:
#             print_light_black(f"{traceback.format_exc()}")
#
#     @staticmethod
#     def update_db_toml(key, value):
#         try:
#             db_pnx = DB_YAML
#             key: str = str(key)
#             func_n = inspect.currentframe().f_code.co_name
#             pk_print(str_working=rf'''{UNDERLINE}{func_n}() %%%FOO%%%''')
#             # 기존의 DB 의 데이터
#             with open(db_pnx, 'r', encoding='utf-8') as f:
#                 db = toml.load(f)
#                 # pk_print("DB 업데이트 전 ")
#                 # pk_print(context=str(db))
#
#             # 데이터 업데이트
#             if key in db:
#                 db[key] = value
#             else:
#                 # db[key] = value
#                 print(f"DB에 key가 없어서 업데이트 할 수 없습니다 key:{key} value:{value}")
#
#             # TOML 파일에 데이터 쓰기
#             with open(db_pnx, 'w', encoding='utf-8') as f:
#                 toml.dump(db, f)
#                 print(f"DB에 데이터가 업데이트되었습니다")
#
#             # DB 변경 확인
#             # with open(db_pnx, 'r') as f:
#             #     db = toml.load(f)
#             #     pk_print("DB 변경 확인")
#             #     pk_print(context=str(db))
#         except:
#             print_light_black(f"{traceback.format_exc()}")
#
#     @staticmethod
#     def insert_db_toml(key, value):
#         try:
#             key = str(key)
#             db_pnx = DB_YAML
#             func_n = inspect.currentframe().f_code.co_name
#             pk_print(str_working=rf'''{UNDERLINE}{func_n}() %%%FOO%%%''')
#             db_pnx = DB_YAML
#             # 기존의 DB 의 데이터
#             with open(db_pnx, 'r', encoding='utf-8') as f:
#                 db = toml.load(f)
#                 # pk_print("DB 업데이트 전 ")
#                 # pk_print(context=str(db))
#
#             # 데이터 삽입
#             if key in db:
#                 # db[key] = value
#                 print(f"이미 값이 존재하여 삽입할 수 없습니다 key:{key} value:{value}")
#             else:
#                 db[key] = value
#
#             # TOML 파일에 데이터 쓰기
#             with open(db_pnx, 'w', encoding='utf-8') as f:
#                 toml.dump(db, f)
#                 print(f"DB에 데이터가 삽입되었습니다")
#
#             # DB 변경 확인
#             # with open(db_pnx, 'r') as f:
#             #     db = toml.load(f)
#             #     pk_print("DB 변경 확인")
#             #     pk_print(context=str(db))
#         except:
#             print_light_black(f"{traceback.format_exc()}")
#
#     @staticmethod
#     def back_up_db_toml():
#         try:
#             func_n = inspect.currentframe().f_code.co_name
#             pk_print(str_working=rf'''{UNDERLINE}{func_n}() %%%FOO%%%''')
#             compress_pnx_via_bz(DB_YAML)
#         except:
#             print_light_black(f"{traceback.format_exc()}")
#
#     @staticmethod
#     def delete_db_toml():
#         try:
#             func_n = inspect.currentframe().f_code.co_name
#             pk_print(str_working=rf'''{UNDERLINE}{func_n}() %%%FOO%%%''')
#             convert_as_zip_with_timestamp(DB_YAML)
#         except:
#             print_light_black(f"{traceback.format_exc()}")
#
#     @staticmethod
#     def is_accesable_local_database():
#         func_n = inspect.currentframe().f_code.co_name
#         pk_print(str_working=rf'''{UNDERLINE}{func_n}() %%%FOO%%%''')
#         if not os.path.exists(DB_YAML):
#             DbTomlUtil.create_db_toml()
#             return False
#         else:
#             return True


# class MySqlUtil:
#     """
#     mysql 에 의존하는 유틸리티 객체
#     """
#
#     class Settings:
#         protocol_type = "http"
#         # db_driver = "mysql+mysqlconnector" # sqlalchemy mysql driver 설정 #  mysql-connector-python 라이브러리 에 의존
#         db_driver = "mysql+pymysql"  # sqlalchemy 의 mysql driver 는 여러 개 built in 되어 있다. #  pymysql 라이브러리 에 의존
#         host = "127.0.0.1"
#         port = 3306
#         id = "root"
#         pw = "admin123!"
#         database_name = 'test_db'
#         # database_url = rf'{protocol_type}://{host}:{port}' # database 에 바로 연결하지 않음, use DB명령어를 써야할 수있음
#         uri = rf"{db_driver}://{id}:{pw}@{host}:{port}/{database_name}?charset=utf8"
#
#     # Base 가 여기에서 설정되어야 동작
#     engine = create_engine(Settings.uri)
#     SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#     Base = declarative_base()
#
#     @staticmethod
#     def get_session():  # ?  generator 로 되어있는데..?
#         db = MySqlUtil.SessionLocal()
#         try:
#             yield db
#         finally:
#             db.close()
#
#     @staticmethod
#     def get_session_local():
#         db = MySqlUtil.SessionLocal()
#         return db
#
#     @staticmethod
#     def execute(native_query: str):  # without sqlarchemy
#         # engine = create_engine(Settings.url)
#         connection = MySqlUtil.engine.connect()
#         print_light_white(native_query)
#         result = connection.execute(sqlalchecdmy_text(native_query))
#         connection.close()
#         return result


# class CommutationManageConstantUtil:
#     """
#     mysql / sqlalchemy / fastapi 의존하는 유틸리티 객체
#     """
#
#     class CommutationManagement(MySqlUtil.Base):
#         __tablename__ = "commutation_management"
#         __table_args__ = {'extend_existing': True}
#         commutation_management_id = Column(Integer, primary_key=True, autoincrement=True)
#         id = Column(VARCHAR(length=30))
#         name = Column(VARCHAR(length=30))
#         phone_no = Column(VARCHAR(length=13))
#         time_to_go_to_office = Column(VARCHAR(length=100))
#         time_to_leave_office = Column(VARCHAR(length=100))
#
#     class CommutationManagementBase(BaseModel):
#         id: str
#         name: str
#         phone_no: str
#         time_to_go_to_office: str
#         time_to_leave_office: str
#
#         # @staticmethod
#         # @field_validator('id')
#         # def validate_id(value):
#         #     CommutationManagevalidate_id(value)
#
#     @staticmethod
#     def get_commutation_management_validated(commutation_management):
#         func_n = inspect.currentframe().f_code.co_name
#         pk_print(str_working=rf'''{UNDERLINE}{func_n}() %%%FOO%%%''')
#
#         # CommutationManagement 클래스의 필드 개수 확인
#         field_count = len(CommutationManageCommutationManagement.__table__.c)
#         print(rf'''field_count : {field_count}''')
#
#         pnxs_validated = [
#             {"field_en": 'id', "field_ko": "아이디", "field_validation_func": CommutationManagevalidate_id, "field_length_limit": CommutationManageCommutationManagement.__table__.c.id.type.length},
#             {"field_en": 'name', "field_ko": "이름", "field_validation_func": CommutationManagevalidate_name, "field_length_limit": CommutationManageCommutationManagement.__table__.c.name.type.length},
#             {"field_en": 'phone_no', "field_ko": "전화번호", "field_validation_func": CommutationManagevalidate_phone_no, "field_length_limit": CommutationManageCommutationManagement.__table__.c.phone_no.type.length},
#             {"field_en": 'time_to_go_to_office', "field_ko": "출근시간", "field_validation_func": CommutationManagevalidate_time_to_go_to_office, "field_length_limit": CommutationManageCommutationManagement.__table__.c.time_to_go_to_office.type.length},
#             {"field_en": 'time_to_go_to_office', "field_ko": "퇴근시간", "field_validation_func": CommutationManagevalidate_time_to_leave_office, "field_length_limit": CommutationManageCommutationManagement.__table__.c.time_to_leave_office.type.length},
#         ]
#         for target in pnxs_validated:
#             field_en = target["field_en"]
#             field_ko = target["field_ko"]
#             field_validation_func = target["field_validation_func"]
#             field_length_limit = target["field_length_limit"]
#             if len(commutation_management[field_en]) > target['field_length_limit']:
#                 raise HTTPException(status_code=400, detail=f"{field_ko}({field_en})의 길이제한은 {field_length_limit}자 이하여야 합니다.")
#             else:
#                 field_validation_func(commutation_management[field_en])  # success, 호출할 수 없는 함수의 내부에 구현된 부분이 필요한것 이므로 내부에 구현된 것을 다른 클래스에 구현해서 참조하도록 로직 분리,
#         return commutation_management
#
#     @staticmethod
#     def validate_commutation_management(commutation_management):
#         func_n = inspect.currentframe().f_code.co_name
#         pk_print(str_working=rf'''{UNDERLINE}{func_n}() %%%FOO%%%''')
#         CommutationManageget_commutation_management_validated(commutation_management)
#
#     class CommutationManagementCreate(CommutationManagementBase):
#         pass
#
#     class CommutationManagementExtendedCommutationManagementBase(CommutationManagementBase):
#         id: str
#         name: str
#         phone_no: str
#         time_to_go_to_office: str
#         time_to_leave_office: str
#
#         class Config:
#             # orm_mode = True
#             from_attributes = True
#
#     @staticmethod
#     def get_commutation_managements(db: Session):
#         return db.query(CommutationManageCommutationManagement).all()
#
#     @staticmethod
#     def get_commutation_management(db: Session, id: int):
#         # return db.query(CommutationManageCommutationManagement).filter(CommutationManageCommutationManagement.id == id).first() # success , 그러나 타입힌팅 에러가...
#         return select(CommutationManageCommutationManagement).where(CommutationManageCommutationManagement.id.in_([id]))  # try
#
#     @staticmethod
#     def insert_commutation_management(db: Session, commutation_management):
#         commutation_management_ = CommutationManageCommutationManagement(**commutation_management)
#         db.add(commutation_management_)
#         db.flush()
#         db.commit()
#         db.refresh(commutation_management_)
#         return commutation_management_
#
#     @staticmethod
#     def update_commutation_management(db: Session, commutation_management, updated_commutation_management):
#         for key, value in updated_commutation_management.model_dump().commutation_managements():
#             setattr(commutation_management, key, value)
#         db.commit()
#         db.refresh(commutation_management)
#         return commutation_management
#
#     @staticmethod
#     def validate_id(value):
#         func_n = inspect.currentframe().f_code.co_name
#         pk_print(str_working=rf'''{UNDERLINE}{func_n}() %%%FOO%%%''')
#         raise_exception_after_special_charcater_check(value, inspect.currentframe().f_code.co_name)
#         return True
#
#     @staticmethod
#     def validate_name(value):
#         func_n = inspect.currentframe().f_code.co_name
#         pk_print(str_working=rf'''{UNDERLINE}{func_n}() %%%FOO%%%''')
#         raise_exception_after_special_charcater_check(value, inspect.currentframe().f_code.co_name)
#         return True
#
#     @staticmethod
#     def validate_phone_no(value):
#         func_n = inspect.currentframe().f_code.co_name
#         pk_print(str_working=rf'''{UNDERLINE}{func_n}() %%%FOO%%%''')
#         # r'^\d{3}-\d{3,4}-\d{4}$'
#         # r'^\d{2}-\d{3,4}-\d{4}$' 둘다
#         if not re.match(r'^\d{2,3}-\d{3,4}-\d{4}$', value):
#             raise HTTPException(status_code=400, detail=f"유효한 전화번호가 아닙니다. {value}")
#         return value
#
#     @staticmethod
#     def validate_time_to_go_to_office(value):
#         func_n = inspect.currentframe().f_code.co_name
#         pk_print(str_working=rf'''{UNDERLINE}{func_n}() %%%FOO%%%''')
#         return True
#
#     @staticmethod
#     def validate_time_to_leave_office(value):
#         func_n = inspect.currentframe().f_code.co_name
#         pk_print(str_working=rf'''{UNDERLINE}{func_n}() %%%FOO%%%''')
#         return True


# class CustomerServiceBoardUtil:
#     """
#     mysql / sqlalchemy / fastapi 의존하는 유틸리티 객체
#     """
#
#     class CustomerServiceBoard(MySqlUtil.Base):  # orm 설정에는 id 있음
#         __tablename__ = "customer_service_board"
#         __table_args__ = {'extend_existing': True}
#         # __table_args__ = {'extend_existing': True, 'mysql_collate': 'utf8_general_ci'} # encoding 안되면 비슷하게 방법을 알아보자  mysql 에 적용이 가능한 코드로 보인다.
#         CustomerServiceBoard_id: str = uuid4().hex + get_time_as_('%Y%m%d%H%M%S%f') + get_random_alphabet()  # table 내 unique id
#         id = Column(Integer, primary_key=True, autoincrement=True)  # index 로 이용
#         writer = Column(VARCHAR(length=30))
#         title = Column(VARCHAR(length=30))
#         contents = Column(VARCHAR(length=13))
#         date_reg = Column(DateTime, nullable=False, default=datetime.now)
#         del_yn = Column(VARCHAR(length=50))
#
#     class CustomerServiceBoardBase(BaseModel):  # pydantic validator 설정에는 CustomerServiceBoard_id 없음
#         id: str
#         writer: str
#         title: str
#         contents: Optional[str]
#         date_reg: str
#         del_yn: str
#
#         @staticmethod
#         @field_validator('id')
#         def validate_id(value):
#             CustomerServiceBoardUtil.validate_id(value)
#
#         @staticmethod
#         @field_validator('writer')
#         def validate_writer(value):
#             CustomerServiceBoardUtil.validate_writer(value)
#
#         @staticmethod
#         @field_validator('title')
#         def validate_title(value):
#             CustomerServiceBoardUtil.validate_title(value)
#
#         @staticmethod
#         @field_validator('contents')
#         def validate_contents(value):
#             CustomerServiceBoardUtil.validate_contents(value)
#
#         @staticmethod
#         @field_validator('date_reg')
#         def validate_date_reg(value):
#             # datetime.strptime(date_join, '%Y-%m-%d %H:%M %S%f')
#             if len(value) != 18:
#                 raise HTTPException(status_code=400, detail="유효한 날짜가 아닙니다.")
#             CustomerServiceBoardUtil.validate_date_reg(value)
#
#         @staticmethod
#         @field_validator('del_yn')
#         def validate_del_yn(value):
#             CustomerServiceBoardUtil.validate_del_yn(value)
#
#     @staticmethod
#     def get_customer_service_board_validated(customer_service_board):
#         func_n = inspect.currentframe().f_code.co_name
#         pk_print(str_working=rf'''{UNDERLINE}{func_n}() %%%FOO%%%''')
#
#         # CustomerServiceBoard 클래스의 필드 개수 확인
#         field_count = len(CustomerServiceBoardUtil.CustomerServiceBoard.__table__.c)
#         print(rf'''field_count : {field_count}''')
#
#         pnxs_validated = [
#             {"field_en": 'id', "field_ko": "아이디", "field_validation_func": CustomerServiceBoardUtil.validate_id, "field_length_limit": CustomerServiceBoardUtil.CustomerServiceBoard.__table__.c.id.type.length},
#             {"field_en": 'writer', "field_ko": "이름", "field_validation_func": CustomerServiceBoardUtil.validate_writer, "field_length_limit": CustomerServiceBoardUtil.CustomerServiceBoard.__table__.c.writer.type.length},
#             {"field_en": 'title', "field_ko": "이메일", "field_validation_func": CustomerServiceBoardUtil.validate_title, "field_length_limit": CustomerServiceBoardUtil.CustomerServiceBoard.__table__.c.title.type.length},
#             {"field_en": 'contents', "field_ko": "전화번호", "field_validation_func": CustomerServiceBoardUtil.validate_contents, "field_length_limit": CustomerServiceBoardUtil.CustomerServiceBoard.__table__.c.contents.type.length},
#             {"field_en": 'date_reg', "field_ko": "주소", "field_validation_func": CustomerServiceBoardUtil.validate_date_reg, "field_length_limit": CustomerServiceBoardUtil.CustomerServiceBoard.__table__.c.date_reg.type.length},
#             {"field_en": 'del_yn', "field_ko": "가입일", "field_validation_func": CustomerServiceBoardUtil.validate_del_yn, "field_length_limit": CustomerServiceBoardUtil.CustomerServiceBoard.__table__.c.del_yn.type.length},
#         ]
#         for target in pnxs_validated:
#             field_en = target["field_en"]
#             field_ko = target["field_ko"]
#             field_validation_func = target["field_validation_func"]
#             field_length_limit = target["field_length_limit"]
#             if len(customer_service_board[field_en]) > target['field_length_limit']:
#                 raise HTTPException(status_code=400, detail=f"{field_ko}({field_en})의 길이제한은 {field_length_limit}자 이하여야 합니다.")
#             else:
#                 field_validation_func(customer_service_board[field_en])  # success, 호출할 수 없는 함수의 내부에 구현된 부분이 필요한것 이므로 내부에 구현된 것을 다른 클래스에 구현해서 참조하도록 로직 분리,
#         return customer_service_board
#
#     @staticmethod
#     def validate_customer_service_board(customer_service_board):
#         func_n = inspect.currentframe().f_code.co_name
#         pk_print(str_working=rf'''{UNDERLINE}{func_n}() %%%FOO%%%''')
#         CustomerServiceBoardUtil.get_customer_service_board_validated(customer_service_board)
#
#     class CustomerServiceBoardCreate(CustomerServiceBoardBase):
#         pass
#
#     class CustomerServiceBoardExtendedCustomerServiceBoardBase(CustomerServiceBoardBase):
#         id: str
#         writer: str
#         title: str
#         contents: str
#         date_reg: str
#         del_yn: str
#
#         class Config:
#             from_attributes = True
#
#
#     @staticmethod
#     def get_customer_service_boards(db: Session):
#         return db.query(CustomerServiceBoardUtil.CustomerServiceBoard).all()
#
#     @staticmethod
#     def get_customer_service_board(id: int):
#         # return db.query(CustomerServiceBoardUtil.CustomerServiceBoard).filter(CustomerServiceBoardUtil.CustomerServiceBoard.id == id).first() # success , 그러나 타입힌팅 에러가...
#         MySqlUtil.execute(f'''SELECT * FROM customer_service_board where id= {id} ORDER BY del_yn LIMIT 2;''')  # LIMIT 2 로 쿼리 성능 향상 기대, 2인 이유는 id가 2개면
#         # 네이티브 쿼리를 한번 더 작성한 이유는 쿼리 디버깅
#         db_data = MySqlUtil.get_session_local().query(CustomerServiceBoardUtil.CustomerServiceBoard).filter_by(id=id).limit(4).all()
#         return db_data  # try
#
#     @staticmethod
#     def insert_customer_service_board(db: Session, customer_service_board):
#         customer_service_board_ = CustomerServiceBoardUtil.CustomerServiceBoard(**customer_service_board)
#         db.add(customer_service_board_)
#         db.flush()  # flush() 메서드 없이 바로 commit() 메서드를 호출하면, 롤백할 수 있는 포인트가 만들어지지 않습니다. (# 나중에 롤백을 수행할 수 있는 포인트가 만들어짐)
#         db.commit()
#         db.refresh(customer_service_board_)  # 데이터베이스에 업데이트된 최신내용을 세션에 가져오는 것.
#         return customer_service_board_
#
#     @staticmethod
#     def update_customer_service_board(db: Session, customer_service_board, updated_customer_service_board):
#         for key, value in updated_customer_service_board.model_dump().customer_service_boards():
#             setattr(customer_service_board, key, value)
#         db.commit()
#         db.refresh(customer_service_board)
#         return customer_service_board
#
#     @staticmethod
#     def delete_customer_service_board(db: Session, customer_service_board):
#         db.delete(customer_service_board)
#         db.commit()
#
#     @staticmethod
#     def is_customer_service_board_joined_by_id(id, request):
#         func_n = inspect.currentframe().f_code.co_name
#         pk_print(str_working=rf'''{UNDERLINE}{func_n}() %%%FOO%%%''')
#
#         result = MySqlUtil.get_session_local().query(CustomerServiceBoardUtil.CustomerServiceBoard).filter(CustomerServiceBoardUtil.CustomerServiceBoard.id == id).limit(2)
#         for customer_service_board in result:
#             print(f"customer_service_board.name: {customer_service_board.name}, customer_service_board.id: {customer_service_board.id}")
#         customer_service_board_count = result.count()
#         print(rf'''customer_service_board_count : {customer_service_board_count}''')
#         if customer_service_board_count == 1:
#             for customer_service_board_joined in result:
#                 print(f'customer_service_board_joined.name: {customer_service_board_joined.name}  customer_service_board_joined.id: {customer_service_board_joined.id}')
#                 request.session['name'] = customer_service_board_joined.name
#             return True
#         else:
#             return False
#
#     @staticmethod
#     def validate_id(value):
#         func_n = inspect.currentframe().f_code.co_name
#         pk_print(str_working=rf'''{UNDERLINE}{func_n}() %%%FOO%%%''')
#         raise_exception_after_special_charcater_check(value, inspect.currentframe().f_code.co_name)
#         return True
#
#     @staticmethod
#     def validate_writer(value):
#         func_n = inspect.currentframe().f_code.co_name
#         pk_print(str_working=rf'''{UNDERLINE}{func_n}() %%%FOO%%%''')
#         raise_exception_after_special_charcater_check(value, inspect.currentframe().f_code.co_name)
#         return True
#
#     @staticmethod
#     def validate_title(value):
#         func_n = inspect.currentframe().f_code.co_name
#         pk_print(str_working=rf'''{UNDERLINE}{func_n}() %%%FOO%%%''')
#         raise_exception_after_special_charcater_check(value, inspect.currentframe().f_code.co_name, ignore_list=["@"])
#         CustomerServiceBoardUtil.validate_title(value)
#         pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
#         if not re.match(pattern, value):
#             # if not date_reg_title.endswith('@kakao.com'):
#             #     raise HTTPException(status_code=400, detail="유효한 카카오 이메일이 아닙니다.")
#             # return date_reg_title
#             raise HTTPException(status_code=400, detail=f"유효한 이메일 주소가 아닙니다. {value}")
#         return value
#
#     @staticmethod
#     def validate_contents(value):
#         func_n = inspect.currentframe().f_code.co_name
#         pk_print(str_working=rf'''{UNDERLINE}{func_n}() %%%FOO%%%''')
#         # r'^\d{3}-\d{3,4}-\d{4}$'
#         # r'^\d{2}-\d{3,4}-\d{4}$' 둘다
#         if not re.match(r'^\d{2,3}-\d{3,4}-\d{4}$', value):
#             raise HTTPException(status_code=400, detail=f"유효한 전화번호가 아닙니다. {value}")
#         return value
#
#     @staticmethod
#     def validate_date_reg(value):
#         func_n = inspect.currentframe().f_code.co_name
#         pk_print(str_working=rf'''{UNDERLINE}{func_n}() %%%FOO%%%''')
#         return True
#
#     @staticmethod
#     def validate_del_yn(value):
#         func_n = inspect.currentframe().f_code.co_name
#         pk_print(str_working=rf'''{UNDERLINE}{func_n}() %%%FOO%%%''')
#         return True


# todo : ref : enum eample
# class TextConvertMode(Enum):
#     STR_TO_LIST = rf' from  test love to  "test love" '
#     GREEN = 2
#     BLUE = 3


# todo : chore : ? 업로드 
# fastapi + http server
# command = f'curl -X POST "https://api.telegram.org/bot{token}/sendDocument" -d "chat_id={chat_id}&document=@{pkg_to_house_zip}"'
# command_run_v2(command=command)
# token_gitlab_repo_url = get_token_from_text_file(token_file=rf'{StateManagePKG_TXT}\token_gitlab_repo_url.txt', initial_token="")
# # commit_ment = "test:initial git push test"
# commit_ment = "feat:add run_release_server() "
# pnx = rf"{StateManagePROJECT_D}\pk_system.py"
# upload_pnx_to_git(git_repository_url=token_gitlab_repo_url, commit_msg=commit_ment, pnx=pnx)

#  todo : ref : logger
# logger = logging.getLogger('pk_system_test_logger')
# hdlr = logging.FileHandler('pk_system_logger.log')
# hdlr.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
# logger.addHandler(hdlr)
# logger.setLevel(logging.INFO)
