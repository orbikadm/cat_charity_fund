from sqlalchemy import Column, Text, Integer, ForeignKey

from app.models.base_model import AbstractBaseModel


class Donation(AbstractBaseModel):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text, nullable=True)
