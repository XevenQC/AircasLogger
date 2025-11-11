import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path


def setup_logger(
        logdir: str = None,
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

    level = logging.DEBUG
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

        level_file_map = {
            logging.DEBUG: log_path / "debug.log",
            logging.INFO: log_path / "info.log",
            logging.WARNING: log_path / "warning.log",
            logging.ERROR: log_path / "error.log",
            logging.CRITICAL: log_path / "critical.log"
        }

        for level, file_path in level_file_map.items():
            handler = RotatingFileHandler(
                file_path,
                maxBytes=maxbytes,
                backupCount=backupcount,
                encoding='utf-8'
            )
            handler.setFormatter(formatter)
            handler.terminator = terminator

            # 添加过滤器：仅允许当前级别（level）的日志通过
            def make_filter(target_level):
                # 闭包函数，捕获当前级别的目标值
                def filter_func(record):
                    return record.levelno == target_level  # 仅匹配目标级别

                return filter_func

            handler.addFilter(make_filter(level))  # 绑定过滤器
            handler.setLevel(level)
            logger.addHandler(handler)

    return logger
