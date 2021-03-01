from fastapi import APIRouter
from typing import List
import json
import sqlite3
from controllers.reddit import users as userController
from controllers.reddit import posts as postController
from models.reddit.users import User as UserModel
from models.reddit.posts import Post as PostModel

router = APIRouter(
    prefix="/api/reddit/users",
    tags=["reddit"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[UserModel])
async def get_all_users():
    return userController.get_users()


@router.get("/{user_id}", response_model=UserModel)
async def get_users_by_post_id(user_id: int):
    return userController.get_user_by_id(user_id)


@router.get("/comments/{user_id}", response_model=UserModel)
async def get_user_with_comments(user_id: int):
    user = userController.get_user_by_id(user_id)
    user["posts"] = postController.get_post_by_user_id(user_id)
    return user
