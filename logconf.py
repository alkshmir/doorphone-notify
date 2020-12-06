from logging import getLogger, StreamHandler, Formatter, FileHandler
import logging

logger = getLogger("Logtest")

def log_init(FILENAME="./test.log"):
    logger.setLevel(logging.DEBUG)
    stream_handler = StreamHandler()
    stream_handler.setLevel(logging.DEBUG)

    handler_format = Formatter("%(asctime)s-%(levelname)s: %(message)s")
    stream_handler.setFormatter(handler_format)
    file_handler = FileHandler(FILENAME, 'a')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(handler_format)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
