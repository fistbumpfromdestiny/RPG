from items_class import Item
import library as lib
from account_handler import playername

class Statue(Item):
    def __init__(self):
        super().__init__()
        self._name = "statue"
        self._desc = None
        self._weight = 1

    def getDesc(self):
        print("As you pick up the statue to look closer at it, you notice it is")
        print("an exact replica of yourself. How strange.\n\n") 
        print("Suddenly an all encompassing voice bellows:\n\n")
        print("\t\tYOU SHALL BE FREE. YOU SHALL SEIZE TO BE.\n\n")
        print("\t\t\t\tGame over.")
        lib.endGame(playername)