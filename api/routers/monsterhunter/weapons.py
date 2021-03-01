from fastapi import APIRouter
from typing import List

from models.monsterhunter.weapons import Weapon as WeaponModel
from controllers.monsterhunter import weapons as weapon_controller

router = APIRouter(
    prefix="/api/monsterhunter/weapons",
    tags=["monsterHunter"],
    responses={404: {"description": "Not Found"}}
)


@router.get("/", response_model=List[WeaponModel])
async def get_all_weapons():
    return weapon_controller.get_weapons()


@router.get("/{weapon_id}", response_model=WeaponModel)
async def get_weapon_by_id(weapon_id: int):
    return weapon_controller.get_weapons_by_id(weapon_id)
