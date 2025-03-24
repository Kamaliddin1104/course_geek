class Base:
    def __init__(self, name, damage: int, health: int):
        self.name = name
        self.damage = damage
        self.hp = health


    def __str__(self):
        return f'Name: {self.name} with {self.damage} attack, and {self.hp} hp.'


    def attack(self, other):
        if other.hp <= 0:
            return f"{other.name} был повержен {self.name}ом"

        other.hp -= self.damage

        if other.hp <= 0:
            return f"{self.name} wins!"

        return f"{other.name} был атакован {self.name}ом, {other.name} hp = {other.hp}"



class Person(Base):
    pass


class Person2(Base):
    pass



kamal = Person(name='Kamaliddin', damage=2, health=800)
abubakr = Person2(name='Abubakr', damage=1, health=800)


while kamal.hp > 0 and abubakr.hp > 0:
    print(abubakr.attack(kamal))
    print(kamal.attack(abubakr))





