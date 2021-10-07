from monster_class import Monster

class Skeleton(Monster):
    def __init__(self, inventory: list):
        super().__init__(self)
        self._hp = 35
        self._str = 2
        self._dex = 2
        self._name = "Skeleton"
        self._desc = "Walking set of bones!"
        self._corpseDesc = "A pile of bones!."
        self._inventory = inventory
        self._giveXP = 55