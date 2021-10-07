from items_class import Item

class Torch(Item):
    def __init__(self):
        super().__init__()
        self._weight = 3
        self._value = 5
        self._name = "torch"
        self._desc ="A stick on fire. "
        self._isOn = False
    
    #returns on/off status of torch
    def getOn(self):
        return self._isOn
    
    #sets torch status to on
    def setOnOff(self, arg):
        self._isOn = arg
    
    def getDesc(self):
        return self._desc