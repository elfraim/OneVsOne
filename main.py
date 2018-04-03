from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import sys
import os
import time

#Magic spells
fireBall = Spell("FireBall", 10, 100, "black")
thunder = Spell("Thunder Strike", 9, 90, "black")
blizzard = Spell("Blizzard", 8, 80, "black")
meteor = Spell("Meteor", 20, 180, "black")
quake = Spell("Earth Quake", 15, 140, "black")

#White magic
cure = Spell("Cure", 12, 120, "white")
greaterCure = Spell("Greater Cure", 18, 200, "white")

## Create items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
big_potion = Item("Big-Potion", "potion", "Heals 100 HP", 100)
super_potion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixer_potion = Item("Red Elixer", "elixer", "Heals 100% HP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 Damage", 500)

player_spells = [fireBall, thunder, blizzard, meteor, quake, cure, greaterCure]
player_items = [potion, big_potion, super_potion, elixer_potion, grenade]

#people
player = Person(460, 65, 60, 34, player_spells, player_items)
enemy = Person(1200, 65, 45, 25, [], [])

running = True

print(bcolors.FAIL + bcolors.BOLD + "An Enemy Attacks" + bcolors.ENDC)

while running:
    print("===============")
    player.choose_action()
    choice = input("Choose Action:")
    index = int(choice) - 1
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "Damage")
        os.system('cls')
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose Magic:")) - 1
        if magic_choice == -1:
            continue

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_dmg()

        current_mp = player.get_mp()
        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP" + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)
        if spell.type == "white":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " Heals for", str(magic_dmg), "HP" + bcolors.ENDC)
            time.sleep(3)
            os.system('cls')
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\nYou cast " + spell.name + " for", str(magic_dmg),"points of damage" + bcolors.ENDC)
            time.sleep(3)
            os.system('cls')

    elif index == 2:
        player.choose_item()
        item_choice = int(input("Choose item: ")) - 1

        if item_choice == -1:
            continue
        item = player.items[item_choice]
        if item.type == "potion":
            player.heal(item.prop)
            print(bcolors.OKGREEN + "\n" + item.name + " Heals for ", str(item.prop), "HP" + bcolors.ENDC)

        elif item.type == "elixer":
            player.hp = player.maxhp
            print(bcolors.OKGREEN + "\n" + item.name + " Heals for 100% HP" + bcolors.ENDC)
        elif item.type == "attack":
            enemy.take_damage(item.prop)
            print(bcolors.FAIL + "\n" + item.name + " dealt", str(item.prop), "Damage" + bcolors.ENDC)
    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)

    print("Enemy attacks for " + bcolors.FAIL + str(enemy_dmg) + bcolors.ENDC, "Damage")

    print("-------------------------")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC)
    print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Your enemy has defeted you!" + bcolors.ENDC)
