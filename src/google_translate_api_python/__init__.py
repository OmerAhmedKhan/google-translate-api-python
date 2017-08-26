# --- core python imports
import os
import logging
import logging.handlers as handlers
# --- core python imports

__name__ = 'googletranslateapi'  # pylint: disable=redefined-builtin


def _setup_logger(filename):
    """ Instantiates a rotating file logger. """
    format_ = '%(asctime)s:%(name)s:%(funcName)s:%(levelname)s:%(process)d:%(lineno)d - %(message)s'
    formatter = logging.Formatter(format_)

    max_log_size = 2 * 1024 * 1024  # 2 MB

    f_handler = handlers.RotatingFileHandler(filename=filename, maxBytes=max_log_size, backupCount=5)
    f_handler.setFormatter(formatter)

    c_handler = logging.StreamHandler()
    c_handler.setFormatter(formatter)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    logger.addHandler(f_handler)
    logger.addHandler(c_handler)

    return logger

# --- globals, logging setup
# get log file from environment variable, else use a default one.
LOG_TO = '/var/log/google_translate_api.log'
LOGGER = _setup_logger(filename=LOG_TO)
# --- globals, logging setup
# --- script entry points
from .cli import google_translate_api_cli
from .translate import translate
# --- script entry points

# pylint 10.00/10.00