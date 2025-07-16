from fastapi import APIRouter

nav_router = APIRouter()

@nav_router.get("/nav-items")
async def get_nav_items():
    return {"items": ["item1", "item2"]}
