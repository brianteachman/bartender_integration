import logging
import os

FORMATTER = logging.Formatter('%(asctime)s: %(name)s - %(levelname)s - %(message)s')


def get_logger(name, log_file, debug=False):
    handler = logging.FileHandler(log_file)
    handler.setFormatter(FORMATTER)
    log = logging.getLogger(name)
    log.setLevel(logging.INFO if debug else logging.WARNING)
    log.addHandler(handler)
    return log


if __name__ == '__main__':
    BASEPATH = os.path.abspath(os.path.dirname(__file__))
    LOG_FILE = os.path.join(BASEPATH, 'data/service.log')
    log = get_logger("Test", log_file=LOG_FILE, debug=True)
    log.info("Test log message.")
