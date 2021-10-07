from items_class import Item

class Armor(Item):
    def __init__(self, name, armorLocation, damageMitigation):
        super().__init__()
        self._value = 10
        self._itemType = "armor"
        self._name = name
        self._armorLocation = armorLocation
        self._damageMitigation = damageMitigation
        self._weight = 2
        
    
    def getArmorLocation(self):
        """Returns armor location."""
        return self._armorLocation
        
    
    def getDamageMitigation(self):
        """Returns damage mitigation."""
        return self._damageMitigation