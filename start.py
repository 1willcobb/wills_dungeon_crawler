from rooms import Rooms
from monsters import Monsters
import player

def game_start():
    will = player.Player("will", 32, "dragon")
    will.initialize_rooms()
    

if __name__ == "__main__":
    print("start the game")