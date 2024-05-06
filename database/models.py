from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import datetime
from sqlalchemy.dialects.postgresql import VARCHAR, TIMESTAMP, FLOAT
from sqlalchemy.ext.asyncio import AsyncAttrs

__all__ = [
    'Weather',
]


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Weather(Base):
    __tablename__ = "weather"

    id: Mapped[int] = mapped_column(primary_key=True)
    temperature: Mapped[float] = mapped_column(FLOAT(), nullable=False)
    wind_speed: Mapped[float] = mapped_column(FLOAT(), nullable=False)
    wind_direction: Mapped[float] = mapped_column(FLOAT(), nullable=False)
    air_pressure: Mapped[float] = mapped_column(FLOAT(), nullable=False)
    precipitation_type: Mapped[str] = mapped_column(VARCHAR(32), nullable=False)
    precipitation_count: Mapped[float] = mapped_column(FLOAT(), nullable=False)
    datetime: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=False),
        default=datetime.datetime.now(),
        nullable=False,
        unique=True
    )

    def __str__(self) -> str:
        return f"{self.datetime}:  {self.temperature}"
