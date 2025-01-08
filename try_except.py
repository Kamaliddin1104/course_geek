# Исключения


# from random import randint
#
#
#
# def get(text: str = None) -> int:
#     data = input(text)
#     try:
#         num = int(data)
#     except ValueError as e:
#         print(f'Ваш ввод привел в ошибке: {e}')
#         num = 1
#         print('Будем считать что вы ввели "1"')
#     return num
#
#
# if __name__ == '__main__':
#     number = get('Введите целый делитель: ')
#     print(f'100 / {number} = {100 / number}')
# print('--------------')
#
#
#
# print('Пример 2\n')
# def get2(text: str = None) -> int:
#     while True:
#         try:
#             num = int(input(text))
#             break
#         except ValueError as e:
#             print(f'Ваш ввод привел к ошибке: {e}\n'
#                   f'Попробуйте снова!')
#     return num
#
#
# if __name__ == '__main__':
#     number = get2('Введите целый делитель: ')
#     print(f'100 / {number} = {100 / number}')
#
# print('--------------------')
#
#
#
#
# # 3
# print('Пример 3\n')
# MAX_COUNT = 5
#
# def get_data():
#     """Получает данные из внешнего источника"""
#     if result := randint(0, 3): # Этот синтаксис присваивает к result - randint(0, 3)
#         return result
#     else:
#         raise ConnectionError
#
#
# count = 0
# while count < MAX_COUNT:
#     count += 1
#     try:
#         data = get_data()
#         break
#     except ConnectionError as e:
#         print(f'Попытка {count} из {MAX_COUNT} завершилась ошибкой {e}')
#
#
# print(data) # noqa
# print('----------------')
#
#
#
# # 4
# print('Пример 4\n')
# def div_hundred_num(string: str = None) -> tuple[int, float]:
#     while True:
#         try:
#             num = int(input(string))
#             div = 100 / num
#             break
#         except ValueError as e:
#             print(f'Ваш ввод привел к ошибке {e}')
#         except ZeroDivisionError:
#             div = float('inf')
#             break
#     return num, div
#
#
#
# if __name__ == '__main__':
#     num, div = div_hundred_num('Введите целый делитель: ')
#     print(f'Результат операции {num} : {div}')
# print('----------------')
#
#
#
#
# # Блок else в try except
# # 5
# print('Else в try except\n')
# MAX_COUNT2 = 5
# result = None
#
# for count in range(1, MAX_COUNT2 + 1):
#     try:
#         user = int(input('Введите число: '))
#         print('Успешно получили целое число!')
#     except ValueError as e:
#         print(f'Попытка {count} из {MAX_COUNT2}, завершилась ошибкой {e}')
#     else:
#         result = 100 / user
#         break
#
#
# print(f"{result = }")
#
#
#
# # 6
# print('\n')
# MAX_COUNT3 = 5
# result2 = None
#
# for count in range(1, MAX_COUNT3 + 1):
#     try:
#         user = int(input('Введите число: '))
#         print('Успешно получили целое число!')
#     except ValueError as e:
#         print(f'Попытка {count} из {MAX_COUNT2}, завершилась ошибкой {e}')
#     else:
#         try:
#             result = 100 / user
#         except ZeroDivisionError as e:
#             result = float('inf')
#         break
#
#
# print(f"{result2 = }")
# print('----------------')
#
#
#
#
# # Команда finally (сработает в любом случае)
# print('Finally\n')
# def get_(string: str = None) -> int:
#     integer = None
#     try:
#         value = int(input(string))
#     except ValueError as x:
#         print(f'Ошибочный ввод: {x}')
#     finally:
#         return integer if isinstance(integer, int) else 1
#
#
# if __name__ == '__main__':
#     res = get_('Введите целый делитель: ')
#     try:
#         print(f'100 / {res} = {100 / res}')
#     except ZeroDivisionError:
#         print('На ноль делить нельзя уебан')
# print('----------------')



# Что вернёт код?
# print('Что вернёт код?\n')
# d = {'43': 73}
# try:
#     key, value  = input('Ключ и значение: ').split()
#     if d[key] == value:
#         r = 'Совпадение'
# except ValueError as e:
#     print(e)
# # except KeyError as e:
# #     print(e)
# # else:
# #     print(r) # Пытаемся распечатать не существующую переменную
# finally:
#     print(d)
#
# print('-------------------')



# 7 - Raise - вызывает ошибку, если нужно разработчику
# print('Raise\n')
# def add_key(dct, keys, values):
#     if keys in dct:
#         raise KeyError('Перезаписывание сущ. ключа запрещено!') # Вызывает ошибку
#     dct[keys] = values
#     return dct
#
#
# data = {'one': 1, 'two': 2}
# print(add_key(data, 'two', 3))
# print('----------------------')



# 8
print('User, пример с raise\n')
class User:
    def __init__(self, name, age):
        if 6 < len(name) < 30:
            self.name = name
        else:
            raise ValueError(f'Длина символов должна быть меньше 30 и больше 6: {name}: {len(name)}')
        if not isinstance(age, (int, float)):
            raise ValueError(f'Возраст должен быть числом! {age = }')
        elif age < 0:
            raise ValueError(f'Возраст должен быть положительным! {age = }')
        else:
            self.age = age


# user = User(name='Alex', age=12) # Длина имени меньше 6 ValueError
# user2 = User(name='Александ', age=-1) # Возраст не может быть меньше 0 ValueError
user3 = User(name='Владимир', age=34) # Здесь все нормально
print('--------------------')



# Что вернёт код?
print('Что вернёт код?\n')
def func(a, b, c):
    if a < b < c:
        raise ValueError('Не перемешано!')
    elif sum((a, b, c)) == 42:
        raise NameError('Имя занято!')
    elif max(a, b, c, key=len) < 5:
        raise MemoryError('Слишком глуп')
    else:
        raise RuntimeError('Что-то не так')


# func(11, 7, 3) # TypeError
# func(3, 2, 3) # TypeError
# func(73, -40, 9) # NameError
# func(10, 20, 30) # ValueError
print('--------------')



# Создание собственных исключений
# Исключения создаются через класс, класс наследуется через Exception!
# Рекомендуется создавать свои исключения в отдельном файле
print('Создание соб. исключений\n')

class UserException(Exception):
    pass


class UserAgeError(UserException):
    def __init__(self, value):
        self.value = value


    def __str__(self):
        return f'Возраст должен быть int либо float и больше 5: {self.value}'


class UserNameError(UserException):
    def __init__(self, name, lower, upper):
        self.name = name
        self.upper = upper
        self.lower = lower

    def __str__(self):
        text = 'Попадает в'
        if len(self.name) < self.lower:
            text = 'меньше нижней'
        elif len(self.name) > self.upper:
            text = 'Больше верхней'
        return (f'Имя пользователя {self.name} содержит {len(self.name)}'
                f'это {text} границы. Попадите в диапазон {self.lower} - {self.upper}')


# Это базовый минимум создания своих исключений

# Использование
class User2:
    MIN_LEN = 1
    MAX_LEN = 15
    def __init__(self, name, age):
        if self.MIN_LEN < len(name) < self.MAX_LEN:
            self.name = name
        else:
            raise UserNameError(name, self.MIN_LEN, self.MAX_LEN)
        if not isinstance(age, (int, float)) or age < 5:
            raise UserAgeError(age)
        else:
            self.age = age



u = User2(name='Kamaliddin', age=5) # UserAgeError
u2 = User2(name='ff', age=17) # UserNameError


