# Декораторы
# Замыкания

import time, random
from typing import Callable

from django.contrib.auth.decorators import permission_required


def a_b(a: int) -> Callable[[int], int]:
    def add_two_str(b: int) -> int:
        return a + b

    return add_two_str

print(a_b(5)(5))



def first_str(a: str) -> Callable[[str], str]:
    def second_str(b: str):
        return f"{a} {b}"
    return second_str


hello = first_str('Hello,')
world = first_str('world!')

print(hello('world!'))
print(world('hello'))



def add_one_str(a: str) -> Callable[[str], str]:
    names = []

    def add_two_str(b: str) -> str:
        names.append(b)
        return a + ', ' + ', '.join(names)
    return add_two_str


hi = add_one_str('Hello!')
bye = add_one_str('GoodBye!')

print(hi('Alex'))
print(bye('Alice'))
print(hi('Kamaliddin'))



def add_first_str(a: str) -> Callable[[str], str]:
    text = ''

    def add_second_str(b: str) -> str:
        nonlocal text
        text += ', ' + b
        return a + text

    return add_second_str


halo = add_first_str('HI!')
goodbye = add_first_str('Bye!')

print(halo('Nafosat'))
print(goodbye('Abu'))
print(halo("I'm"))
print(goodbye('You'))


def mainer(xs: int) -> Callable[[int], dict[int, int]]:
    d = {}

    def loc(y: int) -> dict[int, int]:
        for a in range(y + 1):
            d[a] = xs ** a

        return d
    return loc


small = mainer(42)
big = mainer(73)

print(small(7))
print(big(7))
print(small(3))


# Создание декоратора
def decorator(func: Callable):
    def wrapper(*args, **kwargs):
        print(f"Запуск функции: {func.__name__} в {time.time()}")
        resulting = func(*args, **kwargs)
        print(f"Результат функции: {func.__name__} в {resulting}")
        print(f"Завершение функции: {func.__name__} в {time.time()}")
        return resulting
    return wrapper


@decorator
def factorial(n: int) -> int:
    fact = 1
    for num in range(2, n + 1):
        fact *= num

    return fact

print(factorial(10))


# 3 декоратора
def deco_1(func: Callable):
    def wrapper_1(*args, **kwargs):
        print('Старт декоратора 1')
        print(f'Запуск {func.__name__}')
        resulting = func(*args, **kwargs)
        print('завершение декоратора 1')
        return resulting
    print('Возврат декоратора 1')
    return wrapper_1


def deco_2(func: Callable):
    def wrapper_2(*args, **kwargs):
        print('Старт декоратора 2')
        print(f'Запуск {func.__name__}')
        resulting = func(*args, **kwargs)
        print('завершение декоратора 2')
        return resulting

    print('Возврат декоратора 2')
    return wrapper_2


def deco_3(func: Callable):
    def wrapper_3(*args, **kwargs):
        print('Запуск 3 - декоратора')
        print('Запуск 3 - декоратора')
        resulting = func(*args, **kwargs)
        print('завершение 3 - декоратора')
        return resulting

    print('Возврат 3 - декоратора')
    return wrapper_3



@deco_3
@deco_2
@deco_1
def main():
    print('Старт основной функции')


if __name__ == '__main__':
    print('main запуск')
    main()




def new_deco(func: Callable):
    _cache_dict = {}
    def wrapper(*args):
        if args not in _cache_dict:
            _cache_dict[args] = func(*args)
        return _cache_dict[args]
    return wrapper


@new_deco
def rnd(a: int, b: int) -> int:
    return random.randint(a, b)


print(rnd(1, 10))
print(rnd(1, 10))





# Декоратор с параметрами
def count(n: int = 1):
    def deco(func: Callable):
        def wrapper(*args, **kwargs):
            time_count = []
            result = None
            for _ in range(n):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                stop = time.perf_counter()
                time_count.append(stop - start)
            print(f"Результаты замеров: {time_count}")
            return result

        return wrapper

    return deco


@count(5)
def factorial(n: int):
    result = 1
    for i in range(2, n + 1):
        result *= i

    return result

print(factorial(10))
print(factorial(100))


# 2
def count(num: int = 1):
    def deco(func: Callable):
        randoms = []
        def wrapper(*args, **kwargs):
            for _ in range(num):
                result = func(*args, **kwargs)
                if result not in randoms:
                    randoms.append(result)

            return randoms

        return wrapper
    return deco



@count(5)
def rnd(a: int, b: int) -> int:
    return random.randint(a, b)


print(rnd(1, 10))
print(rnd(1, 100))
print(rnd(1, 1000))




# Декоратор wraps
from functools import wraps

def count(n: int = 1):
    def deco(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time_count = []
            result = None
            for _ in range(n):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                stop = time.perf_counter()
                time_count.append(stop - start)
            print(f"Результаты замеров: {time_count}")
            return result

        return wrapper

    return deco


@count(5)
def factorial(n: int):
    """Возвращает факториал числа n"""
    result = 1
    for i in range(2, n + 1):
        result *= i

    return result

print(factorial.__name__) # wraps нужен для того чтобы когда мы
print(help(factorial))    # вызывали функцию с __name__ или с функцией help,
                          # отображалось имя функции и документация
                          # функции, а не обернутой функции wrapper



# Декоратор cache - Сохраняет результаты прошлых вызовов функции
from functools import cache

@cache
def nod(a: int) -> int:
    print(f"Вычисляю факториал для {a}")
    result = 1
    for i in range(2, a + 1):
        result *= i

    return result

print(nod(1))
print(nod(10))
print(nod(1))