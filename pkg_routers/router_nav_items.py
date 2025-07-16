import inspect
import json

from fastapi import APIRouter, HTTPException

from pkg_py.pk_core_constants import F_NAV_ITEMS_JSON
from pkg_py.pk_colorful_cli_util import pk_print

router = APIRouter()

@router.get("/nav-items/{index}")
def get_nav_items_by_index(index: str):
    func_n = inspect.currentframe().f_code.co_name
    pk_print(f"{func_n}()")
    # NAV_ITEMS = FastapiUtil.init_and_update_json_file(NAV_ITEMS_JSON)
    try:
        with open(F_NAV_ITEMS_JSON, "r", encoding="utf-8") as file:
            NAV_ITEMS = json.load(file)
        return NAV_ITEMS[int(index)]
    except:
        pk_print(f"({len(NAV_ITEMS)})개의 등록된 nav_items 중, index 가 {index}인 nav_item 이 없습니다.")
        raise HTTPException(status_code=404, detail=f"({len(NAV_ITEMS)})개의 등록된 nav_items 중, index 가 {index}인 nav_item 이 없습니다.")
