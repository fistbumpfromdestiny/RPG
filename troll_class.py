from monster_class import Monster

class Troll(Monster):
    def __init__(self, inventory: list):
        super().__init__(self)
        self._hp = 65
        self._str = 5
        self._dex = 1
        self._name = "Troll"
        self._desc = "Disfigured and smells funky"
        self._corpseDesc = "The body of a dead troll."
        self._inventory = inventory
        self._giveXP = 100