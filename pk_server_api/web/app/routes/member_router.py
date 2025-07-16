from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

member_router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@member_router.get("/member", response_class=HTMLResponse)
async def member(request: Request):
    return templates.TemplateResponse("member.html", {"request": request})
