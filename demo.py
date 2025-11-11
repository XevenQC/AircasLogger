from AircasLogger.logger import setup_logger


if __name__ == '__main__':
    logger = setup_logger(
        'tmp', maxbytes=1024, backupcount=10, debug=False)

    logger.debug("这是DEBUG级别的日志")
    logger.info("这是INFO级别的日志")
    logger.warning("这是WARNING级别的日志")
    logger.error("这是ERROR级别的日志")
    logger.critical("这是CRITICAL级别的日志")
