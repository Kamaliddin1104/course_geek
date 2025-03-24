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



# Адаптер (Adapter)
# 👉 Позволяет объектам с несовместимыми интерфейсами работать вместе.

class OldPrinter:
    @staticmethod
    def print_text(self):
        return "Старый принтер печатает"

class NewPrinter:
    @staticmethod
    def print(self):
        return "Новый принтер печатает"

class PrinterAdapter:
    def __init__(self, old_printer):
        self.old_printer = old_printer

    def print(self):
        return self.old_printer.print_text()

printer = PrinterAdapter(OldPrinter())
print(printer.print())  # Старый принтер печатает



# Фасад (Facade)
# 👉 Упрощает сложную систему, предоставляя простой интерфейс.
class Engine:
    def start(self):
        return "Двигатель запущен"

class Lights:
    def turn_on(self):
        return "Фары включены"

class CarFacade:
    def __init__(self):
        self.engine = Engine()
        self.lights = Lights()

    def start_car(self):
        return f"{self.engine.start()} и {self.lights.turn_on()}"

car = CarFacade()
print(car.start_car())  # Двигатель запущен и Фары включены



# Наблюдатель (Observer)
# 👉 Автоматически уведомляет подписчиков об изменениях.
class Observer:
    def update(self, message):
        print(f"Получено уведомление: {message}")

class Subject:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

subj = Subject()
obs1 = Observer()
obs2 = Observer()

subj.add_observer(obs1)
subj.add_observer(obs2)

subj.notify("Новое событие!")
# Получено уведомление: Новое событие!
# Получено уведомление: Новое событие!



#  Стратегия (Strategy)
# 👉 Позволяет менять поведение объекта на лету.
class StrategyA:
    def execute(self):
        return "Используется стратегия A"

class StrategyB:
    def execute(self):
        return "Используется стратегия B"

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self):
        return self.strategy.execute()

context = Context(StrategyA())
print(context.execute_strategy())  # Используется стратегия A

context.strategy = StrategyB()
print(context.execute_strategy())  # Используется стратегия B



# Цепочка обязанностей (Chain of Responsibility)
# 👉 Позволяет передавать запрос по цепочке обработчиков.
class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, request):
        if self.successor:
            return self.successor.handle(request)
        return "Запрос не обработан"

class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request == "A":
            return "Обработано A"
        return super().handle(request)

class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request == "B":
            return "Обработано B"
        return super().handle(request)

handler_chain = ConcreteHandlerA(ConcreteHandlerB())
print(handler_chain.handle("B"))  # Обработано B
