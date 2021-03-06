import random
import pprint


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4M'


class Person:
    def __init__(self, hp, mp, atk, dfc, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkh = atk + 10
        self.atkl = atk - 10
        self.dfc = dfc
        self.magic = magic
        self.actions =["Attack", "Magic", "Items"]
        self.items = items

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.hp = 0
        return self.hp

    def heal(self,dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp (self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print(bcolors.OKGREEN + bcolors.BOLD + "ACTIONS" + bcolors.ENDC)
        for item in self.actions:
            print("    " + str(i) + ".", item)
            i += 1

    def choose_magic(self):
        i = 0
        for spell in self.magic:
            i += 1
            print("    " + str(i) + ".", spell.name, "(cost:", str(spell.cost), ")")

    def choose_item(self):
        i = 1

        print("\n" +bcolors.OKGREEN + bcolors.BOLD + "ITEMS" + bcolors.ENDC)
        for item in self.items:
            print("    " + str(i) + ".", item.name, ":", item.description, " (x5)")
            i += 1