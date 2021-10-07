class Monster:
    """A template for creating a monster object."""
   
    def __init__(self, inventory: list):
        self._hp = 40
        self._str = 1
        self._dex = 5
        self._name = None
        self._inventory = inventory
        self._desc = None
        self._isAlive = True
        self._corpseDesc = None
        self._objectType = "monster"
        self._giveXP = None
    
    def giveXP(self):
        return self._giveXP
    
    def getHP(self):
        return self._hp

    def getDex(self):
        return self._dex
    
    def getObjectType(self):
        return self._objectType
    
    def getName(self):
        if self._isAlive:
            return self._name
        else:
            return "corpse"
    
    def getDesc(self):
        if self._isAlive == True:
            return self._desc
        else:
            return self._corpseDesc

    def getIsAlive(self):
        return self._isAlive
    
    def getInventory(self):
        return self._inventory
    
    def setIsAlive(self, arg):
        self._isAlive = arg
        
    def takeDamage(self, dmg):
        self._hp = self._hp - dmg
        return dmg

    def doDamage(self):
        return self._str
        

    
