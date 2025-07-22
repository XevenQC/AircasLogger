from AircasLogger.logger import setup_logger


if __name__ == '__main__':
    logger = setup_logger(
        'tmp', 'demo', maxbytes=1024, backupcount=10, debug=True, terminator='')

    logger.info('This is a Demo!')
    logger.info('The second line!')
