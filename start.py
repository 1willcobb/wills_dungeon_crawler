import player

def game_start():
    will = player.Player("will", 32, "dragon")
    will.initialize_rooms()
    print(will.name)
    

if __name__ == "__main__":
    print("start the game")
    game_start()