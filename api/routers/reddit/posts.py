from fastapi import APIRouter
from typing import List
from controllers.reddit import posts as postsController

from models.reddit.posts import Post as PostModel

router = APIRouter(
    prefix="/api/reddit/posts",
    tags=["reddit"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[PostModel])
async def get_all_posts():
    return postsController.get_posts()


@router.get("/{post_id}", response_model=PostModel)
async def get_posts_by_post_id(post_id: int):
    return postsController.get_post_by_id(post_id)


@router.get("/posts_by_user/{user_id}", response_model=List[PostModel])
async def get_posts_by_user_id(user_id: int):
    print(f"POST ROUTER : {postsController.get_post_by_user_id(user_id)}")
    return postsController.get_post_by_user_id(user_id)
