from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🔵 FastAPI 앱이 시작됩니다")
    yield
    print("🔴 FastAPI 앱이 종료됩니다")
