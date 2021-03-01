from pydantic import BaseModel


class BaseMonster(BaseModel):
    name: str
    description: str
    hp: int


class Monster(BaseMonster):
    monster_id: int
