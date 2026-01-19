from button import Buttons
import msvcrt
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
    ##clear = lambda: os.system('cls')
    ##clear()

    for i in range(0, len(Current_Menu)):
        if (Current_Menu[i].default == True):
            if(Current_Menu[i].text.count("<=") > 0):
                continue
            else:
                Current_Menu[i].text += " <="
        else:
            Current_Menu[i].text = Current_Menu[i].text.replace(" <=", "")

    Bottyamon_MainTitle()
    Start.Align_Center()
    Start.CreateButton()
    Options.Align_Center()
    Options.CreateButton()
    Quit.Align_Center()
    Quit.CreateButton()


def Bottyamon_MainTitle():
    print("\n")
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


Options = Buttons("OPTIONS",20,5,False)
Options.Align_Center()
Options.CreateButton()

Quit = Buttons("QUIT",20,5,False)
Quit.Align_Center()
Quit.CreateButton()

Current_Menu = [Start,Options,Quit]


renderer()

while True:
    if msvcrt.kbhit():
        key = msvcrt.getch()
        print(key)
        if key == b'q':
            exit(0)

        if key == b's':
            for i in range(0, len(Current_Menu)):
                if (Current_Menu[i].default == True):
                    Current_Menu[i].default = False
                    if(i == len(Current_Menu) - 1):
                        Current_Menu[0].default = True
                    else:
                        Current_Menu[i + 1].default = True
                    break

        if key == b'w':
            for i in range(0, len(Current_Menu)):
                if (Current_Menu[i].default == True):
                    Current_Menu[i].default = False
                    Current_Menu[i - 1].default = True
                    break

        if key == b'\r':
            text = ""

            for i in range(0, len(Current_Menu)):
                if (Current_Menu[i].default == True):
                    text = Current_Menu[i].text

            if(text == "START"):
                pass
                ##TODO: Start a game from another file
            if(text == "OPTIONS"):
                pass
                ##TODO: Add so u can change the controls
            if text.startswith("QUIT"):
                exit(0)

        renderer()
