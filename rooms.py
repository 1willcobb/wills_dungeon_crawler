

# been here before initialization
bhb_1_1 = False
bhb_1_2 = False
bhb_2_1 = False
bhb_2_2 = False
bhb_2_3 = False
bhb_2_4 = False
bhb_3_1 = False
bhb_3_2 = False
bhb_3_3 = False
bhb_3_4 = False
bhb_3_5 = False
bhb_3_6 = False
bhb_4_1 = False
bhb_4_2 = False
discovered = []
keys_to_boss = []


class Room:

    def __init__(self, game, name, monster):
        self.name = name
        self.monster = monster
        self.game = game

    def room_main(self):
        """room_1_image = Image.open('room_1.png')
        room_1_image = room_1_image.resize((500,500))
        room_1_image.show()"""
        typingPrint("\nYou are in a massive room the size of a cathedral.\n"
                    "Firey sconces light 2 rows of pillars,\n"
                    "3 to each side of the cavernus room.\n"
                    "Between each pillar are large rusty doors and a door\n"
                    "3 times the size as the others in the center\n"
                    "\n"
                    "from left to right the doors are:\n"
                    "1. Rusted shut with claw marks near the lock\n"
                    "2. Worn with a movement of air from benith\n"
                    "3. Massive and 3x the the size as the others with a large\n"
                    "   lock in the middle.\n"
                    "4. Half caved in from something large, with the smell of blood.\n"
                    "5. Normal looking door with a bit of rust.\n\n")
        while True:
            door_choice = input(
                "What door tickles your fancy?").strip().lower()
            if door_choice == "1":
                typingPrint("\nYou choose the rusted shut door with claw marks,\n"
                            "it seems like it will budge open...\n")
                prev_room[0] = "room_main"
                self.game.room_1_1()
            elif door_choice == "2":
                typingPrint("\nYou choose the door with some sort of air coming from it...\n"
                            "it appears to open easily\n")
                prev_room[0] = "room_main"
                self.Room(room_2_1)
            elif door_choice == "3":
                print("door 3")
                prev_room[0] = "room_main"
            elif door_choice == "4":
                print("door 4")
                prev_room[0] = "room_main"
            elif door_choice == "5":
                print("door 5")
                prev_room[0] = "room_main"
            elif door_choice == "run":
                break
            else:
                print("that's not an option")
        depressing_endgame_text()


def room_1_1():
    if prev_room[0] == "room_main":
        typingPrint("\nYou enter a musty storage room with"
                    " a rusty back door.\n")
        typingPrint("What do you want to do?\n"
                    "1. Open the door\n"
                    "2. Examine the room\n"
                    "3. Back to the main room\n")
    elif prev_room[0] == "room_1_2":
        typingPrint("\nYou return to the musty storage room with a door "
                    "that returns to the main foyer.\n")
        typingPrint("What do you want to do?\n"
                    "1. Go back to the room I was in\n"
                    "2. Examine the room again\n"
                    "3. Back to the main room\n")
    while True:
        choice = (typingInput(">> ")).strip().lower()
        if choice == "1":
            prev_room[0] = "room_1_1"
            bhb_1_1 = True
            print("You go through the back door...")
            room_1_2()
        elif choice == "2":
            typingPrint("You check out the room and open every drawer "
                        "and check behind every nook and cranny")
            typingPrint(f"You find a {discover['1_1']} and you pocket it")
        elif choice == "3"\
                or choice == "go back"\
                or choice == "back from where you came"\
                or choice == "back from where I came"\
                or choice == "back to the main room"\
                or choice == "main room":
            bhb_1_1 = True
            prev_room[0] = "room_1_1"
            print("You head back to where you entered the room")
            room_main()
        else:
            print("Not sure that will work here...")


def room_main():
    """
    Main Room

    room_1_image = Image.open('room_1.png')
    room_1_image = room_1_image.resize((500,500))
    room_1_image.show()"""
    typingPrint("\nYou are in a massive room the size of a cathedral.\n"
                "Firey sconces light 2 rows of pillars,\n"
                "3 to each side of the cavernus room.\n"
                "Between each pillar are large rusty doors and a door\n"
                "3 times the size as the others in the center\n"
                "\n"
                "from left to right the doors are:\n"
                "1. Rusted shut with claw marks near the lock\n"
                "2. Worn with a movement of air from benith\n"
                "3. Massive and 3x the the size as the others with a large\n"
                "   lock in the middle.\n"
                "4. Half caved in from something large, with the smell of blood.\n"
                "5. Normal looking door with a bit of rust.\n\n")
    while True:
        door_choice = input("What door tickles your fancy?").strip().lower()
        if door_choice == "1":
            typingPrint("\nYou choose the rusted shut door with claw marks,\n"
                        "it seems like it will budge open...\n")
            prev_room[0] = "room_main"
            room_1_1()
        elif door_choice == "2":
            typingPrint("\nYou choose the door with some sort of air coming from it...\n"
                        "it appears to open easily\n")
            prev_room[0] = "room_main"
            room_2_1()
        elif door_choice == "3":
            print("door 3")
            prev_room[0] = "room_main"
        elif door_choice == "4":
            print("door 4")
            prev_room[0] = "room_main"
        elif door_choice == "5":
            print("door 5")
            prev_room[0] = "room_main"
        elif door_choice == "run":
            break
        else:
            print("that's not an option")
    depressing_endgame_text()


def room_1_1():
    if prev_room[0] == "room_main":
        typingPrint("\nYou enter a musty storage room with"
                    " a rusty back door.\n")
        typingPrint("What do you want to do?\n"
                    "1. Open the door\n"
                    "2. Examine the room\n"
                    "3. Back to the main room\n")
    elif prev_room[0] == "room_1_2":
        typingPrint("\nYou return to the musty storage room with a door "
                    "that returns to the main foyer.\n")
        typingPrint("What do you want to do?\n"
                    "1. Go back to the room I was in\n"
                    "2. Examine the room again\n"
                    "3. Back to the main room\n")
    while True:
        choice = (typingInput(">> ")).strip().lower()
        if choice == "1"\
                or choice == "open the door":
            Player.prev_room[0] = "room_1_1"
            bhb_1_1 = True
            print("You go through the back door...")
            room_1_2()
        elif choice == "2"\
                or choice == "examine the room"\
                or choice == "examine":
            print("You check out the room and open every drawer "
                  "and check behind every nook and cranny")
            print(f"You find a {discover['1_1']} and you pocket it")
        elif choice == "3"\
                or choice == "go back"\
                or choice == "back from where you came"\
                or choice == "back from where I came"\
                or choice == "back to the main room"\
                or choice == "main room":
            bhb_1_1 = True
            prev_room[0] = "room_1_1"
            print("You head back to where you entered the room")
            room_main()
        else:
            print("Not sure that will work here...")


def room_1_2():
    global bhb_1_2  # have I been here before initialize false
    while True:
        if (prev_room[0] == "room_1_1"
            and bhb_1_2 == False
                and monsters['1_2']['alive'] == True):
            typingPrint("\nYou entered a dark closet with a small lamp flickering\n"
                        "in the back of the room.\n"
                        f"a {monsters['1_2']['name']} huddles by the lamplight.\n"
                        f"There is only the door you came in through here")
            typingPrint(f"\nWhat do you want to do?\n"
                        f"1. Go back to the room I was in\n"
                        f"2. Examine the room\n"
                        f"3. Confront the {monsters['1_2']['name']}\n")
        elif (prev_room[0] == "room_1_1"
              and bhb_1_2 == True
              and monsters['1_2']['alive'] == True):
            typingPrint("\nYou return to the dark closet with a small flickering\n"
                        "lamp. \nThere is just the door you came in through in here\n")
            typingPrint("What do you want to do?\n"
                        "1. Go back to the room I was in\n"
                        "2. Examine the room again\n")
            if monsters['1_2']['alive'] == True:
                print(f"3. the {monsters['1_2']['name']} is still here")
            else:
                pass
        elif bhb_1_2 == True and monsters['1_2']['alive'] == False:
            typingPrint(f"\nYou are in a dark closet with a small flickering\n"
                        f"lamp. There is dead {monsters['1_2']['name']} "
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
            prev_room[0] = "room_1_2"
            bhb_1_2 = True
            print("You go through the back door...")
            room_1_1()
        elif (choice == "2"
                        or choice == "examine the room"
                        or choice == "examine"):
            if monsters['1_2']['alive'] == True:
                print(f"the {monsters['1_2']['name']} doesnt seem to take\n"
                      f"their gaze off of you... maybe checking things\n"
                      f"out is a bad idea...")
            else:
                check_the_room('1_2')
        elif (choice == "3"
                        or choice == "talk to the creature"
                        or choice == f"talk to the {monsters['1_2']['name']} "
                        or choice == "fight"
                        or choice == "attack"):
            print("The creature doesnt want to talk and becomes hostile\n"
                  "but you slay it easily...")  # update with weapon here
            monsters['1_2']['alive'] = False
            bhb_1_2 = True
            continue
        else:
            print("Not sure that will work here...")


def room_2_1():
    # what we do when we enter the room for the 1st time and any time after
    while True:
        if prev_room[0] == "room_main":
            typingPrint("\nYou enter a small room decorated with prized antlers\n"
                        "mounted all over each wall. There apears to be 1 door\n"
                        "to the right of the room.\n")
            typingPrint("\nWhat do you want to do?\n"
                        "1. Open the door\n"
                        "2. Examine the room\n"
                        "3. Return to the main foyer\n")
        elif prev_room[0] == "room_2_2":
            typingPrint("\nYou return to the room decorated with antlers\n"
                        "and there is a door that leads to the main foyer.\n")
            typingPrint("What do you want to do?\n"
                        "1. Back from where I came\n"
                        "2. Examine the room again\n"
                        "3. Return to the main foyer\n")
        # options in the room
        choice = input(">> ").strip().lower()
        if (choice == "1"
            or choice == "open the door"
            or choice == "go"
            or choice == "open"
            or choice == "back from where i came"
            or choice == "back up"
                or choice == "back"):
            prev_room[0] = "room_2_1"
            print("You go through the back door...")
            room_2_2()
        elif choice == "2"\
                or choice == "examine the room"\
                or choice == "examine"\
                or choice == "examine the room again":
            if "2_1" in discover:
                print("\nYou check out the room and look in every drawer\n"
                      "and check behind every nook and cranny\n")
                print(f'You find a {discover["2_1"]} behind\n'
                      f'some leaves in the corner and you poket it.\n')
                discovered.append(discover["2_1"])
                print("discovered =", discovered[-1])
                del discover["2_1"]
            else:
                print(f"You already have the {discovered[-1]}")
                print(f"\nThere doesnt seem to be anything here...\n")
        elif choice == "3" \
                or choice == "return" \
                or choice == "return to the main foyer" \
                or choice == "main foyer" \
                or choice == "back to the main room" \
                or choice == "main room":
            prev_room[0] = "room_2_1"
            print("\nYou head to the main foyer")
            room_main()
        else:
            print("\nNot sure that will work here...")


def room_2_2():
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


def room_2_3():
    print("room")


def room_2_4():
    print("room")


def room_3_1():
    print("room")


def room_3_2():
    print("room")


def room_3_3():
    print("room")


def room_3_4():
    print("room")


def room_3_5():
    print("room")


def room_3_6():
    print("room")


def room_4_1():
    print("room")


def room_4_2():
    print("room")
