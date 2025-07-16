from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from fastapi import UploadFile
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from passlib.context import CryptContext

from pkg_py.pk_core_constants import D_PROJECT_FASTAPI, D_STATIC, D_PKG_CLOUD, D_PKG_PNG
from pkg_py.pk_core import ensure_pnx_made, get_pnx_os_style
from project_fastapi.project_fastapi_utils import JwtUtil

for d in [D_PROJECT_FASTAPI, D_STATIC, D_PKG_CLOUD, D_PKG_PNG]:
    ensure_pnx_made(mode='d', pnx=d)
    d = get_pnx_os_style(d)

templates = Jinja2Templates(directory=r"pkg_web/templates")

router = APIRouter()
router.mount("/static", StaticFiles(directory=D_STATIC), name="static")  # html 에서 /static 오로 찾게되는 것 같음.

web = "web"  # /web 는 다른 파일에 작성된 부분이다. 라우터를 다른 파일로 분리했기 때문에 이 부분은 유지보수하며 알아내기가 까다롭다 # 하드코딩
# default_redirection_page_without_prefix = '/developer/tests/routing'
register = '/register'
url_seg = f'/{web}{register}'

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="coding-test/jwt")
pw_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "IInrs6KU3n9pSsk5-5aUdKIjxsCQ51JdC3tzuihoKJw"  # python -c import secrets; print(secrets.token_urlsafe(32))' 해서 OS 환경변수에 저장
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def verify_pw(pw_plain, pw_hashed):
    import inspect

    from pkg_py.pk_colorful_cli_util import pk_print
    """return boolean"""
    func_n = inspect.currentframe().f_code.co_name
    pk_print(f"{func_n}()")
    return pw_context.verify(pw_plain, pw_hashed)


def get_pw_hashed(pw_plain):
    import inspect

    from pkg_py.pk_colorful_cli_util import pk_print
    """사용자를 평문 비밀번호를 jwt 로 만들기 전에 pw_plain을 pw_hashed 로 전처리 할때 사용하는 함수"""
    func_n = inspect.currentframe().f_code.co_name
    pk_print(f"{func_n}()")
    return pw_context.hash(pw_plain)


def get_current_user_as_class(rs, form_data_username: str):
    import inspect

    from pkg_py.pk_colorful_cli_util import pk_print
    func_n = inspect.currentframe().f_code.co_name
    pk_print(f"{func_n}()")
    if form_data_username in rs:
        current_user_dict = rs[form_data_username]
        return UserInDB(**current_user_dict)


def authenticate_user(form_data_username: str, form_data_password: str):
    import inspect

    from pkg_py.pk_colorful_cli_util import pk_print
    from project_fastapi.test_project_fastapi import MySqlUtil
    func_n = inspect.currentframe().f_code.co_name
    pk_print(f"{func_n}()")

    # # jwt 생성
    # jwt = get_jwt(data=dict(user_as_dict[form_data_username]), secret_key=SECRET_KEY, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    # # jwt = get_jwt(data=form_data_username, secret_key=SECRET_KEY, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))

    # # DB에 JWT 유무 판단
    # rs = JwtUtil.get_jwts_by_token(db=MySqlUtil.get_session_local(), token=jwt)
    # [print(sample) for sample in rs]
    # print(rf'rs : {rs}')
    # print(rf'type(rs) : {type(rs)}')
    # print(rf'len(rs) : {len(rs)}')
    # if len(rs) != 1:
    #     return {"detail": f"{func_n}() 에서 유효하지 않은 토큰으로 판정되었습니다"}

    rs = JwtUtil.get_jwts(db=MySqlUtil.get_session_local())
    user = get_current_user_as_class(rs, form_data_username)
    pk_print(rf'user : {user}')
    pk_print(rf'type(user) : {type(user)}')

    if not user:
        pk_print(rf'''인증실패(DB 에 없는 경우)''')
        return False  # DB 에 없는 경우
    if not verify_pw(pw_plain=form_data_password, pw_hashed=user.pw_hashed):
        pk_print(rf'''인증실패(pw 가 다른 경우)''')
        return False  # pw 가 다른 경우
    pk_print(rf'''인증성공''')
    return user  # DB 에 있고 pw 가 같은 경우


@router.post("/jwt")
async def post_jwt(form_data: OAuth2PasswordRequestForm = Depends()):
    import inspect
    import sys
    import traceback

    from fastapi import HTTPException
    from starlette import status
    from pkg_py.pk_colorful_cli_util import pk_print
    from project_fastapi.test_project_fastapi import MySqlUtil
    func_n = inspect.currentframe().f_code.co_name
    pk_print(f"{func_n}()")
    try:
        # 파라미터 제어
        pk_print(rf'''form_data.username : {form_data.username}''')
        pk_print(rf'''form_data.password : {form_data.password}''')

        # api 사용자 입력 바인딩
        _jwt = form_data.username

        # _jwt 유효성 디버깅
        pk_print(rf'''_jwt : {_jwt}''')
        decode_jwt_token(_jwt)

        # 유저 인증 로직
        # jwt 인증
        duplication_chk = []
        rs = JwtUtil.get_jwts(db=MySqlUtil.get_session_local())
        pk_print(rf'rs : {rs}')
        pk_print(rf'len(rs) : {len(rs)}')

        for row in rs:
            if _jwt == row.token:
                duplication_chk.append(_jwt)

        pk_print(rf'duplication_chk : {duplication_chk}')
        pk_print(rf'type(duplication_chk) : {type(duplication_chk)}')
        pk_print(rf'len(duplication_chk) : {len(duplication_chk)}')

        if len(duplication_chk) != 1:
            credentials_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                # detail="Could not validate credentials",
                detail=f"{func_n}() 에서 의도하지 않은 중복 검출 판정이 이루어졌습니다. 다시 시도해 주세요",
                headers={"WWW-Authenticate": "Bearer"},
            )
            pk_print(rf'''인증실패(DB 에 없는 경우)''')
            raise credentials_exception

        # return jwt # success
        return {"access_token": _jwt, "token_type": "bearer"}  # success
    except:
        traceback.print_exc(file=sys.stdout)
        return {"detail": f"에러가 발생했습니다"}



@router.get("/input-param")
async def get_input_param(jwt_: Annotated[str, Depends(oauth2_scheme)]):
    import inspect
    import sys
    import traceback

    from pkg_py.pk_colorful_cli_util import pk_print
    func_n = inspect.currentframe().f_code.co_name
    pk_print(f"{func_n}()")
    try:
        # _jwt 유효성 디버깅
        pk_print(rf'''jwt_ : {jwt_}''')
        # decode_jwt_token(jwt_)

        # 랜덤연산식 영문
        param = get_random_math_expression_english_input_for_code_test()
        return {"param": param}
    except:
        traceback.print_exc(file=sys.stdout)
        return {"detail": f"에러가 발생했습니다"}


@router.get("/solution")
async def get_solution(jwt_: Annotated[str, Depends(oauth2_scheme)]):
    import inspect
    import sys
    import traceback

    from pkg_py.pk_colorful_cli_util import pk_print

    # async def get_solution():
    func_n = inspect.currentframe().f_code.co_name
    pk_print(f"{func_n}()")
    try:
        # _jwt 유효성 디버깅
        pk_print(rf'''jwt_ : {jwt_}''')
        # decode_jwt_token(jwt_)

        # get_input_param() requests 모듈로 post request.
        # url = "http://127.0.0.1:8080/coding-test/input-param"  # 동일한 엔드포인트로 요청을 보내는 경우
        # headers = {
        #     "accept": "application/json",
        #     "Content-Type": "application/json",
        #     'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InN0cmluZyIsInB3X2hhc2hlZCI6IiQyYiQxMiQ0NGltUU1zVzFwUk9Ma2x6WVIybmYuakVOVlZFSHFVSEZZb2JYckREa1psODQuRlRqM1ZSRyIsImV4cCI6MTcwODQ3OTkxNX0.5QBV3PGmitjVa5Fp4Zxd7fVf3GqHKCwLcNRnLIToosY'
        # }
        # response = requests.get(url, headers=headers)
        # test_token = response.json()
        # [pk_print(sample) for sample in test_token ]
        # pk_print(rf'test_token : {test_token}')
        # pk_print(rf'type(test_token) : {type(test_token)}')
        # pk_print(rf'len(test_token) : {len(test_token)}')

        # 랜덤연산식 영문
        test_token = get_random_math_expression_english_input_for_code_test()
        test_token = convert_math_expression_english_to_math_expression_math(test_token)
        solution = await get_operation_result_of_parser_for_code_test(test_token)
        pk_print(rf'''solution : {solution}''')
        return {"solution": solution}
    except:
        traceback.print_exc(file=sys.stdout)
        return {"detail": f"에러가 발생했습니다"}


@router.post("/submit")
async def post_submit(file: UploadFile, jwt_: Annotated[str, Depends(oauth2_scheme)]):
    import inspect
    import os.path
    import sys
    import traceback

    from pkg_py.pk_core_constants import D_CODING_TEST_RESULT
    from pkg_py.pk_core import ensure_pnx_made
    from pkg_py.pk_colorful_cli_util import pk_print
    # async def post_submit(jwt_: Annotated[str, Depends(oauth2_scheme)], file: UploadFile = File(...)):
    # async def post_submit(file: binary, jwt_: Annotated[str, Depends(oauth2_scheme)]):
    func_n = inspect.currentframe().f_code.co_name
    pk_print(f"{func_n}()")
    try:
        # _jwt 유효성 디버깅
        pk_print(rf'''jwt_ : {jwt_}''')
        # decode_jwt_token(jwt_)

        # 파일 저장
        directory_coding_test_result = D_CODING_TEST_RESULT
        files_bytes = 0
        files_name = []

        content = await file.read()
        pk_print(rf'''file.filename : {file.filename}''')
        if file.filename.strip() == "":
            return {"result_msg": "선택된 파일이 없습니다."}

        file_path = rf'{directory_coding_test_result}/{file.filename}'

        ensure_pnx_made(mode='f', f=file_path)
        with open(file_path, "wb") as fp:
            fp.write(content)
        files_bytes += os.path.getsize(file_path)
        files_name.append(file.filename)

        return {
            "result_msg": "파일이 성공적으로 제출되었습니다.",
            "files_name": files_name,
            "files_bytes": files_bytes
        }
    except:
        traceback.print_exc(file=sys.stdout)
        return {"detail": f"에러가 발생했습니다"}
