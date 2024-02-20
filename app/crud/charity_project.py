from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charityproject import CharityProject


# Создаем новый класс, унаследованный от CRUDBase.
class CRUDMeetingRoom(CRUDBase):

    # Преобразуем функцию в метод класса.
    async def get_room_id_by_name(
            # Дописываем параметр self.
            # В качестве альтернативы здесь можно
            # применить декоратор @staticmethod.
            self,
            room_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        db_room_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == room_name
            )
        )
        db_room_id = db_room_id.scalars().first()
        return db_room_id


# Объект crud наследуем уже не от CRUDBase,
# а от только что созданного класса CRUDMeetingRoom.
# Для инициализации передаем модель, как и в CRUDBase.
charity_project_crud = CRUDMeetingRoom(CharityProject)
