# 1 - Singleton (Одиночка)

class Singleton:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.name = None
            cls.__instance.age = None

        return cls.__instance


    def __str__(self):
        return f'{self.name}, {self.age}'


    def __init__(self, name, age):
        if self.name is None and self.age is None:
            self.name = name
            self.age = age



first = Singleton(name='Kamaliddin', age=17)
second = Singleton(name='Madina', age=16)
third = Singleton(name='Abdusamad', age=16)

print(first) # Kamaliddin, 17
print(second) # Kamaliddin, 17
print(third) # Kamaliddin, 17



# 2 Паттерн - Fabric (Фабрика)

# Зачем это нужно?
#
# Код становится более гибким — можно легко добавить новые классы машин.
# Код не зависит от конкретных классов, а использует только фабрику.

# Пример без Fabric

class Tesla:
    @staticmethod
    def drive():
        return "Еду на Tesla"

class BMW:
    @staticmethod
    def drive():
        return "Еду на BMW"

car1 = Tesla()
car2 = BMW()



# С Fabric


class CarFactory:
    @staticmethod
    def create_car(car_type):
        if car_type == "tesla":
            return Tesla()
        elif car_type == "bmw":
            return BMW()
        else:
            raise ValueError("Неизвестный тип машины")


car = CarFactory.create_car("tesla")
print(car.drive())  # Выведет: "Еду на Tesla"























