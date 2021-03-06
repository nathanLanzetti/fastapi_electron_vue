from fastapi import APIRouter

from models.projects.a import A as AModel
from controllers.projects import a as a_controller

router = APIRouter(
    prefix="/api/projects/a",
    tags=["projects"],
    responses={404: {"description": "Not Found"}}
)


@router.get("/name", response_model=AModel)
async def get_project_name():
    return a_controller.get_project_name()
