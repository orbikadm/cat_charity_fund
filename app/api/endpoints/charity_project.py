from fastapi import APIRouter, Depends, HTTPException

# from sqlalchemy.ext.asyncio import AsyncSession

# from app.core.db import get_async_session
# # Вместо импортов 6 функций импортируйте объект meeting_room_crud.
# from app.crud.meeting_room import meeting_room_crud
from app.core.user import current_superuser
# from app.models.meeting_room import MeetingRoom
# from app.schemas.meeting_room import (
#     MeetingRoomCreate, MeetingRoomDB, MeetingRoomUpdate
# )
# from app.api.validators import check_name_duplicate, check_meeting_room_exists
# from app.crud.reservation import reservation_crud
from app.schemas.charityproject import CharityProjectUpdate, CharityProjectDB, CharityProjectCreate


router = APIRouter()


@router.post(
    '/',
    response_model=CharityProjectDB,
    # response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def create_charity_project(
        charity_project: CharityProjectCreate,
        # session: AsyncSession = Depends(get_async_session),
):
    """
    Только для суперюзеров.

    Создаёт благотворительный проект.
    """
    # await check_name_duplicate(meeting_room.name, session)
    # # Замените вызов функции на вызов метода.
    # new_room = await meeting_room_crud.create(meeting_room, session)
    # return new_room
    return {'charity_project': 'charity_project СОЗДАН НОВЫЙ'}


@router.get(
    '/',
    response_model=list[CharityProjectDB],
    # response_model_exclude_none=True,
)
async def get_all_charity_projects(
        # session: AsyncSession = Depends(get_async_session),
):
    """Возвращает список всех проектов."""
    # Замените вызов функции на вызов метода.
    # all_rooms = await meeting_room_crud.get_multi(session)
    # return all_rooms
    return {'charity_project': 'Получены все проекты'}


@router.patch(
    '/{project_id}',
    response_model=CharityProjectDB,
    # response_model_exclude_none=True,
    # # Новая зависимость.
    dependencies=[Depends(current_superuser)],
)
async def update_charity_project(
        project_id: int,
        obj_in: CharityProjectUpdate,
        # session: AsyncSession = Depends(get_async_session),
):
    """
    Только для суперюзеров.

    Закрытый проект нельзя редактировать; нельзя установить требуемую сумму
    меньше уже вложенной.
    """
    # meeting_room = await check_meeting_room_exists(
    #     meeting_room_id, session
    # )

    # if obj_in.name is not None:
    #     await check_name_duplicate(obj_in.name, session)

    # # Замените вызов функции на вызов метода.
    # meeting_room = await meeting_room_crud.update(
    #     meeting_room, obj_in, session
    # )
    # return meeting_room
    return {'charity_project': 'charity_project ОБНОВЛЕН'}


@router.delete(
    '/{project_id}',
    response_model=CharityProjectDB,
    # response_model_exclude_none=True,
    # # Новая зависимость.
    dependencies=[Depends(current_superuser)],
)
async def delete_charity_project(
        project_id: int,
        # session: AsyncSession = Depends(get_async_session),
):
    """
    Только для суперюзеров.

    Удаляет проект. Нельзя удалить проект, в который уже были инвестированы
    средства, его можно только закрыть.
    """
    # meeting_room = await check_meeting_room_exists(meeting_room_id, session)
    # # Замените вызов функции на вызов метода.
    # meeting_room = await meeting_room_crud.remove(meeting_room, session)
    return {'charity_project': 'charity_project УДАЛЕН'}
