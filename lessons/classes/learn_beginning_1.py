# Классы
# Начало


print('Person\n')
class Person:
    max_xp = 500 # Атрибут класса или переменная



p1 = Person() # p1 - экземпляр класса Person

print(f"{p1.max_xp = }")
print(f"{Person.max_xp = }")
print('--------------------------')



print('Person2\n')
class Person2:
    max_up = 3


o1 = Person2()
o2 = Person2()
print(f"{Person2.max_up = }, {o1.max_up = }, {o2.max_up = }")


o1.max_up = 9
print(f"{Person2.max_up = }, {o1.max_up = }, {o2.max_up = }")


Person2.max_up = 56
print(f"{Person2.max_up = }, {o1.max_up = }, {o2.max_up = }")
print('--------------------------------------')



print('Person3\n')
class Person3:
    hp = 300



e1 = Person3()
e2 = Person3()

Person3.level = 1 # Создание нового аттрибута класса, не рекомендуется такой способ!
print(f"{Person3.level = }, {e1.level = }, {e2.level = }")


e1.damage = 100 # Создание нового аттрибута экземпляра
# print(f"{Person3.damage = }, {e1.damage = }, {e2.damage}") # Ошибка AttributeError
print(f"{e1.damage = }")
print('-----------------')




print('Person4\n')
class Person4:
    pass



a1 = Person4()
a1.level = 2
a1.health = 200

dict_person4 = {}
dict_person4['level'] = 2
dict_person4['health'] = 200

print(f"{a1.health = }")
print(f"{dict_person4['health'] = }\n-----------------------------")



print('Person5\n')
class Person5:
    max_up = 3

    def __init__(self): # Магический метод класса, к этой функции - класс доступа не имеет
        self.level = 1 # self - Экземпляр класса
        self.hp = 100



w1 = Person5()
w2 = Person5()

print(f"{w1.max_up = }, {w1.level = }, {w1.hp}")
print(f"{w2.max_up = }, {w2.level = }, {w2.hp}")
# print(f"{Person5.max_up = }, {Person5.level = }, {Person5.hp}") # AttributeError
print(f"{Person5.max_up = }")

Person5.level = 5
print(f"{Person5.level = }, {w1.level = }, {w2.level = }\n--------------------------------")



print('Person6\n')
class Person6:
    max_up = 2

    def __init__(self):
        self.level = 2
        self.hp = 500

        print(f"{id(self) = }")


r1 = Person6()
print(f"{id(r1) = }")
r2 = Person6()
print(f"{id(r2) = }")
print('------------------')



print('Person7\n')
class Person7:
    max_up = 6

    def __init__(self, name, race = 'unknown'):
        self.level = 2
        self.hp = 200
        self.name = name
        self.race = race



s1 = Person7(name='Crow', race='Птица')
s2 = Person7(name='Shelly', race='Человек')
s3 = Person7(name='Spayk')

print(f"{s1.name = }, {s1.race}")
print(f"{s2.name = }, {s2.race}")
print(f"{s3.name = }, {s3.race}")
print('---------------------------')



print('Person8\n')
class Person8:
    max_up = 6

    def __init__(self, name, race='unknown'):
        self.level = 2
        self.hp = 200
        self.name = name
        self.race = race


    def level_up(self):
        self.level += 1



t1 = Person8(name='Силвана', race='Эльф')
t2 = Person8(name='Игорь', race='Человек')
t3 = Person8(name='Грогу')

print(f"{t1.level = }, {t2.level = }, {t3.level = }")
t1.level_up()
t2.level_up()
t3.level_up()
print(f"{t1.level = }, {t2.level = }, {t3.level = }")
print('--------------------------------------')



print('Person9\n')
class  Person9:
    max_up = 3

    def __init__(self, name, race='unknown'):
        self.level = 2
        self.hp = 200
        self.name = name
        self.race = race

    def level_up(self):
        self.level += 1

    def change_hp(self, other, quantity):
        self.hp += quantity
        other.hp -= quantity




y1 = Person9(name='Сильвана', race='Эльф')
y2 = Person9(name='Игорь', race='Человек')
y3 = Person9(name='Грогу')

print(f"{y1.hp = }, {y2.hp = }, {y3.hp = }")

y1.change_hp(y2, 10)
print(f"{y1.hp = }, {y2.hp = }, {y3.hp = }\n------------------------------")



# Задачка - что вернёт код?
print('Задачка что вернёт код?... User\n')

class User:
    count = []

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


u1 = User(name='One', phone='123-45-67')
u2 = User(name='NoOne', phone='76-54-321')
u1.count.append(42)
u1.count.append(73)
u2.counter = 256
u2.count.append(u2.counter)
u1.count.append(u1.count[-1])

print(f"{u1.name = }, {u1.phone = }, {u1.count = }") # Ваш ответ
print(f"{u2.name = }, {u2.phone = }, {u2.count = }") # Ваш ответ
print('-----------------------------------------')



# Инкапсуляция: protected - защищенный доступ к аттрибутам и методам _
print('Инкапсуляция: protected - защищенный доступ...Person10\n')
class Person10:
    max_up = 3
    _max_level = 80 # Защищенный атрибут _max_level

    def __init__(self, name, race='unknown', speed=300): # Магический метод
        self.name = name
        self.race = race
        self.level = 2
        self.hp = 200
        self._speed = speed

    def _check_level(self): # Защищенный метод класса
        return self.level < self._max_level


    def level_up(self): # Публичный метод - поднимает уровень персонажа
        if self._check_level():
            self.level += 1
        else:
            self.level = self._max_level

    def change_hp(self, other, quantity): # Публичный метод - поднимает здоровье экземпляра и вычитает столько же у другого экземпляра
        self.hp += quantity
        other.hp -= quantity



person1 = Person10(name='8-bit', race='computer', speed=100)
person2 = Person10(name='Edgar', race='people', speed=500)
person3 = Person10(name='Colt')

print(f"{person1._max_level = }") # Подсвечивается желтым, потому что это защищенный атрибут
print(f"{person3._speed = }") # Также защищенный атрибут _speed
person2._speed = 0 # Зато можно изменять значение аттрибута 👍 ГЕНИАЛЬНО!
print(f"{person2._speed = }")

person2.level_up() # Поднимаем уровень экземпляра person2 на 1
print(f"{person2.level = }")
person2.level = 80 # Указываем макс.значение для level
person2.level_up() # Не получается повысить уровень т.к.уровень уже максимален
print(f"{person2.level = }")
person2.level = 100 # Но можно тупо проскочить через это ограничение, указав явно - уровень🤦‍♂️
print(f"{person2.level = }")
person2.level_up() # Но если попытаетесь увеличить уровень, вас откинет на максимальный уровень - 80
print(f"{person2.level = }")
print('-------------------')



# Инкапсуляция: private - приватный доступ к аттрибутам и методам __
print('Инкапсуляция - private: приватный доступ... Person10\n')
class Person10:
    __max_up = 3
    _max_level = 80

    def __init__(self, name, race='Unknown', speed=100):
        self.name = name
        self.race = race
        self.level = 1
        self.hp = 200
        self._speed = speed
        self.up = 2

    def check_level(self):
        return self.level < self._max_level


    def level_up(self):
        if self.check_level():
            self.level += 1
        else:
            self.level = self._max_level

    def change_hp(self, other, quantity):
        self.hp += quantity
        other.hp -= quantity

    def add_up(self):
        self.up += 1
        self.up = min(self.up, self.__max_up)




i1 = Person10(name='Mendy', race='Nigger', speed=150)

print(f"{i1.up = }")
i1.add_up()
print(f"{i1.up = }")
for _ in range(5):
    # Все методы запускаются 5 раз
    i1.add_up()
    i1.level_up()
    i1.change_hp(person3, 50)

print(f"{i1.up = }, {i1.level = }, {i1.hp = }, {person3.hp = }")

# print(i1.__max_up) # AttributeError, в этот раз мы не можем получить доступ к приватному аттрибуту 👍

# Как получить доступ к приватному аттрибуту?
private = i1._Person10__max_up

i1._Person10__max_up = 10
i1.add_up()
print(f"{i1.up = }")
print('-------------------------')



# Задачка - что вернёт код?
print('Что вернёт код?... User2\n')
class User2:
    def __init__(self, name, phone, password):
        self.__name__ = name
        self._phone = phone
        self.__password = password


d1 = User2(name='Alex', phone='123-45-67', password='qwerty')
print(d1.__name__, d1._phone, d1._User2__password)
print('-------------------------')



# Наследование
class Person11(object): # Пример
    pass


print('Наследование... Hero\n')
class Hero(Person10):
    def __init__(self, power, *args, **kwargs):
        self.power = power
        super().__init__(*args, **kwargs)


f1 = Hero(power='ult', name='Сильвана')
print(f1.name)
print('------------------------')



# Переопределение методов в наследовании
print('Переопределение методов в наследовании... Hero2(Person10)\n')
class Hero2(Person10):
    def __init__(self, power, *args, **kwargs): # __init__ указывается еще раз, из-за нового аттрибута power
        self.power = power
        super().__init__(*args, **kwargs)

    def change_hp(self, other, quantity): # Переопределение метода происходит здесь
        self.hp += quantity * 2
        other.hp -= quantity * 2

    def add_many_up(self):
        self.up += 1
        self.up = min(self.up, self._Person10__max_up * 2)



j1 = Hero2(power="hasn't", name='Vampire', race='Not people', speed=999)
j2 = Person10(name='Hitman', race='Человек')

print(f"{j1.hp = }, {j2.hp = }")

j1.change_hp(j2, 100) # Отнимаем у i1 200 hp, и прибавляем его к j1
print(f"{j1.hp = }, {j2.hp = }")
j2.change_hp(j1, 100) # Отнимаем у i1 100 hp, и прибавляем его к j1
print(f"{j1.hp = }, {j2.hp = }")


j1.add_many_up()
j1.add_many_up()
print(f"{j1.up = }")
print('------------------------')



# Начинается ХАРДКОР
# Множественное наследование
print('Множественное наследование... Hero3\n')
class Address:
    def __init__(self, county, city, street):
        self.country = county or ''
        self.city = city or ''
        self.street = street or ''

    def say_address(self):
        return f"Адрес героя: {self.country}, {self.city}, {self.street}"




class Weapon:
    def __init__(self, right_hand, left_hand):
        self.right_hand = right_hand or 'Лук'
        self.left_hand = left_hand or 'Клинок'


# Наследуем ...
class Hero3(Person10, Address, Weapon):
    def __init__(self, power, name=None, race=None, speed=None, country=None, city=None,
                 street=None, left_hand=None, right_hand=None):
        self.power = power
        Person10.__init__(self, name, race, speed)
        Address.__init__(self, country, city, street)
        Weapon.__init__(self, left_hand, right_hand)

    def change_hp(self, other, quantity):
        self.hp += quantity
        other.hp -= quantity

    def add_many_up(self):
        self.up += 1
        self.up = min(self.up, self._Person10__max_up * 2)



z1 = Hero3(power='speed ending',name='astro', race='people', country='USA', city='New-York', street='7', right_hand='dick', left_hand='phone')
print(z1.say_address())
print(f"{z1.right_hand = }, {z1.left_hand = }")
print('--------------------------')




# Полиморфизм
# Не до конца понял что это такое 🤷‍♂️
print('Полиморфизм...DivStr\n')
class DivStr(str):
    def __init__(self, obj):
        self.object = str(obj)

    def __truediv__(self, other):
        first = self.object.endswith('/')
        start = self.object

        if isinstance(other, str):
            second = other.startswith('/')
            finish = other
        elif isinstance(other, DivStr):
            second = other.object.startswith('/')
            finish = other.object
        else:
            second = str(other).startswith('/')
            finish = str(other)

        if first and second:
            return DivStr(start[:-1] + finish)
        elif (first and not second) or (not first and second):
            return DivStr(start + finish)
        elif not first and not second:
            return DivStr(start + '/' + finish)


path_1 = DivStr('/home/user/')
path_2 = DivStr('/my_project/workdir')
result = path_1 / path_2 # Теперь мы можем делить строки 🤯

print(f"{result = }, {type(result) = }")
print(f"{result / 'text' = }")
print(f"{result / 42}")
print(f"{result * 3 = }")



