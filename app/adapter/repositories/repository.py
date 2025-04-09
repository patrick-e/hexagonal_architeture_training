from app.core.entities.developer import DeveloperModel, Developer
from app.infra.database import Sessionlocal
from app.core.repository.IDeveloperRepository import IDeveloperRepository


class SQLAlchemyDeveloperRepository(IDeveloperRepository):
    def save(self, developer: Developer) -> Developer:
        with Sessionlocal() as session:
            developer_model = DeveloperModel(
                name=developer.name,
                skills=",".join(developer.skills)
            )
            session.add(developer_model)
            session.commit()
            developer.id = developer_model.id
        return developer