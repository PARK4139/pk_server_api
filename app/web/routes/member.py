from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/web/templates")

@router.get("/member")
def render_member_page(request: Request):
    return templates.TemplateResponse("member.html", {"request": request})
