import datetime
from typing import List, Optional
from sqlalchemy import func
from sqlalchemy.future import select

import sqlalchemy.orm

from data import db_session
from data.package import Package
from data.release import Release


async def package_count() -> int:
    async with db_session.create_async_session() as session:
        query = select(func.count(Package.id))
        result = await session.execute(query)
        return result.scalar()


async def release_count() -> int:
    async with db_session.create_async_session() as session:
        query = select(func.count(Release.id))
        result = await session.execute(query)
        return result.scalar()


async def last_packages(limit) -> List[Package]:
    async with db_session.create_async_session() as session:
        query = select(Release) \
            .options(
            sqlalchemy.orm.joinedload(Release.package)
        ).order_by(Release.created_date.desc()) \
            .limit(limit)
        results = await session.execute(query)
        releases = results.scalars()
    return list({r.package for r in releases})


async def get_package_by_id(package_name: str) -> Package:
    async with db_session.create_async_session() as session:
        query = select(Package).filter(Package.id == package_name)
        result = await session.execute(query)
        return result.scalar_one_or_none()


async def get_latest_release_for_package(package_name: str) -> Optional[Release]:
    async with db_session.create_async_session() as session:
        query = select(Release).filter(Release.package_id == package_name).order_by(Release.created_date.desc())
        results = await session.execute(query)
        release = results.scalar()
        return release
