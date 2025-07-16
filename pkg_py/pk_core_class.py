import json
from typing import Any

from pkg_py.pk_colorful_cli_util import pk_print
from pkg_py.pk_core import get_pk_input


class A2zCarDataStructure:
    # vpc_data_orm
    class RemoteDeviceDataStructure:
        vpc_local_ssh_public_key = None
        vpc_local_ssh_private_key = None
        vpc_purpose = None
        vpc_type = None
        vpc_ip = None
        vpc_port = None
        vpc_user_n = None
        vpc_pw = None
        vpc_side = None
        vpc_aifw_version = None
        vpc_aifw_packing_mode = None
        vpc_aifw_branch_n = None
        vpc_with_flash_image = None
        vpc_flash_image_version = None
        vpc_core_cnt = None
        vpc_proceser_name = None
        vpc_nvidia_serial = None
        vpc_os_distro_n = None
        vpc_identifier = None
        vpc_identifier_number = None
        vpc_jetpack_version = None
        vpc_wired_connection_reset = {}
        vpc_wired_connection_initial = {}
        vpc_wired_connection_1_new = {}
        vpc_wired_connection_3_new = {}
        vpc_available_test_ip_set = set()

        def __init__(self):
            pass

        def set_remote_device_data_field_all(self, pk_structure):
            from pkg_py.pk_core import LTA
            try:
                # self.identifier = pk_structure.identifier
                # self.jetpack_ver = pk_structure.jetpack_ver
                # self.vpc_flash_image = pk_structure.vpc_flash_image

                # swallow copy all field of pk_structure
                for key, value in pk_structure.__dict__.items():
                    setattr(self, key, value)

            except:
                import traceback
                from pkg_py.pk_colorful_cli_util import pk_print
                pk_print(working_str=rf"{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''} ", print_color='red')

        def print_remote_device_data_field_all(self, instance_name, with_none=0):
            from pkg_py.pk_core import LTA
            from pkg_py.pk_colorful_cli_util import pk_print, print_pk_divider
            if instance_name is None:
                instance_name = self.__class__.__name__
            print_pk_divider('%%%FOO%%%')
            if with_none == 1:
                for key, value in self.__dict__.items():
                    pk_print(f'''{instance_name}.{key}={value} {'%%%FOO%%%' if LTA else ''}''', print_color='blue')
            else:
                for key, value in self.__dict__.items():
                    if value is not None:
                        pk_print(f'''{instance_name}.{key}={value} {'%%%FOO%%%' if LTA else ''}''', print_color='blue')
            print_pk_divider('%%%FOO%%%')


class PkState250701():
    question = None
    option_download_and_play = None
    option_download_and_skip = None
    answer = None


from typing import Optional


class PkStateFromDB:
    def __init__(self):
        import sqlite3

        from pkg_py.pk_core_constants import D_PKG_DB

        self.sqlite3 = sqlite3

        self.pk_db_pnx = f"{D_PKG_DB}/pk.db"
        self.ensure_pk_db(self.pk_db_pnx)
        self.pk_db_connection = sqlite3.connect(self.pk_db_pnx)
        self.ensure_pk_db_table()

    def ensure_pk_db(self, pk_db_pnx):
        import os

        # sqlite3 는 file 기반이다. file 이 있어야 한다.
        if not os.path.exists(pk_db_pnx):
            os.makedirs(os.path.dirname(pk_db_pnx), exist_ok=True)

    def ensure_pk_db_table(self):
        cur = self.pk_db_connection.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS pk_table_state (
                id TEXT PRIMARY KEY,
                question TEXT,
                options_json TEXT,
                answer TEXT
            )
        """)
        self.pk_db_connection.commit()

    def save_answer(
            self,
            db_id: str,
            question: str,
            options: list[str],
    ) -> str:
        import json
        answer = get_pk_input(
            message=f'{question} answer=',
            answer_options=options
        )

        cur = self.pk_db_connection.cursor()
        cur.execute("""
            INSERT INTO pk_table_state (id, question, options_json, answer)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                question=excluded.question,
                options_json=excluded.options_json,
                answer=excluded.answer
        """, (db_id, question, json.dumps(options), answer))
        self.pk_db_connection.commit()
        return answer

    def get_v1(self, db_id: str) -> Optional[str]:
        from pkg_py.pk_core import LTA
        # db 에서 상태를 가져옴
        cur = self.pk_db_connection.cursor()
        cur.execute("SELECT answer FROM pk_table_state WHERE id = ?", (db_id,))
        row = cur.fetchone()
        value = row[0] if row else None
        pk_print(f'''db_id=value : {db_id}={value} {'%%%FOO%%%' if LTA else ''}''', print_color="green")
        return value

    def default_input_func(self, message: str, answer_options: list[str]) -> str:
        print(message)
        for i, opt in enumerate(answer_options):
            print(f"{i + 1}. {opt}")
        choice = input("선택: ")
        try:
            idx = int(choice.strip()) - 1
            return answer_options[idx]
        except:
            return answer_options[0]

    def reset_value(self, db_id: str):
        # pk db 초기화
        cur = self.pk_db_connection.cursor()
        cur.execute("UPDATE pk_table_state SET answer = NULL WHERE id = ?", (db_id,))
        self.pk_db_connection.commit()

    def set_v1(self, db_id: str, value):
        """
        # value 가 str 인 경우는 처리가능
        # TBD value 가 list 인 경우도 처리 가능하도록
        주어진 db_id에 대해 answer 값을 설정합니다.
        값이 이미 존재하면 업데이트하고, 없다면 새로 추가합니다.
        """
        cur = self.pk_db_connection.cursor()

        # 먼저 해당 id가 존재하는지 확인
        cur.execute("SELECT COUNT(*) FROM pk_table_state WHERE id = ?", (db_id,))
        exists = cur.fetchone()[0] > 0

        if exists:
            cur.execute("UPDATE pk_table_state SET answer = ? WHERE id = ?", (value, db_id))
        else:
            cur.execute("INSERT INTO pk_table_state (id, answer) VALUES (?, ?)", (db_id, value))

        self.pk_db_connection.commit()

    def set(self, db_id: str, value: Any):
        """
        주어진 db_id에 대해 answer 값을 설정합니다.
        value가 str, list, dict 등인 경우 모두 JSON으로 직렬화하여 저장합니다.
        """
        cur = self.pk_db_connection.cursor()

        # value를 JSON 문자열로 직렬화 (ensure_ascii=False → 한글 깨짐 방지)
        serialized_value = json.dumps(value, ensure_ascii=False)

        # 해당 id가 존재하는지 확인
        cur.execute("SELECT COUNT(*) FROM pk_table_state WHERE id = ?", (db_id,))
        exists = cur.fetchone()[0] > 0

        if exists:
            cur.execute("UPDATE pk_table_state SET answer = ? WHERE id = ?", (serialized_value, db_id))
        else:
            cur.execute("INSERT INTO pk_table_state (id, answer) VALUES (?, ?)", (db_id, serialized_value))

        self.pk_db_connection.commit()

    def get(self, db_id: str) -> Optional[Any]:
        """
        주어진 db_id에 대한 answer 값을 가져옵니다.
        JSON 문자열이면 자동으로 역직렬화하여 원래 Python 객체로 반환합니다.
        """
        from pkg_py.pk_core import LTA  # 사용 여부에 따라 유지
        cur = self.pk_db_connection.cursor()
        cur.execute("SELECT answer FROM pk_table_state WHERE id = ?", (db_id,))
        row = cur.fetchone()
        raw_value = row[0] if row else None

        # JSON 역직렬화 시도
        try:
            value = json.loads(raw_value) if raw_value is not None else None
        except (json.JSONDecodeError, TypeError):
            value = raw_value  # JSON 형식이 아니면 원본 그대로 반환

        # 디버그 출력
        pk_print(
            f'''db_id={db_id}, value={value} {'%%%FOO%%%' if LTA else ''}''',
            print_color="green"
        )
        return value

    def close(self):
        self.pk_db_connection.close()


class PkMents2025:
    # EN='ENGLISH MODE' # 아이디어 받자
    # KR='KOREAN MODE'
    # if KR:
    skip = "스킵"
    play = "재생"
    NOT_PREPARED_YET = "아직 준비되지 않은 서비스입니다"
    test = "테스트"
    NO = "아니오"
    YES = "응"
    CHECKED = "확인"
    OK_I_WILL_DO_IT_NOW = "지금할게"
    DONE = "했어"
    I_WANT_TO_TO_DO_NEXT_TIME = "다음에 할게"
    NEGATIVE = 'No'
    POSITIVE = 'Yes'
