from app.core.entities.developer import DeveloperModel, Developer
from app.infra.database import Sessionlocal
from app.core.repository.IDeveloperRepository import IDeveloperRepository
from app.core.exceptions.exception import DeveloperNotFoundException


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

    def find_by_id(self, developer_id: int) -> Developer:
        with Sessionlocal() as session:
            developer_model = session.query(DeveloperModel).filter_by(id=developer_id).first()
            if not developer_model:
                raise DeveloperNotFoundException(developer_id)
            return Developer(
                id=developer_model.id,
                name=developer_model.name,
                skills=developer_model.skills.split(",")
            )