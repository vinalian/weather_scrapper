from sys import stdout
from loguru import logger


async def setup_logger():
    # Remove basic console logging
    # logger.remove()

    # Add custom console logging
    logger.add(
        sink=stdout,
        format="{level} {time: DD.MM.YYYY - HH:mm:ss} File: {module} Funk: {function} Line: {line} Message: {message}",
        level="INFO"
    )

    # Add file logging
    logger.add(
        sink="logs/errors.log",
        backtrace=True,
        format="{level} {time: DD.MM.YYYY - HH:mm:ss} File: {module} Funk: {function} Line: {line} Message: {message}",
        diagnose=True,
        level="ERROR",
        rotation="2 week",
        compression="zip"
    )
