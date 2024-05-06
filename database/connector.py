from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from core.config import settings

# Create async SQLAlchemy engine
DATABASE_URL = f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@" + \
               f"{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"

async_engine = create_async_engine(DATABASE_URL, echo=True)

# Create session maker
async_session = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)

# Init base model class
Base = declarative_base()


async def get_session() -> AsyncSession:
    """
    Function create and return Sqlalchemy session.
    :return: Sqlalchemy async session.
    """
    async with async_session() as session:
        return session
