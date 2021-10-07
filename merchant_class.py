class Merchant:
    def __init__(self, inventory: list):
        self._inventory = inventory
        self._objectType = "merchant"
        self._name = "shop"
        self._coin = 500
    
    def getName(self):
        return self._name

    def getObjectType(self):
        return self._objectType

    def getCoin(self):
        return self._coin

    def getInventory(self):
        return self._inventory

    def buy(self, item):
        self._inventory.append(item)

    def sell(self, item):
        self._inventory.remove(item)

    def setCoin(self, amount):
        self._coin += amount
    