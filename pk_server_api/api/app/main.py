from fastapi import FastAPI
from app.routes import nav_router

app = FastAPI()
app.include_router(nav_router)

@app.get("/")
async def root():
    return {"message": "Welcome to pk_server_api API"}
