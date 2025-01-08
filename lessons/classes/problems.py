# Задачи по классам
from datetime import date



class People:
    def __init__(self, age, name='Unknown', surname='Unknown'):
        self.name = name
        self.surname = surname
        self.__age = age

    def birthday(self):
        self.__age += 1

    def full_name(self):
        return f'Full_name : {self.name}, {self.surname}'

    def get_age(self):
        return f'Person age: {self.__age}'


people = People(name='Kamaliddin', surname='Abzalov', age=16)
print(people.name, people.surname, people.get_age())
people.birthday()
print(people.get_age())
print('--------------')



class Book:
    def __init__(self, name, author, since):
        self.name = name
        self.author = author
        self.since = since

    def info(self):
        return f'Книга называется: {self.name}, Автор: {self.author}, Год создания: {self.since}'


my_book = Book(name='Грокаем алгоритмы', author='Дмитрий Пидоренко', since='1234')
z = my_book.info()
print(z)
print('--------------------')



class Calculator:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        try:
            if not self.a:
                return self.a / self.b
            elif self.b == 0:
                return self.b / self.a
            else:
                return self.a / self.b
        except ZeroDivisionError:
            return 'Невозможно делить на ноль. Попробуйте другое число'


calculator = Calculator(a=0, b=0)
print(calculator.add())
print(calculator.multiply())
print(calculator.divide())
print(calculator.subtract())



class Pet:
    def __init__(self, name, animal_type, sound):
        self.name = name
        self.animal_type = animal_type
        self.sound = sound


    def get_sound(self):
        return self.sound



cat = Pet(name='Whyskas', animal_type='Cat', sound='Мяу')
dog = Pet(name='', animal_type='dog', sound='Гав')
cow = Pet(name='Lolly', animal_type='Cow', sound='Му')

cow.get_sound()
dog.get_sound()
cat.get_sound()
print('--------------------')




class Car:
    def __init__(self, company, version, year):
        self.car_name = company
        self.version = version
        self.year = year


    def calculate_age_car(self):
        now_year = date.today().year
        print(now_year - int(self.year))


car = Car(company='BMW', version='c33', year='2000')
car.calculate_age_car()
print('--------------------')




class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.__balance = 1000
        self.properties = {}
        self.deposit = 1000


    def see_balance(self):
        """Просмотр баланса __balance"""
        print(f"{self.__balance} $")


    def get_deposit(self):
        """Получение денег из депозита"""
        amount = int(input(f'В депозите {self.deposit}: '))
        if amount > self.deposit:
            print('Столько нет в вашем депозите!')
        elif self.deposit <= 0:
            print('В депозите не осталось средств!')

        elif amount >= self.deposit:
            self.__balance += amount
            self.deposit -= amount
            print(f"Deposit: {self.deposit}/1000")



    def buy_property(self):
        """Покупка имущества, продуктов, машин"""
        print('Cars\n')
        cars = {
            '1. Волга Original': 6000,
            '2. Жигули Original': 7000,
            '3. Matiz The Best': 7500,
            '4. Кобальт-1': 10000,
            '5. BYD Seagull': 11000,
            '6. Mercedes-Benz 2015 года': 15000
        }
        print(cars)
        print('------------------')
        print('Houses\n')
        houses = {
            '7. Двушка в старом 9-этажном доме': 30000,
            '8. Трех-этажная квартира в многоэтажке': 45000
        }
        print(houses)

        buy_process = '12fevev'
        count_fails = 0
        while not buy_process.isdigit():
            if count_fails > 0:
                print('Неверный порядковый номер! Попробуйте снова')
            buy_process = input('Порядковый номер имущества: ')

        houses_cars = houses | cars

        for key, value in houses_cars.items():
            if buy_process == key[0] or buy_process == key[:2]:
                if self.__balance >= value:
                    confirm = input("Подтвердите покупку 'ok': ")
                    if confirm.lower() == 'ok':
                        self.__balance -= value
                        self.properties[key] = value

                        print(f'Теперь вы обладатель: {key}')
                        print(f'Ваш баланс: {self.see_balance()}')


                    else:
                        print('Вы не подтвердили покупку')

                else:
                    print('У вас не хватает средств!')


    def purchased_properties(self):
        print(self.properties)



kamal = BankAccount(owner='Kamal1104')

kamal.see_balance()
print('--------------------')



class Students:
    students_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Students.students_count += 1



first_st = Students(name='Alan', age=22)
second = Students(name='Alice', age=20)
third = Students(name='Adam', age=19)

print(Students.students_count)



class Worker(People):
    def __init__(self, id_number: int, age):
        super().__init__(age)
        self.id_worker = id_number


    def calculate_level_access(self):
        count = 0
        str_id = str(self.id_worker)
        if len(str_id) != 6:
            return 'len of id incorrect!'
        else:
            for i in str_id:
                count += int(i)

        return count // 7


worker = Worker(id_number=111111, age=20)
print(worker.calculate_level_access())
print('-------------------------')



class Animal:
    def __init__(self, name='unknown', age=None):
        self.name = name
        self.age = age


    def return_name_age(self):
        return f'Name of animal: {self.name}, возраст: {self.age}'



class Cat(Animal):
    def __init__(self, name, age, animal_type):
        super().__init__(name, age)
        self.animal_type = animal_type


    def return_specific(self):
        return f'{self.animal_type}'



class Dog(Animal):
    def __init__(self, name, age, sound):
        super().__init__(name, age)
        self.sound = sound

    def return_specific(self):
        return {self.sound}



class Wolf(Animal):
    def __init__(self, name, age, safe):
        super().__init__(name, age)
        self.is_safe = safe


    def return_specific(self):
        return self.is_safe




class User:
    def __init__(self, username, gmail, password):
        self.username = username
        self.gmail = gmail
        self.__password = password


    def check_password(self, type_pass):
        return type_pass == self.__password


    def reset_password(self, *, now_pass, new_pass):
        if now_pass == self.__password:
            self.__password = new_pass
            return self.__password
        else:
            return False




# class Admin(User):
#     def __init__(self, username, gmail, password):
#         super().__init__(username, gmail, password)
#
#
#     def ban_user(self, type_username, gmail):
#         ban_users = {}
#         if












