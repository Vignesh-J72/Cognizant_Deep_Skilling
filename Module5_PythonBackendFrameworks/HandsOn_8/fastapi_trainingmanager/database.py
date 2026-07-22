from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

ASYNC_DATABASE_URL = "sqlite+aiosqlite:///./fastapi_training.db"
engine = create_async_engine(ASYNC_DATABASE_URL, echo=True)

async_session = async_sessionmaker(
    bind=engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass

async def get_db():
    async with async_session() as session:
        yield session