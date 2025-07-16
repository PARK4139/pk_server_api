import os
import sys
import traceback

from colorama import init as pk_colorama_init

from pk_core import download_youtube_video, get_pk_input
from pkg_py.pk_core_constants import D_PKG_DB, UNDERLINE, D_PROJECT
from pk_colorful_cli_util import pk_print
from pkg_py.pk_core_class import PkMents2025, PkState250701, PkStateFromDB

pkg_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
if pkg_path not in sys.path:
    sys.path.append(pkg_path)

if __name__ == "__main__":
    try:
        pk_colorama_init(autoreset=True)
        
        pk_db = PkStateFromDB()
        db_id = 'download_option'
        pk_db.reset_value(db_id = db_id) 
        pk_db.save_answer(question= "play or skip video after download?", options=[PkMents2025.skip, PkMents2025.play], db_id = db_id)
        
        pk_db = PkStateFromDB()
        db_id = 'open historical f' # failed list, 재시도하기 좋도록 이력을 남긴다. 성공한것은 삭제한다.
        pk_db.reset_value(db_id = db_id) 
        pk_db.save_answer(question= "open historical file?", options=[PkMents2025.NO, PkMents2025.YES], db_id = db_id)
        
        while 1:
            download_youtube_video()
    except Exception as e:
        import traceback
        traceback.print_exc()
        # 예외 처리
        pk_print(f'{UNDERLINE}예외발생 s\n\n', print_color='red')
        pk_print(f'{traceback.format_exc()}\n', print_color='red')
        pk_print(f'{UNDERLINE}예외발생 e\n\n', print_color='red')
        script_to_run_python_program_in_venv = rf'{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate'
        pk_print(script_to_run_python_program_in_venv)