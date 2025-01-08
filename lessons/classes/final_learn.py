# Финальный урок ООП, __call__
from collections import defaultdict

# Вызов класса/экземпляра как функция
print('Number, callable()\n')
class Number:
    def __init__(self, num):
        self.num = num


n = Number(23)
print(f"{callable(Number) = }") # Проверка является ли объект-функции или нет
print(f'{callable(n) = }') # False Экземпляр
print('--------------------')



# Наглядный пример __call__
print('Storage, __call__\n')
class Storage:
    def __init__(self):
        self.storage = defaultdict(list)

    def __str__(self):
        txt = '\n'.join((f'{k}: {v}' for k, v in self.storage.items()))
        return f'Объекты хранилища по типам:\n{txt}'

    def __call__(self, value):
        self.storage[type(value)].append(value)
        return f'К типу {type(value)} добавлен {value}'


storage = Storage()
print(storage(42))
print(storage(72))
print(storage('Hello world!'))
print(storage(0))
print(storage)
print('-----------')




# Класс как функция, что вернёт код?
print('MyClass, Что вернёт функция?\n')
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def __repr__(self):
        return f'MyClass(a={self.a}, b={self.b})'

    def __call__(self, *args, **kwargs):
        self.a.append(args)
        self.b.update(kwargs)
        return True


x = MyClass([42], {73: True})
y = x(3.14, 100, 500, start=1)
x(y=y)
print(x) # [42, 3.14, 100, 500], {73: True, start: 1}









