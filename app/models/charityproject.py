from datetime import datetime

from pydantic import BaseModel


class CharityProject(BaseModel):
    id: int
    name: str
    description: str
    full_amount: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: datetime


class Donation(BaseModel):
    id: int
    name: str
    description: str
    full_amount: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: datetime
