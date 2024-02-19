from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, PositiveInt


TIME_EXAMPLE = "2024-02-19T11:51:11.389Z"   # ДОЛЖЕН БЫТЬ НЕ В СХЕМЕ
# class DonationBase(BaseModel):
#     name: Optional[str] = Field(None, min_length=1, max_length=100)
#     description: Optional[str]


class DonationCreate(BaseModel):
    full_amount: PositiveInt
    comment: Optional[str]

    # class Config:
    #     orm_mode = True


class DonationDB(BaseModel):
    full_amount: PositiveInt
    comment: Optional[str]
    id: int
    create_date: datetime = Field(None, example=TIME_EXAMPLE)


class DonationAdminDB(BaseModel):
    full_amount: PositiveInt
    comment: Optional[str]
    id: int
    create_date: datetime = Field(None, example=TIME_EXAMPLE)
    user_id: int
    invested_amount: int
    fully_invested: bool
    close_date: Optional[datetime] = Field(None, example=TIME_EXAMPLE)
