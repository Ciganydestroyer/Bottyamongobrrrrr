import msvcrt
import os
import random

from button import Buttons
from saves import save
import world

Current_Menu = []

DEFAULT_FLAVOR_TEXT = "What would u like to do?"
Flavor_text = DEFAULT_FLAVOR_TEXT
Status = "MENU"
Turns = 0

Chosen_Bottyamon = 0

def load_last_save():
    global Turns, Status, Flavor_text

    from saves import read_save

    try:
        p, bottyamons = read_save("save.json")
        world.player = p
        world.Bottyamons = bottyamons
    except FileNotFoundError:
        # nincs mentés -> nincs mit betölteni
        pass

    Turns = 0
    Status = "MENU"
    Flavor_text = DEFAULT_FLAVOR_TEXT
    os.system("cls")
    world.Game_Render()

def _decrement_item(item_name: str) -> bool:
    inv = world.player.inventory
    if inv.get(item_name, 0) <= 0:
        return False
    inv[item_name] -= 1
    if inv[item_name] <= 0:
        del inv[item_name]
    return True

def build_menu():
    global Current_Menu, Status

    Current_Menu.clear()

    if Status == "MENU":
        Current_Menu.append(Buttons("ATTACK", 20, 5, True))
        Current_Menu.append(Buttons("ITEMS", 20, 5, False))
        Current_Menu.append(Buttons("SWITCH BOTTYAMON", 20, 5, False))
        Current_Menu.append(Buttons("RUN", 20, 5, False))
        return

    if Status == "ATTACK":
        Current_Menu.append(Buttons("NORMAL ATTACK", 20, 5, True))
        Current_Menu.append(Buttons("TYPE ATTACK", 20, 5, False))
        Current_Menu.append(Buttons("RETURN", 20, 5, False))
        return

    if Status == "ITEMS":
        inv = world.player.inventory if hasattr(world, "player") else {}
        heal_count = inv.get("Heal candy", 0)
        stat_count = inv.get("Perm. Stat up", 0)
        ball_count = inv.get("Bottyaball", 0)

        Current_Menu.append(Buttons(f"HEAL CANDY ({heal_count})", 24, 5, True))
        Current_Menu.append(Buttons(f"PERM. STAT UP ({stat_count})", 24, 5, False))
        Current_Menu.append(Buttons(f"BOTTYABALL ({ball_count})", 24, 5, False))
        Current_Menu.append(Buttons("RETURN", 20, 5, False))
        return

    if Status == "SWITCH":
        # Bottyamon választó menü névvel
        for idx, b in enumerate(world.Bottyamons):
            label = f"{idx+1}. {b.name}"
            Current_Menu.append(Buttons(label, 30, 5, idx == Chosen_Bottyamon))
        Current_Menu.append(Buttons("RETURN", 20, 5, False))
        return

def Combat():
    global Current_Menu, Turns, Flavor_text, Status, Enemy_Bottyamon, Chosen_Bottyamon

    if(Turns == 0):
        Types = ["Thunder", "Earth", "Water", "Gas", "Dark", "Shadow", "Rock", "Fire"]

        hp = random.randint(10,50)

        lvl = world.Bottyamons[Chosen_Bottyamon].lvl - 1

        Enemy_Bottyamon = world.Bottyamon("ENEMY",Types[random.randint(0, len(Types) - 1)], hp + 1 * (lvl / 10), hp + 1 * (lvl / 10) , random.randint(1,10) + 1 * (lvl / 10), random.randint(1,10) + 1 * (lvl / 10), random.randint(1,10) + 1 * (lvl / 10), random.randint(1,100), lvl )

    Turns += 1

    build_menu()
    combat_renderer()

    while True:
        if Status == "WON":
            b = world.Bottyamons[Chosen_Bottyamon]
            b.lvl += 1
            b.maxhp = int(round(b.maxhp * 1.1))
            b.attack = int(round(b.attack * 1.1))
            b.defense = int(round(b.defense * 1.1))
            b.speed = int(round(b.speed * 1.1))

            # Pénzjutalom győzelemért (100-250)
            reward = random.randint(100, 250)
            world.player.money += reward

            save()

            print(f"U won! You got {reward} money. Press enter to continue")
            input()
            Turns = 0
            Status = "MENU"
            Flavor_text = DEFAULT_FLAVOR_TEXT
            os.system("cls")
            world.Game_Render()
            return

        if Status == "RAN":
            print("U manage to ran away. Press enter to continue")
            input()
            Turns = 0
            Status = "MENU"
            Flavor_text = DEFAULT_FLAVOR_TEXT
            os.system("cls")
            world.Game_Render()
            return

        if Status == "CAUGHT":
            print("You caught the Bottyamon! Press enter to continue")
            input()
            Turns = 0
            Status = "MENU"
            Flavor_text = DEFAULT_FLAVOR_TEXT
            os.system("cls")
            world.Game_Render()
            return

        if msvcrt.kbhit():
            key = msvcrt.getch()

            if key in (b'\x00', b'\xe0'):  # UP and DOWN arrowkeys
                key = msvcrt.getch()

                if key == b'H':  # UP
                    for i in range(len(Current_Menu)):
                        if Current_Menu[i].default:
                            Current_Menu[i].default = False
                            Current_Menu[i - 1].default = True
                            break

                if key == b'P':  # DOWN
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
                        if (i == len(Current_Menu) - 1):
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

                if text.startswith("ATTACK"):
                    Status = "ATTACK"
                if text.startswith("ITEMS"):
                    Status = "ITEMS"
                if text.startswith("SWITCH BOTTYAMON"):
                    Status = "SWITCH"
                if text.startswith("RUN"):
                    chance = random.randint(1,10)

                    if chance < 4:
                        Status = "RAN"
                        save()
                    else:
                        Flavor_text = "You didnt manage to run away"
                if text.startswith("NORMAL ATTACK"):
                    fight_resolve(False)
                if text.startswith("TYPE ATTACK"):
                    fight_resolve(True)

                if text.startswith("HEAL CANDY"):
                    if world.player.inventory.get("Heal candy", 0) > 0:
                        b = world.Bottyamons[Chosen_Bottyamon]
                        b.hp = b.maxhp
                        _decrement_item("Heal candy")
                        Flavor_text = "Full heal!"
                        save()
                    else:
                        Flavor_text = "You don't have Heal candy"

                if text.startswith("PERM. STAT UP"):
                    if world.player.inventory.get("Perm. Stat up", 0) > 0:
                        b = world.Bottyamons[Chosen_Bottyamon]
                        stat = random.choice(["maxhp", "attack", "defense", "speed"])
                        if stat == "maxhp":
                            b.maxhp += 5
                            b.hp = min(b.hp + 5, b.maxhp)
                            Flavor_text = "Perm. Stat up: +5 maxhp"
                        else:
                            setattr(b, stat, getattr(b, stat) + 1)
                            Flavor_text = f"Perm. Stat up: +1 {stat}"

                        _decrement_item("Perm. Stat up")
                        save()
                    else:
                        Flavor_text = "You don't have Perm. Stat up"

                if text.startswith("BOTTYABALL"):
                    if world.player.inventory.get("Bottyaball", 0) > 0:
                        _decrement_item("Bottyaball")
                        # 50% esély a befogásra
                        if random.random() < 0.5:
                            os.system("cls")
                            print("You caught it! Name your new Bottyamon:")
                            new_name = input().strip()
                            while new_name == "":
                                print("Name can't be empty. Try again:")
                                new_name = input().strip()

                            # Új Bottyamon: az enemy statjaival, a player által adott névvel
                            caught = world.Bottyamon(
                                new_name,
                                Enemy_Bottyamon.type,
                                Enemy_Bottyamon.hp,
                                Enemy_Bottyamon.maxhp,
                                Enemy_Bottyamon.attack,
                                Enemy_Bottyamon.defense,
                                Enemy_Bottyamon.speed,
                                Enemy_Bottyamon.critchance,
                                Enemy_Bottyamon.lvl,
                            )
                            world.Bottyamons.append(caught)
                            save()
                            Flavor_text = "Caught!"
                            Status = "CAUGHT"
                        else:
                            Flavor_text = "It broke free!"
                            save()
                    else:
                        Flavor_text = "You don't have Bottyaball"

                if text.startswith("RETURN"):
                    Status = "MENU"

                # SWITCH menü: Bottyamon kiválasztás név alapján
                if Status == "SWITCH":
                    # gomb formátum: "N. Name"
                    if text[0:1].isdigit() and "." in text:
                        try:
                            idx = int(text.split(".", 1)[0]) - 1
                            if 0 <= idx < len(world.Bottyamons):
                                Chosen_Bottyamon = idx
                                Flavor_text = f"Switched to {world.Bottyamons[idx].name}"
                                Status = "MENU"
                        except ValueError:
                            pass

                # Állapotváltás után új menü
                build_menu()
            combat_renderer()

def combat_renderer():
    os.system('cls')

    print(Flavor_text)

    for i in range(0, len(Current_Menu)):
        if (Current_Menu[i].default == True):
            if (Current_Menu[i].text.count("<=") > 0):
                continue
            else:
                Current_Menu[i].text += " <="
        else:
            Current_Menu[i].text = Current_Menu[i].text.replace(" <=", "")

    for i in range(len(Current_Menu)):
        Current_Menu[i].Align_Center()
        Current_Menu[i].CreateButton()

    print("Your Bottyamon HP: ")
    print(world.Bottyamons[Chosen_Bottyamon].hp,"/",world.Bottyamons[Chosen_Bottyamon].maxhp)
    print("Enemy's HP: ")
    print(Enemy_Bottyamon.hp,"/",Enemy_Bottyamon.maxhp)

def fight_resolve(special):
    global Flavor_text, Turns, Status

    Turns += 1

    if(not special):
        if(Enemy_Bottyamon.speed > world.Bottyamons[Chosen_Bottyamon].speed):
            world.Bottyamons[Chosen_Bottyamon].hp -= Enemy_Bottyamon.Damange()

            if(0 >= world.Bottyamons[Chosen_Bottyamon].hp):
                print("You lost! Loading last save...")
                input()
                load_last_save()
                Status = "RAN"
                return

            Enemy_Bottyamon.hp -= world.Bottyamons[Chosen_Bottyamon].Damange()

            if (0 >= Enemy_Bottyamon.hp):
                save()
                Status = "WON"
                return
        else:
            Enemy_Bottyamon.hp -= world.Bottyamons[Chosen_Bottyamon].Damange()

            if (0 >= Enemy_Bottyamon.hp):
                save()
                Status = "WON"
                return

            world.Bottyamons[Chosen_Bottyamon].hp -= Enemy_Bottyamon.Damange()

            if (0 >= world.Bottyamons[Chosen_Bottyamon].hp):
                print("You lost! Loading last save...")
                input()
                load_last_save()
                Status = "RAN"
                return
    else:

        TypeChart = {
            "Thunder": {"strong": "Water", "weak": "Earth"},
            "Earth": {"strong": "Thunder", "weak": "Water"},
            "Water": {"strong": "Fire", "weak": "Thunder"},
            "Fire": {"strong": "Rock", "weak": "Water"},
            "Rock": {"strong": "Gas", "weak": "Fire"},
            "Gas": {"strong": "Earth", "weak": "Shadow"},
            "Shadow": {"strong": "Dark", "weak": "Fire"},
            "Dark": {"strong": "Thunder", "weak": "Shadow"}
        }

        attacker_type = world.Bottyamons[Chosen_Bottyamon].type

        defender_type = Enemy_Bottyamon.type

        if (Enemy_Bottyamon.speed > world.Bottyamons[Chosen_Bottyamon].speed):
            if defender_type == TypeChart[attacker_type]["strong"]:
                world.Bottyamons[Chosen_Bottyamon].hp -= Enemy_Bottyamon.Damange() * 2
                Flavor_text = "The Enemies attack was strong against you"
            elif defender_type == TypeChart[attacker_type]["weak"]:
                Flavor_text = "The Enemies attack was weak against you"
                world.Bottyamons[Chosen_Bottyamon].hp -= Enemy_Bottyamon.Damange() * 0.5
            else:
                world.Bottyamons[Chosen_Bottyamon].hp -= Enemy_Bottyamon.Damange()


            if (0 >= world.Bottyamons[Chosen_Bottyamon].hp):
                print("You lost! Loading last save...")
                input()
                load_last_save()
                Status = "RAN"
                return


            if attacker_type == TypeChart[defender_type]["strong"]:
                Enemy_Bottyamon.hp -= world.Bottyamons[Chosen_Bottyamon].Damange() * 2
                Flavor_text = "Your attack was strong againts the enemy"
            elif attacker_type == TypeChart[defender_type]["weak"]:
                Flavor_text = "Your attack was weak againts the enemy"
                Enemy_Bottyamon.hp -= world.Bottyamons[Chosen_Bottyamon].Damange() * 0.5
            else:
                Enemy_Bottyamon.hp -= world.Bottyamons[Chosen_Bottyamon].Damange()


            if (0 >= Enemy_Bottyamon.hp):
                save()
                Status = "WON"
                return
        else:

            if attacker_type == TypeChart[defender_type]["strong"]:
                Enemy_Bottyamon.hp -= world.Bottyamons[Chosen_Bottyamon].Damange() * 2
                Flavor_text = "Your attack was strong againts the enemy"
            elif attacker_type == TypeChart[defender_type]["weak"]:
                Flavor_text = "Your attack was weak againts the enemy"
                Enemy_Bottyamon.hp -= world.Bottyamons[Chosen_Bottyamon].Damange() * 0.5
            else:
                Enemy_Bottyamon.hp -= world.Bottyamons[Chosen_Bottyamon].Damange()

            if (0 >= Enemy_Bottyamon.hp):
                save()
                Status = "WON"
                return

            if defender_type == TypeChart[attacker_type]["strong"]:
                world.Bottyamons[Chosen_Bottyamon].hp -= Enemy_Bottyamon.Damange() * 2
                Flavor_text = "The Enemies attack was strong against you"
            elif defender_type == TypeChart[attacker_type]["weak"]:
                Flavor_text = "The Enemies attack was weak against you"
                world.Bottyamons[Chosen_Bottyamon].hp -= Enemy_Bottyamon.Damange() * 0.5
            else:
                world.Bottyamons[Chosen_Bottyamon].hp -= Enemy_Bottyamon.Damange()

            if (0 >= world.Bottyamons[Chosen_Bottyamon].hp):
                print("You lost! Loading last save...")
                input()
                load_last_save()
                Status = "RAN"
                return


    # Kör vége: vissza a menübe, a fő Combat loop majd újrarajzol.
    Status = "MENU"
    return