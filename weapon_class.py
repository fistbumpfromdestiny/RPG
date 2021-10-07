from items_class import Item

class Weapon(Item):
    def __init__(self):
        super().__init__()
        self._damage = None
        self._itemType = "weapon"
        self._value = 1
    
    def getDamage(self):
        """Returns weapon damage."""
        return self._damage