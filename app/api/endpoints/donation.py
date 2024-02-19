from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
# Вместо импортов 6 функций импортируйте объект meeting_room_crud.
# from app.crud.meeting_room import meeting_room_crud
from app.core.user import current_superuser, current_user
# from app.models.meeting_room import MeetingRoom
# from app.schemas.meeting_room import (
#     MeetingRoomCreate, MeetingRoomDB, MeetingRoomUpdate
# )
# from app.api.validators import check_name_duplicate, check_meeting_room_exists
# from app.crud.reservation import reservation_crud
from app.schemas.donation import DonationCreate, DonationDB, DonationAdminDB


router = APIRouter()


@router.post(
    '/',
    response_model=DonationDB,
    # response_model_exclude_none=True,
    dependencies=[Depends(current_user)],
)
async def create_donation(
        donation: DonationCreate,
        # session: AsyncSession = Depends(get_async_session),
):
    """Сделать пожертвование."""
    # await check_name_duplicate(meeting_room.name, session)
    # # Замените вызов функции на вызов метода.
    # new_room = await meeting_room_crud.create(meeting_room, session)
    # return new_room
    return {'new_donations': 'Отправлен новый донат'}


@router.get(
    '/',
    response_model=list[DonationAdminDB],
    dependencies=[Depends(current_superuser)],
    # response_model_exclude_none=True,
)
async def get_all_donations(
        # session: AsyncSession = Depends(get_async_session),
):
    """
    Только для суперюзеров.

    Возвращает список всех пожертвований.
    """
    # Замените вызов функции на вызов метода.
    # all_rooms = await meeting_room_crud.get_multi(session)
    # return all_rooms
    return {'all_donations': 'Список всех донатов'}


@router.get(
    '/my',
    response_model=list[DonationDB],
    # Добавляем множество с полями, которые надо исключить из ответа.
    # response_model_exclude={'user_id'},
    dependencies=[Depends(current_user)],
)
async def get_user_donations(
        # meeting_room_id: int,
        # session: AsyncSession = Depends(get_async_session),
):
    """Вернуть список пожертвований пользователя, выполняющего запрос."""
    # await check_meeting_room_exists(meeting_room_id, session)
    # reservations = await reservation_crud.get_future_reservations_for_room(
    #     room_id=meeting_room_id, session=session
    # )
    # return reservations
    return {'my_donations': 'Список моих донатов'}
