import logging


logger = logging.getLogger(__name__)

def log_all():
    logger.debug('Подробная отладочная информация. Заменяем множество принтов')
    logger.info('Немного информации о работе кода')
    logger.warning('Внимание надвигается буря!')
    logger.error('Поймали ошибку. Дальше только неизвестность')
    logger.critical('Приехали')


if __name__ == '__main__':
    log_all()