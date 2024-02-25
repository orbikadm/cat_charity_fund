from datetime import datetime
from typing import Optional

from pydantic import Field, PositiveInt, BaseModel


TIME_EXAMPLE = "2024-02-19T11:51:11.389Z"   # ДОЛЖЕН БЫТЬ НЕ В СХЕМЕ


class AbstractBaseSchema(BaseModel):
    full_amount: PositiveInt
    invested_amount: int
    fully_invested: bool
    create_date: datetime = Field(..., example=TIME_EXAMPLE)
    close_date: Optional[datetime] = Field(None, example=TIME_EXAMPLE)
