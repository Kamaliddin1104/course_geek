import logging
from importing import log_all

# Подробнее о basicConfig
# Запись логов в файл

logging.basicConfig(level=logging.INFO, filename='logs.log', filemode='w', encoding='utf-8')
logger = logging.getLogger('Этот файл')
logger.warning('Начинаем вызывать функции из другого файла')
log_all()


# Форматирования
# Подробный вывод информации о работе кода
FORMAT = "{levelname:<8} - {asctime}. В модуле '{name}'" \
    "в строке {lineno:03d} функция '{funcName}()'" \
    "в {created} секунд записала сообщение: {msg}"

logging.basicConfig(format=FORMAT, style='{', level=logging.INFO)
logger = logging.getLogger('main')
logger.warning('Вызываем функция из др файла')
log_all()