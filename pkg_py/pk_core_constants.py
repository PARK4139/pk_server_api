import os
import socket
from enum import Enum
from pathlib import Path
# ____________________________________________________________________________________
HOSTNAME = os.environ.get('HOSTNAME', socket.gethostname())  # Windows, Linux, macOS 모두 처리
# ____________________________________________________________________________________
D_PROJECT = str(Path(__file__).parent.parent.absolute())  # __init__ 해당파일로 되어 있기 때문에. 위치가 복잡하게 되어 버렸다. 이를 __file__ 로 기준을 잡아서 경로를 수정하였다. 빌드를 하면서 알게되었는데 상대경로의 사용은 필연적인데, 상대경로로 경로를 설정할때 기준이 되는 절대경로 하나는 반드시 필요한 것 같다.
D_PROJECT_PARENTS = os.path.dirname(D_PROJECT)
D_HOME = os.environ.get('USERPROFILE', os.environ.get('HOME'))  # Windows나 Linux/macOS 모두 처리
# ____________________________________________________________________________________
D_C_DRIVE = rf'C:/'
D_D_DRIVE = rf'D:/'
D_F_DRIVE = rf'F:/'
D_G_DRIVE = rf'G:/'
D_H_DRIVE = rf'H:/'
D_I_DRIVE = rf'I:/'
D_J_DRIVE = rf'J:/'
D_DOWNLOADS = rf'{D_HOME}/Downloads'
D_WORKING = rf"{D_DOWNLOADS}/pk_working"
D_PK_MEMO = rf"{D_DOWNLOADS}/pk_memo"
D_WORKING_EXTERNAL = rf"D:/pk_working"
D_VENV = rf'{D_PROJECT}/.venv'
D_XLS_TO_MERGE = rf'{D_PROJECT}/pkg_xls/to_merge'
D_XLS_MERGED = rf'{D_PROJECT}/pkg_xls/merged'
D_VIDEOES_MERGED = rf"{D_WORKING}/pk_video_merged"
D_PK_RECYCLE_BIN = rf"{D_WORKING}/pk_recycle_bin"
D_PROJECT_VSTEST = rf'{D_PROJECT}/project_vstest'
D_PROJECT_RELEASE_SERVER = rf'{D_PROJECT}/project_release_server'
D_PROJECT_FASTAPI = rf'{D_PROJECT}/project_fastapi'
D_PROJECT_CMAKE = rf'{D_PROJECT}/project_cmake'
D_STATIC = os.path.join(D_PROJECT_FASTAPI, "pkg_web", "static")
D_PKG_EXE = rf'{D_PROJECT}/pkg_exe'
D_PKG_DB = rf'{D_PROJECT}/pkg_db'
D_PKG_CSV = rf'{D_PROJECT}/pkg_csv'
D_PKG_VIDEO = rf'{D_PROJECT}/pkg_video'
D_PKG_TXT = rf'{D_PROJECT}/pkg_txt'
D_PKG_TOML = rf'{D_PROJECT}/pkg_toml'
D_PKG_PK = rf'{D_PROJECT_PARENTS}/pk_memo/pkg_pk'
D_PKG_PY = rf'{D_PROJECT}/pkg_py'
D_PKG_PNG = rf'{D_PROJECT_FASTAPI}/pkg_png'
D_PKG_LOG = rf'{D_PROJECT}/pkg_log'
D_PKG_JSON = rf'{D_PROJECT}/pkg_json'
D_PKG_IMAGE = rf'{D_PROJECT}/pk_image'
D_PKG_DPL = rf'{D_PROJECT}/pkg_dpl'
D_PKG_CLOUD = rf'{D_PROJECT_FASTAPI}/pkg_cloud'
D_PKG_CMD = rf'{D_PROJECT}/pkg_cmd'
D_HOW = rf"{D_DOWNLOADS}/pk_working/pk_how"
D_EMPTY = rf"{D_WORKING}/pk_empty"
D_DOWNLOADING = rf"{D_WORKING}/pk_downloading"
D_DESKTOP = rf'{D_HOME}/Desktop'
D_DEPRECATED_EXTERNAL = rf"F:/pk_working/pk_deprecated"
D_CODING_TEST_RESULT = rf'{D_PROJECT}/pkg_coding_test_submit'
D_CLASSIFIED = rf"{D_DOWNLOADS}/pk_working"
D_ARCHIVED_EXTERNAL = rf"F:/pk_working/pk_archived"
D_ARCHIVED = rf"{D_DOWNLOADS}/pk_working/pk_archived"
D_PK_TEMP = rf"{D_HOME}/pk_temp"
D_PKG_PKL = rf"{D_PROJECT}/pkg_pkl"
# ____________________________________________________________________________________
F_VPC_MAMNAGEMENT_MAP_TOML = f'{D_PKG_TOML}/vpc_mamnagement_map.toml'
F_ALIAS_CMD = rf'{D_PKG_CMD}/pk_alias.cmd'
F_CONFIG_TOML = rf'{D_PROJECT}/pkg_toml/pk_config.toml'
F_VIDEO_LIST_ALLOWED_TO_LOAD_TXT = rf'{D_PKG_TXT}/f_video_list_allowed_to_load.txt'
F_LOCAL_PKG_CACHE = rf'{D_PROJECT}/pkg_alba/__pycache__/__init__.cpython-312.pyc'
F_MEMO_TRASH_BIN_TOML = rf'{D_PKG_TOML}/memo_trash_bin.toml'
F_MEMO_WORK_PK = rf"{D_PKG_PK}/pk_memo_working.pk"
F_MEMO_HOW_PK = rf"{D_PKG_PK}/pk_memo_how.pk"
F_ICON_PNG = rf"{D_PROJECT}/pkg_png/icon.PNG"
F_LOSSLESSCUT_EXE = rf"{D_DOWNLOADS}/pk_archived/LosslessCut-win-x64/LosslessCut.exe"
# F_FFMPEG_EXE = rf"{D_PKG_EXE}/ffmpeg.exe"
F_FFMPEG_EXE = rf"{D_DOWNLOADS}/pk_archived/LosslessCut-win-x64/resources/ffmpeg.exe"
F_SUCCESS_LOG = rf'{D_PROJECT}/pkg_log/success.log'
F_MACRO_LOG = rf'{D_PROJECT}/pkg_log/macro.log'
# DIRSYNC_LOG = rf'{PROJECT_D}/pkg_log/dirsync.log'
# YT_DLP_CMD = rf"{PROJECT_D}/pkg_yt_dlp/yt-dlp.cmd" # 2023.11.15 구버전
F_YT_DLP_EXE = rf"{D_PROJECT}/pkg_yt_dlp/yt-dlp.exe"  # 2024.04.09 신버전
F_JQ_WIN64_EXE = rf"{D_PROJECT}/pkg_jq/jq-win64.exe"
F_DB_YAML = rf"{D_PROJECT}/pkg_yaml/db.yaml"
F_USELESS_FILE_NAMES_TXT = rf"{D_PKG_TXT}/useless_file_names.txt"
F_SILENT_MP3 = rf"{D_PROJECT}/pkg_sound/silent.mp3"
F_POP_SOUND_POP_SOUND_WAV = rf"{D_PROJECT}/pkg_sound/pop_sound.wav"
F_PKG_SOUND_POTPLAYER64_DPL = rf"{D_PROJECT}/pkg_sound/PotPlayer64.dpl"
F_PKG_VIDEO_POTPLAYER64_DPL = rf"{D_PROJECT}/pkg_video/PotPlayer64.dpl"
F_DB_JSON = rf"{D_PKG_JSON}/db.json"
F_BOOKS_JSON = rf"{D_PKG_JSON}/books.json"
F_USERS_JSON = rf"{D_PKG_JSON}/users.json"
F_NAV_ITEMS_JSON = rf"{D_PKG_JSON}/nav_items.json"
# PYCHARM64_EXE: str = rf'{os.environ.get("PyCharm Community Edition").replace(";", "")}/pycharm64.exe'
F_PYCHARM64_EXE = rf'{(os.environ.get("PyCharm Community Edition") or "").replace(";", "")}/pycharm64.exe'
F_MERGED_EXCEL_FILE = rf'{D_PROJECT}/pkg_xls/merged/머지결과물.xlsx'
F_MONTSERRAT_THIN_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-Thin.ttf"
F_NOTOSANSKR_VARIABLEFONT_WGHT_TTF = rf"{D_PROJECT}/pkg_font/Noto_Sans_KR/NotoSansKR-VariableFont_wght.ttf"
F_NOTOSANSKR_BLACK_TTF = rf"{D_PROJECT}/pkg_font/NotoSansKR-Black.ttf"
F_NOTOSANSKR_BOLD_TTF = rf"{D_PROJECT}/pkg_font/NotoSansKR-Bold.ttf"
F_NOTOSANSKR_EXTRABOLD_TTF = rf"{D_PROJECT}/pkg_font/NotoSansKR-ExtraBold.ttf"
F_NOTOSANSKR_EXTRALIGHT_TTF = rf"{D_PROJECT}/pkg_font/NotoSansKR-ExtraLight.ttf"
F_NOTOSANSKR_LIGHT_TTF = rf"{D_PROJECT}/pkg_font/NotoSansKR-Light.ttf"
F_NOTOSANSKR_MEDIUM_TTF = rf"{D_PROJECT}/pkg_font/NotoSansKR-Medium.ttf"
F_NOTOSANSKR_REGULAR_TTF = rf"{D_PROJECT}/pkg_font/NotoSansKR-Regular.ttf"
F_NOTOSANSKR_SEMIBOLD_TTF = rf"{D_PROJECT}/pkg_font/NotoSansKR-SemiBold.ttf"
F_NOTOSANSKR_THIN_TTF = rf"{D_PROJECT}/pkg_font/NotoSansKR-Thin.ttf"
F_GMARKETSANSTTFBOLD_TTF = rf"{D_PROJECT}/pkg_font/GmarketSansTTFBold.ttf"
F_GMARKETSANSTTFLIGHT_TTF = rf"{D_PROJECT}/pkg_font/GmarketSansTTFLight.ttf"
F_GMARKETSANSTTFMEDIUM_TTF = rf"{D_PROJECT}/pkg_font/GmarketSansTTFMedium.ttf"
F_ITALIC_VARIABLEFONT_WGHT_TTF = rf"{D_PROJECT}/pkg_font/Montserrat/Montserrat-Italic-VariableFont_wght.ttf"
F_MONTSERRAT_VARIABLEFONT_WGHT_TTF = rf"{D_PROJECT}/pkg_font/Montserrat/Montserrat-VariableFont_wght.ttf"
F_MONTSERRAT_BLACK_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-Black.ttf"
F_MONTSERRAT_BLACKITALIC_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-BlackItalic.ttf"
F_MONTSERRAT_BOLD_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-Bold.ttf"
F_MONTSERRAT_BOLDITALIC_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-BoldItalic.ttf"
F_MONTSERRAT_EXTRABOLD_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-ExtraBold.ttf"
F_MONTSERRAT_EXTRABOLDITALIC_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-ExtraBoldItalic.ttf"
F_MONTSERRAT_EXTRALIGHT_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-ExtraLight.ttf"
F_MONTSERRAT_EXTRALIGHTITALIC_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-ExtraLightItalic.ttf"
F_MONTSERRAT_ITALIC_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-Italic.ttf"
F_MONTSERRAT_LIGHT_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-Light.ttf"
F_MONTSERRAT_LIGHTITALIC_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-LightItalic.ttf"
F_MONTSERRAT_MEDIUM_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-Medium.ttf"
F_MONTSERRAT_MEDIUMITALIC_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-MediumItalic.ttf"
F_MONTSERRAT_REGULAR_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-Regular.ttf"
F_MONTSERRAT_SEMIBOLD_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-SemiBold.ttf"
F_MONTSERRAT_SEMIBOLDITALIC_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-SemiBoldItalic.ttf"
F_MONTSERRAT_THINITALIC_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-ThinItalic.ttf"
F_POPPINS_BLACK_TTF = rf"{D_PROJECT}/pkg_font/Poppins-Black.ttf"
F_POPPINS_BLACKITALIC_TTF = rf"{D_PROJECT}/pkg_font/Poppins-BlackItalic.ttf"
F_POPPINS_BOLD_TTF = rf"{D_PROJECT}/pkg_font/Poppins-Bold.ttf"
F_POPPINS_BOLDITALIC_TTF = rf"{D_PROJECT}/pkg_font/Poppins-BoldItalic.ttf"
F_POPPINS_EXTRABOLD_TTF = rf"{D_PROJECT}/pkg_font/Poppins-ExtraBold.ttf"
F_POPPINS_EXTRABOLDITALIC_TTF = rf"{D_PROJECT}/pkg_font/Poppins-ExtraBoldItalic.ttf"
F_POPPINS_EXTRALIGHT_TTF = rf"{D_PROJECT}/pkg_font/Poppins-ExtraLight.ttf"
F_POPPINS_EXTRALIGHTITALIC_TTF = rf"{D_PROJECT}/pkg_font/Poppins-ExtraLightItalic.ttf"
F_POPPINS_ITALIC_TTF = rf"{D_PROJECT}/pkg_font/Poppins-Italic.ttf"
F_POPPINS_LIGHT_TTF = rf"{D_PROJECT}/pkg_font/Poppins-Light.ttf"
F_POPPINS_LIGHTITALIC_TTF = rf"{D_PROJECT}/pkg_font/Poppins-LightItalic.ttf"
F_POPPINS_MEDIUM_TTF = rf"{D_PROJECT}/pkg_font/Poppins-Medium.ttf"
F_POPPINS_MEDIUMITALIC_TTF = rf"{D_PROJECT}/pkg_font/Poppins-MediumItalic.ttf"
F_POPPINS_REGULAR_TTF = rf"{D_PROJECT}/pkg_font/Poppins-Regular.ttf"
F_POPPINS_SEMIBOLD_TTF = rf"{D_PROJECT}/pkg_font/Poppins-SemiBold.ttf"
F_POPPINS_SEMIBOLDITALIC_TTF = rf"{D_PROJECT}/pkg_font/Poppins-SemiBoldItalic.ttf"
F_POPPINS_THIN_TTF = rf"{D_PROJECT}/pkg_font/Poppins-Thin.ttf"
F_POPPINS_THINITALIC_TTF = rf"{D_PROJECT}/pkg_font/Poppins-ThinItalic.ttf"
F_RUBIKDOODLESHADOW_REGULAR_TTF = rf"{D_PROJECT}/pkg_font/RubikDoodleShadow-Regular.ttf"  # 너무 귀여운 입체감 있는 영어폰트
F_PYCHARM64_EDITION_2024_03_01_EXE = r"C:/Program Files/JetBrains/PyCharm Community Edition 2024.3.1/bin/pycharm64.exe"
F_HISTORICAL_PNX =  rf'{D_PKG_TXT}/historical_pnx.txt'
F_HISTORICAL_SEARCH_KEYWORD =  rf'{D_PKG_TXT}/historical_search_keyword.txt'
# ____________________________________________________________________________________
PK_WSL_DISTRO_N='wsl_pk_ubuntu_24_04'
# ____________________________________________________________________________________
STAMP_DICT = "[ DICT ]"
STAMP_TUPLE = "[ TUPLE ]"
STAMP_SET = "[ SET ]"
STAMP_LIST = "[ LIST ]"
STAMP_SUCCEEDED = "[ SUCCEEDED ]"
STAMP_ATTEMPTED = '[ ATTEMPTED ]'
STAMP_INFO = "[ INFO ]"
STAMP_DEBUG = "[ DEBUG ]"
STAMP_RETRY = "[ RETRY ]"
STAMP_ERROR = "[ ERROR ]"
STAMP_INTERACTIVE = "[ INTERACTIVE ]"
STAMP_REMOTE_DEBUG = "[ REMOTE DEBUG ]"
STAMP_REMOTE_ERROR = "[ REMOTE ERROR ]"
STAMP_PYTHON_DEBUGGING_NOTE = '[ DEBUGGING NOTE ]'
STAMP_EXCEPTION_DISCOVERED = '[ EXCEPTION DISCOVERED ]'
STAMP_UNIT_TEST_EXCEPTION_DISCOVERED = '[ UNIT TEST EXCEPTION DISCOVERED ]'
STAMP_TRY_GUIDE = '[ TRY GUIDE ]'
STAMP_TORRENTQQ = '[ TORRENTQQ ]'
STAMP_TEST = "[ TEST ]"
STAMP_PK_DEBUGER_ENVIRONMENT = rf"(pk_debuger)"
STAMP_PK_ENVIRONMENT = rf"(pk)"
STAMP_PK_ENVIRONMENT_WITHOUT_BRAKET = rf"pk"
# STAMP_PK_ENVIRONMENT = rf"(pk_server_fastapi)"
# ____________________________________________________________________________________
NO = "그냥 닫아"
YES = "응"


# ____________________________________________________________________________________
# def __init__(self):
#     try:
#         os.system('chcp 65001 >nul')
#         Friday.PYCHARM64_EXE = rf'{os.environ.get("PyCharm Community Edition").replace(";", "")}/pycharm64.exe'
#     except AttributeError:
#         pass
#     except Exception:
#         print_light_black(f"{traceback.format_exc()}")

class ColormaColorMap(Enum):
    RED = 'red'
    GREEN = "GREEN"
    BLACK = "BLACK"
    YELLOW = "YELLOW"
    BLUE = "BLUE"
    MAGENTA = "MAGENTA"
    CYAN = "CYAN"
    WHITE = "WHITE"
    RESET = "RESET"
    LIGHTBLACK_EX = "LIGHTBLACK_EX"
    LIGHTRED_EX = "LIGHTRED_EX"
    LIGHTGREEN_EX = "LIGHTGREEN_EX"
    LIGHTYELLOW_EX = "LIGHTYELLOW_EX"
    LIGHTBLUE_EX = "LIGHTBLUE_EX"
    LIGHTMAGENTA_EX = "LIGHTMAGENTA_EX"
    LIGHTCYAN_EX = "LIGHTCYAN_EX"
    LIGHTWHITE_EX = "LIGHTWHITE_EX"


class Encoding(Enum):
    # class Encoding(Enum, str):
    # class Encoding(str, Enum):
    CP949 = 'cp949'
    UTF8 = 'utf-8'
    euc_kr = 'euc-kr'

    # def __str__(self):
    #     return self.value # Encoding.CP949.value 해도 되는데, chatGPT 는 __str__()를 override 해서 사용하는 것을 추천


class PkFilter(Enum):
    url_like = 'url_like'
    url_false = 'url_false'


# ____________________________________________________________________________________
UNDERLINE = '_' * 59 + " "  # 제목작성 시 앞부분에 적용되는 기준인데 pep8 최대권장길이(79)를 기준으로 20 자 내외로 제목작성을 작성을 최대한 준수
UNDERLINE_SHORT = '_' * 6
INDENTATION_PROMISED = ' ' * 5
PK_BLANK = ' '
BIGGEST_PNXS = []  # 300 MB 이상 백업대상
SMALLEST_PNXS = []
PLAYING_SOUNDS = []
PYGLET_PLAYER = None  # context 로 state 저장하는 것이 나을 듯.
PREVIOUS_MP3_LENGTH_USED_IN_SPEAK_AS_ASYNC = 0
ROUTINES = [
    '즐거운일 1개',
    '음악틀기',
    '물 한컵',
    '선풍기로 방환기 1분 이상',
    '세수',
    '로션',
    '아침식사',
    "프로폴리스 한알",
    '물가글(혹시 구내염 있으시면 가글양치)',
    '양치 WITHOUT TOOTH PASTE',
    '양치 WITH TOOTH PASTE',
    '양치 WITH GARGLE',
    '물가글',
    '스트레칭 밴드 V 유지 런지 30개',
    '계단 스쿼트 30 개',
    '푸쉬업 30 개',
    '점심식사',
    '저녁식사',
]
COUNTS_FOR_GUIDE_TO_SLEEP = []
VIDEO_IDS_ALLOWED = [
    '617', '616', '625', '620', '614', '609', '606',
    '315', '313', '303', '302', '308',
    '248', '247', '244', '137', '136', '133',
]
AUDIO_IDS_ALLOWED = [
    '234', '140-2', '140-1', '251', '249', '233', '140', '139',
    # '250',
]
members = []  # 리스트에 저장, 런타임 중에만 저장이 유지됨, 앱종료 시 데이터 삭제
todos = []  # 리스트에 저장, 런타임 중에만 저장이 유지됨, 앱종료 시 데이터 삭제

pi = 3.141592

click_detected = False  # 클릭 감지 상태를 저장하는 클래스 변수 # 1 곳에서만 호출됨 # todo : 확인해서 필요없는 기능이면 추후 삭제