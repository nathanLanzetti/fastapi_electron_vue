from pydantic import BaseModel


class A(BaseModel):
    project_id: int
    project_name: str
