from datetime import datetime
from typing import Union
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.donation import Donation
from app.models.charity_project import CharityProject
from app.core.db import get_async_session





async def mark_fully_invested(obj, session):
    obj.fully_invested = True
    obj.close_date = datetime.now()


async def investment_process(
        obj_in: Union[CharityProject, Donation],
        session: AsyncSession = Depends(get_async_session)
) -> None:

    obj_db_model = CharityProject if isinstance(obj_in, Donation) else Donation

    objs_db = await session.execute(
        select(obj_db_model)
        .where(obj_db_model.fully_invested == 0)
        .order_by(obj_db_model.create_date.desc())
    )

    objs_db = objs_db.scalars().all()

    if not objs_db:
        return obj_in

    if isinstance(obj_in, Donation):
        for project in objs_db:
            need_money = project.full_amount - project.invested_amount
            to_invest = obj_in.full_amount - obj_in.invested_amount

            if obj_in.fully_invested:
                break

            if need_money > to_invest:
                project.invested_amount += to_invest
                obj_in.invested_amount = obj_in.full_amount
                await mark_fully_invested(obj_in, session)
                break

            elif need_money == to_invest:
                obj_in.invested_amount = obj_in.full_amount
                project.invested_amount = project.full_amount
                await mark_fully_invested(obj_in, session)
                await mark_fully_invested(project, session)
                break

            elif need_money < to_invest:
                obj_in.invested_amount += need_money
                project.invested_amount = project.full_amount
                await mark_fully_invested(project, session)


        await session.commit()

    if isinstance(obj_in, CharityProject):

        for donate in objs_db:
            to_invest = donate.full_amount - donate.invested_amount
            need_money = obj_in.full_amount - obj_in.invested_amount

            if need_money > to_invest:
                obj_in.invested_amount += to_invest
                donate.invested_amount = obj_in.full_amount
                await mark_fully_invested(donate, session)

            if need_money == to_invest:
                obj_in.invested_amount = obj_in.full_amount
                donate.invested_amount = donate.full_amount
                await mark_fully_invested(obj_in, session)
                await mark_fully_invested(donate, session)

            if need_money < to_invest:
                obj_in.invested_amount += need_money
                donate.invested_amount = donate.full_amount
                await mark_fully_invested(donate, session)

            if obj_in.fully_invested:
                return obj_in
        await session.commit()
    return obj_in
