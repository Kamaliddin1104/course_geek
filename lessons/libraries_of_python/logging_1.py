# Стандартная библиотека Python

# Модуль Logging (логирование или журналистика)
# Дает информацию как работает код при его запуске и работе
import logging

logging.info('Немного информации')
logging.error('Подловили ошибку')

# Уровни логирования:
# 1. NOTSET, 0 - Уровень не установлен. Регистрируются все события.
# 2. DEBUG, 10 - подробная информация, обычно представляющая интерес только при диагностике проблем.
# 3. INFO, 20 - подтверждение того, что все работает, так как ожидалось.
# 4. WARNING, 30 - предупреждение, что произошло что-то неожиданное, или указание на проблему
#    в ближайшем будущем (нехватка памяти) программа по-прежнему работает так, как ожидалось.
# 5. ERROR, 40 - из-за более серьезной проблемы программа не может выполнять некоторые функции.
# 6. CRITICAL, 50 - серьезная ошибка, указывающая на то, что сама программа не может продолжать работу


logging.basicConfig(level=logging.NOTSET) # Указываем уровень логирования - NOTSET (логирование всех событий)
logging.debug('Подробная отладочная информация. Заменяем множество принтов')
logging.info('Немного информации о работе кода')
logging.warning('Внимание надвигается буря!')
logging.error('Поймали ошибку. Дальше только неизвестность')
logging.critical('Приехали\n')


# В документации logging написано
# Что напрямую обращаться к функциям модуля logging - не лучший вариант как наверху
# А хороший стиль это воспользоваться функцией getLogger('имя файла'):


logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)

logger.debug('Подробная отладочная информация. Заменяем множество принтов')
logger.info('Немного информации о работе кода')
logger.warning('Внимание надвигается буря!')
logger.error('Поймали ошибку. Дальше только неизвестность')
logger.critical('Приехали\n')