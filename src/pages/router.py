from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from starlette.responses import HTMLResponse

from src.ops.routes import get_all_posts

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="src/templates")


@router.get("/base")
def get_base_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})


@router.get("/auth/login", response_class=HTMLResponse)
def get_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/posts")
def get_all_posts_page(request: Request, posts=Depends(get_all_posts)):
    return templates.TemplateResponse("posts.html", {"request": request, "posts": posts})


@router.get("/chat")
def get_chat_page(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})
