from pydantic import BaseModel


class Weapon(BaseModel):
    weapons_id: int
    name: str
    rank: int
    dmg: int
