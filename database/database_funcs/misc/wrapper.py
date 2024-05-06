from asyncio import iscoroutinefunction
from database.connector import get_session
import datetime
from loguru import logger


def database_connector(func):
    # Get session before function
    # commit + close session after function.
    async def wrapper(*args, **kwargs):
        if not iscoroutinefunction(func):
            # if function not async.
            raise ValueError("Decorator must be used for async functions!")

        session = None
        # try to complete database function
        try:
            start_time = datetime.datetime.now()
            session = await get_session()
            func_ = await func(session=session, *args, **kwargs)

            await session.commit()
            await session.close()

            end_time = datetime.datetime.now()

            logger.debug(f'Func: {func.__name__}, Database Request Time: {end_time-start_time}')
            return func_
        except Exception as e:
            # if session to be created, but func finished with error.
            if session:
                await session.rollback()
                await session.commit()
                await session.close()

            logger.critical(f'Func: {func.__name__}, Database Request Error! Message: {e}')
            return False

    return wrapper
