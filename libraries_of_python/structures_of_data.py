from collections import namedtuple
from _datetime import datetime
import time

# Структуры данных
# namedtuple - Именованный кортеж

User = namedtuple('User', ['firstname', 'lastname', 'birthday'])
u1 = User('Исаак', 'Ньютон', datetime(1643, 1, 3))
print(u1)
print(f"{type(u1) = }", f"{type(User) = }")

print(u1.firstname, u1.lastname) # Точечная нотация
print(u1.birthday.day)
print()

# Пример 2, defaults

SECONDS = 2
User2 = namedtuple('User', ['firstname', 'lastname', 'birthday'], defaults=['Иванов', datetime.now()])
u2 = User2(firstname='Исаак')
print(f"{u2.lastname}, {u2.birthday.strftime('%H:%M:%S')}")
print(f'Пауза в {SECONDS} секунды')
time.sleep(SECONDS)
u3 = User2('Галилео', 'Галилей')
print(f"{u3.lastname}, {u3.birthday.strftime('%H:%M:%S')}") # Подводный камень: Время осталось таким же как в прошлом u2
print()
# Примечания: лучше в defaults не передавать функции!


# Пример 3

Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
a = Point(2, 3, 4)
b = a._replace(z=0, x=a.x + 4)
print(a)
print(b)
print()



# Модуль array - массив, экономичен к памяти чем list,
# хранит числа, есть несколько параметров ('l', B) и т.д.
# Они отвечают за какой объем информации мы будем записывать
from array import array, typecodes

byte_array = array('B', (1, 2, 3, 255)) # целое число без знака 1 байт
print(byte_array)
print(typecodes)
print()


# Пример 2
long_array = array('l', [-6000, 800, 100500]) # l - числа со знаком 4 байт
long_array.append(42)
print(long_array)
print(long_array[2])
print(long_array.pop())
print()



# Пример 3
long_array = array('l', [-6000, 800, 100500])
# long_array.append(2 ** 32) # OverflowError - число превышает 4 байта
# long_array.append(3.12) # TypeError, 'l' - мы в массив помещаем только числа
print(long_array)
print()



# Что вернет код?
Data = namedtuple('Data', ['mathematics', 'chemistry',
                           'physics', 'genetics'], defaults=[5, 5, 5, 5])


d = {
    'Ivanov': Data(4, 5, 3, 5),
    'Petrov': Data(physics=4, genetics=3),
    'Sidorov': Data()
}

print(d)














