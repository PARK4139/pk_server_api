import os.path
from typing import Literal, Optional
from uuid import uuid4

from pydantic import BaseModel, field_validator
from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import Session

from pkg_py.pk_core_constants import D_STATIC, D_PROJECT_FASTAPI, D_PKG_CLOUD, D_PKG_PNG, F_CONFIG_TOML
from pkg_py.pk_core import get_time_as_, ensure_pnx_made, get_pnx_os_style
# import openpyxl  # pip install openpyxl
# import os
# import pandas as pd
# from openpyxl.styles import Font, Alignment, PatternFill, Color, Border, Side
# from colorama import Fore
# from datetime import datetime
# from enum import Enum
# from fastapi import HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from functools import partial
# from gtts import gTTS  # Google TTS 적용
# from mutagen.mp3 import MP3
# from pkg_py import constants
# from pkg_py.pk_core_constants import D_PROJECT, F_CONFIG_TOML
# from pkg_py.pk_core import click_center_of_img_recognized_by_mouse_left, get_random_alphabet, press
# from pkg_py.pk_core import get_time_as_, make_pnx, is_letters_cnt_zero, write_str_to_f
# from pkg_py.pk_core import raise_exception_after_special_charcater_check
# from pkg_py.pk_colorful_cli_util import pk_print
# from pydantic import BaseModel, field_validator
# from sqlalchemy import Column, Integer, String, text as sqlalchecdmy_text, VARCHAR, select, DateTime
# from sqlalchemy import create_engine
# from sqlalchemy.orm import Session
# from sqlalchemy.orm import sessionmaker, declarative_base
# from typing import Literal, Optional, TypeVar
# from uuid import uuid4, UUID
# import asyncio
# import inspect
# import json
# import keyboard
# import mutagen
# import numpy
# import os.path
# import pandas as pd
# import platform
# import pyglet
# import random
# import re
# import send2trash  # pip install send2trash
# import shutil
# import string
# import subprocess
# import sys
# import threading
# import time
# import toml
# import traceback
# import urllib.parse as urllib_parser

# [OPTION] 개발/운영 모드
LOCAL_TEST_ACTIVATE = 1

class ProjectDatabaseUtil:
    # Pydantic은 Python의 데이터 유효성 검사 및 직렬화를 위한 라이브러리,
    # BaseModel은 Pydantic에 built in 되어 있다,
    # 데이터 모델을 정의하고 유효성을 검사하며 직렬화/역직렬화를 수행하는 기능을 제공합니다
    # auto increment 하고 싶어 pydantic model 로 구현
    class Board(BaseModel):
        id: int
        title: str
        content: str

    @staticmethod
    def is_board_validated(board: Board) -> bool:
        # Board(게시물)의 유효성을 검사하는 커스텀 비지니스 로직을 구현, create/update 의 경우에 사용
        if not board.title:
            return False
        if not board.content:
            return False
        return True

    class Book(BaseModel):  # BaseModel 를 상속받은 Book 은 일반적인 객체가 아니다. type 을 출력해봐도 pydantic 의 하위 객체를 상속한 것으로 보인다
        id: Optional[str] = uuid4().hex  # Optional 을 설정하면 nullable 되는 거야? # 여기서 할당을 시키면 put() 동작하며 id가 바뀌어버린다. put()에서 업데이트되도록 따로 설정했다.
        name: str
        genre: Literal["러브코메디", "러브픽션", "액션"]  # string literal validation 설정, 이 중 하나만 들어갈 수 있음
        # price: float
        price: int

    class TodoItem(BaseModel):
        id: str
        title: str
        completed: bool

    class User(BaseModel):  # 여기에 validation 해두면 docs에서 post request 시 default 값 지정해 둘 수 있음.
        # id: str = uuid4().hex + get_time_as_('%Y%m%d%H%M%S%f') + get_random_alphabet()  # 진짜id 는 이렇게 default 로 들어가게하고, 사용자 id 는 e-mail
        id: str
        pw: str
        name: str
        date_join: str = get_time_as_('%Y-%m-%d %H:%M %S%f')
        date_logout_last: str
        address_house: str
        address_e_mail: str
        number_phone: str

        @classmethod
        @field_validator('id')
        def validate_id(cls, id):
            if 53 < len(id) or 53 < len(id):
                return {"fail", "id 는 53 자리 이상 이거나 이하 일 수 없습니다"}
            return id

        @classmethod
        @field_validator('pw')
        def validate_pw(cls, pw):
            # 다시 작성
            return pw

        @classmethod
        @field_validator('name')
        def validate_name(cls, name):
            if 30 < len(name):
                return {"fail", "name 은 30 자리 이상 일 수 없습니다"}
            return name

        @classmethod  # class 간 종속 관계가 있을 때 하위 class 에 붙여 줘야하나?, cls, 파라미터와 함께? , instance를 생성하지 않고 호출 가능해?
        @field_validator('date_join')
        def validate_date_join(cls, date_join):
            # datetime.strptime(date_join, '%Y-%m-%d %H:%M %S%f')
            # 다시 작성
            return date_join

        @classmethod
        @field_validator('address_e_mail')
        def validate_address_e_mail(cls, address_e_mail):
            # 다시 작성
            return address_e_mail

    class LoginForm(BaseModel):
        id: str
        pw: str

    class JoinForm(BaseModel):  # 회원가입 유효성검사 설정
        id: str  # 필수항목
        pw: str
        pw2: str
        name: str
        pw: str
        phone_no: str
        address: str
        e_mail: str
        age: str
        birthday: str
        date_joined: Optional[str]  # nullable
        date_canceled: Optional[str]
        fax_no: Optional[str]
        business_registration_no: Optional[str]
        company_name: Optional[str]
        department: Optional[str]
        position: Optional[str]
        company_address: Optional[str]

    class jinja_data(BaseModel):  # 모든 데이터를 수집하고, Optional 로 할당.
        id: Optional[str]  # nullable
        pw: Optional[str]
        prefix_promised: Optional[str]
        random_bytes: Optional[str]
        random_str: Optional[str]
        pw2: Optional[str]
        name: Optional[str]
        pw: Optional[str]
        phone_no: Optional[str]
        address: Optional[str]
        e_mail: Optional[str]
        age: Optional[str]
        date_joined: Optional[str]
        date_canceled: Optional[str]
        fax_no: Optional[str]
        business_registration_no: Optional[str]
        company_name: Optional[str]
        department: Optional[str]
        position: Optional[str]
        company_address: Optional[str]
        birthday: Optional[str]
        items: Optional[list]


class MySqlUtil:
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, declarative_base
    import toml
    config = toml.load(F_CONFIG_TOML)
    pk_driver = config["pk_mysql"]["driver"]
    pk_host = config["pk_mysql"]["host"]
    pk_port = config["pk_mysql"]["port"]
    pk_user = config["pk_mysql"]["user"]
    pk_pw = config["pk_mysql"]["pw"]
    pk_database = config["pk_mysql"]["database_n"]
    pk_charset = config["pk_mysql"]["charset"]
    pk_mysql_uri = f"{pk_driver}://{pk_user}:{pk_pw}@{pk_host}:{pk_port}/{pk_database}?charset={pk_charset}"

    engine = create_engine(pk_mysql_uri)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()

    @staticmethod
    def get_session():  # ?  generator 로 되어있는데..?
        db = MySqlUtil.SessionLocal()
        try:
            yield db
        finally:
            db.close()

    @staticmethod
    def get_session_local():
        db = MySqlUtil.SessionLocal()
        return db

    @staticmethod
    def execute(native_query: str):  # without sqlarchemy
        from sqlalchemy import text as sqlalchecdmy_text
        # engine = create_engine(Config.url)
        connection = MySqlUtil.engine.connect()
        try:
            for word_reserved in ['delete', 'update']:
                if word_reserved in native_query.lower():
                    from sqlalchemy import text as sqlalchemy_text
                    connection.execute(sqlalchemy_text(native_query))
                    # connection.execute(sqlalchecdmy_text(native_query))
                    pk_print(native_query)
                    return
            for word_reserved in ['truncate']:
                if word_reserved not in native_query.lower():
                    cr = connection.execute(sqlalchecdmy_text(native_query))
                    df = pd.DataFrame(cr.fetchall(), columns=cr.keys())  # result.fetchall() 를 DataFrame으로 변환
                    pk_print(native_query)
                    return df
                else:
                    pk_print(rf'''word_reserved : {word_reserved}''')
        except Exception:
            traceback.print_exc(file=sys.stdout)
        finally:
            connection.close()

    @staticmethod
    def execute2(native_query: str):
        import mysql.connector
        try:
            config = toml.load(F_CONFIG_TOML)
            mysql_config = {
                "user": config["pk_mysql"]["user"],
                "pw": config["pk_mysql"]["pw"],
                "host": config["pk_mysql"]["host"],
                "database": config["pk_mysql"]["database_n"],
                "raise_on_warnings": config["pk_mysql"]["raise_on_warnings"]
            }
            conn = mysql.connector.connect(**mysql_config)
            cursor = conn.cursor()

            query = native_query
            cursor.execute(query)

            result = cursor.fetchall()  # 모든 결과를 가져올 때
            pk_print(rf'''type(result) : {type(result)}''')
            pk_print(rf'''len(result) : {len(result)}''')

            # result = cursor.fetchone()  # 첫 번째 결과만 가져올 때
            # pk_print(rf'''type(result) : {type(result)}''')
            # pk_print(rf'''len(result) : {len(result)}''')

        except:
            traceback.print_exc(file=sys.stdout)
        finally:
            cursor.close()
            conn.close()


class MemberUtil:
    class Member(MySqlUtil.Base):  # orm 설정에는 id 있음
        __tablename__ = "members"
        __table_args__ = {'extend_existing': True}
        # __table_args__ = {'extend_existing': True, 'mysql_collate': 'utf8_general_ci'} # encoding 안되면 비슷하게 방법을 알아보자  mysql 에 적용이 가능한 코드로 보인다.
        Member_id = Column(Integer, primary_key=True, autoincrement=True)
        id = Column(VARCHAR(length=30))
        name = Column(VARCHAR(length=30))
        e_mail = Column(VARCHAR(length=30))
        phone_no = Column(VARCHAR(length=13))
        address = Column(VARCHAR(length=255))
        birthday = Column(VARCHAR(length=50))
        pw = Column(VARCHAR(length=100))
        date_joined = Column(VARCHAR(length=50))
        date_canceled = Column(VARCHAR(length=50))

    class MemberBase(BaseModel):  # pydantic validator 설정에는 Member_id 없음
        name: str
        pw: str
        phone_no: str
        address: str
        e_mail: str
        age: str
        id: str
        date_joined: str
        date_canceled: str

        @staticmethod
        @field_validator('id')
        def validate_id(value):
            MemberUtil.validate_id(value)

        @staticmethod
        @field_validator('name')
        def validate_name(value):
            MemberUtil.validate_name(value)

        @staticmethod
        @field_validator('e_mail')
        def validate_e_mail(value):
            MemberUtil.validate_e_mail(value)

        @staticmethod
        @field_validator('phone_no')
        def validate_phone_no(value):
            MemberUtil.validate_phone_no(value)

        @staticmethod
        @field_validator('address')
        def validate_address(value):
            MemberUtil.validate_address(value)

        @staticmethod
        @field_validator('birthday')
        def validate_birthday(value):
            MemberUtil.validate_birthday(value)

        @staticmethod
        @field_validator('pw')
        def validate_pw(value):
            MemberUtil.validate_pw(value)

        @staticmethod
        @field_validator('date_joined')
        def validate_date_joined(value):
            MemberUtil.validate_date_joined(value)

        @staticmethod
        @field_validator('date_canceled')
        def validate_date_canceled(value):
            MemberUtil.validate_date_canceled(value)

        @staticmethod  # class 간 종속 관계가 있을 때 하위 class 에 붙여 줘야하나?, cls, 파라미터와 함께? , instance를 생성하지 않고 호출 가능해?
        @field_validator('date_join')
        def validate_date_join(value):
            MemberUtil.validate_date_join(value)
            # datetime.strptime(date_join, '%Y-%m-%d %H:%M %S%f')
            if len(value) != 18:
                raise HTTPException(status_code=400, detail="유효한 날짜가 아닙니다.")
            return value

        @staticmethod
        @field_validator('pw')
        def validate_pw(value):
            MemberUtil.validate_pw(value)
            if len(value) != MemberUtil.Member.__table__.c.vpc_pw.type.length:
                raise HTTPException(status_code=400, detail="유효한 이메일 주소가 아닙니다.")
            return value

    @staticmethod
    def get_member_validated(member):
        pk_print(f"{inspect.currentframe().f_code.co_name}()")

        # Member 클래스의 필드 개수 확인
        field_count = len(MemberUtil.Member.__table__.c)
        print(rf'''field_count : {field_count}''')

        targets_validated = [
            {"field_en": 'name', "field_ko": "이름", "field_validation_func": MemberUtil.validate_name, "field_length_limit": MemberUtil.Member.__table__.c.name.type.length},
            {"field_en": 'id', "field_ko": "아이디", "field_validation_func": MemberUtil.validate_id, "field_length_limit": MemberUtil.Member.__table__.c.id.type.length},
            {"field_en": 'phone_no', "field_ko": "전화번호", "field_validation_func": MemberUtil.validate_phone_no, "field_length_limit": MemberUtil.Member.__table__.c.phone_no.type.length},
            {"field_en": 'e_mail', "field_ko": "이메일", "field_validation_func": MemberUtil.validate_e_mail, "field_length_limit": MemberUtil.Member.__table__.c.e_mail.type.length},
            {"field_en": 'pw', "field_ko": "비밀번호", "field_validation_func": MemberUtil.validate_pw, "field_length_limit": MemberUtil.Member.__table__.c.vpc_pw.type.length},
            {"field_en": 'address', "field_ko": "주소", "field_validation_func": MemberUtil.validate_address, "field_length_limit": MemberUtil.Member.__table__.c.address.type.length},
            {"field_en": 'birthday', "field_ko": "생년월일", "field_validation_func": MemberUtil.validate_birthday, "field_length_limit": MemberUtil.Member.__table__.c.birthday.type.length},
            {"field_en": 'date_joined', "field_ko": "가입일", "field_validation_func": MemberUtil.validate_date_joined, "field_length_limit": MemberUtil.Member.__table__.c.date_joined.type.length},
            {"field_en": 'date_canceled', "field_ko": "탈퇴일", "field_validation_func": MemberUtil.validate_date_canceled, "field_length_limit": MemberUtil.Member.__table__.c.date_canceled.type.length},
        ]
        for target in targets_validated:
            field_en = target["field_en"]
            field_ko = target["field_ko"]
            field_validation_func = target["field_validation_func"]
            field_length_limit = target["field_length_limit"]
            try:
                pk_print(rf'''member[field_en] : {member[field_en]}''')
                if len(member[field_en]) > target['field_length_limit']:
                    raise HTTPException(status_code=400, detail=f"{field_ko}({field_en})의 길이제한은 {field_length_limit}자 이하여야 합니다.")
                else:
                    field_validation_func(member[field_en])  # success, 호출할 수 없는 함수의 내부에 구현된 부분이 필요한것 이므로 내부에 구현된 것을 다른 클래스에 구현해서 참조하도록 로직 분리,
            except KeyError:
                pk_print(rf'''member[field_en] 에서 KeyError 발생했습니다, field_en={field_en}''')
                pass
        return member

    @staticmethod
    def validate_member(member):
        pk_print(f"{inspect.currentframe().f_code.co_name}()")
        MemberUtil.get_member_validated(member)

    class MemberCreate(MemberBase):
        pass

    class MemberExtendedMemberBase(MemberBase):
        name: str
        pw: str
        phone_no: str
        address: str
        e_mail: str
        birthday: str
        id: str
        date_joined: str
        date_canceled: str

        class Config:
            # orm_mode = True
            from_attributes = True

    @staticmethod
    def get_members(db: Session):
        return db.query(MemberUtil.Member).all()

    @staticmethod
    def get_member(db: Session, id: int):
        # return db.query(MemberUtil.Member).filter(MemberUtil.Member.id == id).first() # success , 그러나 타입힌팅 에러가...
        MySqlUtil.execute(f'''SELECT * FROM members where id= {id} ORDER BY date_joined LIMIT 2;''')  # LIMIT 2 로 쿼리 성능 향상 기대, 2인 이유는 id가 2개면
        # 네이티브 쿼리를 한번 더 작성한 이유는 쿼리 디버깅
        return select(MemberUtil.Member).where(MemberUtil.Member.id.in_([id]))  # try

    @staticmethod
    def insert_member(db: Session, member):
        member_ = MemberUtil.Member(**member)
        db.add(member_)
        db.flush()  # flush() 메서드 없이 바로 commit() 메서드를 호출하면, 롤백할 수 있는 포인트가 만들어지지 않습니다. (# 나중에 롤백을 수행할 수 있는 포인트가 만들어짐)
        db.commit()
        db.refresh(member_)  # 데이터베이스에 업데이트된 최신내용을 세션에 가져오는 것.
        return member_

    @staticmethod
    def is_member_joined_by_id(id, request):
        pk_print(f"{inspect.currentframe().f_code.co_name}()")

        result = MySqlUtil.get_session_local().query(MemberUtil.Member).filter(MemberUtil.Member.id == id).limit(2)
        for member in result:
            print(f"member.name: {member.name}, member.id: {member.id}")
        member_count = result.count()
        print(rf'''member_count : {member_count}''')
        if member_count == 1:
            for member_joined in result:
                print(f'member_joined.name: {member_joined.name}  member_joined.id: {member_joined.id}')
                request.session['name'] = member_joined.name
            return True
        else:
            return False

    @staticmethod
    def is_member_joined(id, pw, request):
        pk_print(f"{inspect.currentframe().f_code.co_name}()")

        # native query
        # sql injection 에 취약,
        # 위험해서, 로그인 로직에 그냥은 못 쓴다.
        # rows = MySqlUtil.execute(f'''SELECT count(*) FROM members where id="{id}" and pw="{pw}" ORDER BY date_joined LIMIT 2;''')
        # id_count = rows.fetchone()[0]
        # print(rf'id_count : {id_count}')
        # if id_count == 1:
        #     return True
        # else:
        #     return False

        # orm
        # sql injection 에 강화됨.
        result = MySqlUtil.get_session_local().query(MemberUtil.Member).filter(MemberUtil.Member.id == id, MemberUtil.Member.pw == pw).limit(2)
        for member in result:
            print(f"member.name: {member.name}, member.id: {member.id}, member.pw: {member.pw}")
        member_count = result.count()
        print(rf'''member_count : {member_count}''')
        if member_count == 1:
            return True
        else:
            return False

    @staticmethod
    def get_member_name_joined(id, pw, request):
        pk_print(f"{inspect.currentframe().f_code.co_name}()")
        result = MySqlUtil.get_session_local().query(MemberUtil.Member).filter(MemberUtil.Member.id == id, MemberUtil.Member.pw == pw).limit(2)
        member_count = result.count()
        print(rf'''member_count : {member_count}''')
        if member_count == 1:
            for member in result:
                return member.name

    @staticmethod
    def validate_id(value):
        pk_print(f"{inspect.currentframe().f_code.co_name}()")
        # raise_exception_after_special_charcater_check(value, inspect.currentframe().f_code.co_name)
        return True

    @staticmethod
    def validate_name(value):
        pk_print(f"{inspect.currentframe().f_code.co_name}()")
        #         raise_exception_after_special_charcater_check(value, inspect.currentframe().f_code.co_name)
        return True

    @staticmethod
    def validate_e_mail(value):
        pk_print(f"{inspect.currentframe().f_code.co_name}()")
        raise_exception_after_special_charcater_check(value, inspect.currentframe().f_code.co_name, ignore_list=["@"])
        MemberUtil.validate_address_e_mail(value)
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, value):
            # if not address_e_mail.endswith('@kakao.com'):
            #     raise HTTPException(status_code=400, detail="유효한 카카오 이메일이 아닙니다.")
            # return address_e_mail
            raise HTTPException(status_code=400, detail=f"유효한 이메일 주소가 아닙니다. {value}")
        return value

    @staticmethod
    def validate_phone_no(value):
        import re
        pk_print(f"{inspect.currentframe().f_code.co_name}()")
        # r'^\d{3}-\d{3,4}-\d{4}$'
        # r'^\d{2}-\d{3,4}-\d{4}$' 둘다
        if not re.match(r'^\d{2,3}-\d{3,4}-\d{4}$', value):
            raise HTTPException(status_code=400, detail=f"유효한 전화번호가 아닙니다. {value}")
        return value

    @staticmethod
    def validate_address(value):
        pk_print(f"{inspect.currentframe().f_code.co_name}()")

        return True

    @staticmethod
    def validate_birthday(value):
        pk_print(f"{inspect.currentframe().f_code.co_name}()")

        return True

    @staticmethod
    def validate_pw(value):
        pk_print(f"{inspect.currentframe().f_code.co_name}()")

        return True

    @staticmethod
    def validate_date_joined(value):
        pk_print(f"{inspect.currentframe().f_code.co_name}()")

        return True

    @staticmethod
    def validate_date_canceled(value):
        pk_print(f"{inspect.currentframe().f_code.co_name}()")

        return True

    @staticmethod
    def validate_date_join(value):
        pk_print(f"{inspect.currentframe().f_code.co_name}()")

        return True

    @staticmethod
    def validate_address_e_mail(value):
        pk_print(f"{inspect.currentframe().f_code.co_name}()")
        return True

def set_database():
    try:
        from dotenv import load_dotenv

        pk_print(rf'''LOCAL_TEST_ACTIVATE="{LOCAL_TEST_ACTIVATE}" %%%FOO%%%''')
        pk_print(rf'''os.path.basename(__file__)="{os.path.basename(__file__)}" %%%FOO%%%''')

        if LOCAL_TEST_ACTIVATE:
            MySqlUtil.Base.metadata.drop_all(bind=MySqlUtil.engine)
            pk_print(rf'''데이터베이스 드롭''')

            MySqlUtil.Base.metadata.create_all(bind=MySqlUtil.engine)  # 데이터베이스에, Base 클래스에 정의된 모든 테이블을 생성, class Item(Base): 다음에 호출되어야 동작한다
            pk_print(rf'''데이터베이스 테이블 생성''')

        if LOCAL_TEST_ACTIVATE:
            member_data = {
                'id': "`",
                'pw': "`",
                'name': "아이유",
                'phone_no': "",
                'address': "",
                'e_mail': "",
                'birthday': "",
                'date_joined': get_time_as_('%Y_%m_%d_%H_%M_%S'),
                'date_canceled': ''
            }
            MemberUtil.insert_member(member=member_data, db=MySqlUtil.get_session_local())
            pk_print(rf'''데이터베이스 테스트 계정 생성 ''', print_color='green')

            # 관리자 계정
            member_data = {
                'id': "``",
                'pw': "``",
                'name': "관리자",
                'phone_no': "",
                'address': "",
                'e_mail': "",
                'birthday': "",
                'date_joined': get_time_as_('%Y_%m_%d_%H_%M_%S'),
                'date_canceled': ''
            }
            df = MySqlUtil.execute(f'''select * from members where id = '{member_data['id']}' and  pw = '{member_data['pw']}' limit 2; ''')
            if len(df) == 0:
                MemberUtil.insert_member(member=member_data, db=MySqlUtil.get_session_local())
                pk_print(rf'''데이터베이스 {member_data['name']} 생성''', print_color='green')

            # 우리가족 공유계정
            load_dotenv(r'./pkg_env/.env')
            member_data = {
                'id': os.environ.get('FAMILY_SHARING_ACCOUNT_ID'),
                'pw': os.environ.get('FAMILY_SHARING_ACCOUNT_PW'),
                'name': "우리가족 공유계정",
                'phone_no': "",
                'address': "",
                'e_mail': "",
                'birthday': "",
                'date_joined': get_time_as_('%Y_%m_%d_%H_%M_%S'),
                'date_canceled': ''
            }
            df = MySqlUtil.execute(f'''select * from members where id = '{member_data['id']}' and  pw = '{member_data['pw']}' limit 2; ''')
            if len(df) == 0:
                MemberUtil.insert_member(member=member_data, db=MySqlUtil.get_session_local())
                pk_print(rf'''데이터베이스 {member_data['name']} 생성 ''', print_color='green')

    except:
        traceback.print_exc(file=sys.stdout)
        pk_print(rf'''예약된 데이터베이스 작업을 수행할 수 없었습니다.''', print_color='blue')

    # 서버 인사
    if LOCAL_TEST_ACTIVATE:
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker, declarative_base
        import toml
        config = toml.load(F_CONFIG_TOML)
        pk_driver = config["pk_mysql"]["driver"]
        pk_host = config["pk_mysql"]["host"]
        pk_port = config["pk_mysql"]["port"]
        pk_user = config["pk_mysql"]["user"]
        pk_pw = config["pk_mysql"]["pw"]
        pk_database = config["pk_mysql"]["database_n"]
        pk_charset = config["pk_mysql"]["charset"]
        pk_mysql_uri = f"{pk_driver}://{pk_user}:{pk_pw}@{pk_host}:{pk_port}/{pk_database}?charset={pk_charset}"
        pk_print(rf'pk_mysql_uri   : {pk_mysql_uri}', print_color='green')
        pk_print(rf"✧*｡٩(ˊᗜˋ*)و✧*｡", print_color='green')

    # swagger 실행
    # explorer(fr"{UvicornUtil.Config.protocol_type}://{uvicorn_host}:{uvicorn_port}/docs")
    # explorer(fr"{UvicornUtil.Config.protocol_type}://{uvicorn_host}:{uvicorn_port}/redoc")
    # explorer(fr"{UvicornUtil.Config.protocol_type}://{uvicorn_host}:{uvicorn_port}")

    # 더미 데이터 객체 생성
    # explorer(fr"{UvicornUtil.Config.protocol_type}://{uvicorn_host}:{uvicorn_port}/make-dummyies")
    # FastapiUtil.test_client_post_request() # swagger 로 해도 되지만, test 용도

    # 클라이언트 테스트
    # FastapiUtil.test_client_post_request()  # swagger 로 해도 되지만, test 용도로 고민 중

    # 콘솔 타이틀 변경 테스트
    # lines = subprocess.check_output(rf'start cmd /k title NETWORK TEST CONSOLE', shell=True).decode('utf-8').split("\n")

    yield  # lifespan의 동작트리거, 전후로 startup/shutdown 동작

    pk_print(f"애플리케이션 종료를 진행합니다", print_color='green')


for d in [D_PROJECT_FASTAPI, D_STATIC, D_PKG_CLOUD, D_PKG_PNG]:
    ensure_pnx_made(mode='d', pnx=d)
    d = get_pnx_os_style(d)

if __name__ == "__main__":
    # 이 파일이 직접 실행되는 경우만 이 코드 블록은 실행됩니다.
    # 이 파일을 import하여 사용할 때는 해당 코드 블록이 실행되지 않습니다.
    import traceback
    import toml
    import sys
    import re
    import pandas as pd
    import os.path
    import os
    import json
    import inspect
    from sqlalchemy.orm import sessionmaker, declarative_base
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine
    from sqlalchemy import Column, Integer, text as sqlalchecdmy_text, VARCHAR, select
    from pydantic import BaseModel, field_validator
    from pkg_py.pk_colorful_cli_util import pk_print
    from pkg_py.pk_core import get_time_as_, ensure_pnx_made, is_letters_cnt_zero, write_str_to_f
    from pkg_py.pk_core import get_time_as_, ensure_pnx_made, get_pnx_os_style, raise_exception_after_special_charcater_check
    from pkg_py.pk_core_constants import D_STATIC, D_PROJECT_FASTAPI, D_PKG_CLOUD, D_PKG_PNG
    from fastapi import HTTPException

    set_database()