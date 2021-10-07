from monster_class import Monster

class Goblin(Monster):
    def __init__(self, inventory: list):
        super().__init__(self)
        self._hp = 10
        self._str = 1
        self._dex = 1
        self._name = "Goblin"
        self._desc = "A goblin! It's small, ugly and hungry. Better watch out!"
        self._corpseDesc = "The body of a dead goblin."
        self._inventory = inventory
        self._giveXP = 25
    


