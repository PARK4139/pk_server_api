import os
import tempfile
import shutil
from pathlib import Path

def self_delete_project():
    project_root = Path(__file__).resolve().parent
    bat_path = Path(tempfile.gettempdir()) / "self_delete.bat"

    with open(bat_path, "w", encoding="utf-8") as f:
        f.write(f'''@echo off
timeout /t 2 > nul
rmdir /s /q "{project_root}"
del "%~f0"
''')

    os.system(f'start /min cmd /c "{bat_path}"')

if __name__ == "__main__":
    self_delete_project()

import os
import tempfile
import shutil
from pathlib import Path

def self_delete_project():
    project_root = Path(__file__).resolve().parent
    bat_path = Path(tempfile.gettempdir()) / "self_delete.bat"

    with open(bat_path, "w", encoding="utf-8") as f:
        f.write(f'''@echo off
timeout /t 2 > nul
rmdir /s /q "{project_root}"
del "%~f0"
''')

    os.system(f'start /min cmd /c "{bat_path}"')

if __name__ == "__main__":
    self_delete_project()




def _TEST_CASE_파일_제어기():
    # todo 인터넷될때
    from pkg_py.pk_core import assist_to_find_pnx_list_like_everything
    assist_to_find_pnx_list_like_everything()


def _TEST_CASE_출력하고TTS():
    # todo 인터넷 있을때 테스트 가능
    from pkg_py.pk_core import pk_speak
    # working_str = 'what time is it'
    working_str = '테스트이다'
    pk_speak(working_str=working_str, after_delay=1.00)

    # print_and_speak("Playing music...")


def get_latest_tracking_only_from_sqlite_xc_status_db():
    from pkg_py.pk_colorful_cli_util import pk_print
    import sqlite3
    import pandas as pd
    f_local_db = f"{D_PKG_DB}/xc_status.db"
    f_local_db = get_pnx_os_style(f_local_db)
    conn = sqlite3.connect(f_local_db)
    query = """
       WITH ranked AS (
           SELECT *,

                  ROW_NUMBER() OVER (
                      PARTITION BY 장비식별자
                      ORDER BY 업무수행일 DESC
                  ) AS rn
           FROM xc_status
       )
       SELECT *
       FROM ranked
       WHERE rn = 1
       ORDER BY CAST(SUBSTR(장비식별자, 5) AS INTEGER);
    """
    df_latest = pd.read_sql(query, conn)
    conn.close()
    pk_print(f"📌 최신 업무트래킹 기준으로 {len(df_latest)}개 장비 조회됨", print_color='blue')
    return df_latest


def _TEST_CASE_장비현황_엑셀파일에서_로컬DB로_마이그레이션():
    get_migrate_device_table_from_f_xlsx_to_local_db()


def _TEST_CASE_장비현황_로컬DB에서_최신현황만_조회():
    df_latest = get_latest_tracking_only_from_sqlite_xc_status_db()
    print(df_latest)
    return df_latest


def _TEST_CASE_장비현황_로컬DB에서_최신현황만_CSV파일로_저장():
    from pkg_py.pk_core import does_pnx_exist, cmd_to_os, get_p
    from pkg_py.pk_colorful_cli_util import pk_print
    from pkg_py.pk_core_constants import D_PKG_CSV

    from datetime import datetime
    import os

    df_latest = get_latest_tracking_only_from_sqlite_xc_status_db()

    # 컬럼 리네이밍 & 날짜 포맷 변환
    df_latest = df_latest.rename(columns={
        "장비식별자": "장비식별자",
        "Nvidia Serial": "Nvidia Serial",
        "장비 용도": "장비 용도",
        "위치": "위치",
        "업무트래킹": "업무트래킹",
        "업무수행일": "업무수행일"
    })

    # 업무수행일 → yyyy-mm-dd 형식으로 변환 (예: 250318 → 2025-03-18)
    def parse_tracking_date(x):
        try:
            return datetime.strptime(str(int(x)), "%y%m%d").strftime("%Y-%m-%d")
        except:
            return None

    df_latest["업무수행일"] = df_latest["업무수행일"].apply(parse_tracking_date)

    today_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    f_save_csv = f"{D_PKG_CSV}/xc_latest_tracking_{today_str}.csv"
    f_save_csv = get_pnx_os_style(f_save_csv)

    os.makedirs(get_p(f_save_csv), exist_ok=True)

    df_latest.to_csv(f_save_csv, index=False, encoding="utf-8-sig")
    if does_pnx_exist(f_save_csv):
        pk_print(f"최신 현황 CSV 저장 완료 → {f_save_csv}", print_color="green")
        cmd_to_os(rf'explorer {f_save_csv}')
    return f_save_csv


def _TEST_CASE_장비현황_로컬DB에서_최신현황만_CSV파일로_저장_AND_업무수행일_check_마킹_v6():
    from pkg_py.pk_core import does_pnx_exist, cmd_to_os, get_p, get_pnx_os_style
    from pkg_py.pk_colorful_cli_util import pk_print
    from pkg_py.pk_core_constants import D_PKG_CSV
    from datetime import datetime
    import os
    import pandas as pd
    import sqlite3

    # 1. 전체 xc_status 테이블 불러오기
    f_local_db = f"{D_PKG_DB}/xc_status.db"
    f_local_db = get_pnx_os_style(f_local_db)
    conn = sqlite3.connect(f_local_db)
    df_all = pd.read_sql("SELECT * FROM xc_status", conn)
    conn.close()

    # 2. 업무수행일 → 정수형으로 변환
    df_all["업무수행일"] = pd.to_numeric(df_all["업무수행일"], errors="coerce")

    # ✅ 장비식별자 기준 최신 업무트래킹 내림차순 정렬
    df_all["장비번호"] = df_all["장비식별자"].str.extract(r"XC\s?#?(\d+)", expand=False).astype(float)
    df_all = df_all.sort_values(["장비식별자", "업무수행일"], ascending=[True, False])

    # ✅ 장비별 첫 번째만 "TRUE", 나머지 ""
    df_all["장비별최신업무여부"] = df_all.duplicated(subset=["장비식별자"], keep="first").map(lambda x: "" if x else "TRUE")

    # ✅ 날짜 포맷 변환
    def parse_tracking_date(x):
        try:
            return datetime.strptime(str(int(x)), "%y%m%d").strftime("%Y-%m-%d")
        except:
            return None

    # df_all["업무수행일"] = df_all["업무수행일"].apply(parse_tracking_date)

    # ✅ 정렬 후 장비번호 제거, 표순번 추가
    df_all = df_all.drop(columns=["장비번호"])
    df_all.insert(0, "표순번", range(1, len(df_all) + 1))

    # ✅ 컬럼 순서 정리 (비고 포함 시)
    expected_cols = [
        "표순번", "장비식별자", "스티커라벨(장비식별자)", "Nvidia Serial", "장비 용도", "AI framework 배포파일 버전",
        "위치", "업무트래킹", "업무수행일", "장비별최신업무여부", "비고"
    ]
    df_all = df_all[[col for col in expected_cols if col in df_all.columns]]

    # ✅ Nvidia Serial → 수식 문자열로 변환 (Excel/Notion 지수표기 방지)
    if "Nvidia Serial" in df_all.columns:
        df_all["Nvidia Serial"] = df_all["Nvidia Serial"].apply(lambda x: f'="{x}"' if pd.notna(x) else "")

    # 4. 저장 경로 지정
    today_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    f_save_csv = f"{D_PKG_CSV}/xc_full_tracking_with_latest_flag_{today_str}.csv"
    f_save_csv = get_pnx_os_style(f_save_csv)
    os.makedirs(get_p(f_save_csv), exist_ok=True)

    # 5. 저장
    df_all.to_csv(f_save_csv, index=False, encoding="utf-8-sig")

    if does_pnx_exist(f_save_csv):
        pk_print(f"✅ 전체 장비현황 CSV 저장 완료 (v6, Serial 수식처리 적용) → {f_save_csv}", print_color="green")
        cmd_to_os(rf'explorer {f_save_csv}')

    return f_save_csv


def _TEST_CASE_장비현황_로컬DB에서_최신현황만_CSV파일로_저장_AND_업무수행일_check_마킹():
    _TEST_CASE_장비현황_로컬DB에서_최신현황만_CSV파일로_저장_AND_업무수행일_check_마킹_v6()


def _TEST_CASE_장비현황_데이터로우추가_로컬DB로():
    # dbeaber/쿼리 참조
    pass


def _TEST_CASE_장비현황_로컬DB_table_truncate():
    # dbeaber/쿼리 참조
    pass


def _TEST_CASE_LAZY_IMPORT_코드_자동완성():
    # todo lazy import
    # add_lazy_import_all_modules_to_outter_functions(f=f)
    # # add_lazy_import_to_outter_functions(f=f)
    # # add_lazy_import_to_functions(f=f)
    pass


def _TEST_CASE_에러재현():
    raise ValueError("의도적으로 에러 발생")


def _TEST_CASE_타임루프제어():
    import time
    time_limit = 3
    time_s = time.time()
    while 1:
        if time.time() - time_s > time_limit:
            return False
        pk_sleep(seconds=0.5)


def test_string_handling():
    # todo :  {'%%%FOO%%%' if LTA else ''} 부분 autofill dev tool 적용

    # mkr_로깅 (시간, 객체, 함수, 필드)
    # class cmd_modes():
    #     cli='cli'
    #     gui='gui'
    #     startup='startup'
    #     scheduler='scheduler'
    #     sequence='test'
    # print_class_field_and_value(class_name=cmd_modes)

    # mkr_텍스트 변환
    # text=r"""
    # python -m PyInstaller -i ".\pkg_png\icon.PNG" console_blurred.py
    # """
    # print_text_converted(text=text)

    # mkr_텍스트 변환
    # texts=[
    #     # rf'echo y | rmdir /s "{}"',
    #     # rf'echo y | del /f "{}"',
    #     rf".\dist\console_blurred\console_blurred.exe"
    # ]
    # for text in texts:
    #     print_and_get_text_converted(text=text)
    pass


def _TEST_CASE_시간확인_v1():
    from pkg_py.pk_core import is_year, is_minute, is_hour, is_day, is_month
    from pk_core import pk_sleep

    # 밤12시 12분
    state_time_to_system_sleep = 0
    while 1:
        if is_year(yyyy=2025):
            if is_month(mm=3):
                if is_day(dd=21):
                    if is_hour(hh=0):
                        if is_minute(mm=12):
                            state_time_to_system_sleep = 1
                            break
        pk_sleep(seconds=1)


def _TEST_CASE_시간확인():
    _TEST_CASE_시간확인_v1()


def _TEST_CASE_시간확인_v2():
    pass


def _TEST_CASE_출력하고TTS():
    pk_print_and_speak("Playing music...")


def _TEST_CASE_어시스트_스케쥴():
    # todo
    assist_to_do_pk_schedule()


def _EXCUTE_UNIT_TEST():
    # todo 집에서 할일
    # https://www.youtube.com/watch?v=IQJL3htsDyQ
    # https://www.youtube.com/watch?v=XaBUAP1SGtM
    # https://www.youtube.com/watch?v=2QmQVk0HmQ0
    # https://www.youtube.com/watch?v=GLnv68VNY0A
    # https://www.youtube.com/watch?v=XaBUAP1SGtM
    # https://www.youtube.com/watch?v=2QmQVk0HmQ0
    # https://www.youtube.com/watch?v=GLnv68VNY0A

    # todo window state taacking
    # pk.py excute_cnt #  sqlite
    # todo window state 저장

    # todo %%%FOO%%% # replace_text_B_and_text_C_interchangeably_at_text_A_by_using_
    # test_fill_with_auto_no
    # f_list_in_d = os.listdir(d) # f_list_in_d 아니고 f_nx_list_in_d 인지 확인필요
    # STAMP_POSITION = rf'[%%%FOO%%%]'
    # todo : dictionary : 딕셔너리 통합, 딕셔너리를 f_txt 로 만드는 게 나을까? Enum 으로 만드는게 나을까?
    # todo : dictionary : str vs string vs item_str
    # todo : dictionary : ment vs prompt
    # todo : dictionary : src vs pnx
    # todo : dictionary : text vs txt
    # todo : dictionary : cwd vs d_started vs starting_d vs  working_d vs opening_d vs pwd vs current_d # 이건 상황별로 확인필요
    # todo : dictionary : current_d vs d_current
    # todo : dictionary : 퇴근루틴 > 작업종료루틴
    # todo : dictionary : 실행 > exec > run
    # todo : dictionary : back_up vs bkup
    # todo : dictionary : os.path.exists vs does_pnx_exist
    # download vs bring vs get
    # upload vs send

    # todo : 밤루틴 수면양말 동굴이불

    # todo
    # ask_to_chat_gpt(question="가 뭐야?") # 질문하기
    # found_pnx_list_in_tree()
    # print_user_input_organized_duplicated_hashed() # 해시테그 오름차순 정리
    # reconnect_to_qcy_h3_anc_headset_via_bluetooth()
    # reconnect_to_wifi()
    # run_venv_in_cmd_exe()
    # should_i_do(ment="알송을 종료할까요?", function=partial(taskkill, 'ALSong.exe'),  auto_click_negative_btn_after_seconds=15)
    # should_i_enter_to_power_saving_mode()
    # pk_sleep(min=50, show_mode=True) # console 에  #   카운트다운이 되면서 출력이 되도록 하자.
    # speak_ment_experimental(ment='자자', comma_delay=0.43, thread_join_mode=True)
    # speak_ment_experimental(ment=f'{get_time_as_('%H')}시 입니다', comma_delay=0.43, thread_join_mode=True)
    # speak_today_time_info()
    # sum_via_txt_f() # 합 연산
    # test_string_handling()
    # UiUtil.pop_up_as_complete(title_="모니터링감지보고", ment="test", auto_click_positive_btn_after_seconds=3)
    # windows_shutdown(seconds=60)
    # 출근해라 to telegram/chat_room/ # via smartphone # txt, 작은파일은 보낼 수 있으니까 schedule 프로그램에서 동작하도록
    # make_shellscript_version_new_via_hard_coded() # 쉘 스크립트 버전 자동 업데이트
    assist_to_make_d_for_work()

    # todo control device
    # ssh(users=users_mac, ip=ip_private_mac, wsl_linux_version=wsl_linux_version, wsl_window_title_seg=f"{users_desktop_wsl}@{HOSTNAME}", pw=pw_mac, exit_mode=False)
    # ping(ip=ip_private_mac)
    # cmd_to_remote_os_via_wsl(command=rf'sudo reboot', users=users_mac, ip=ip_private_mac, wsl_linux_version=wsl_linux_version, wsl_window_title_seg=f"{users_desktop_wsl}@{HOSTNAME}", pw=pw_mac, exit_mode=False)
    # cmd_to_remote_os_via_wsl(command=rf'sudo poweroff', users=users_mac, ip=ip_private_mac, wsl_linux_version=wsl_linux_version, wsl_window_title_seg=f"{users_desktop_wsl}@{HOSTNAME}", pw=pw_mac, exit_mode=False)
    # mstsc(ip = ip_private_mac, port=port_rdp_mac)
    # remmina(users=users_mac, ip=ip_private_mac, wsl_linux_version=wsl_linux_version, wsl_window_title_seg=f"{users_desktop_wsl}@{HOSTNAME}", pw=pw_mac, exit_mode=False)
    # xfreerdp(users=users_mac, ip=ip_private_mac, wsl_linux_version=wsl_linux_version, wsl_window_title_seg=f"{users_desktop_wsl}@{HOSTNAME}", pw=pw_mac, exit_mode=False)
    # install_chrome_remote_desktop_server_to_remote_os(users=users_mac, ip=ip_private_mac, wsl_linux_version=wsl_linux_version, wsl_window_title_seg=f"{users_desktop_wsl}@{HOSTNAME}", pw=pw_mac, exit_mode=False)
    # install_chrome_remote_desktop_client_to_remote_os(users=users_mac, ip=ip_private_mac, wsl_linux_version=wsl_linux_version, wsl_window_title_seg=f"{users_desktop_wsl}@{HOSTNAME}", pw=pw_mac, exit_mode=False)
    # chrome_remote_desktop(hostname = hostname) # todo GPU 없는 장비는 사용불가, pin 입력 로직 검토필요
    # teamviewer(hostname = hostname) # todo

    # todo system control
    # change_os_to_power_saving_mode()
    # change_os_to_shutdown()
    # change_os_to_shutdown(seconds=60)
    # change_os_to_shutdown(mins=3)
    # change_os_to_shutdown(mins=10)
    # change_os_to_shutdown(mins=15)
    # change_os_to_shutdown(restart_mode=True)
    # should_i_enter_to_power_saving_mode()

    # todo build via pyinstaller
    # build_pk_project_via_pyinstaller() #
    # 프로젝트 빌드파일 삭제
    # 시간별로 빌드 VS 버전별로 빌드
    # 프로젝트 빌드파일 다운로드
    # 프로젝트 빌드파일 실행
    # 프로젝트 빌드파일 삭제

    # todo : get_list_removed_element_by_idx(items)
    # del routines[cursor_position]

    # todo : delete module imported
    # del sys.modules['numpy']

    # todo : python decorater 를 통한 fail tracking      [fail] module function(), red          [success] module function() , green

    # todo : pkg_txt 에서 f내용이 empty 이면 f명 앞에 prefix 를 [text_empty]_를 이동하여 rename

    # todo : think : 추출한 magnets를 {search_keyword}.txt 에 저장

    # todo : df control
    # pk_print(f"{df.head()}") # df 로깅 (df 내 데이터 유무 확인)
    # pk_print(f"{df.columns.tolist()}") # df 로깅 (df 내의 모든 컬럼명 출력)
    # pk_print(f"{len(df)}") # df 로깅 (df 전체 행의 줄이 몇개인지 출력)
    # pk_print(f"{df.iloc[0]}") # df 로깅 (df 내의 첫번째 줄만 출력)

    # todo : pop_sound.wav 음질 향상을 위한 음향제어
    # import librosa
    # import soundfile as sf
    # import numpy as np
    # from scipy.signal import butter, lfilter

    # # 1. 오디오 f 로드
    # def load_audio(f):
    #     signal, sr = librosa.load(f, sr=None)
    #     pk_print(f"Loaded audio with shape: {signal.shape}, Sample Rate: {sr}")
    #     return signal, sr

    # # 2. 저역 통과 필터
    # def low_pass_filter(signal, cutoff, fs, order=4):
    #     nyquist = 0.5 * fs
    #     normal_cutoff = cutoff / nyquist
    #     b, a = butter(order, normal_cutoff, btype='low', analog=False)
    #     return lfilter(b, a, signal)

    # # 3. 고역 통과 필터
    # def high_pass_filter(signal, cutoff, fs, order=4):
    #     nyquist = 0.5 * fs
    #     normal_cutoff = cutoff / nyquist
    #     b, a = butter(order, normal_cutoff, btype='high', analog=False)
    #     return lfilter(b, a, signal)

    # # 4. 볼륨 조정 (정규화)
    # def normalize_signal(signal, target_level=0.9):
    #     max_val = max(abs(signal))
    #     return signal * (target_level / max_val)
    #
    #
    # # 5. 리버브 효과 추가
    # def add_reverb(signal, decay=0.5):
    #     reverb_signal = np.zeros_like(signal)
    #     for i in range(len(signal)):
    #         reverb_signal[i] = signal[i]
    #         if i > 0:
    #             reverb_signal[i] += decay * reverb_signal[i - 1]
    #     return reverb_signal
    #
    #
    # # 6. 오디오 처리 및 저장
    # def process_audio(input_f, output_f, low_cutoff, high_cutoff, reverb_decay, volume_level):
    #     # Step 1: Load audio
    #     signal, sr = load_audio(input_f)
    #
    #     # Step 2: Apply filters
    #     low_filtered = low_pass_filter(signal, low_cutoff, sr)
    #     high_filtered = high_pass_filter(low_filtered, high_cutoff, sr)
    #
    #     # Step 3: Normalize signal
    #     normalized = normalize_signal(high_filtered, target_level=volume_level)
    #
    #     # Step 4: Add reverb
    #     processed_signal = add_reverb(normalized, decay=reverb_decay)
    #
    #     # Step 5: Save processed audio
    #     sf.write(output_f, processed_signal, sr)
    #     pk_print(f"Processed audio saved to {output_f}")
    #
    # # 7. exec
    #     # 입력 f과 출력 f 경로 설정
    #     input_audio = "example.wav"  # 원본 오디오 f 경로
    #     output_audio = "processed_audio.wav"  # 처리된 f 저장 경로
    #
    #     # 필터 및 효과 설정
    #     low_cutoff = 500  # 저역 통과 필터 주파수 (Hz)
    #     high_cutoff = 2000  # 고역 통과 필터 주파수 (Hz)
    #     reverb_decay = 0.3  # 리버브 감쇠
    #     volume_level = 0.9  # 볼륨 정규화 수준 (0.0 ~ 1.0)
    #
    #     # 오디오 처리 exec
    #     process_audio(input_audio, output_audio, low_cutoff, high_cutoff, reverb_decay, volume_level)

    # todo : 드래그한상태에서 특정단축키를 누르면, chatgpt 에게 질문을 하는 프로세스
    # via chatgpt api , via chatgpt web

    # todo : 드래그한상태에서 특정단축키를 누르면, cmd 에서 exec 을 하는 프로세스

    # todo
    # get_comprehensive_weather_information_from_web()
    # print_sub_pnx_list(src=rf"D:\#기타\pkg_files")
    # print_from_pnx_list_to_semantic_words(pnx =rf"D:\#기타\pkg_files")

    # todo : 회의록 자동화
    # 네이버 클로바 : STT
    # chatGPT : 내용 요약
    # liost

    # todo # drag 한 내용 + 특정 단축키 > dragged language 분류 > 실행

    # _TEST_CASE_장비현황_로컬DB_table_truncate()
    # _TEST_CASE_장비현황_데이터로우추가_로컬DB로()
    # _TEST_CASE_장비현황_로컬DB에서_최신현황만_CSV파일로_저장_AND_업무수행일_check_마킹()
    # 노션/데이터베이스/속성(장비 용도, AI framework 배포파일 버전, 위치) 텍스트로 변경
    # 노션/데이터베이스/csv 와 병합
    # 노션/데이터베이스/속성(장비 용도, AI framework 배포파일 버전, 위치) 원복

    # _TEST_CASE_어시스트_스케쥴()
    _TEST_CASE_출력하고TTS()
    pk_print('단위테스트', print_color='green')


if __name__ == "__main__":
    try:
        import traceback

        from pkg_py.pk_core import pk_copy, get_migrate_device_table_from_f_xlsx_to_local_db, get_pnx_os_style, pk_sleep, cmd_to_os, ensure_pnx_made, ensure_pnx_removed, LTA, is_year, is_minute, is_hour, is_day, is_month, assist_to_do_pk_schedule, copy_pnx, F_PK_CONFIG_TOML, pk_back_up_pnx, pk_decompress_f_via_zip, get_pn, get_pk_python_program_available_idx_list, get_pk_python_program_pnx_list, \
    get_available_pk_python_program_pnx, pk_run_process, get_time_as_, set_state_from_f_pk_config_toml, get_state_from_f_pk_config_toml, make_d_with_timestamp, assist_to_make_d_for_work, pk_print_and_speak, run_project_docker_base
        from pkg_py.pk_colorful_cli_util import pk_print
        from pkg_py.pk_core_constants import D_PROJECT, UNDERLINE, STAMP_TRY_GUIDE, STAMP_EXCEPTION_DISCOVERED, D_PKG_DB, D_PKG_CMD, D_PK_RECYCLE_BIN, D_HOME

        _EXCUTE_UNIT_TEST()

    except:
        traceback_format_exc_list = traceback.format_exc().split("\n")
        pk_print(working_str=f'{UNDERLINE}', print_color='red')
        for traceback_format_exc_str in traceback_format_exc_list:
            pk_print(working_str=f'{STAMP_EXCEPTION_DISCOVERED} {traceback_format_exc_str}', print_color='red')
        pk_print(working_str=f'{UNDERLINE}', print_color='red')

    finally:
        script_to_run_python_program_in_venv = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
        pk_print(working_str=f'{UNDERLINE}')
        pk_print(working_str=f'{STAMP_TRY_GUIDE} {script_to_run_python_program_in_venv}')
        pk_print(working_str=f'{UNDERLINE}')

def _TEST_CASE_프로젝트_FASTAPI():
    f_dockerfile_script_list = [
        f'# FROM python:3.12.8-alpine',
        f'# FROM python:3.12-slim # Ubuntu-slim [fail]',
        f'FROM ubuntu:24.04',
        f'WORKDIR /container_workspace',
        f'ENV TZ=Asia/Seoul',
        f'RUN export LANG=en_US.UTF-8',
        f'RUN apt-get update && apt-get install -y \
                                python3 \
                                python3-pip \
                                python3-venv \
                                bash \
                                bash-completion \
                                curl \
                                wget \
                                unzip \
                                nano \
                                ca-certificates \
                                software-properties-common \
                                locales \
                                tzdata \
                                build-essential \
                                pkg-config \
                                libmariadb-dev \
                                gcc \
                                portaudio19-dev \
                                && rm -rf /var/lib/apt/lists/*  # 설치 후 패키지 목록 삭제하여 용량 최적화',
        f'',
        f'RUN python3 -m venv /container_workspace/.venv',
        f'RUN /container_workspace/.venv/bin/pip install --upgrade pip setuptools wheel ',
        f'',
        f'COPY requirements.toml .',
        f'# RUN apt-get install uvicorn',
        f'RUN /container_workspace/.venv/bin/pip install --no-cache-dir -r requirements.toml',
        f'',
        f'COPY . .',
        f'',
        f'CMD ["/container_workspace/.venv/bin/python", "-m", "uvicorn", "project_fastapi.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]',
        f'',
    ]
    # run_project_docker_base(f=rf'{D_PROJECT}/project_fastapi.Dockerfile',f_dockerfile_script_list=f_dockerfile_script_list)
    run_project_docker_base(f=rf'{D_PROJECT}/test.Dockerfile', dockerfile_script_list=f_dockerfile_script_list)


# todo : pytest + assert 기반 마이그레이션
# todo : 테스트결과가 pass fail 형태로 종합되어 출력이 되도록, 실제 시스템, 서비스, 파일에는 반영이 안되어야 한다. 더미파일을 생성해서 확인하는 방향으로 설계.
# pk_dictionary.toml
# pk_dictionary.md
# todo : readme.md 에 dictionary 작성
# todo : dictionary
# todo : dictionary splitext vs
# shutdown ->> kill
# close ->>> kill # for 짧은단어
# start ->> open
# run ->> open
# exec ->> open
# restart ->> rerun
# open ->> activate
# assist # loop 로서 도움을 주는 프로그램
# save vs export
# import
# todo : add dictionary : item vs target, dirname vs p, basename vs nx, temp vs $
# todo uv 기반 파이썬 패키지 관리
# todo wsl ubuntu pkg nvim install
# todo : dictionary : ensure(pk code) vs verify(business code)
# necessary >  mandantory
