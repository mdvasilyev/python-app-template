import uvicorn
from fastapi import FastAPI
from loguru import logger

from .core import GlobalConfig, get_config, setup_logger


def main():
    setup_logger()

    logger.debug("Getting config.")
    config: GlobalConfig = get_config()

    app: FastAPI = FastAPI(
        debug=config.app.debug,
        title=config.app.name,
    )

    logger.debug("Running application.")
    uvicorn.run(app, host=config.app.host, port=config.app.port)


if __name__ == "__main__":
    main()
