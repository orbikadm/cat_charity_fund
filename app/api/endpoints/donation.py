from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.donation import donation_crud
from app.schemas.donation import DonationCreate, DonationDB, DonationAdminDB
from app.models import User


router = APIRouter()


@router.post(
    '/',
    response_model=DonationDB,
    # response_model_exclude_none=True,
)
async def create_donation(
    donation: DonationCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    """Сделать пожертвование."""
    new_donation = await donation_crud.create(donation, session, user)
    return new_donation


@router.get(
    '/',
    response_model=list[DonationAdminDB],
    dependencies=[Depends(current_superuser)],
    # response_model_exclude_none=True,
)
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session),
):
    """
    Только для суперюзеров.

    Возвращает список всех пожертвований.
    """
    all_donations = await donation_crud.get_multi(session)
    print(all_donations)
    return all_donations


@router.get(
    '/my',
    response_model=list[DonationDB],
    # response_model_exclude={'user_id'},
)
async def get_user_donations(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session),
):
    """Вернуть список пожертвований пользователя, выполняющего запрос."""
    # await check_meeting_room_exists(meeting_room_id, session)
    donations = await donation_crud.get_by_user(
        user=user, session=session
    )
    return donations
