import inspect
import os
import shutil
import uuid
from tempfile import NamedTemporaryFile
from typing import List, IO

from fastapi import APIRouter
from fastapi import File, UploadFile
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse, FileResponse, StreamingResponse, Response, HTMLResponse

from pkg_pk_server_api_for_linux import DebuggingUtil, FastapiUtil, BusinessLogicUtil, StateManagementUtil, TestUtil, FileSystemUtil, UvicornUtil

templates = Jinja2Templates(directory=r"pkg_web/templates")

router = APIRouter()
# router.mount("/static", StaticFiles(directory=os.path.join(D_PROJECT_FASTAPI, 'pkg_web', 'static')), name="static")
router.mount("/static", StaticFiles(directory="pkg_web/static"), name="static")
# router.mount("/static", StaticFiles(directory=os.path.join(D_PROJECT_FASTAPI, 'pkg_web', 'static')), name="static")
router.mount("/static2", StaticFiles(directory="pkg_xlsx"), name="static2")


prefix_promised = "web"  # /web 는 다른 파일에 작성된 부분이다. 라우터를 다른 파일로 분리했기 때문에 이 부분은 유지보수하며 알아내기가 까다롭다 # 하드코딩
default_redirection_page_without_prefix = '/excel-merge'
default_redirection_page = f'/{prefix_promised}{default_redirection_page_without_prefix}'


@router.get("/excel-merge")
async def get_excel_merge(request: Request):
    func_n = inspect.currentframe().f_code.co_name
    pk_print(f"{func_n}()")
    FastapiUtil.jinja_data.web = prefix_promised

    if 'id' in request.session and request.session['id'] != '':
        # session 기간 내에 로그인 한 경우
        context = {"request": request, "jinja_data": FastapiUtil.jinja_data}
        return templates.TemplateResponse("/excel_merge.html", context=context)
    else:
        # session 기간 내에 로그인 하지 않은 경우
        context = {"request": request, "jinja_data": FastapiUtil.jinja_data}
        return RedirectResponse('/member')


@router.post("/excel-merge")
async def post_excel_merge(request: Request):
    func_n = inspect.currentframe().f_code.co_name
    pk_print(f"{func_n}()")
    FastapiUtil.jinja_data.web = prefix_promised

    if 'id' in request.session and request.session['id'] != '':

        # 디렉토리를 재생성. 주의, 하위파일은 모두 삭제됨, 복구불가
        DIR_PATH = D_XLS_TO_MERGE
        truncate_tree(DIR_PATH)

        # 디렉토리를 재생성. 주의, 하위파일은 모두 삭제됨, 복구불가
        DIR_PATH = DIRECTORY_XLS_MERGED
        truncate_tree(DIR_PATH)


        # session 기간 내에 로그인 한 경우
        context = {"request": request, "jinja_data": FastapiUtil.jinja_data}
        return templates.TemplateResponse("/excel_merge.html", context=context)
    else:
        # session 기간 내에 로그인 하지 않은 경우
        context = {"request": request, "jinja_data": FastapiUtil.jinja_data}
        return RedirectResponse('/member')


@router.post("/excel-merge2")
async def post_excel_merge2(files: List[UploadFile]):
    func_n = inspect.currentframe().f_code.co_name
    pk_print(f"{func_n}()")
    FastapiUtil.jinja_data.web = prefix_promised

    if len(files)==0:
        return HTMLResponse(content=f'''<script>alert("선택된 파일이 없습니다");window.history.go(-1);</script>''')

    # 이와같은 방식으로 여러명이 동시에 접속하여 머지하면 문제가 있을 것 같은 생각이 드는데..?
    # 알아서 관리가 되는지 잘 모르겠다.
    # 이래서 DB 에 저장하는 도움을 줄 것 같긴한데,
    # 지금의 구현된 엑셀머지 기능은 엑셀머지를 하려면 어찌됬든 폴더에 있어야 한다.

    # 디렉토리를 재생성. 주의, 하위파일은 모두 삭제됨, 복구불가
    truncate_tree(D_XLS_TO_MERGE)

    # 디렉토리를 재생성. 주의, 하위파일은 모두 삭제됨, 복구불가
    truncate_tree(DIRECTORY_XLS_MERGED)

    # 클라이언트에서 보낸파일들 서버의 지정된 디렉토리에 저장
    DIR_PATH = D_XLS_TO_MERGE
    for file in files:
        content = await file.read()
        pk_print(file.filename)
        with open(os.path.join(DIR_PATH, file.filename), "wb") as fp:
            fp.write(content)

    # 엑셀파일들 병합
    merge_excel_files(D_XLS_TO_MERGE)

    # 디렉토리를 재생성. 주의, 하위파일은 모두 삭제됨, 복구불가
    truncate_tree(D_XLS_TO_MERGE)

    # client 다운로드 폴더에 저장
    file_name_downloaded = get_target_as_nx(constants.FILE_MERGED_EXCEL_XLSX)
    return FileResponse(path = constants.FILE_MERGED_EXCEL_XLSX, filename=file_name_downloaded, media_type='application/octet-stream')


