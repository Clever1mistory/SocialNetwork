from pydantic import BaseModel

from src.auth.schemas import UserRead


class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    pass


class Post(PostBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True


class LikeBase(BaseModel):
    pass


class LikeCreate(LikeBase):
    post_id: int


class Like(LikeBase):
    id: int
    post: Post
    user: UserRead

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str
