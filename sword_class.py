from weapon_class import Weapon

class Sword(Weapon):

    def __init__(self):
        super().__init__()
        self._weight = 1
        self._value = 50
        self._name = "sword"
        self._desc = "Excalibur"
        self._damage = 3