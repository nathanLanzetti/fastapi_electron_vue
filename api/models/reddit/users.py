from pydantic import BaseModel
from typing import Optional, List
from models.reddit.posts import Post


class User(BaseModel):
    user_id: int
    firstname: str
    lastname: str
    pseudo: str
    posts: Optional[List[Post]] = None
