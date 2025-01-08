import argparse

# Модуль argparse


# parser = argparse.ArgumentParser(description='My first arg parser')
# parser.add_argument('numbers', metavar='N', type=float, nargs='*', help='press some numbers')
# args = parser.parse_args()
# print(f'В скрипт передано {args}')


# Metavar - имя, которое выводится о справке.
# Type - тип, для преобразования аргумента.
# Nargs - указывает на количество значений, которые надо собрать из командной строки и собрать результат в список list.
# Help - вывод подсказки об аргументе.

r"""
Примеры запуска в терминале:
python .\module_argparse.py 42 3.14 73
python .\module_argparse.py --help
python .\module_argparse.py Hello world! # Error: Hello world! не является числом
"""



# Пример 2

# parser2 = argparse.ArgumentParser(prog='average',
#                                   description='My second arg parser',
#                                   epilog='returns the arithmetic mean')
#
# parser2.add_argument('numbers', metavar='N', type=float, nargs='*', help='press some numbers')
# arguments = parser2.parse_args()
# print(f'В скрипт передано {arguments}')

r"""
Примеры запуска в терминале:
python .\module_argparse.py --help
"""


# Выгружаем результаты parse_args

# parser = argparse.ArgumentParser(description='My first arg parser')
# parser.add_argument('numbers', metavar='N', type=float, nargs='*', help='press some numbers')
# args = parser.parse_args()
# print(f"Получили экземпляр Namespace: {args}")
# print(f'У Namespace работает точечная нотация: {args.numbers = }')
# print(f'Объекты внутри могут быть любыми: {args.numbers[1] = }')


r"""
Примеры запуска в терминале:
python .\module_argparse.py 42 3.14 73
"""


# Добавляем аргументы, add_argument

# def quadratic_equations(a, b, c):
#     d = b ** 2 - 4 * a * c
#     if d > 0:
#         return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
#     elif d == 0:
#         return -b / (2 * a)
#     return None
#
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='Solving quadratic equations')
#     parser.add_argument('-a', metavar='a', type=float,
#                         help='Enter a ax^2+bx+c=0', default=1)
#     parser.add_argument('-b', metavar='b', type=float,
#                         help='Enter b for ax^2+bx+c=0')
#     parser.add_argument('-c', metavar='c', type=float,
#                         help='Enter b for ax^2+bx+c=0')
#     args = parser.parse_args()
#     print(quadratic_equations(args.a, args.b, args.c))



# Параметр action

parser = argparse.ArgumentParser(description='Sample')
parser.add_argument('-x', action='store_const', const=42)
parser.add_argument('-y', action='store_true')
parser.add_argument('-z', action='append')
parser.add_argument('-i', action='append_const', const=int, dest='types')
parser.add_argument('-f', action='append_const', const=float, dest='types')
parser.add_argument('-s', action='append_const', const=str, dest='types')
args = parser.parse_args()
print(args)

r"""
Примеры запуска в терминале:
python .\module_argparse.py -h
python .\module_argparse.py -x -y -z 42 -z 73 -i -f -s
"""