from apscheduler.schedulers.asyncio import AsyncIOScheduler
from scrapper.main import scrapper_main
from core.config import settings
from loguru import logger

# создаём объект для запуска задач в определенное время
scheduler = AsyncIOScheduler()


async def setup_task():
    # добавляяем задачу с уведомлениями
    scheduler.add_job(scrapper_main, "interval", seconds=settings.SCRAPPER_INTERVAL, name='scrapper')

    logger.info("Starting scheduler")
    # запускаем откладчик задач
    scheduler.start()


if __name__ == "__main__":
    import asyncio
    # Создаём eventloop
    event_loop = asyncio.new_event_loop()
    # Добавляем задачи Scheduler
    event_loop.create_task(setup_task())
    # Запускаем бесконечную работу event loop
    event_loop.run_forever()
