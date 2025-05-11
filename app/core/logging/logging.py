from pathlib import Path

from loguru import logger

from app.core.config import LoggingConfig, get_config


def setup_logger() -> None:
    config: LoggingConfig = get_config().logging

    logger.remove()

    Path(config.log_file).parent.mkdir(parents=True, exist_ok=True)

    logger.add(
        config.log_file,
        level=config.level,
        rotation=config.rotation,
        retention=config.retention,
        compression=config.compression,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} - {message}",
        enqueue=True,
        backtrace=True,
        diagnose=True,
        mode="w",
    )

    logger.debug("Logging is set up.")
