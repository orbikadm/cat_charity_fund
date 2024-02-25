# from datetime import datetime

# from fastapi import Depends
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy import select

# from app.models.donation import Donation
# from app.models.charityproject import CharityProject
# from app.core.db import get_async_session





# def mark_fully_invested(obj, session):
#     obj.fully_invested = True
#     obj.close_date = datetime.now()


# async def investment_process(
#         donation: Donation,
#         project: CharityProject,
#         session: AsyncSession = Depends(get_async_session)
# ) -> None:

#     projects = await session.execute(
#         select(project)
#         .where(project.fully_invested == 0)
#         .order_by(project.create_date.desc())
#     )
#     projects: list[CharityProject] = projects.scalars().all()

#     while projects and donation.full_amount > donation.invested_amount:
#         actual_project = projects.pop()
#         money_in_donate = donation.full_amount - donation.invested_amount

#         need_money = actual_project.full_amount - actual_project.invested_amount

#         if need_money > money_in_donate:
#             donation.invested_amount = donation.full_amount
#             actual_project.invested_amount += donation.full_amount

#             if donation.invested_amount == 0:
#                 mark_fully_invested(donation)
#         else:
#             donation.invested_amount += need_money
#             mark_fully_invested(donation)







    # найти проекты
    # пока есть деньги в донате:
    #     берем неполный проект
    #     считаем недостающую сумму
    #     если недостающая сумма > доната:
    #         деньги с доната кладем в проект
    #         донат отмечаем fully_invested
    #         если сумма доната == нулю:
    #             отмечаем донат fully_invested
    #     иначе:
    #         инвестировано в донате увеличиваем на недостающую сумму
    #         отмечаем донат как fully_invested


# def investment_process(project):
#     найти донаты
#     пока есть деньги для проекта:
#         берем донат с деньгами
#         считаем недостающую сумму
#         если недостающая сумма > доната:
#             деньги с доната кладем в проект
#             донат отмечаем fully_invested
#             если сумма доната == нулю:
#                 отмечаем донат fully_invested
#         иначе:
#             сумму в донате уменьшаем на недостающую сумму
#             отмечаем донат как fully_invested





from datetime import datetime
from typing import Union

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.charity_project import CharityProject
from app.models.donation import Donation


def mark_as_invested(db_obj):
    db_obj.fully_invested = True
    db_obj.close_date = datetime.now()


async def investment_process(
    obj_in: Union[CharityProject, Donation], session: AsyncSession
):
    db_obj = CharityProject if isinstance(obj_in, Donation) else Donation

    db_objs = await session.execute(
        select(db_obj)
        .where(db_obj.fully_invested == 0)
        .order_by(db_obj.create_date.desc(), db_obj.id.desc())
    )
    db_objs = db_objs.scalars().all()

    while db_objs and obj_in.full_amount > obj_in.invested_amount:
        db_obj = db_objs.pop()

        needed_money = db_obj.full_amount - db_obj.invested_amount

        if obj_in.full_amount > needed_money:
            obj_in.invested_amount += needed_money
        else:
            obj_in.invested_amount = obj_in.full_amount
            mark_as_invested(obj_in)

            db_obj.invested_amount += obj_in.full_amount

            if db_obj.invested_amount == db_obj.full_amount:
                mark_as_invested(db_obj)

        session.add(db_obj)

    session.add(obj_in)
    await session.commit()
    await session.refresh(obj_in)
    return obj_in
