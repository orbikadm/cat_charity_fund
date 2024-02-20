from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, PositiveInt


TIME_EXAMPLE = "2024-02-19T11:51:11.389Z"   # ДОЛЖЕН БЫТЬ НЕ В СХЕМЕ
# class DonationBase(BaseModel):
#     name: Optional[str] = Field(None, min_length=1, max_length=100)
#     description: Optional[str]


class CharityProjectCreate(BaseModel):
    name: str = Field(..., max_length=100)
    description: str
    full_amount: PositiveInt

    # class Config:
    #     orm_mode = True


class CharityProjectDB(BaseModel):
    name: str = Field(..., max_length=100)
    description: str
    full_amount: PositiveInt
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime = Field(None, example=TIME_EXAMPLE)
    close_date: datetime = Field(None, example=TIME_EXAMPLE)

    class Config:
        orm_mode = True


class CharityProjectUpdate(BaseModel):
    name: str = Field(..., max_length=100)
    description: str
    full_amount: PositiveInt
