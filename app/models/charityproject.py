from sqlalchemy import Column, Text, String

from app.models.base_model import AbstractBaseModel


class CharityProject(AbstractBaseModel):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
