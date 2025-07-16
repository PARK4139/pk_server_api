

import os
from enum import Enum
from typing import TypeVar, Optional, Literal, List

import asyncio
import inspect
import json
import os.path
import random
import re
import secrets
import shutil
import string
import subprocess
import threading
import time
import traceback
import urllib.parse
from collections import Counter
from datetime import datetime, timedelta
from functools import partial
from pathlib import Path
from uuid import uuid4

import keyboard
import numpy as np
import pandas as pd
import pygetwindow
from colorama import Fore
from pydantic import BaseModel, field_validator
from sqlalchemy import Column, Integer, String, VARCHAR, select, DateTime
from sqlalchemy.orm import Session

from pkg_friday import MySqlUtil


# from click import command # todo 확인필요한데 command 같은 일반적인 단어는 못쓰네..
# from venv import create
# from app.routes import index, auth


# logger = logging.getLogger('pk_server_fastapi_test_logger')
# hdlr = logging.FileHandler('pk_server_fastapi_logger.log')
# hdlr.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
# logger.addHandler(hdlr)
# logger.setLevel(logging.INFO)

class MemberUtil:
    from pydantic import BaseModel
    """
    mysql / sqlalchemy / fastapi 의존하는 유틸리티 객체
    """

    class Member(MySqlUtil.Base):  # orm 설정에는 id 있음
        from sqlalchemy import Column, Integer, VARCHAR
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
            from fastapi import HTTPException
            MemberUtil.validate_date_join(value)
            # datetime.strptime(date_join, '%Y-%m-%d %H:%M %S%f')
            if len(value) != 18:
                raise HTTPException(status_code=400, detail="유효한 날짜가 아닙니다.")
            return value

        @staticmethod
        @field_validator('pw')
        def validate_pw(value):
            from fastapi import HTTPException
            MemberUtil.validate_pw(value)
            if len(value) != MemberUtil.Member.__table__.c.vpc_pw.type.length:
                raise HTTPException(status_code=400, detail="유효한 이메일 주소가 아닙니다.")
            return value

    @staticmethod
    def get_member_validated(member):
        func_n = inspect.currentframe().f_code.co_name
        pk_print(str_working=rf'''{UNDERLINE}{func_name}() %%%FOO%%%''')

        # Member 클래스의 필드 개수 확인
        field_count = len(MemberUtil.Member.__table__.c)
        print(rf'''field_count : {field_count}''')

        pnxs_validated = [
            {"field_en": 'id', "field_ko": "아이디", "field_validation_func": MemberUtil.validate_id, "field_length_limit": MemberUtil.Member.__table__.c.id.type.length},
            {"field_en": 'name', "field_ko": "이름", "field_validation_func": MemberUtil.validate_name, "field_length_limit": MemberUtil.Member.__table__.c.name.type.length},
            {"field_en": 'e_mail', "field_ko": "이메일", "field_validation_func": MemberUtil.validate_e_mail, "field_length_limit": MemberUtil.Member.__table__.c.e_mail.type.length},
            {"field_en": 'phone_no', "field_ko": "전화번호", "field_validation_func": MemberUtil.validate_phone_no, "field_length_limit": MemberUtil.Member.__table__.c.phone_no.type.length},
            {"field_en": 'address', "field_ko": "주소", "field_validation_func": MemberUtil.validate_address, "field_length_limit": MemberUtil.Member.__table__.c.address.type.length},
            {"field_en": 'birthday', "field_ko": "생년월일", "field_validation_func": MemberUtil.validate_birthday, "field_length_limit": MemberUtil.Member.__table__.c.birthday.type.length},
            {"field_en": 'pw', "field_ko": "비밀번호", "field_validation_func": MemberUtil.validate_pw, "field_length_limit": MemberUtil.Member.__table__.c.vpc_pw.type.length},
            {"field_en": 'date_joined', "field_ko": "가입일", "field_validation_func": MemberUtil.validate_date_joined, "field_length_limit": MemberUtil.Member.__table__.c.date_joined.type.length},
            {"field_en": 'date_canceled', "field_ko": "탈퇴일", "field_validation_func": MemberUtil.validate_date_canceled, "field_length_limit": MemberUtil.Member.__table__.c.date_canceled.type.length},
        ]
        for target in pnxs_validated:
            field_en = target["field_en"]
            field_ko = target["field_ko"]
            field_validation_func = target["field_validation_func"]
            field_length_limit = target["field_length_limit"]
            if len(member[field_en]) > target['field_length_limit']:
                from fastapi import HTTPException
                raise HTTPException(status_code=400, detail=f"{field_ko}({field_en})의 길이제한은 {field_length_limit}자 이하여야 합니다.")
            else:
                field_validation_func(member[field_en])  # success, 호출할 수 없는 함수의 내부에 구현된 부분이 필요한것 이므로 내부에 구현된 것을 다른 클래스에 구현해서 참조하도록 로직 분리,
        return member

    @staticmethod
    def validate_member(member):
        func_n = inspect.currentframe().f_code.co_name
        pk_print(str_working=rf'''{UNDERLINE}{func_name}() %%%FOO%%%''')
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

    from sqlalchemy.orm import Session

    @staticmethod
    def get_members(db: Session):
        return db.query(MemberUtil.Member).all()

    @staticmethod
    def get_member(db: Session, id: int):
        from sqlalchemy import select
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
    def update_member(db: Session, member, updated_member):
        for key, value in updated_member.model_dump().members():
            setattr(member, key, value)
        db.commit()
        db.refresh(member)
        return member

    @staticmethod
    def delete_member(db: Session, member):
        db.delete(member)
        db.commit()

    @staticmethod
    def is_member_joined_by_id(id, request):
        func_n = inspect.currentframe().f_code.co_name
        pk_print(str_working=rf'''{UNDERLINE}{func_name}() %%%FOO%%%''')

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
        func_n = inspect.currentframe().f_code.co_name
        pk_print(str_working=rf'''{UNDERLINE}{func_name}() %%%FOO%%%''')

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
            print(f"member.name: {member.name}, member.id: {member.id}, member.pw: {member.vpc_pw}")
        member_count = result.count()
        print(rf'''member_count : {member_count}''')
        if member_count == 1:
            return True
        else:
            return False

    @staticmethod
    def get_member_name_joined(id, pw, request):
        func_n = inspect.currentframe().f_code.co_name
        pk_print(str_working=rf'''{UNDERLINE}{func_name}() %%%FOO%%%''')
        result = MySqlUtil.get_session_local().query(MemberUtil.Member).filter(MemberUtil.Member.id == id, MemberUtil.Member.pw == pw).limit(2)
        member_count = result.count()
        print(rf'''member_count : {member_count}''')
        if member_count == 1:
            for member in result:
                return member.name

    @staticmethod
    def validate_id(value):
        func_n = inspect.currentframe().f_code.co_name
        pk_print(str_working=rf'''{UNDERLINE}{func_name}() %%%FOO%%%''')
        Friday.raise_exception_after_special_charcater_check(value, inspect.currentframe().f_code.co_name)
        return True

    @staticmethod
    def validate_name(value):
        func_n = inspect.currentframe().f_code.co_name
        pk_print(str_working=rf'''{UNDERLINE}{func_name}() %%%FOO%%%''')
        Friday.raise_exception_after_special_charcater_check(value, inspect.currentframe().f_code.co_name)
        return True

    @staticmethod
    def validate_e_mail(value):
        func_n = inspect.currentframe().f_code.co_name
        pk_print(str_working=rf'''{UNDERLINE}{func_name}() %%%FOO%%%''')
        Friday.raise_exception_after_special_charcater_check(value, inspect.currentframe().f_code.co_name, ignore_list=["@"])
        MemberUtil.validate_address_e_mail(value)
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, value):
            # if not address_e_mail.endswith('@kakao.com'):
            #     raise HTTPException(status_code=400, detail="유효한 카카오 이메일이 아닙니다.")
            # return address_e_mail
            from fastapi import HTTPException
            raise HTTPException(status_code=400, detail=f"유효한 이메일 주소가 아닙니다. {value}")
        return value

    @staticmethod
    def validate_phone_no(value):
        func_n = inspect.currentframe().f_code.co_name
        pk_print(str_working=rf'''{UNDERLINE}{func_name}() %%%FOO%%%''')
        # r'^\d{3}-\d{3,4}-\d{4}$'
        # r'^\d{2}-\d{3,4}-\d{4}$' 둘다
        if not re.match(r'^\d{2,3}-\d{3,4}-\d{4}$', value):
            from fastapi import HTTPException
            raise HTTPException(status_code=400, detail=f"유효한 전화번호가 아닙니다. {value}")
        return value

    @staticmethod
    def validate_address(value):
        func_n = inspect.currentframe().f_code.co_name
        pk_print(str_working=rf'''{UNDERLINE}{func_name}() %%%FOO%%%''')

        return True

    @staticmethod
    def validate_birthday(value):
        func_n = inspect.currentframe().f_code.co_name
        pk_print(str_working=rf'''{UNDERLINE}{func_name}() %%%FOO%%%''')

        return True

    @staticmethod
    def validate_pw(value):
        func_n = inspect.currentframe().f_code.co_name
        pk_print(str_working=rf'''{UNDERLINE}{func_name}() %%%FOO%%%''')

        return True

    @staticmethod
    def validate_date_joined(value):
        func_n = inspect.currentframe().f_code.co_name
        pk_print(str_working=rf'''{UNDERLINE}{func_name}() %%%FOO%%%''')

        return True

    @staticmethod
    def validate_date_canceled(value):
        func_n = inspect.currentframe().f_code.co_name
        pk_print(str_working=rf'''{UNDERLINE}{func_name}() %%%FOO%%%''')

        return True

    @staticmethod
    def validate_date_join(value):
        func_n = inspect.currentframe().f_code.co_name
        pk_print(str_working=rf'''{UNDERLINE}{func_name}() %%%FOO%%%''')

        return True

    @staticmethod
    def validate_address_e_mail(value):
        func_n = inspect.currentframe().f_code.co_name
        pk_print(str_working=rf'''{UNDERLINE}{func_name}() %%%FOO%%%''')

        return True


class ItemsUtil:
    class Item(MySqlUtil.Base):  # orm 설정에는 id 있음
        __tablename__ = "items"
        # __table_args__ = {'extend_existing': True}  # 이옵션을 쓰면 여기에 작성된 item 대로 테이블이 다르면 새로확장이되는 거란다.
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String(30))
        # price = Column(Integer)

    class ItemBase(BaseModel):  # pydantic validator 설정에는 id 없음
        name: str

    class ItemCreate(ItemBase):
        pass

    class ItemExtendedItemBase(ItemBase):
        id: int

        class Config:
            # orm_mode = True
            from_attributes = True

    @staticmethod
    def get_items(db: Session):
        return db.query(ItemsUtil.Item).all()

    @staticmethod
    def get_item(db: Session, id: int):
        # return db.query(ItemsUtil.Item).filter(column("id") == id).first()
        # return db.query(ItemsUtil.Item).filter(ItemsUtil.Item.id == id).first() , success , 그러나 타입힌팅 에러가...
        # return select(ItemsUtil.Item).where(ItemsUtil.Item.id.in_(["id1","id2"]))
        return select(ItemsUtil.Item).where(ItemsUtil.Item.id.in_([id]))

    @staticmethod
    def create_item(db: Session, item):
        db_item = ItemsUtil.Item(**item.model_dump())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    @staticmethod
    def update_item(db: Session, item, updated_item):
        for key, value in updated_item.model_dump().items():
            setattr(item, key, value)
        db.commit()
        db.refresh(item)
        return item

    @staticmethod
    def delete_item(db: Session, item):
        db.delete(item)
        db.commit()


class FaqBoardUtil:
    """
    mysql / sqlalchemy / fastapi 의존하는 유틸리티 객체
    """

    class FaqBoard(MySqlUtil.Base):  # orm 설정에는 id 있음
        __tablename__ = "faq_boards"
        __table_args__ = {'extend_existing': True}
        # __table_args__ = {'extend_existing': True, 'mysql_collate': 'utf8_general_ci'} # encoding 안되면 비슷하게 방법을 알아보자  mysql 에 적용이 가능한 코드로 보인다.
        FaqBoard_id: str = uuid4().hex + get_time_as_('%Y%m%d%H%M%S%f') + get_random_alphabet()  # table 내 unique id
        id = Column(Integer, primary_key=True, autoincrement=True)  # index 로 이용
        writer = Column(VARCHAR(length=30))
        title = Column(VARCHAR(length=30))
        contents = Column(VARCHAR(length=13))
        date_reg = Column(DateTime, nullable=False, default=datetime.now)
        del_yn = Column(VARCHAR(length=50))

    class FaqBoardBase(BaseModel):  # pydantic validator 설정에는 FaqBoard_id 없음
        id: str
        writer: str
        title: str
        contents: Optional[str]
        date_reg: str
        del_yn: str

        @staticmethod
        @field_validator('id')
        def validate_id(value):
            FaqBoardUtil.validate_id(value)

        @staticmethod
        @field_validator('writer')
        def validate_writer(value):
            FaqBoardUtil.validate_writer(value)

        @staticmethod
        @field_validator('title')
        def validate_title(value):
            FaqBoardUtil.validate_title(value)

        @staticmethod
        @field_validator('contents')
        def validate_contents(value):
            FaqBoardUtil.validate_contents(value)

        @staticmethod
        @field_validator('date_reg')
        def validate_date_reg(value):
            # datetime.strptime(date_join, '%Y-%m-%d %H:%M %S%f')
            if len(value) != 18:
                from fastapi import HTTPException
                raise HTTPException(status_code=400, detail="유효한 날짜가 아닙니다.")
            FaqBoardUtil.validate_date_reg(value)

        @staticmethod
        @field_validator('del_yn')
        def validate_del_yn(value):
            FaqBoardUtil.validate_del_yn(value)

    @staticmethod
    def get_faq_board_validated(faq_board):
        func_n = inspect.currentframe().f_code.co_name
        pk_print(str_working=rf'''{UNDERLINE}{func_name}() %%%FOO%%%''')

        # FaqBoard 클래스의 필드 개수 확인
        field_count = len(FaqBoardUtil.FaqBoard.__table__.c)
        print(rf'''field_count : {field_count}''')

        pnxs_validated = [
            {"field_en": 'id', "field_ko": "아이디", "field_validation_func": FaqBoardUtil.validate_id, "field_length_limit": FaqBoardUtil.FaqBoard.__table__.c.id.type.length},
            {"field_en": 'writer', "field_ko": "이름", "field_validation_func": FaqBoardUtil.validate_writer, "field_length_limit": FaqBoardUtil.FaqBoard.__table__.c.writer.type.length},
            {"field_en": 'title', "field_ko": "이메일", "field_validation_func": FaqBoardUtil.validate_title, "field_length_limit": FaqBoardUtil.FaqBoard.__table__.c.title.type.length},
            {"field_en": 'contents', "field_ko": "전화번호", "field_validation_func": FaqBoardUtil.validate_contents, "field_length_limit": FaqBoardUtil.FaqBoard.__table__.c.contents.type.length},
            {"field_en": 'date_reg', "field_ko": "주소", "field_validation_func": FaqBoardUtil.validate_date_reg, "field_length_limit": FaqBoardUtil.FaqBoard.__table__.c.date_reg.type.length},
            {"field_en": 'del_yn', "field_ko": "가입일", "field_validation_func": FaqBoardUtil.validate_del_yn, "field_length_limit": FaqBoardUtil.FaqBoard.__table__.c.del_yn.type.length},
        ]
        for target in pnxs_validated:
            field_en = target["field_en"]
            field_ko = target["field_ko"]
            field_validation_func = target["field_validation_func"]
            field_length_limit = target["field_length_limit"]
            if len(faq_board[field_en]) > target['field_length_limit']:
                from fastapi import HTTPException
                raise HTTPException(status_code=400, detail=f"{field_ko}({field_en})의 길이제한은 {field_length_limit}자 이하여야 합니다.")
            else:
                field_validation_func(faq_board[field_en])  # success, 호출할 수 없는 함수의 내부에 구현된 부분이 필요한것 이므로 내부에 구현된 것을 다른 클래스에 구현해서 참조하도록 로직 분리,
        return faq_board

    @staticmethod
    def validate_faq_board(faq_board):
        func_n = inspect.currentframe().f_code.co_name
        pk_print(str_working=rf'''{UNDERLINE}{func_name}() %%%FOO%%%''')
        FaqBoardUtil.get_faq_board_validated(faq_board)

    class FaqBoardCreate(FaqBoardBase):
        pass

    class FaqBoardExtendedFaqBoardBase(FaqBoardBase):
        id: str
        writer: str
        title: str
        contents: str
        date_reg: str
        del_yn: str

        class Config:
            from_attributes = True

    @staticmethod
    def get_faq_boards(db: Session):
        return db.query(FaqBoardUtil.FaqBoard).all()

    @staticmethod
    def get_faq_board(db: Session, id: int):
        # return db.query(FaqBoardUtil.FaqBoard).filter(FaqBoardUtil.FaqBoard.id == id).first() # success , 그러나 타입힌팅 에러가...
        MySqlUtil.execute(f'''SELECT * FROM faq_boards where id= {id} ORDER BY del_yn LIMIT 2;''')  # LIMIT 2 로 쿼리 성능 향상 기대, 2인 이유는 id가 2개면
        # 네이티브 쿼리를 한번 더 작성한 이유는 쿼리 디버깅
        return select(FaqBoardUtil.FaqBoard).where(FaqBoardUtil.FaqBoard.id.in_([id]))  # try

    @staticmethod
    def insert_faq_board(db: Session, faq_board):
        faq_board_ = FaqBoardUtil.FaqBoard(**faq_board)
        db.add(faq_board_)
        db.flush()  # flush() 메서드 없이 바로 commit() 메서드를 호출하면, 롤백할 수 있는 포인트가 만들어지지 않습니다. (# 나중에 롤백을 수행할 수 있는 포인트가 만들어짐)
        db.commit()
        db.refresh(faq_board_)  # 데이터베이스에 업데이트된 최신내용을 세션에 가져오는 것.
        return faq_board_

    @staticmethod
    def update_faq_board(db: Session, faq_board, updated_faq_board):
        for key, value in updated_faq_board.model_dump().faq_boards():
            setattr(faq_board, key, value)
        db.commit()
        db.refresh(faq_board)
        return faq_board

    @staticmethod
    def delete_faq_board(db: Session, faq_board):
        db.delete(faq_board)
        db.commit()

    @staticmethod
    def is_faq_board_joined_by_id(id, request):
        func_n = inspect.currentframe().f_code.co_name
        pk_print(str_working=rf'''{UNDERLINE}{func_name}() %%%FOO%%%''')

        result = MySqlUtil.get_session_local().query(FaqBoardUtil.FaqBoard).filter(FaqBoardUtil.FaqBoard.id == id).limit(2)
        for faq_board in result:
            print(f"faq_board.name: {faq_board.name}, faq_board.id: {faq_board.id}")
        faq_board_count = result.count()
        print(rf'''faq_board_count : {faq_board_count}''')
        if faq_board_count == 1:
            for faq_board_joined in result:
                print(f'faq_board_joined.name: {faq_board_joined.name}  faq_board_joined.id: {faq_board_joined.id}')
                request.session['name'] = faq_board_joined.name
            return True
        else:
            return False

    @staticmethod
    def validate_id(value):
        func_n = inspect.currentframe().f_code.co_name
        pk_print(str_working=rf'''{UNDERLINE}{func_name}() %%%FOO%%%''')
        Friday.raise_exception_after_special_charcater_check(value, inspect.currentframe().f_code.co_name)
        return True

    @staticmethod
    def validate_writer(value):
        func_n = inspect.currentframe().f_code.co_name
        pk_print(str_working=rf'''{UNDERLINE}{func_name}() %%%FOO%%%''')
        Friday.raise_exception_after_special_charcater_check(value, inspect.currentframe().f_code.co_name)
        return True

    @staticmethod
    def validate_title(value):
        func_n = inspect.currentframe().f_code.co_name
        pk_print(str_working=rf'''{UNDERLINE}{func_name}() %%%FOO%%%''')
        Friday.raise_exception_after_special_charcater_check(value, inspect.currentframe().f_code.co_name, ignore_list=["@"])
        FaqBoardUtil.validate_title(value)
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, value):
            # if not date_reg_title.endswith('@kakao.com'):
            #     raise HTTPException(status_code=400, detail="유효한 카카오 이메일이 아닙니다.")
            # return date_reg_title
            from fastapi import HTTPException
            raise HTTPException(status_code=400, detail=f"유효한 이메일 주소가 아닙니다. {value}")
        return value

    @staticmethod
    def validate_contents(value):
        func_n = inspect.currentframe().f_code.co_name
        pk_print(str_working=rf'''{UNDERLINE}{func_name}() %%%FOO%%%''')
        # r'^\d{3}-\d{3,4}-\d{4}$'
        # r'^\d{2}-\d{3,4}-\d{4}$' 둘다
        if not re.match(r'^\d{2,3}-\d{3,4}-\d{4}$', value):
            from fastapi import HTTPException
            raise HTTPException(status_code=400, detail=f"유효한 전화번호가 아닙니다. {value}")
        return value

    @staticmethod
    def validate_date_reg(value):
        func_n = inspect.currentframe().f_code.co_name
        pk_print(str_working=rf'''{UNDERLINE}{func_name}() %%%FOO%%%''')
        return True

    @staticmethod
    def validate_del_yn(value):
        func_n = inspect.currentframe().f_code.co_name
        pk_print(str_working=rf'''{UNDERLINE}{func_name}() %%%FOO%%%''')
        return True