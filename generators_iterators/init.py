"""
В будущем придётся работать с байтами.
Например: когда нужно работать с Mp3 jpeg или png
ибо когда нужно передавать информацию по сети нужно
конвертировать данные в байты и работать с ними
"""
eng_text, rus_text = 'Hello world!', 'Привет мир!'
rus_byte, eng_byte = rus_text.encode('utf-8'), eng_text.encode()
print(rus_byte, eng_byte)


# Поочерёдное записывание большой информации в файл с использованием
# генератора, чтобы не нагружать память
def copy_large_file(src, dest, chunk_size=1024):
    with open(src, "rb") as f_src, open(dest, "wb") as f_dest:
        for chunk in iter(lambda: f_src.read(chunk_size), b""):
            f_dest.write(chunk)

# Использование
copy_large_file("Скороговорка_лигурия.txt", "destination.txt")


# Задачи, которые дал GPT
# Бесконечный счетчик

def infinite_count(from_n: int):
    yield from_n
    while True:
        from_n += 1
        yield from_n


gen = infinite_count(10)

print(next(gen))  # 10
print(next(gen))  # 11
print(next(gen))  # 12


# Выдаёт только чётные числа начиная с N

def even_numbers(n: int):
    while True:
        n += 1
        if n % 2 == 0:
            yield n

gen = even_numbers(7)
print(next(gen))  # 8
print(next(gen))  # 10
print(next(gen))  # 12


# Бесконечное чередование элементов

def cycle(elements):
    while True:
        for i in elements:
            yield i


gen = cycle("abc")
print(next(gen))  # 'a'
print(next(gen))  # 'b'
print(next(gen))  # 'c'
print(next(gen))  # 'a'


# Фильтр на генераторах
def is_vowel(char):
    return char in "aeiou"


def filtered(func, predicate):
    for item in func:
        if predicate(item):
            yield item


gen = filtered(cycle("abcde"), is_vowel)
print(next(gen))  # 'a'
print(next(gen))  # 'e'


# Числа Фибоначчи

def fibo_nums():
    a1, a2 = 0, 1
    yield a1
    while True:
        a1, a2 = a2, a1 + a2
        yield a1


gen = fibo_nums()
print([next(gen) for _ in range(7)]) # [0, 1, 1, 2, 3, 5, 8]





















