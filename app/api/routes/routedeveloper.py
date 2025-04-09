# filepath: app/api/routes/developer_routes.py
from fastapi import APIRouter, Depends
from app.api.schemas.schemas import DeveloperCreateSchema, DeveloperResponseSchema
from app.core.services.service import DeveloperServices
from app.adapter.repositories.repository import SQLAlchemyDeveloperRepository

router = APIRouter()

def get_developer_service():
    repository = SQLAlchemyDeveloperRepository()
    return DeveloperServices(repository)

@router.post("/developers", response_model=DeveloperResponseSchema)
def create_developer(
    developer: DeveloperCreateSchema,
    service: DeveloperServices = Depends(get_developer_service),
):
    return service.create_developer(developer.name, developer.skills)