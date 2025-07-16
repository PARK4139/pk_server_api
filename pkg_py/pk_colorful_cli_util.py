from enum import Enum
from pkg_py.pk_core_constants import ColormaColorMap, STAMP_TEST, UNDERLINE

def print_prompt_via_colorama(prompt, colorama_code: Enum, line_feed_mode=1):
    from colorama import Fore
    # from colorama import init as pk_colorama_init # pk_print() 함수에서 import 하면 엄청 느려짐
    # pk_colorama_init(autoreset=True) # colorama 초기화 # [97m[ 출력예방 # 색상전이를 막을 수 있음, 최적화를 한다면 연산되어 콘솔에 출력되는 것을 모두 중단처리. CliUtilStateUtil.is_op_mode == True 에서 동작하도록 하는 것도 방법이다.
    # 혹시나 싶었는데 console_blurred 에서 팝업 기능과 충돌이 되는 것으로 보인다.

    # colorama_color 값에 해당하는 Fore 값으로 매핑, 리펙토리 후
    colorama_code_map_dict = {
        ColormaColorMap.BLACK: Fore.BLACK,
        ColormaColorMap.RED: Fore.RED,
        ColormaColorMap.GREEN: Fore.GREEN,
        ColormaColorMap.YELLOW: Fore.YELLOW,
        ColormaColorMap.BLUE: Fore.BLUE,
        ColormaColorMap.MAGENTA: Fore.MAGENTA,
        ColormaColorMap.CYAN: Fore.CYAN,
        ColormaColorMap.WHITE: Fore.WHITE,
        ColormaColorMap.RESET: Fore.RESET,
        ColormaColorMap.LIGHTBLACK_EX: Fore.LIGHTBLACK_EX,
        ColormaColorMap.LIGHTRED_EX: Fore.LIGHTRED_EX,
        ColormaColorMap.LIGHTGREEN_EX: Fore.LIGHTGREEN_EX,
        ColormaColorMap.LIGHTYELLOW_EX: Fore.LIGHTYELLOW_EX,
        ColormaColorMap.LIGHTBLUE_EX: Fore.LIGHTBLUE_EX,
        ColormaColorMap.LIGHTMAGENTA_EX: Fore.LIGHTMAGENTA_EX,
        ColormaColorMap.LIGHTCYAN_EX: Fore.LIGHTCYAN_EX,
        ColormaColorMap.LIGHTWHITE_EX: Fore.LIGHTWHITE_EX
    }
    colorama_code = colorama_code_map_dict.get(colorama_code, Fore.RESET)
    if line_feed_mode == 1:
        print(f"{colorama_code}{prompt}")
        return  # return 필요 검토
    elif line_feed_mode == 0:
        print(f"{colorama_code}{prompt}", end='')
    # colorama_color = colorama_to_fore.get(ColoramaUtil.LIGHTBLACK_EX, Fore.RESET)
    # print(f"{colorama_color}")


def print_red(prompt, line_feed_mode=1):
    print_prompt_via_colorama(prompt, colorama_code=ColormaColorMap.RED, line_feed_mode=line_feed_mode)


def print_success(prompt, line_feed_mode=1):
    print_prompt_via_colorama(prompt, colorama_code=ColormaColorMap.LIGHTGREEN_EX, line_feed_mode=line_feed_mode)


def print_magenta(prompt, line_feed_mode=1):
    print_prompt_via_colorama(prompt, colorama_code=ColormaColorMap.LIGHTMAGENTA_EX, line_feed_mode=line_feed_mode)


def print_light_white(prompt, line_feed_mode=1):
    print_prompt_via_colorama(prompt, colorama_code=ColormaColorMap.LIGHTWHITE_EX, line_feed_mode=line_feed_mode)


def print_light_yellow(prompt, line_feed_mode=1):
    print_prompt_via_colorama(prompt, colorama_code=ColormaColorMap.LIGHTYELLOW_EX, line_feed_mode=line_feed_mode)


def print_yellow(prompt, line_feed_mode=1):
    print_prompt_via_colorama(prompt, colorama_code=ColormaColorMap.YELLOW, line_feed_mode=line_feed_mode)


def print_light_blue(prompt, line_feed_mode=1):
    print_prompt_via_colorama(prompt, colorama_code=ColormaColorMap.LIGHTBLUE_EX, line_feed_mode=line_feed_mode)


def print_green(prompt, line_feed_mode=1):
    print_prompt_via_colorama(prompt, colorama_code=ColormaColorMap.LIGHTGREEN_EX, line_feed_mode=line_feed_mode)


def print_light_black(prompt, line_feed_mode=1):
    print_prompt_via_colorama(prompt, colorama_code=ColormaColorMap.LIGHTBLACK_EX, line_feed_mode=line_feed_mode)


def print_cyan(prompt, line_feed_mode=1):
    print_prompt_via_colorama(prompt, colorama_code=ColormaColorMap.CYAN, line_feed_mode=line_feed_mode)


def pk_print_v1(working_str, print_color='', line_feed_mode=1, STAMP=None, mode_verbose=1):
    from pkg_py.pk_core_constants import STAMP_DEBUG, STAMP_ERROR, STAMP_INTERACTIVE
    from pkg_py.pk_core_constants import STAMP_SUCCEEDED, STAMP_INFO
    from pkg_py.pk_core import get_time_as_
    from pkg_py.pk_core import get_txt_highlighted

    print_color = print_color.strip()

    try:
        if mode_verbose == 1:
            STAMP_TIME = rf'[ {get_time_as_('now')} ]'

            if STAMP is None:
                STAMP = STAMP_DEBUG
            if print_color == "grey":
                highlight_config_dict = {
                    "grey": [
                        STAMP_TIME, STAMP, working_str
                    ],
                }
                print(get_txt_highlighted(txt_whole=f'''{STAMP_TIME} {working_str}''', config_highlight_dict=highlight_config_dict))
            elif print_color == 'red':
                STAMP = STAMP_ERROR
                highlight_config_dict = {
                    'red': [
                        STAMP, working_str
                    ],
                    # "white": [
                    #     prompt
                    # ],
                    "grey": [
                        STAMP_TIME
                    ],
                }
                print(get_txt_highlighted(txt_whole=f'''{STAMP_TIME} {STAMP} {working_str}''', config_highlight_dict=highlight_config_dict))
            elif print_color == "yellow":
                STAMP = STAMP_TEST
                highlight_config_dict = {
                    "yellow": [
                        STAMP
                    ],
                    "white": [
                        working_str
                    ],
                    "grey": [
                        STAMP_TIME
                    ],
                }
                print(get_txt_highlighted(txt_whole=f'''{STAMP_TIME} {STAMP} {working_str}''', config_highlight_dict=highlight_config_dict))
            elif print_color == "blue":
                STAMP = STAMP_INFO
                highlight_config_dict = {
                    "blue": [
                        STAMP
                    ],
                    "white": [
                        working_str
                    ],
                    "grey": [
                        STAMP_TIME
                    ],
                }
                print(get_txt_highlighted(txt_whole=f'''{STAMP_TIME} {STAMP} {working_str}''', config_highlight_dict=highlight_config_dict))
            elif print_color == "green":
                STAMP = STAMP_SUCCEEDED
                highlight_config_dict = {
                    "green": [
                        STAMP
                    ],
                    "white": [
                        working_str
                    ],
                    "grey": [
                        STAMP_TIME
                    ],
                }
                print(get_txt_highlighted(txt_whole=f'''{STAMP_TIME} {STAMP} {working_str}''', config_highlight_dict=highlight_config_dict))
                # todo
                #  if success sound:
                #   success sound 를 print_color = 'green' 에 연동
            elif print_color == "white":
                STAMP = STAMP_INTERACTIVE
                print_light_white(f'''{STAMP_TIME} {STAMP} {working_str}''', line_feed_mode=line_feed_mode)
            elif print_color == "magenta":
                print_magenta(f'''{STAMP_TIME} {working_str}''', line_feed_mode=line_feed_mode)
            else:
                print_light_black(f'''{STAMP_TIME} {STAMP} {working_str}''')
                # [SUGGEST] # 조치, 제안,#  다른컬러가 있나?

        elif mode_verbose == 0:
            if print_color == "grey":
                print_light_black(f'''{working_str}''', line_feed_mode=line_feed_mode)
            elif print_color == 'red':
                print_red(f'''{working_str}''', line_feed_mode=line_feed_mode)
            elif print_color == "yellow":
                print_yellow(f'''{working_str}''', line_feed_mode=line_feed_mode)
            elif print_color == "blue":
                print_light_blue(f'''{working_str}''', line_feed_mode=line_feed_mode)
            elif print_color == "green":
                print_green(f'''{working_str}''', line_feed_mode=line_feed_mode)
            elif print_color == "white":
                print_light_white(f'''{working_str}''', line_feed_mode=line_feed_mode)
            elif print_color == "magenta":
                print_magenta(f'''{working_str}''', line_feed_mode=line_feed_mode)
            else:
                print_light_black(f'''{working_str}''')
                # [SUGGEST] # 조치, 제안,#  다른컬러가 있나?
    except:
        import traceback
        from pkg_py.pk_core import LTA
        print(f"{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}")
    # pk_print_v1 를 여러번 호출을 하면 호출횟수의 증가에 따라 속도저하 문제가 있음.-> pk_print_v2

def pk_print_v2(working_str, print_color='', line_feed_mode=1, STAMP=None, mode_verbose=1, highlight_config_dict=None):
    import traceback
    from pkg_py.pk_core_constants import (
        STAMP_DEBUG, STAMP_ERROR, STAMP_INTERACTIVE,
        STAMP_SUCCEEDED, STAMP_INFO, STAMP_TEST
    )
    from pkg_py.pk_core import get_time_as_, get_txt_highlighted, LTA
    try:
        STAMP_TIME = rf'[ {get_time_as_("now")} ]'
        print_color = print_color.strip()

        # 기본 STAMP 매핑
        default_stamp_by_color = {
            'red': STAMP_ERROR,
            'yellow': STAMP_TEST,
            'blue': STAMP_INFO,
            'green': STAMP_SUCCEEDED,
            'white': STAMP_INTERACTIVE,
            'grey': STAMP_DEBUG,
            '': STAMP_DEBUG,
        }

        # mode_verbose=1 (high detail)
        if mode_verbose == 1:
            stamp_to_use = STAMP if STAMP is not None else default_stamp_by_color.get(print_color, STAMP_DEBUG)
            color_config = {
                'red':     {'red': [stamp_to_use, working_str], 'grey': [STAMP_TIME]},
                'yellow':  {'yellow': [stamp_to_use], 'white': [working_str], 'grey': [STAMP_TIME]},
                'blue':    {'blue': [stamp_to_use], 'white': [working_str], 'grey': [STAMP_TIME]},
                'green':   {'green': [stamp_to_use], 'white': [working_str], 'grey': [STAMP_TIME]},
                'white':   None,  # handled separately
                'magenta': None,  # handled separately
                'grey':    {'grey': [STAMP_TIME, stamp_to_use, working_str]},
                '':        {'grey': [STAMP_TIME, stamp_to_use, working_str]}
            }

            # 별도 처리 색상
            if print_color == 'white':
                print_light_white(f'''{STAMP_TIME} {stamp_to_use} {working_str}''', line_feed_mode=line_feed_mode)
            elif print_color == 'magenta':
                print_magenta(f'''{STAMP_TIME} {working_str}''', line_feed_mode=line_feed_mode)
            else:
                config = color_config.get(print_color, color_config[''])
                if config:
                    print(get_txt_highlighted(
                        txt_whole=f'''{STAMP_TIME} {stamp_to_use} {working_str}''',
                        config_highlight_dict=config
                    ))

        # mode_verbose=0 (brief output only)
        elif mode_verbose == 0:
            color_func = {
                'grey': print_light_black,
                'red': print_red,
                'yellow': print_yellow,
                'blue': print_light_blue,
                'green': print_green,
                'white': print_light_white,
                'magenta': print_magenta,
                '': print_light_black
            }.get(print_color, print_light_black)

            color_func(working_str, line_feed_mode=line_feed_mode)

    except Exception:
        fallback = traceback.format_exc()
        print_light_black(f"[EXCEPTION in pk_print] {fallback} {'%%%FOO%%%' if LTA else ''}")

def pk_print_v3(working_str, print_color='', line_feed_mode=1, STAMP=None, mode_verbose=1, highlight_config_dict=None):
    import traceback
    from pkg_py.pk_core_constants import (
        STAMP_DEBUG, STAMP_ERROR, STAMP_INTERACTIVE,
        STAMP_SUCCEEDED, STAMP_INFO, STAMP_TEST
    )
    from pkg_py.pk_core import get_time_as_, get_txt_highlighted, LTA

    try:
        STAMP_TIME = rf'[ {get_time_as_("now")} ]'
        print_color = print_color.strip()

        default_stamp_by_color = {
            'red': STAMP_ERROR,
            'yellow': STAMP_TEST,
            'blue': STAMP_INFO,
            'green': STAMP_SUCCEEDED,
            'white': STAMP_INTERACTIVE,
            'grey': STAMP_DEBUG,
            '': STAMP_DEBUG,
        }

        if mode_verbose == 1:
            stamp_to_use = STAMP if STAMP is not None else default_stamp_by_color.get(print_color, STAMP_DEBUG)

            color_config = {
                'red':     {'red': [stamp_to_use, working_str], 'grey': [STAMP_TIME]},
                'yellow':  {'yellow': [stamp_to_use], 'white': [working_str], 'grey': [STAMP_TIME]},
                'blue':    {'blue': [stamp_to_use], 'white': [working_str], 'grey': [STAMP_TIME]},
                'green':   {'green': [stamp_to_use], 'white': [working_str], 'grey': [STAMP_TIME]},
                'white':   None,
                'magenta': None,
                'grey':    {'grey': [STAMP_TIME, stamp_to_use, working_str]},
                '':        {'grey': [STAMP_TIME, stamp_to_use, working_str]}
            }

            if print_color == 'white':
                print_light_white(f'''{STAMP_TIME} {stamp_to_use} {working_str}''', line_feed_mode=line_feed_mode)
            elif print_color == 'magenta':
                print_magenta(f'''{STAMP_TIME} {working_str}''', line_feed_mode=line_feed_mode)
            else:
                config = color_config.get(print_color, color_config[''])
                if config:
                    print(get_txt_highlighted(
                        txt_whole=f'''{STAMP_TIME} {stamp_to_use} {working_str}''',
                        config_highlight_dict=config
                    ))

        elif mode_verbose == 0:
            color_func = {
                'grey': print_light_black,
                'red': print_red,
                'yellow': print_yellow,
                'blue': print_light_blue,
                'green': print_green,
                'white': print_light_white,
                'magenta': print_magenta,
                '': print_light_black
            }.get(print_color, print_light_black)

            color_func(working_str, line_feed_mode=line_feed_mode)

    except Exception:
        fallback = traceback.format_exc()
        print_light_black(f"[EXCEPTION in pk_print] {fallback} {'%%%FOO%%%' if LTA else ''}")

def pk_print(working_str, print_color='', line_feed_mode=1, STAMP=None, mode_verbose=1, highlight_config_dict=None):
    # pk_print_v2(working_str=working_str, print_color=print_color, line_feed_mode=line_feed_mode, STAMP=STAMP, mode_verbose=mode_verbose, highlight_config_dict=highlight_config_dict)
    pk_print_v3(working_str=working_str, print_color=print_color, line_feed_mode=line_feed_mode, STAMP=STAMP, mode_verbose=mode_verbose, highlight_config_dict=highlight_config_dict)

def print_pk_divider(working_str = ''):
    print_magenta(f'''{UNDERLINE}{working_str}''', line_feed_mode=1)



def load_logged_set(PKL_PATH):
    import os
    import pickle

    if os.path.exists(PKL_PATH):
        with open(PKL_PATH, 'rb') as f:
            return pickle.load(f)
    return set()

def save_logged_set(logged_set, PKL_PATH):
    import os
    import pickle
    with open(PKL_PATH, 'wb') as f:
        pickle.dump(logged_set, f)

def pk_print_once(msg):
    from pkg_py.pk_core_constants import D_PKG_PKL
    import os
    f_pkl = f'{D_PKG_PKL}/state_about_pk_print_once.pkl'  
    logged_set = load_logged_set(f_pkl)
    if msg in logged_set:
        return
    pk_print(msg)
    logged_set.add(msg)
    save_logged_set(logged_set, f_pkl)
