import sys, shutil
import commands as cmd
from account_handler import player


"""function for printing information about the room the player is in"""
def printInterface(currentRoom):
    if not canPlayerSee(currentRoom):
        print("Its too dark to see.")
    else:
        print(currentRoom.getRoomDesc())
        for item in currentRoom.getObjects():
            print(f"A "+item.getName() +".")
        printVisibleExits(currentRoom)    


def canPlayerSee(currentRoom):
    """Checks if room is lit, returns desc if true. If room is not lit, checks if
       player has a lit torch in inventory. If so, displays the room's description.
       If all fails, room is too dark to see."""
    if currentRoom.getDark() and not player.getIlluminated():
        return False
    else:
        return True


def checkWeight(item):
    if (player.getTotalWeight() + item.getWeight()) <= (player.getStr() * 10):
        return True
    else:
        print("It's too heavy!")
        return False
        

def endGame(playername):
    shutil.rmtree(f'{playername.lower()}')
    sys.exit()


def printInventory(target):
    for thing in target.getInventory():
        print(thing.getName().title())


def printVisibleExits(currentRoom):
    roomExits = []
    print("Visible exits: ", end='')
    if currentRoom.getExitWest():
        roomExits.append("West")   
    if currentRoom.getExitEast():
        roomExits.append("East")     
    if currentRoom.getExitNorth():
        roomExits.append("North")
    if currentRoom.getExitSouth():
        roomExits.append("South")
    print(str(roomExits).replace('[', '').replace(']', ''))