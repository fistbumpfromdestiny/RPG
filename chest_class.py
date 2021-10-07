from items_class import Item
from lock_class import Lock

class Chest(Item):
    def __init__(self, inventory: list, lock: Lock):
        super().__init__()
        self._inventory = inventory
        self._lock = lock
        self._isOpen = False
        self._desc = "A treasure chest."
        self._name = "chest"
        self._weight = 1000
        
    def getLock(self):
        return self._lock

    def getIsOpen(self):
        return self._isOpen
      
    def getDesc(self):
        if self._isOpen:
            return self._desc + "\nIt's open!"
        elif not self._isOpen:
            return self._desc + "\nIt's closed."

    def setIsOpen(self, arg):
        self._isOpen = arg
    
    def getInventory(self):
        return self._inventory