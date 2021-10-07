from character_class import Character
import pickle
import os

playername = input("What is your name? ")

def loginPlayer(playername):
    try:
        open(f'{playername}/{playername.lower()}.P')
        return True
    except IOError:
        return False


def saveGame(player, caves):
    with open(f'{playername}/{player._name.lower()}.P', 'wb') as f:
        pickle.dump(player, f)
    
    with open(f'{playername}/{player._name.lower()}_caves.P', 'wb') as f:
        pickle.dump(caves, f)


if loginPlayer(playername):
    with open(f'{playername}/{playername.lower()}.P', 'rb') as f:
        player = pickle.load(f)
        print("An all encompassing voice bellows:\n")
        print(f"BE AGAIN, {player.getName().upper()}")
else:
    player = Character(f'{playername.title()}', [])
    print("An all encompassing voice bellows:\n")
    print("FROM NOTHING, SOMETHING.\n")
    print(f"You slowly materialize in a cave. You're someone. You're {playername.title()}.")
    print("Type 'help', and get going.")
    os.mkdir(f'{playername}')
    

