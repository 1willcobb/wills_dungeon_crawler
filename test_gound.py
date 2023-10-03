import player
import monsters as mst


player_1 = player.Player(input("name > "), input("age > "), input("class > "))

mst.sir_dragon.monster_attacks(player_1.name)

print(player_1)
player_1.init_weapons()
for x in player_1.weapons.keys():
    print(x)
    weapon_choice = player_1.weapons_check()
    print(f"out of nowhere a {mst.sir_dragon.type} appears and wants to fight\n")
if mst.sir_dragon.life > 0:
    while True:
        print(f"You grab your {weapon_choice} and try to attack the {mst.sir_dragon.type}.\n"
              f"You stike causing 25 damange")
        print(f"the dragon is still standing")

def room_2_2('bhb?', 'monstor', 'item'):
	global bhb_2_2  # have I been here before initialize false
	while True:
		if (prev_room[0] == "room_1_1"
				and bhb_2_2 == False
				and monsters['2_2']['alive'] == True):
			typingPrint(
				"\nYou entered a dark closet with a small lamp flickering\n"
				"in the back of the room.\n"
				f"a {monsters['2_2']['name']} huddles by the lamplight.\n"
				f"There is only the door you came in through here")
			typingPrint(f"\nWhat do you want to do?\n"
						f"1. Go back to the room I was in\n"
						f"2. Examine the room\n"
						f"3. Confront the {monsters['1_2']['name']}\n")
		elif (prev_room[0] == "room_1_1"
			  and bhb_2_2 == True
			  and monsters['2_2']['alive'] == True):
			typingPrint(
				"\nYou return to the dark closet with a small flickering\n"
				"lamp. \nThere is just the door you came in through in here\n")
			typingPrint("What do you want to do?\n"
						"1. Go back to the room I was in\n"
						"2. Examine the room again\n")
			if monsters['2_2']['alive'] == True:
				print(f"3. the {monsters['2_2']['name']} is still here")
			else:
				pass
		elif bhb_2_2 == True and monsters['2_2']['alive'] == False:
			typingPrint(
				f"\nYou are in a dark closet with a small flickering\n"
				f"lamp. There is dead {monsters['2_2']['name']} "
				f"by the lamp.\n"
				f"There is just the door you came in through in here\n")
			typingPrint("What do you want to do?\n"
						"1. Go back to the room I was in\n"
						"2. Examine the room\n")
		else:
			pass
		choice = (typingInput("\n>> ")).strip().lower()
		if (choice == "1"
				or choice == "open the door"
				or choice == "go"
				or choice == "open"
				or choice == "back from where i came"
				or choice == "back up"
				or choice == "back"):
			prev_room[0] = "room_2_2"
			bhb_2_2 = True
			print("You go through the back door...")
			room_1_1()
		elif (choice == "2"
			  or choice == "examine the room"
			  or choice == "examine"):
			if monsters['2_2']['alive'] == True:
				print(
					f"the {monsters['2_2']['name']} doesnt seem to take\n"
					f"their gaze off of you... maybe checking things\n"
					f"out is a bad idea...")
			else:
				check_the_room('1_2')
		elif (choice == "3"
			  or choice == "talk to the creature"
			  or choice == f"talk to the {monsters['2_2']['name']} "
			  or choice == "fight"
			  or choice == "attack"):
			print("The creature doesnt want to talk and becomes hostile\n"
				  "but you slay it easily...")  # update with weapon here
			monsters['2_2']['alive'] = False
			bhb_2_2 = True
			continue
		else:
			print("Not sure that will work here...")