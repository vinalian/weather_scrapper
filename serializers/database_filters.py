from pydantic import BaseModel
from datetime import datetime


class GetWeatherFilters(BaseModel):
    limit: int = 10


class WeatherToAdd(BaseModel):
    temperature: float
    wind_speed: float
    wind_direction: float
    air_pressure: float
    precipitation_type: str
    precipitation_count: float
    datetime: datetime

    def __str__(self):
        return (f'{self.datetime}, '
                f'{self.temperature}, '
                f'{self.wind_speed}, '
                f'{self.wind_direction}, '
                f'{self.air_pressure}, '
                f'{self.precipitation_type}, '
                f'{self.precipitation_count}')


a = WeatherToAdd(
    temperature=1.2,
    wind_speed=1.2,
    wind_direction=1.2,
    air_pressure=1.2,
    precipitation_type='21',
    precipitation_count=1.2,
    datetime=datetime.now()
)
