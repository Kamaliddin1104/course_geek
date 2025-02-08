def test():
    for i in range(3):
        yield i # yield - возвращает итератор, по которому нужно итерироваться
                # c next или циклом for.

a = test()
# Итерация с next()
print(next(a))
print(next(a))
print(next(a))
# print(next(a)) # StopIteration!

# Итерация с циклом
for i in a:
    print(i)



def start():
    yield from [8, 5, 6, 3, 0]


o = start()
print(next(o))
print(next(o))
print(next(o))
print(next(o))
print(next(o))
# print(next(o)) STOP ITERATION!



def test():
    yield from (x for x in range(20))

res = test()

for i in res:
    print(i)


# Бесконечная генерация
def infinite_generator():
    print('Запуск')
    while True:
        yield 1
        yield 2

res = infinite_generator()
# for i in res:
#     print(i) Бесконечная генерация
print(infinite_generator().__sizeof__())

print(next(res)) # 1
print(next(res)) # 2
print(next(res)) # 1



big_number = range(999999)
evens = (n for n in big_number if n % 2 == 0) # Это тоже генератор
                                              #