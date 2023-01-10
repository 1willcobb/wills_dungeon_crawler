from dataclasses import dataclass
from rooms import Room

# Dataclass attempt for setting up a new player
@dataclass
class Player():
    name: str
    age: int
    type: str
    life = 100
    prev_room = ["room_main"]
    weapons = {}
    pack = []
    keys = []
    weapon_choices = {
	"AXE" : {
		"NAME" : "axe",
		"STRENGTH" : 6,
		"DURABILITY" : 6,
		"RANGE" : 0
	},
	"MACE" : {
		"NAME" : "mace",
		"STRENGTH" : 7,
		"DURABILITY" : 4,
		"RANGE" : 2
	},
	"SWORD" : {
		"NAME" : "sword",
		"STRENGTH" : 6,
		"DURABILITY" : 5,
		"RANGE" : 1
	},
	"LANCE" : {
		"NAME" : "lance",
		"STRENGTH" : 8,
		"DURABILITY" : 2,
		"RANGE" : 4
	},
	"BOW" : {
		"NAME" : "bow",
		"STRENGTH" : 5,
		"DURABILITY" : 5,
		"RANGE" : 10
	},
	"DAGGER" : {
		"NAME" : "dagger",
		"STRENGTH" : 4,
		"DURABILITY" : 7,
		"RANGE" : 0
	},
	"HAMMER" : {
		"NAME" : "hammer",
		"STRENGTH" : 8,
		"DURABILITY" : 8,
		"RANGE" : 2
	},
}

    def initialize_rooms(self):
        room_1_1 = Room(self, "1_1", "Dragon")
        print(room_1_1.name)

    def attack(self):
        """attack action"""
        print("attack")

    def cower(self):
        """Cower action"""
        print("cower in a corner")
 
    def stats_check(self):
        """show your player stats during game"""
        print(f"{self.name}, your stats are:\n"
              f"Age: {self.age}\n"
              f"Type: {self.type}\n"
              f"Life: {self.life}\n"
              f"Pack: {self.pack}\n"
              f"Weapons: {self.weapons}\n"
              f"Keys: {self.keys}\n"
        )
    
    def transfer_weapon(self):
        self.weapons["AXE"] = self.weapon_choices["AXE"]
        print("weapon transfered")

    def init_weapons(self):
        """initial 3x weapons to start game AUTO RUN """
        increment = 0
        while 2 >= len(self.weapons):
            print("These are your weapon choices")
            weapon_number = increment + 1
            for i in self.weapon_choices.keys():
                print(i.title())
            weapon_1 = input(f"Choose weapon number {weapon_number} > ")
            try:
                if weapon_1.strip().lower() == self.weapon_choices["AXE"]["NAME"]:
                    self.weapons["AXE"] = self.weapon_choices["AXE"]
                    del self.weapon_choices["AXE"]
                    increment += 1
            except NameError:
                print("That weapon isn't here you fool!")
            except KeyError:
                pass
            try:
                if weapon_1.strip().lower() == self.weapon_choices["MACE"]["NAME"]:
                    self.weapons["MACE"] = self.weapon_choices["MACE"]
                    del self.weapon_choices["MACE"]
                    increment += 1
            except NameError:
                print("That weapon isn't here you fool!")
            except KeyError:
                pass
            try:
                if weapon_1.strip().lower() == self.weapon_choices["SWORD"]["NAME"]:
                    self.weapons["SWORD"] = self.weapon_choices["SWORD"]
                    del self.weapon_choices["SWORD"]
                    increment += 1
            except NameError:
                print("That weapon isn't here you fool!")
            except KeyError:
                pass
            try:
                if weapon_1.strip().lower() == self.weapon_choices["LANCE"]["NAME"]:
                    self.weapons["LANCE"] = self.weapon_choices["LANCE"]
                    del self.weapon_choices["LANCE"]
                    increment += 1
            except NameError:
                print("That weapon isn't here you fool!")
            except KeyError:
                pass
            try:
                if weapon_1.strip().lower() == self.weapon_choices["BOW"]["NAME"]:
                    self.weapons["BOW"] = self.weapon_choices["BOW"]
                    del self.weapon_choices["BOW"]
                    increment += 1
            except NameError:
                print("That weapon isn't here you fool!")
            except KeyError:
                pass
            try:
                if weapon_1.strip().lower() == self.weapon_choices["DAGGER"]["NAME"]:
                    self.weapons["DAGGER"] = self.weapon_choices["DAGGER"]
                    del self.weapon_choices["DAGGER"]
                    increment += 1
            except NameError:
                print("That weapon isn't here you fool!")
            except KeyError:
                pass
            try:
                if weapon_1.strip().lower() == self.weapon_choices["HAMMER"]["NAME"]:
                    self.weapons["HAMMER"] = self.weapon_choices["HAMMER"]
                    del self.weapon_choices["HAMMER"]
                    increment += 1
            except NameError:
                print("That weapon isn't here you fool!")
            except KeyError:
                pass
    
    def weapons_check(self):
        """weapon to attack with"""
        print("What Weapon do you choose to attack with?")
        print("My Weapons")
        for i in self.weapons.keys():
            print(i)
        pack_list = list(self.weapons)
        while True:
            weapon_of_choice = input(">>>  ").strip().upper()
            try:
                if weapon_of_choice == pack_list[0] or weapon_of_choice == pack_list[1] or weapon_of_choice == pack_list[2]:
                    print("great choice")
                    break
                else:
                    print("you dont have that")
            except IndexError:
                print("you dont have that!")
                pass
        return weapon_of_choice.upper()

will = Player("will")
will.initialize_rooms()