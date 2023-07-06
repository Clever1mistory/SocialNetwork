# from datetime import datetime
#
# from fastapi_users.db import SQLAlchemyBaseUserTable
# from sqlalchemy import Column, Integer, String, Boolean, DateTime
# from sqlalchemy.orm import relationship, DeclarativeMeta, declarative_base
#
# from database import Base
#
#
# class User(SQLAlchemyBaseUserTable[int], Base):
#     __tablename__ = "users"
#
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)
#     created_at = Column(DateTime, default=datetime.utcnow())
#     is_superuser = Column(Boolean, default=False, nullable=False)
#     is_verified = Column(Boolean, default=False, nullable=False)
#
#     posts = relationship("Post", back_populates="author")
#     likes = relationship("Like", back_populates="user")
