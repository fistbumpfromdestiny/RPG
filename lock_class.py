from items_class import Item

class Lock(Item):
    def __init__(self, id):
        super().__init__()
        self._isLocked = True
        self._id = id
        self._desc = None
    
    def getID(self):
        return self._id
    
    def getLocked(self):
        return self._isLocked
        
    def setLocked(self, arg):
        self._isLocked = arg