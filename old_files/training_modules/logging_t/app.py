import logging
import os


logging.basicConfig(level=os.environ.get('LOGLEVEL', 'INFO'))

logger = logging.getLogger(__name__)
print(logger)

loger_handler = logging.StreamHandler()

def main(n):
    logger.debug('Working')
    n =+ 1
    return n


if __name__ == '__main__':
    main(0)