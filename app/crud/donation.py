from datetime import datetime
from typing import Optional

from sqlalchemy import and_, between, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Donation, User


class CRUDDonation(CRUDBase):

    # async def get_reservations_at_the_same_time(
    #         self,
    #         from_reserve: datetime,
    #         to_reserve: datetime,
    #         meetingroom_id: int,
    #         session: AsyncSession,
    # ) -> list[Donation]:
    #     reservations = await session.execute(
    #         select(Donation).where(
    #             Donation.meetingroom_id == meetingroom_id,
    #             and_(
    #                 from_reserve <= Donation.to_reserve,
    #                 to_reserve >= Donation.from_reserve
    #             )
    #         )
    #     )
    #     reservations = reservations.scalars().all()
    #     return reservations

    # async def get_future_reservations_for_room(
    #         self,
    #         room_id: int,
    #         session: AsyncSession,
    # ):
    #     reservations = await session.execute(
    #         # Получить все объекты Reservation.
    #         select(Reservation).where(
    #             # Где внешний ключ meetingroom_id 
    #             # равен id запрашиваемой переговорки.
    #             Reservation.meetingroom_id == room_id,
    #             # А время конца бронирования больше текущего времени.
    #             Reservation.to_reserve > datetime.now()
    #         )
    #     )
    #     reservations = reservations.scalars().all()
    #     return reservations

    async def get_by_user(
            self, session: AsyncSession, user: User
    ):
        donations = await session.execute(
            select(Donation).where(
                Donation.user_id == user.id
            )
        )
        return donations.scalars().all()


donation_crud = CRUDDonation(Donation)
