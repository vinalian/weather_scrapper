from aiohttp import ClientSession

from core.config import settings

from loguru import logger


class Scrapper:
    def __init__(self):
        self.session: ClientSession = ClientSession()
        self.__url: str = "https://api.open-meteo.com/v1/forecast"

    @property
    def params(self) -> dict:
        params = {
            "latitude": settings.SCRAPPER_LATITUDE,
            "longitude": settings.SCRAPPER_LONGITUDE,
            "hourly": ["temperature_2m", "precipitation", "rain", "snowfall", "pressure_msl",
                       "wind_speed_10m", "wind_direction_10m"],
            "timezone": "Europe/Moscow",
            "forecast_days": 1
        }
        return params

    async def get_weather(self) -> dict:
        async with self.session.get(
            url=self.__url,
            params=self.params
        ) as response:
            if response.status != 200:
                logger.error("Error getting weather. Status code: %s", response.status)
                return

            return await response.json()


async def test():
    sc = Scrapper()
    print(await sc.get_weather())
    await sc.session.close()

if __name__ == '__main__':
    import asyncio

    asyncio.run(test())
