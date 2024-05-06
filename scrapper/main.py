from scrapper.scrapper_class import Scrapper
from scrapper.validate_data import Data
from serializers.database_filters import WeatherToAdd
from database.funcs import insert_weather

from loguru import logger


async def append_data_to_database(valid_object_list: list[WeatherToAdd]) -> None:
    counter = 0
    obj_count = len(valid_object_list)

    for obj in valid_object_list:
        res = await insert_weather(
            weather=obj
        )
        if not res:
            logger.error(f"Weather not append!\n Weather data: {obj.__str__()}")
        counter += 1

    logger.info(f"{counter}/{obj_count} was added to database")
    return


async def scrapper_main():
    scrapper = Scrapper()
    logger.info("Starting scraper")
    weather_data = await scrapper.get_weather()
    logger.info("Data was successfully parsed")
    valid_object_list = await Data.validate(full_data=weather_data)
    logger.info("Data was successfully validate")
    await append_data_to_database(valid_object_list=valid_object_list)
    await scrapper.session.close()

if __name__ == "__main__":
    import asyncio

    asyncio.run(scrapper_main())
