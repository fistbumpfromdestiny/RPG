from items_class import Item

class Key(Item):
    def __init__(self, id, desc):
        super().__init__()
        self._weight = 2
        self._value = 50
        self._name = "key"
        self._id = id
        self._desc = desc
    
    def getDesc(self):
       return self._desc
    
    def getID(self):
        return self._id