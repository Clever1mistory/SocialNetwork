from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db
from src.ops.models import Post, Like, User
from src.ops.schemas import PostCreate, LikeCreate, PostUpdate
from src.auth.base_config import current_user


router = APIRouter()


@router.get("/posts")
async def get_all_posts(session: AsyncSession = Depends(get_db)):
    query = select(Post)
    result = await session.execute(query)
    posts = result.scalars().all()
    return posts


@router.get("/posts/{post_id}")
# Получение поста по id
async def get_post(post_id: int, session: AsyncSession = Depends(get_db)):
    query = select(Post).where(Post.id == post_id)
    result = await session.execute(query)
    return result.scalars().all()


@router.post("/posts/create_post/")
# Создание нового поста авторизованным пользователем
async def create_post(new_post: PostCreate, current_user: User = Depends(current_user),
                      session: AsyncSession = Depends(get_db)):
    stmt = insert(Post).values(**new_post.dict(), author_id=current_user.id)
    await session.execute(stmt)
    await session.commit()
    return {"status": "successfully created"}


@router.put("/posts/{post_id}")
async def update_post(post_id: int, updated_post: PostUpdate, current_user: User = Depends(current_user),
                      session: AsyncSession = Depends(get_db)):
    # Проверяем, является ли пользователь автором поста
    post = await session.execute(select(Post).where(Post.id == post_id))
    post = post.scalar_one()
    if post.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="Only the author can update the post")

    # Обновляем данные поста
    stmt = update(Post).where(Post.id == post_id).values(**updated_post.dict(exclude_unset=True))
    await session.execute(stmt)
    await session.commit()
    return {"status": "successfully updated"}


@router.delete("/posts/{post_id}")
async def delete_post(post_id: int, current_user: User = Depends(current_user),
                      session: AsyncSession = Depends(get_db)):
    # Проверяем, является ли пользователь автором поста
    post = await session.execute(select(Post).where(Post.id == post_id))
    post = post.scalar_one()
    if post.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="Only the author can delete the post")

    # Удаляем пост
    stmt = delete(Post).where(Post.id == post_id)
    await session.execute(stmt)
    await session.commit()
    return {"status": "successfully deleted"}


@router.post("/posts/like_post")
# Лайк поста авторизованным пользователем
async def like_post(new_like: LikeCreate, current_user: User = Depends(current_user),
                    session: AsyncSession = Depends(get_db)):
    stmt = insert(Like).values(**new_like.dict(), user_id=current_user.id)
    await session.execute(stmt)
    await session.commit()
    return {"status": "successfully liked"}
