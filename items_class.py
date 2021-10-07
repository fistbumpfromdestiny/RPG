class Item:
    def __init__(self):
        self._weight = None
        self._value = None
        self._name = None
        self._itemType = "item"
        self._objectType = "item"
        self._desc = None

    #method for getting type desciption
    def getName(self):
        return self._name

    #method for getting item value
    def getValue(self):
        return self._value

    #method for getting item weight
    def getWeight(self):
        return self._weight

    #method for getting what type of item 
    def getItemType(self):
        return self._itemType
    
    #method for getting what type of object  
    def getObjectType(self):
        return self._objectType
        
    def getDesc(self):
        return self._desc





