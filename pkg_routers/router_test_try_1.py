import inspect
import random
from datetime import datetime, timedelta
from typing import Optional

import clipboard
from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from starlette.requests import Request
from starlette.staticfiles import StaticFiles

from pkg_pk_server_fastapi_for_linux import DebuggingUtil, SecurityUtil, JwtUtil, MySqlUtil, TestUtil
from typing import Annotated

pw_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="test/jwt")

router = APIRouter()
router.mount("/static", StaticFiles(directory=os.path.join(D_PROJECT_FASTAPI, 'pkg_web', 'static')), name="static")
router.mount("/static", StaticFiles(directory="pkg_web/static"), name="static")

prefix_promised = "web"  # /web 는 다른 파일에 작성된 부분이다. 라우터를 다른 파일로 분리했기 때문에 이 부분은 유지보수하며 알아내기가 까다롭다 # 하드코딩
# default_redirection_page_without_prefix = '/developer/tests/routing'
default_redirection_page_without_prefix = '/test'
default_redirection_page = f'/{prefix_promised}{default_redirection_page_without_prefix}'

# SECRET_KEY 설정
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class data_register(BaseModel):
    name: str
    email: str


class data_auth(BaseModel):
    token: str


class Token(BaseModel):
    access_token: str
    token_type: str


class User(BaseModel):
    # username: str
    full_name: Optional[str] = None
    email: Optional[str] = None
    disabled: Optional[bool] = None


class UserInDB(User):
    pw_hashed: str


def verify_pw(pw_plain, pw_hashed):
    """return boolean"""
    func_n = inspect.currentframe().f_code.co_name
    pk_print(f"{func_n}()")
    return pw_context.verify(pw_plain, pw_hashed)


def get_pw_hashed(pw_plain):
    """사용자를 평문 비밀번호를 jwt 로 만들기 전에 pw_plain을 pw_hashed 로 전처리 할때 사용하는 함수"""
    func_n = inspect.currentframe().f_code.co_name
    pk_print(f"{func_n}()")
    return pw_context.hash(pw_plain)


def get_current_user_as_class(rs, form_data_username: str):
    func_n = inspect.currentframe().f_code.co_name
    pk_print(f"{func_n}()")
    if form_data_username in rs:
        current_user_dict = rs[form_data_username]
        return UserInDB(**current_user_dict)






# @router.post("/register")
# async def route_post_register(data: data_register,form_data: OAuth2PasswordRequestForm = Depends()):
#     func_n = inspect.currentframe().f_code.co_name
#     pk_print(f"{func_n}()")
#
#     # 파라미터 제어
#     pk_print(rf'''data.name : {data.name}''')
#     pk_print(rf'''data.email : {data.email}''')
#     pk_print(rf'''form_data.username : {form_data.username}''')
#     pk_print(rf'''form_data.password : {form_data.password}''')
#     TestUtil.pause()
#
#     # 유저 인증 로직 구현 해서  foo(id, pw, name, email): 이런 식으로 작성하는게 일반적인 것 같아보인다.
#     # 유저 인증 로직
#     # user = authenticate_user(username, password)
#     # if not user:
#     #     raise HTTPException(status_code=401, detail="Invalid username or password")
#     # 벤치마킹 하는 부분에는 없는 것 같아 보여 구현안함.
#
#     user_authorized = authenticate_user(form_data.username=form_data.username, form_data.password=form_data.password)
#     # # DB에 등록되지 않은 경우
#     # if not user_authorized:
#     #     # pk_print("not auth")
#     #     # jwt = ""
#     #     # return jwt
#     #     # else:
#     #     #     # jwt 생성
#     #     #     jwt = SecurityUtil.get_jwt(data=dict(user_authorized), secret_key=SECRET_KEY, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
#     #     #     # DB에 jwt 저장
#     #     #
#     #     credentials_exception = HTTPException(
#     #         status_code=status.HTTP_401_UNAUTHORIZED,
#     #         detail="Could not validate credentials",
#     #         headers={"WWW-Authenticate": "Bearer"},
#     #     )
#     #     raise credentials_exception
#
#     # JWT 생성
#     # 백엔드용 아이디/패스워드/secret_key 를 데이터를 기반으로 jwt을 만들어 발급
#     jwt_encoded = SecurityUtil.get_jwt(data=dict(user_authorized), secret_key=SECRET_KEY, expires_delta=timedelta(minutes=60))
#
#
#     # DB에 JWT 유무 확인 (중복확인)
#     rs = JwtUtil.get_jwts_by_token(db=MySqlUtil.get_session_local(), token=jwt_encoded)
#     if len(rs) != 0:
#         # return {"detail": f"{func_n}() 에서 의도하지 않은 중복 검출 판정이 이루어졌습니다. 다시 시도해 주세요"}
#         return {"detail": f"{func_n}() 에서 에러가 발생했습니다. 다시 시도해 주세요"}
#
#     # DB에 저장 (jwt)
#     jwt_data = {
#         'token': jwt_encoded,
#     }
#     JwtUtil.insert_jwt_encoded(db=MySqlUtil.get_session_local(), jwt_data=jwt_data)
#
#     # 개발 편의용 코드
#     clipboard.copy(jwt_encoded)
#
#     return {"access_token": jwt_encoded, "token_type": "bearer"}



