from database.database_funcs.misc.wrapper import database_connector

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert as pg_insert
from database.models import Weather
from sqlalchemy.ext.asyncio import AsyncSession

from serializers.database_filters import GetWeatherFilters, WeatherToAdd

__all__ = [
    'get_weather',
    'insert_weather'
]


@database_connector
async def get_weather(
        session: AsyncSession,
        filters: GetWeatherFilters
) -> list[Weather]:
    orm = select(
        Weather
    )

    if filters.limit:
        orm = orm.limit(
            limit=filters.limit
        )

    res = await session.execute(orm)
    return res.scalars()


@database_connector
async def insert_weather(
        session: AsyncSession,
        weather: WeatherToAdd
) -> Weather or None:
    orm = (pg_insert(
        Weather
    ).values(
        **weather.__dict__
    ).on_conflict_do_update(
            index_elements=['datetime'],
            set_=weather.__dict__
    ).returning(
        Weather
    ))
    res = await session.execute(orm)
    return res.scalar_one_or_none()
