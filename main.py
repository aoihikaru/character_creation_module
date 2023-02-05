from random import randint

DEFAULT_ATTACK = 5


class Character:
    RANGE_VALUE_ATTACK = (1, 3)

    def __init__(self, name):
        self.name = name

    def attack(self):
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}')

    def defence(self):
        pass

    def special(self):
        pass


class Warrior(Character):
    pass


class Mage(Character):
    pass


class Healer(Character):
    pass
