from pydantic import BaseModel


class Post(BaseModel):
    post_id: int
    content: str
    upvotes: int
    downvotes: int
    begin_date: str
    user_id: int
