from button import Buttons
from world import Game_Start
import msvcrt
import os

def renderer():
    os.system("cls")

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

Quit = Buttons("QUIT",20,5,False)

Current_Menu = [Start,Options,Quit]


renderer()

while True:
    if msvcrt.kbhit():
        key = msvcrt.getch()

        if key in (b'\x00', b'\xe0'): # UP and DOWN arrowkeys
            key = msvcrt.getch()

            if key == b'H': #UP
                for i in range(len(Current_Menu)):
                    if Current_Menu[i].default:
                        Current_Menu[i].default = False
                        Current_Menu[i - 1].default = True
                        break

            if key == b'P': #DOWN
                for i in range(len(Current_Menu)):
                    if Current_Menu[i].default:
                        Current_Menu[i].default = False
                        if i == len(Current_Menu) - 1:
                            Current_Menu[0].default = True
                        else:
                            Current_Menu[i + 1].default = True
                        break

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

            if text.startswith("START"):
                Game_Start()
                exit(0)
            if text.startswith("OPTIONS"):
                pass
            if text.startswith("QUIT"):
                exit(0)

        renderer()
