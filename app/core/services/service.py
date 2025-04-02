from app.core.entities.developer import Developer

class DeveloperServices:
    def __init__(self, developer_repository):
        self.developer_repository = developer_repository

    def create_developer(self,name: str, skills:list[str]) -> Developer:
        developer = Developer(id=None,name=name,skills=skills)
        return self.developer_repository.save(developer)