import inspect
from typing import Optional

import pandas as pd
from fastapi import HTTPException
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse, FileResponse

from project_fastapi.router_utils import FastapiUtil
from pkg_py.pk_colorful_cli_util import pk_print

import sys
import traceback

from fastapi import APIRouter


templates = Jinja2Templates(directory=r"pkg_web/templates")

router = APIRouter()

prefix_promised = "web"  # /web 는 다른 파일에 작성된 부분이다. 라우터를 다른 파일로 분리했기 때문에 이 부분은 유지보수하며 알아내기가 까다롭다 # 하드코딩
default_redirection_page_without_prefix = '/world-finance-data'

default_redirection_page = f'/{prefix_promised}{default_redirection_page_without_prefix}'


@router.get("/world-finance-data")
async def get_world_finance_data(request: Request):
    func_n = inspect.currentframe().f_code.co_name
    pk_print(f"{func_n}()")
    FastapiUtil.jinja_data.web = prefix_promised

    try:
        # 로그인 한 경우
        if 'id' in request.session and request.session['id'] != '':

            # FastapiUtil.jinja_data.items 에 저장
            FastapiUtil.jinja_data.items = []

            class Item:
                ticker: Optional[str]
                stock_name: Optional[str]
                market_name: Optional[str]

            FILE_XLSX = f"{constants.D_PKG_XLSX}/update_ticker_xlsx_watched().xlsx"
            df = pd.read_excel(FILE_XLSX)
            df = df[:len(constants.WATCH_KEYWORDS_LIST)]
            # pk_print(rf'''df : {df}''')
            # fig = ff.create_table(df)
            # fig.show()

            for index, row in df.iterrows():
                item = Item()  # for 문 내에 있어야 한다. item 는 재초기화된 item 과 데이터 공유를 private 설정
                item.ticker = row['ticker']
                item.stock_name = row['stock_name']
                item.market_name = row['market_name']
                FastapiUtil.jinja_data.items.append(item)
                pk_print(rf'''item.ticker : {item.ticker}''')
                pk_print(rf'''item.stock_name : {item.stock_name}''')
                pk_print(rf'''item.market_name : {item.market_name}''')

            context = {"request": request, "jinja_data": FastapiUtil.jinja_data}
            return templates.TemplateResponse("/world_finance_data.html", context=context)
        # 로그인 하지 않은 경우
        else:
            raise HTTPException(status_code=400, detail="로그인 후 사용이 가능한 기능입니다")
    except:
        traceback.print_exc(file=sys.stdout)
        return {"detail": f"에러가 발생했습니다"}


@router.post("/world-finance-data")
async def post_world_finance_data(request: Request):
    func_n = inspect.currentframe().f_code.co_name
    pk_print(f"{func_n}()")
    try:
        FastapiUtil.jinja_data.web = prefix_promised

        if 'id' in request.session and request.session['id'] != '':
            # 로그인 한 경우
            context = {"request": request, "jinja_data": FastapiUtil.jinja_data}
            return templates.TemplateResponse("/world_finance_data.html", context=context)
        else:
            # 로그인 하지 않은 경우
            return RedirectResponse('/member')
    except:
        traceback.print_exc(file=sys.stdout)
        return {"detail": f"에러가 발생했습니다"}


@router.get("/world-finance-data/download-file/{file_nx}")
# async def get_out_cloud_download_file_nx(file_nx):
async def get_out_cloud_download_file_nx(file_nx, request: Request):
    func_n = inspect.currentframe().f_code.co_name
    pk_print(f"{func_n}()")
    targetFile = rf"{constants.D_PKG_XLSX}/{file_nx}"
    pk_print(f"targetFile:{INDENTATION_PROMISED}{targetFile}")
    try:
        if 'id' in request.session and request.session['id'] != '':
            return FileResponse(path=targetFile, filename=file_nx)  # media_type- 미디어 유형을 제공. 설정하지 않으면 파일 이름이나 경로를 사용하여 미디어 유형을 추론합니다.
        else:
            return RedirectResponse('/member')
    except:
        traceback.print_exc(file=sys.stdout)
        return {"detail": f"에러가 발생했습니다"}
