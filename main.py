import math
import keyboard
from button import Buttons

class Player:
    def __init__(self, hp, attack, defense, speed, critchance, lvl):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.critchance = critchance
        self.lvl = lvl





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


Start = Buttons("START",20,5,True)

Start.Align_Center()
Start.CreateButton()

Settings = Buttons("SETTINGS",21,5,False)

Settings.Align_Center()
Settings.CreateButton()

Quit = Buttons("QUIT",21,5,False)

Quit.Align_Center()
Quit.CreateButton()

