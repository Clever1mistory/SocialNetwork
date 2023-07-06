from fastapi import FastAPI


from src.auth.base_config import auth_backend, fastapi_users
from src.auth.schemas import UserRead, UserCreate

from src.ops.routes import router as router_operation
from src.pages.router import router as router_pages
from src.chat.router import router as router_chat


app = FastAPI(
    title="Social Network"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(router_operation)
app.include_router(router_pages)
app.include_router(router_chat)
