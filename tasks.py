# Здесь собраны все задачи на языке Python
# Которые я решал за всё обучение

import copy
import time


# Обновление словаря
def is_update_dict(old_dict, **kwargs) -> tuple[dict, bool]:
    is_update = False
    copy_dict = copy.deepcopy(old_dict)
    for key, value in kwargs.items():
        old_dict[key] = value
    if old_dict != copy_dict:
        is_update = True

    return old_dict, is_update


print(is_update_dict({'name': 'Kamal', 'age': 17}, job='Py3 developer'))




# 2 - Нахождение студентов с проходным баллом

students = [
    {'name': 'Kamaliddin', 'age': 17, 'marks': [8, 8, 7, 9, 8]},
    {'name': 'Abdusamad', 'age': 16, 'marks': [8, 7, 8, 8, 8]},
    {'name': 'Madina', 'age': 16, 'marks': [7, 7, 7, 7, 7]},
    {'name': 'Ali', 'age': 17, 'marks': [10, 10 ,10, 9, 10]},
    {'name': 'Unknown', 'age': 11, 'marks': None}
]


def best_students(list_students: list[dict]) -> list[dict]:
    passing_score = 8
    bests = []
    for student in list_students:
        marks = student['marks']
        if marks is None:
            continue
        else:
            average_marks = sum(marks) / len(marks)
            if average_marks >= passing_score:
                bests.append(student)

    return bests



print(best_students(students))



# Однострочные элегантные решения задач
# 3 - сумма нечетных чисел списка

def sum_if_nums_2(iterable):
    return sum(i for i in iterable if i % 2 != 0)


print(sum_if_nums_2([5, 7, 2])) # 12



# 4 - Выводит сколько слов в тексте

def words_in_string(string: str) -> int:
    return len(string.split())


print(words_in_string('Hello my bro!'))



# 5 - Проверяет палиндром ли строка

def is_palindrome(word):
    return word.lower() == word[::-1].lower()


print(is_palindrome('aziza'))



# 6 - Выводит квадраты чисел с до введенного числа

def square_of_nums(finish: int) -> list[int]:
    return [i ** 2 for i in range(1, finish + 1)]


print(square_of_nums(12))



# 7 - Декоратор, измеряющий время выполнения функции

def time_finish_func(func):
    def wrapper(*args, **kwargs):
        begin = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        print(f"{finish - begin:.6f}")
        return result
    return wrapper



# 8 - Выводит максимальную разницу между числами в списке

@time_finish_func
def max_diff(iterable_nums) -> int:
    return max(abs(iterable_nums[i] - iterable_nums[i + 1]) for i in range(len(iterable_nums) - 1))



print(max_diff([1, 3, 8, 2, 10]))














