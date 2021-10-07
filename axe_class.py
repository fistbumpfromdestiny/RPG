from weapon_class import Weapon

class Axe(Weapon):
    def __init__(self):
        super().__init__()
        self._weight = 10
        self._value = 20
        self._name = "axe"
        self._desc = "An axe with a wooden handle"
        self._damage = 6