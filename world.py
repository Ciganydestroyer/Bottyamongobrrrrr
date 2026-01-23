from map import Map
import os
import msvcrt

class Bottyamon:
    def __init__(self, name, hp, attack, defense, speed, critchance, lvl):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.critchance = critchance
        self.lvl = lvl

class Player:
    def __init__(self,x,y,inventory,money):
        self.x = x
        self.y = y
        self.inventory = inventory
        self.money = money

def Game_Start():
    print("Before anything starts what will your Bottyamon name will be?")
    name = input()

    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()




def Game_Render():
    clear = lambda: os.system('cls')
    clear()

    test = Map()
    test1 = test.Parse_Map_Electric_Bogoloo()[0]
    for i in test1:
        print("".join(i))