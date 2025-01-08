"""
Задача-1 : Сделать декоратор, который говорит при каждом вызове
           обернутой функции декоратора сколько раз она вызвалась
"""
from functools import wraps
from typing import Callable
import time

# Задачи - которые дал GPT

# 1
def log_decorator(func: Callable):
    def wrapper(*args, **kwargs):
        print("Начинаем выполнение функции...")
        result = func(*args, **kwargs)
        print("Функция выполнена.")
        return result
    return wrapper


@log_decorator
def greet(name):
    print(f"Привет, {name}!")

greet("Камолиддин")


# 2
def repeat_decorator(func: Callable):
    """2 раза вызывает функцию"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result2 = func(*args, **kwargs)
        return f"{result}\n{result2}"
    return wrapper


@repeat_decorator
def say_hello():
    print("Привет!")

say_hello()


# 3
def time_decorator(func: Callable):
    """Декоратор возвращает за сколько выполняется функция"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        finish = time.perf_counter()
        result_time = finish - start
        print(f"{func.__name__} выполняется за {result_time}")
        return result

    return wrapper




@time_decorator
def slow_function():
    """Медленная функция"""
    time.sleep(1)
    print("Функция завершена.")


slow_function()



# 4 - Преобразование результата функции в строку
def to_string(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return str(result)
    return wrapper


@to_string
def add(a, b):
    return a + b


result = add(3, 5)



# 5
def positive_args(func: Callable):
    def wrapper(*args, **kwargs):
        if any(x < 0 for x in args if isinstance(x, (int, float))):
            return 'Ошибка: все аргументы должны быть положительными!'
        elif any(value < 0 for value in kwargs.values() if isinstance(value, (int, float))):
            return 'Ошибка: все аргументы должны быть положительными!'
        return func(*args, **kwargs)
    return wrapper



@positive_args
def multiply(a, b):
    return a * b

print(multiply(3, 5))   # 15
print(multiply(-3, 5))  # Ошибка: все аргументы должны быть положительными!
print(multiply(3, -5))  # Ошибка: все аргументы должны быть положительными!
print(multiply(a=3, b=5))  # 15
print(multiply(a=3, b=-5)) # Ошибка: все аргументы должны быть положительными!









