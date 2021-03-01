from fastapi import APIRouter
from typing import List, Dict

from models.monsterhunter.monsters import Monster as MonsterModel, BaseMonster as BaseMonsterModel
from controllers.monsterhunter import monsters as monster_controller
from controllers.projects import projects

router = APIRouter(
    prefix="/api/projects",
    tags=["projects"],
    responses={404: {"description": "Not Found"}}
)


@router.get("/{project_name}")
async def open_project(project_name: str):
    return projects.open_projects(project_name)
