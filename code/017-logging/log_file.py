import logging

logger = logging.getLogger('file_logger')
logger.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler('new.log')
logger.addHandler(fileHandler)


logger.info("test... test...")