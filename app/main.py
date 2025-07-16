from fastapi import FastAPI
from app.core.lifespan import lifespan
from app.core.middleware import register_middlewares
from app.api.routes import api_router
from app.web.routes import web_router
from starlette.staticfiles import StaticFiles

app = FastAPI(lifespan=lifespan)

register_middlewares(app)

app.include_router(api_router, prefix="/api")
app.include_router(web_router, prefix="/web")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
