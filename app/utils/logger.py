import logging
import logging.config

from app.utils.config import get_config

config = get_config()


logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(asctime)s %(levelname)s [%(filename)s %(lineno)s] %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
            "stream": "ext://sys.stderr",
        }
    },
    "loggers": {
        "console": {
            "level": config.log_level.value,
            "handlers": ["console"],
            "propagate": False,
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console"],
        "propagate": False,
    },
}

# logging.config.dictConfig(logging_config)
# logger = logging.getLogger("console")

logger = logging.getLogger("uvicorn")
logger.setLevel("DEBUG")

logger.debug("test log")
