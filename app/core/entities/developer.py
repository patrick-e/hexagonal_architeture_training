from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DeveloperModel(Base):
    __tablename__ = "developers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    skills = Column(String, nullable=False)

class Developer:
    def __init__(self, id, name, skills):
        self.id = id
        self.name = name
        self.skills = skills
