from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
# # Вместо импортов 6 функций импортируйте объект meeting_room_crud.
from app.crud.charity_project import charity_project_crud
from app.core.user import current_superuser
# from app.models.meeting_room import MeetingRoom
# from app.schemas.meeting_room import (
#     MeetingRoomCreate, MeetingRoomDB, MeetingRoomUpdate
# )
from app.api.validators import check_name_duplicate, check_charity_project_exists, check_close_project
# from app.crud.reservation import reservation_crud
from app.schemas.charityproject import CharityProjectUpdate, CharityProjectDB, CharityProjectCreate


from app.service.investment import investment_process

router = APIRouter()


@router.post(
    '/',
    response_model=CharityProjectDB,
    # response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def create_charity_project(
        charity_project: CharityProjectCreate,
        session: AsyncSession = Depends(get_async_session),
):
    """
    Только для суперюзеров.

    Создаёт благотворительный проект.
    """
    await check_name_duplicate(charity_project.name, session)
    new_project = await charity_project_crud.create(charity_project, session)
    new_project = await investment_process(new_project, session)
    return new_project


@router.get(
    '/',
    response_model=list[CharityProjectDB],
    # response_model_exclude_none=True,
)
async def get_all_charity_projects(
        session: AsyncSession = Depends(get_async_session),
):
    """Возвращает список всех проектов."""
    all_rooms = await charity_project_crud.get_multi(session)
    return all_rooms


@router.patch(
    '/{project_id}',
    response_model=CharityProjectDB,
    # response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def update_charity_project(
        project_id: int,
        obj_in: CharityProjectUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    """
    Только для суперюзеров.

    Закрытый проект нельзя редактировать; нельзя установить требуемую сумму
    меньше уже вложенной.
    """
    charity_project = await check_charity_project_exists(
        project_id, session
    )

    if obj_in.name is not None:
        await check_name_duplicate(obj_in.name, session)
    
    check_close_project(charity_project)


    charity_project = await charity_project_crud.update(
        charity_project, obj_in, session
    )
    return charity_project


@router.delete(
    '/{project_id}',
    response_model=CharityProjectDB,
    # response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def delete_charity_project(
        project_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    """
    Только для суперюзеров.

    Удаляет проект. Нельзя удалить проект, в который уже были инвестированы
    средства, его можно только закрыть.
    """
    charity_project = await check_charity_project_exists(project_id, session)
    charity_project = await charity_project_crud.remove(charity_project, session)
    return charity_project
