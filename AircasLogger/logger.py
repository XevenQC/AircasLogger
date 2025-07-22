import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path


def setup_logger(
        logdir: str = None,
        logname: str = None,
        maxbytes: int = 0,
        backupcount: int = 0,
        debug: bool = False,
        name: str = None,
        formatter: logging.Formatter = None,
        terminator='\n'
) -> logging.Logger:
    # Set up the logger
    if name:
        logger = logging.getLogger(name)
    else:
        logger = logging.getLogger()

    level = logging.DEBUG if debug else logging.INFO
    logger.setLevel(level)

    logger.propagate = False

    # Create and configure the StreamHandler with the appropriate formatter and level
    if formatter is None:
        formatter = logging.Formatter(
            '%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s')

    if debug:
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        stream_handler.terminator = terminator
        stream_handler.setLevel(level)
        logger.addHandler(stream_handler)

    if logdir is not None:
        log_path = Path(logdir)
        log_path.mkdir(parents=True, exist_ok=True)
        handler = RotatingFileHandler(
            log_path / 'aircas.log' if logname is None else log_path / (logname + '.log'),
            maxBytes=maxbytes,
            backupCount=backupcount,
            encoding='utf-8'
        )
        handler.setFormatter(formatter)
        handler.terminator = terminator
        handler.setLevel(level)
        logger.addHandler(handler)

    return logger
