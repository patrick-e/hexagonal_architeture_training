from abc import ABC,abstractmethod
from app.core.entities.developer import Developer

class IDeveloperRepository(ABC):

    @abstractmethod
    def save(self,developer:Developer) -> Developer:
        pass

    def find_by_id(self,developer_id:int) -> Developer:
        pass