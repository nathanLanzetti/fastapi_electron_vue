from fastapi import APIRouter
from typing import List, Dict

from models.monsterhunter.monsters import Monster as MonsterModel, BaseMonster as BaseMonsterModel
from controllers.monsterhunter import monsters as monster_controller

router = APIRouter(
    prefix="/api/monsterhunter/monsters",
    tags=["monsterHunter"],
    responses={404: {"description": "Not Found"}}
)


@router.get("/", response_model=List[MonsterModel])
async def get_all_monsters():
    return monster_controller.get_monsters()


@router.get("/{weapon_id}", response_model=MonsterModel)
async def get_monster_by_id(weapon_id: int):
    return monster_controller.get_monster_by_id(weapon_id)


@router.post("/")
async def create_monster(monster_to_create: BaseMonsterModel):
    return monster_controller.create_monster(monster_to_create.dict())
