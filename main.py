import math
import keyboard

class Player:
    def __init__(self, hp, attack, defense, speed, critchance, lvl):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.critchance = critchance
        self.lvl = lvl

class Buttons:
    screenlength = 105
    alignment = 0

    def __init__(self,text,x,y,isdefault):
        self.text = text
        self.x = x
        self.y = y
        self.default = isdefault

    def CreateButton(self):
        for i in range(0,self.y):
            if(i == 0 or i == self.y - 1):
                print(" " * self.alignment + "+" + "-" * (self.x + len(self.text)) + "+")
            elif(i == math.floor(self.y / 2)):
                print(" " * self.alignment + "|" + " " * math.floor(self.x / 2) + self.text + " " * math.ceil(self.x / 2) + "|")
            else:
                print(" " * self.alignment + "|" + " " * (self.x + len(self.text))  + "|")

        print("\n")

    def Align_Center(self):
        total_lenght = len("+" + "-" * (self.x + len(self.text)) + "+")
        self.alignment = math.floor((self.screenlength - total_lenght) / 2)

    def Align_Right(self):
        total_lenght = len("+" + "-" * (self.x + len(self.text)) + "+")
        self.alignment = self.screenlength - total_lenght





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


Start = Buttons("START",15,5,True)

Start.Align_Center()
Start.CreateButton()

Settings = Buttons("SETTINGS",15,5,False)

Settings.Align_Center()
Settings.CreateButton()

Quit = Buttons("QUIT",15,5,False)

Quit.Align_Center()
Quit.CreateButton()

