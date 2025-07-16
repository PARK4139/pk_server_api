from fastapi import APIRouter

router = APIRouter()

@router.get("/nav-items")
def get_nav_items():
    return {"items": ["item1", "item2"]}
