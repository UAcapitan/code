import logging

logger = logging.getLogger(__name__)
print(logger)

def main(n):
    logger.debug('Working')
    n =+ 1
    return n

if __name__ == '__main__':
    main(0)