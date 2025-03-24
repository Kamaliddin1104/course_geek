# ООП, особенности Python

print('Повторение пройденного\n')
class User: # Повторение пройденного
    def __init__(self, *, name: str, equipment: list = None):
        self.name = name
        self.equipment = equipment if equipment is not None else []
        self.life = 3
        # принтим только в учебных целях, а не для реальных задач
        print(f'Создал {self} со свойствами: \n'
              f'{self.name = }, {self.equipment}, {self.life = }')



print('Создаём первый раз')
q1 = User(name='tundra')
print('Создаём второй раз')
q2 = User(name='Kolotun', equipment=['холодно-пиздец', 'хочется-греться'])
print("Создаём третий раз")
q3 = User(name='Kolotumba', equipment=['ошалеть-как-холодно', 'хочется-ебаться'])
print('--------------------------')



# Магический метод __new__ Нужен, чтобы контролировать создание экземпляра класса
print('User2, дандер-метод - __new__\n')
class User2:
    def __init__(self, *, name):
        self.name = name
        print(f'Создал {self.name}')

    def __new__(cls, *args, **kwargs): # __new__ нужен для контроля создания экземпляров класса
        instance = super().__new__(cls)
        print(f'Создал класс {cls}')
        return instance


print('Cоздаём первый раз')
w1 = User2(name='Shelly')
print('Cоздаём второй раз')
w2 = User2(name='Bruh')
print('--------------')




print('UserInt(int)\n')
class NamedInt(int):
    def __new__(cls, value, name: str):
        instance = super().__new__(cls, value)
        instance.name = name
        print(f'Создал класс {cls}')
        return instance



e1 = NamedInt(42, 'Сорок-Два')
e2 = NamedInt(300, 'От#### у тракториста')
e3 = NamedInt(777, 'Красивое число')

print(e1.name)
print('---------------')




print('Singleton, одиночный экземпляр\n')
class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name):
        self.name = name



a = Singleton(name='Kamal')
b = Singleton(name='Restley')

print(a.name, b.name)
print(a is b)
print(id(a), id(b))
print('---------------')



# Магический метод __del__ # Удаляет объекты
# import sys
#
# print('User3, __del__\n')
# class User3:
#     def __init__(self, name: str):
#         self.name = name
#         print(f'Создали {self.name}')
#
#     def __del__(self):
#         print(f'Удаление экземпляра {self.name}')
#
#
#
# user = User3(name='Kamal')
# print(f"{sys.getrefcount(user) = }") # Выводятся ссылки на экземпляр
# user2 = user
# print(f"{sys.getrefcount(user) = }, {sys.getrefcount(user2) = }") # Здесь счётчик увеличился, из-за новой переменной которая ссылается на тот же объект
# del user # Удаляем переменную user и его ссылку
# print(f"{sys.getrefcount(user2) = }")
# print('Завершение работы')




# Игра что вернёт код?
print('Count, Что вернёт код?\n')

class Count:
    _count = 0
    _last = None
    def __new__(cls, *args, **kwargs):
        if cls._count < 2:
            cls._last = super().__new__(cls)
            cls._count += 1
        return cls._last

    def __init__(self, name: str):
        self.name = name


ekz1 = Count(name='Kamal')
ekz2 = Count(name='Two_ekz')
ekz3 = Count(name='Three_ekz')
ekz4 = Count(name='fourthekz')
print(ekz2.name)
print('--------------')



print('User4, Строка документации\n')
class User4:
    """Документация класса"""
    def __init__(self, string: str):
        """Документация __init__ внутри класса"""
        self.string = string

    def simple_func(self):
        """Документация метода внутри класса"""
        return self.string.capitalize()


# Два способа просмотра осмотра документации
r1 = User4(string='Hello, world!')
help(r1) # Большая информация об объекте класса
help(User4) # Большая информация о классе
print(User4.__doc__) # Вызывается только документация класса
print(r1.simple_func.__doc__) # Вызывается документация метода внутри класса
print('----------------------------')




# Магический метод __str__ нужен для улучшения читаемости объекта
print('User5, __str__\n')
class User5:
    def __init__(self, name: str):
        self.name = name

    def func(self):
        self.name.capitalize()


    def __str__(self):
        return f'Экземпляр класса с именем {self.name}'


t1 = User5(name='Kamaliddin')
print(t1) # Теперь выводится то что внутри __str__, а не <__main__.User5 object at 0x000002E0ED1494F0> 👍
print('--------------------')



# Магический метод __repr__ предназначен для разработчиков для формального вывода объекта
print('User6, __repr__\n')
class User6:
    def __init__(self, name: str, equipment: list = None):
        self.name = name
        self.equipment = equipment if equipment is not None else []
        self.life = 3

    def __repr__(self):
        return f'User({self.name}, {self.equipment})'




user = User6(name='Shelly', equipment=['Контузия'])
print(user)
print('------------')




print('User7, Как вызвать определенный метод __str__ или __repr__ если в коде присутствуют оба?')
class User7:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Имя: {self.name}, возраст: {self.age}'

    def __repr__(self):
        return f'User({self.name}, {self.age})'



y1 = User7(name='Kamal', age=16)
print(y1) # Выводится __str__
print(repr(y1)) # Выведется __repr__
print('---------------------')



# Математические операции в классах

# Скипаем т.к.не хочу ебать себе мозги, и врят ли я ими буду пользоваться


# Сравнение классов

# __eq__ - ==
# __ne__ - !=
# __gt__ - >
# __ge__ - <=
# __lt__ - <
# __le__ - >=
print('Triangle, сравнение классов\n')
class Triangle:
    def __init__(self, c, d, e):
        self.c = c
        self.d = d
        self.e = e

    def __str__(self):
        return f'Треугольник со сторонами {self.c}, {self.d}, {self.e}'

    def __eq__(self, other):
        first = sorted((self.c, self.d, self.e))
        second = sorted((other.a, other.b, other.e))
        return first == second


triangle = Triangle(23, 3, 3)
print(triangle)
print('----------------')



# Обработка аттрибутов
# __getattribute__
print('Triangle, __getattr__\n')
class Triangle:
    def __init__(self, c, d, e):
        self.c = c
        self.d = d
        self.e = e

    def __str__(self):
        return f'Треугольник со сторонами: {self.c}, {self.d}, {self.e}'

    def __getattribute__(self, item):
        if item == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__getattribute__(self, item)



triangle = Triangle(2, 12, 2)
# print(triangle.z) # AttributeError(item)
print(triangle.e)
print('---------------')



# __setattr__ Блокирует создание аттрибута и присваивание к нему значения
print('Triangle2, __getattr__\n')
class Triangle2:
    def __init__(self, c, d, e):
        self.c = c
        self.d = d
        self.e = e

    def __str__(self):
        return f'Треугольник со сторонами: {self.c}, {self.d}, {self.e}'

    def __getattribute__(self, item):
        if item == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__getattribute__(self, item)


triangle2 = Triangle2(12, 2, 21)
triangle2.x = 3 # Аттрибут добавляется без проблем
triangle2.z = 3 # __setattr__ блокирует создание z
print('-------------------')



# __getattr__ - Обращение к несуществующему объекту приведет к None
print('Man, __getattr__\n')
class Man:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def __getattr__(self, item):
        return f'Нету такого аттрибута {item}'


man = Man(name='Alex', age=22, job='Porn-Actor')
print(man.a)
print('----------------')



# __delattr__ Контролирует удаление аттрибута из класса
print('Triangle3, __delattr__\n')
class Triangle3:
    def __init__(self, c, d, e):
        self.c = c
        self.d = d
        self.e = e

    def __str__(self):
        return f'Треугольник со сторонами: {self.c}, {self.d}, {self.e}'

    def __getattribute__(self, item):
        if item == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__getattribute__(self, item)

    def __delattr__(self, item):
        if item in ('c', 'd', 'e'):
            setattr(self, item, 0)
        else:
            object.__delattr__(self, item)

    def __repr__(self):
        return f'Triangle3 = triangle({self.c}, {self.d}, {self.e})'




triangle3 = Triangle3(2, 3, 4)
triangle3.x = 3
print(f"{triangle3 = }, {triangle3.x = }")
del triangle3.c # Значение обнуляется
print(f'{triangle3.c}')