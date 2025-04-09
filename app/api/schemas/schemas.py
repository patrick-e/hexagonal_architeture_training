from pydantic import BaseModel

class DeveloperCreateSchema(BaseModel):
    name: str
    skills: list[str]

class DeveloperResponseSchema(BaseModel):
    id: int
    name: str
    skills: list[str]