from pydantic import BaseModel, Field, PositiveInt

from app.schemas.base import AbstractBaseSchema


class CharityProjectCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1)
    full_amount: PositiveInt


class CharityProjectUpdate(CharityProjectCreate):
    name: str = Field(None, min_length=1, max_length=100)
    description: str = Field(None, min_length=1)
    full_amount: PositiveInt


class CharityProjectDB(AbstractBaseSchema, CharityProjectCreate):
    id: int

    class Config:
        orm_mode = True
