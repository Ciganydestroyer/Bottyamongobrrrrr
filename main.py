from button import Buttons
import packages.keyboard
from packages.colorama import Fore,Back,init
init(autoreset=True)
import time
import os

class Player:
    def __init__(self, hp, attack, defense, speed, critchance, lvl):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.critchance = critchance
        self.lvl = lvl

def renderer():
    clear = lambda: os.system('cls')
    clear()

    Bottyamon_MainTitle()
    Start.Align_Center()
    Start.CreateButton()
    TEST1.Align_Center()
    TEST1.CreateButton()
    TEST2.Align_Center()
    TEST2.CreateButton()

def Bottyamon_MainTitle():
    print(r"+-------------------------------------------------------------------------------------------------------+")
    print(r"|                                                                                                       |")
    print(r"|      /$$$$$$$              /$$     /$$                                                                |")
    print(r"|     | $$__  $$            | $$    | $$                                                                |")
    print(r"|     | $$  \ $$  /$$$$$$  /$$$$$$ /$$$$$$   /$$   /$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$$$$$$       |")
    print(r"|     | $$$$$$$  /$$__  $$|_  $$_/|_  $$_/  | $$  | $$ |____  $$| $$_  $$_  $$ /$$__  $$| $$__  $$      |")
    print(r"|     | $$__  $$| $$  \ $$  | $$    | $$    | $$  | $$  /$$$$$$$| $$ \ $$ \ $$| $$  \ $$| $$  \ $$      |")
    print(r"|     | $$  \ $$| $$  | $$  | $$ /$$| $$ /$$| $$  | $$ /$$__  $$| $$ | $$ | $$| $$  | $$| $$  | $$      |")
    print(r"|     | $$$$$$$/|  $$$$$$/  |  $$$$/|  $$$$/|  $$$$$$$|  $$$$$$$| $$ | $$ | $$|  $$$$$$/| $$  | $$      |")
    print(r"|     |_______/  \______/    \___/   \___/   \____  $$ \_______/|__/ |__/ |__/ \______/ |__/  |__/      |")
    print(r"|                                            /$$  | $$                                                  |")
    print(r"|                                           |  $$$$$$/                                                  |")
    print(r"|                                            \______/                                                   |")
    print(r"|                                                                                                       |")
    print(r"+-------------------------------------------------------------------------------------------------------+")
    print("\n")

Bottyamon_MainTitle()

Start = Buttons("START",20,5,True)


TEST1 = Buttons("OPTIONS",20,5,False)
TEST1.Align_Center()
TEST1.CreateButton()

TEST2 = Buttons("QUIT",20,5,False)
TEST2.Align_Center()
TEST2.CreateButton()

Current_Menu = [Start,TEST1,TEST2]

for i in range(0, len(Current_Menu)):
    if(Current_Menu[i].default == True):
        Current_Menu[i].text += " <="
    else:
        Current_Menu[i].text.replace("<=","")


while True:
    renderer()
    time.sleep(0.5)
