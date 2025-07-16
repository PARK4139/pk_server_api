from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from starlette.middleware.exceptions import ExceptionMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.templating import Jinja2Templates

from pkg_py.pk_core_constants import D_STATIC, D_PROJECT_FASTAPI, D_PKG_CLOUD, D_PKG_PNG
from pkg_py.pk_core import get_random_bytes, ensure_pnx_made, get_pnx_os_style, LTA
from project_fastapi.pkg_routers import router_nav_items

templates = Jinja2Templates(directory=r"pkg_web/templates")

def init_cors_policy(app):
    from fastapi.middleware.cors import CORSMiddleware

    # op 에서는 nginx 에서 CORS 설정을 할 것 이므로
    # CORS 두개 설정하면 multi header 로 인한 Control-Allow-Origin' header contains multiple values '*, https://www.pjh4139.store', but only one is allowed. 에러가 발생할 것이다.
    app.add_middleware(
        # success, fastapi CORS allow_origins 동적 할당은 대안 못찾았고, # 초기 origins 값을 와일드카드로 설정
        CORSMiddleware,  # 노란줄 원인 뭘까? #_noqa 를 적용해야 할지 고민 중
        allow_credentials=True,  # cookie 포함 여부를 설정. 기본은 False
        allow_origins=['*'],
        allow_methods=["*"],  # 허용할 method를 설정할 수 있으며, 기본값은 'GET'이다. OPTIONS request ?
        allow_headers=["*"],  # 허용할 http header 목록을 설정할 수 있으며 Content-Type, Accept, Accept-Language, Content-Language은 항상 허용된다.

        # try, 보안강화
        # fastapi CORS allow_origins 정적 할당 # 톳시하나 틀리면 안됨.
        # allow_origins=[,
        #     # "http://localhost",  # fail
        #     # "http://localhost/",  # fail
        #     # "http://localhost:3000",# success
        #     "http://localhost:3000/service-dev-diary",
        #     # "http://127.0.0.1:3000",#
        #     "https://e-magazine-jung-hoon-parks-projects.vercel.app",
        #     # "https://e-magazine-jung-hoon-parks-projects.vercel.app/",
        #     "https://e-magazine-jung-hoon-parks-projects.vercel.app/````````````````````",
        # ],
    )


def init_Logging_via_middleware(app):
    # 미들웨어를 통한 로깅
    # @app.middleware("http")
    # async def log_requests(request: Request, call_next):
    #     logging.debug(f"요청: {request.method} {request.url}")
    #     response = await call_next(request)
    #     logging.debug(f"응답: {response.status_code}")
    #     return response
    pass


def init_domain_address_allowed(app):
    # 접속허용도메인 주소 제한, 이 서버의 api 를 특정 도메인에서만 호출 가능하도록 설정
    # @app.middleware("http")
    # async def domain_middleware(request: Request, call_next):
    #     allowed_domains = ["example.com", "subdomain.example.com"]
    #     client_host = request.client.host
    #     client_domain = client_host.split(":")[0]  # 도메인 추출
    #     if client_domain not in allowed_domains:
    #         raise HTTPException(status_code=403, detail="Forbidden")
    #     response = await call_next(request)
    #     return response
    pass


def init_ip_address_allowed(app):
    # 접속허용IP 주소 제한
    # @app.middleware("http")
    # async def ip_middleware(request: Request, call_next):
    #     allowed_ips = [
    #         "127.0.0.1",
    #         "10.0.0.1",
    #     ]
    #     client_ip = request.client.host
    #     if client_ip not in allowed_ips:
    #         raise HTTPException(status_code=403, detail="Forbidden")
    #     response = await call_next(request)
    #     return response
    pass


async def preprocess_after_request(request):
    if LTA:
        pk_print(f"{str(request.url)} 로 라우팅 시도 중...")
    pass


async def preprocess_before_response_return(request, response):
    if LTA:
        pk_print(f"{str(request.url)} 로 라우팅 되었습니다")
    pass


def init_and_update_f_json(f_json, objects=None):
    import os
    import json
    from pkg_py.pk_core import is_letters_cnt_zero, write_str_to_f

    from pkg_py.pk_core import ensure_pnx_made
    if objects is None:
        objects = []
    try:
        ensure_pnx_made(pnx=f_json, mode='f')
        if os.path.exists(f_json):
            if is_letters_cnt_zero(f=f_json) == True:
                write_str_to_f(txt=f"[]\n", f=f_json, mode="a")

            else:
                if not os.path.isfile(f_json):
                    with open(f_json, "w", encoding='utf-8') as f:
                        # json.dump(objects, f, ensure_ascii=False)  # ensure_ascii=False 는 encoding 을 그대로 유지하는 것 같다. ascii 로 변환하는게 안전할 지도 모르겠다.
                        json.dump(objects, f)  # ensure_ascii=False 는 encoding 을 그대로 유지하는 것 같다. ascii 로 변환하는게 안전할 지도 모르겠다.
                else:
                    with open(f_json, "r", encoding='utf-8') as f:
                        # pk_print(f"{BOOKS_FILE} 업로드 되었습니다")
                        objects = json.load(f)
                    return objects
    except IOError as e:
        print("파일 작업 중 오류가 발생했습니다:", str(e))


# 영한 버전 설정
# en.yaml/ko.yaml

@asynccontextmanager
async def lifespan(app: FastAPI):  # oneshot trigger
    # 앱 시작 후 1번만 실행 # app 객체 생성 뒤
    import traceback
    import sys
    import os
    from pkg_py.pk_colorful_cli_util import pk_print

    try:
        pk_print(rf'''LTA="{LTA}" %%%FOO%%%''')
        pk_print(rf'''os.path.basename(__file__)="{os.path.basename(__file__)}" %%%FOO%%%''')


    except:
        traceback.print_exc(file=sys.stdout)
        pk_print(rf'''예약된 데이터베이스 작업을 수행할 수 없었습니다.''', print_color='blue')

    # 서버 인사
    if LTA:
        pk_print(rf'pk_uvicorn_url : {pk_uvicorn_url}', print_color='green')
        pk_print(rf"✧*｡٩(ˊᗜˋ*)و✧*｡", print_color='green')

    # swagger 실행
    # explorer(fr"{UvicornUtil.Config.protocol_type}://{uvicorn_host}:{uvicorn_port}/docs")
    # explorer(fr"{UvicornUtil.Config.protocol_type}://{uvicorn_host}:{uvicorn_port}/redoc")
    # explorer(fr"{UvicornUtil.Config.protocol_type}://{uvicorn_host}:{uvicorn_port}")

    # 클라이언트 테스트
    # FastapiUtil.test_client_post_request()  # swagger 로 해도 되지만, test 용도로 고민 중

    # 콘솔 타이틀 변경 테스트
    # lines = subprocess.check_output(rf'start cmd /k title NETWORK TEST CONSOLE', shell=True).decode('utf-8').split("\n")

    # 머신러닝 모델 더미 생성
    # def fake_answer_to_everything_ml_model(x: float):
    #     return x * 42
    #
    # # Load the ML model
    # ml_models["answer_to_everything"] = fake_answer_to_everything_ml_model

    yield  # lifespan의 동작트리거, 전후로 startup/shutdown 동작

    pk_print(f"애플리케이션 종료를 진행합니다", print_color='green')

    # 백업도 작성대기

    # # Clean up the ML models and release the resources
    # ml_models.clear()


for d in [D_PROJECT_FASTAPI, D_STATIC, D_PKG_CLOUD, D_PKG_PNG]:
    ensure_pnx_made(mode='d', pnx=d)
    d = get_pnx_os_style(d)

app = FastAPI(lifespan=lifespan, swagger_ui_parameters={"tryItOutEnabled": True})
app.mount("/static", StaticFiles(directory=D_STATIC), name="static")  # html 에서 /static 오로 찾게되는 것 같음.
app.mount("/pkg_cloud", StaticFiles(directory=D_PKG_CLOUD), name="pkg_cloud")
app.mount("/pkg_png", StaticFiles(directory=D_PKG_PNG), name="pkg_png")

# 미들웨어
# UvicornUtil.init_ip_address_allowed(app) # nginx 가 앞단이므로 nginx 에서 설정하는 것이 효율적일듯
# UvicornUtil.init_domain_address_allowed(app) # nginx 가 앞단이므로 nginx 에서 설정하는 것이 효율적일듯
if not LTA:
    init_cors_policy(app)  # nginx 가 앞단이므로 nginx 에서 설정하는 되어 있으므로 dev 에서 테스트 시에만 필요

# fastapi 기본 예외처리 핸들러
# FastAPI는 기본적으로 예외 처리를 으로 처리하고 오류 응답을 생성합니다. 하지만 커스텀 핸들러를 추가하여, 예외를 직접 처리할 수 있음
@app.exception_handler(RequestValidationError)
async def reqeust_validation_exception_handler(request: Request, exc):  # exc : Exception
    from starlette.responses import HTMLResponse, JSONResponse
    from pkg_py.pk_colorful_cli_util import pk_print

    pk_print(rf'''request.url : {request.url}''')
    # 이거 고민되는데 api 라면 json 으로 respon 하는게 좋겠고, web이라면 http 로 respon 하는게 맞을 것 같은데 이를 알아낼 수 있으면 좋겠다. 우선은 json 으로 respon 하자
    if "/web" in request.url:
        # return HTMLResponse(content=f'''<script>alert("{ment_error}");window.history.go(-1);</script>''')
        return HTMLResponse(content=f'''<script>alert("{exc.detail}");window.history.go(-1);</script>''')
    else:
        # json 으로 처리
        context = {
            "request": request,

            # "exc_body": exc.body,
            "exe_detail": exc.detail,
        }
        return JSONResponse(content=context)


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc):  # exc : Exception\
    from starlette.responses import HTMLResponse, JSONResponse
    from pkg_py.pk_colorful_cli_util import pk_print

    pk_print(rf'''request.url : {request.url}''')
    # 이거 고민되는데 api 라면 json 으로 respon 하는게 좋겠고, 
    # web이라면 http 로 respon 하는게 맞을 것 같은데
    # 이를 알아낼 수 있으면 좋겠다. 
    # 우선은 json 으로 respon 하자
    if "/web" in str(request.url):
        # html 파일로 처리
        # context = {
        #     "request": request,
        #     "msg": msg,
        #     'status_code': status_code,
        #     
        #     "exc_body": exc.body,
        #     "window_location_href": default_redirection_page,
        # }
        # return templates.TemplateResponse("/errors/main.html", context=context, status_code=status_code)

        # js alert 로 처리
        # window.history.go(-1);// 전 페이지로 이동
        # //window.history.go(-2);// 전전 페이지로 이동
        # //window.history.go(1);// 다음 페이지로 이동
        # //window.history.go(2);// 다다음 페이지로 이동
        # return HTMLResponse(content=f'''<script>alert("exec.detail : {exc.detail}");window.history.go(-1);</script>''')
        return HTMLResponse(content=f'''<script>alert("{exc.detail}");window.history.go(-1);</script>''')
    else:
        # json 으로 처리
        context = {
            "request": request,
            # "exc_body": exc.body,
            "exe_detail": exc.detail,
        }
        return JSONResponse(content=context)


app.add_middleware(ExceptionMiddleware)
# 커스텀 예외처리 핸들러, Exception 추가 작업 처리를 기대
# async def custom_exception_handler(request: Request, exc: Any) -> JSONResponse:
#     # custom exception handling logic
#     return JSONResponse(
#         status_code=500,
#         content={"message": "Custom exception handler 작동"}
#     )
# exception_handlers: Dict[Type[Exception], Coroutine[Any, Any, JSONResponse]] = {
#     Exception: custom_exception_handler
# }
# app.exception_handlers = exception_handlers


app.add_middleware(
    SessionMiddleware,
    secret_key=get_random_bytes(),  # 난수생성기로 세션시크릿 생성 # 세션이 동적으로 생성이 되게 하려고 했는데 그러면, 서버 재시작시 세션데이터가 손실, 동일서버를 다중서버로 운영 시 시크릿 키가 서로 다르면 문제가 됨. 고로 같아야함.
    max_age=3600,  # 세션 수명 3600 초(1시간)
)

@app.middleware("http")
async def preprocess_after_request(request, call_next):
    # 매 라우팅 전에 동작하는 함수 # 일종의 aop 같이 처리? # request 감지하고 트리거로서 가로채기를 하는 느낌이다
    await preprocess_after_request(request)
    response = await call_next(request)
    return response


@app.middleware("http")
async def preprocess_before_response_return(request, call_next):
    # 매 라우팅 후에 동작하는 함수
    response = await call_next(request)
    await preprocess_before_response_return(request, response)
    return response

# 라우팅 동작 설계 (잠정)
# https://pk_system.store/api/
# https://pk_system.store/web/
# https://pjh4139.store/search/p=

# 파비콘 라우팅 처리
# @app.get('/favicon.ico', include_in_schema=False)
# async def get_favicon():
#     #     # return PlainTextResponse('')
#     #     # return Response(content=b'', media_type='image/x-icon')
#     #     # raise HTTPException(status_code=404)
#     #     # raise HTTPException(status_code=500)
#     pass  # favicon 요청에 대한 콘솔에 출력.

# 라우터 설정
@app.get("/", tags=["API 테스트"])  # tags 파라미터는 FastAPI 문서화에 사용되는 데이터, 엔드포인트를 그룹화하는 데 사용되는 기능, # tags 를 동일하게 입력하면 하나의 api 그룹으로 묶을 수 있다
async def check_api_health(request: Request):
    import os
    import inspect
    from starlette.responses import RedirectResponse
    from pkg_py.pk_colorful_cli_util import pk_print
    from pkg_py.pk_core import print_iterable_as_vertical

    router_n = inspect.currentframe().f_code.co_name
    pk_print(f"{router_n}()", print_color='blue')
    if LTA:
        urls = []
        for index, route in enumerate(app.routes):
            if hasattr(route, "path"):
                url = f"{str(request.base_url)[0:-1]}{route.path}"
                pk_print(f'''url={url} %%%FOO%%%''')
                urls.append(url)
        print_iterable_as_vertical(item_iterable=urls, item_iterable_n=urls)
        # return json
        return {"success": f"fastapi 서버로서 {os.path.basename(__file__)}를 구동 중 입니다"}
    else:
        # redirect web
        return RedirectResponse(url="/web/member")

# web
# app.include_router(router_main.router, prefix="/web", tags=["회원관리 메인 web (MySql)"])
# app.include_router(router_join.router, prefix="/web", tags=["회원관리 가입 web (MySql)"])
# app.include_router(router_login.router, prefix="/web", tags=["회원관리 로그인 web (MySql)"])
# app.include_router(router_commutation.router, prefix="/web", tags=["근태관리 web (MySql)"])
# app.include_router(router_customer_service.router, prefix="/web", tags=["CS 관리 web (MySql)"])
# app.include_router(router_excel_merge.router, prefix="/web", tags=["엑셀파일 병합 web (Server Local Directory)"])
# app.include_router(router_cloud.router, prefix="/web", tags=["파일공유 web (Server Local Directory)"])  # 백업
# app.include_router(router_developer_special.router, prefix="/web", tags=["개발자 web (Not Defined)"])
# app.include_router(router_finance_data.router, prefix="/web", tags=["금융정보 web (Open Api)"])
# app.include_router(router_developer_special.router, prefix="/web", tags=["백오피스 web"])

# api
app.include_router(router_nav_items.router, prefix="/api", tags=["nav-items API #DB JSON"])
# app.include_router(router_test_try_1.router, prefix="/test", tags=["x test try 1"])
# app.include_router(router_test_try_2.router, prefix="/test", tags=["x test try 2"])
# app.include_router(router_test_try_3.router, prefix="/test", tags=["x test try 3"])
# app.include_router(router_item.router, prefix="/api", tags=["상품관리 API"])
# app.include_router(router_todo.router, prefix="/api", tags=["할일관리 API(mysql.test_db.todos 에 저장), 미완성"])
# app.include_router(router_member.router, prefix="/api", tags=["회원관리 API(maria.test_db.members 에 저장), 미완성"])
# app.include_router(router_user.router, prefix="/api", tags=["회원관리 API(mysql.test_db.users 에 저장), 미완성"])
# app.include_router(router_test.router, prefix="/test", tags=["JWT/OAuth2 test4 (MySql)"])

# 이 파일을 uvicorn으로 실행하면 해당 코드 블록이 실행되지 않습니다.
def main():
    import os.path
    import uvicorn
    import traceback
    import toml
    import sys
    import os.path
    import os
    import json
    import inspect
    from starlette.templating import Jinja2Templates
    from starlette.responses import HTMLResponse, RedirectResponse, JSONResponse
    from pkg_py.pk_colorful_cli_util import pk_print
    from pkg_py.pk_core import print_iterable_as_vertical
    from pkg_py.pk_core import ensure_pnx_made, is_letters_cnt_zero, write_str_to_f
    from pkg_py.pk_core import get_n, ensure_pnx_made
    from fastapi.middleware.cors import CORSMiddleware
    from pkg_py.pk_core_constants import F_CONFIG_TOML

    config = toml.load(F_CONFIG_TOML)
    pk_protocol_type = config["pk_uvicorn"]["protocol_type"]
    pk_host = config["pk_uvicorn"]["host"]
    pk_port = config["pk_uvicorn"]["port"]
    pk_uvicorn_url = f"{pk_protocol_type}://{pk_host}:{pk_port}"
    pk_print(f'''pk_uvicorn_url={pk_uvicorn_url} %%%FOO%%%''')

    uvicorn.run(app=f"{get_n(__file__)}:app", host=pk_host, port=pk_port)


if __name__ == "__main__":
    # 이 파일이 직접 실행되는 경우만 이 코드 블록은 실행됩니다.
    # 이 파일을 import하여 사용할 때는 해당 코드 블록이 실행되지 않습니다.
    main()