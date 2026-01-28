import random

from map import Map
import os
import msvcrt


class Bottyamon:
    def __init__(self, name, type, hp, maxhp, attack, defense, speed, critchance, lvl):
        self.name = name
        self.type = type
        self.hp = hp
        self.maxhp = maxhp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.critchance = critchance
        self.lvl = lvl

    def to_dict(self):
        return {
            "name": self.name,
            "type": self.type,
            "hp": self.hp,
            "maxhp": self.maxhp,
            "attack": self.attack,
            "defense": self.defense,
            "speed": self.speed,
            "critchance": self.critchance,
            "lvl": self.lvl
        }

    def Damange(self):
        numbah = random.randint(1,100)

        crit = False

        if(self.critchance > numbah):
            crit = True

        if(crit):
            return self.attack * 2
        else:
            return self.attack

class Player:
    def __init__(self,x,y,mapx,mapy,inventory,money):
        self.x = x
        self.y = y
        self.mapx = mapx
        self.mapy = mapy
        self.inventory = inventory
        self.money = money

    def to_dict(self):
        return {
            "x": self.x,
            "y": self.y,
            "mapx": self.mapx,
            "mapy": self.mapy,
            "inventory": self.inventory,
            "money": self.money
        }

player = Player(0,0,0,0,{},0)
Bottyamons = []

Status = "GAME"

def Game_Start():
    global Status

    Status = "PREGAME"

    Game_Render()

    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'w' and can_move(player.x - 1, player.y):
                player.x -= 1
            if key == b's' and can_move(player.x + 1, player.y):
                player.x += 1
            if key == b'a' and can_move(player.x, player.y - 1):
                player.y -= 1
            if key == b'd' and can_move(player.x, player.y + 1):
                player.y += 1

            if key == b'e':
                for i in range(-3, 3):
                    for j in range(-3, 3):
                        tile = tile_at(player.x + i, player.y + j)
                        if tile == '🚪':
                            doorx = player.x + i
                            doory = player.y + j
                            if doorx == 25 and doory == 66:
                                Status = "SHOP"

            if key == b'i':
                for i in player.inventory:
                    print(i, player.inventory[i])


            grid = len(actual_map[player.mapx][player.mapy])

            debounce = True

            if player.x == 0 and debounce:
                debounce = False
                player.mapx -= 1

                new_grid = len(actual_map[player.mapx][player.mapy])

                if new_grid == grid:
                    player.x = grid - 3
                else:
                    player.x = new_grid - 3
                    if(new_grid > 25):
                        player.y += int(new_grid / 2) + 3
                    else:
                        player.y -= int(new_grid / 2) + 12 #Btw new_grid has no relation to the length but if it works don't touch it


            if player.x == grid - 2 and debounce:
                debounce = False
                player.mapx += 1
                player.x = 1

                new_grid = len(actual_map[player.mapx][player.mapy])

                if new_grid != grid:
                    if (new_grid > 25):
                        player.y += int(new_grid / 2) + 3
                    else:
                        player.y -= int(new_grid / 2) + 12

            if player.y == 1 and debounce:
                debounce = False
                player.mapy -= 1

                map_length = 0
                new_grid = len(actual_map[player.mapx][player.mapy])

                if (new_grid == 19):
                    map_length = 50
                else:
                    map_length = 100

                player.y = map_length - 3

                if new_grid != grid:
                    if (new_grid > 25):
                        player.x += 8
                    else:
                        player.x -= 8

            if (grid == 19):
                map_length = 50
            else:
                map_length = 100


            if player.y == map_length - 2 and debounce:
                player.mapy += 1
                player.y = 2

                new_grid = len(actual_map[player.mapx][player.mapy])

                if new_grid != grid:
                    if (new_grid > 25):
                        player.x += 8
                    else:
                        player.x -= 8

            tile = tile_at(player.x, player.y)
            if tile == '🟩':
                szam = random.randint(1,10)

                if(szam == 1):
                    from combat import Combat
                    Combat()

            Game_Render()

game_map = Map()
actual_map = [[None,game_map.Get_Map_From_Type(15),game_map.Get_Map_From_Type(8),None,None,game_map.Get_Map_From_Type(7),game_map.Get_Map_From_Type(17),None],
              [game_map.Get_Map_From_Type(7),game_map.GRASS(1),game_map.Get_Map_From_Type(16),game_map.Get_Map_From_Type(5),game_map.GRASS(5),game_map.Get_Map_From_Type(18),None,game_map.Get_Map_From_Type(13)],
              [game_map.Get_Map_From_Type(20),None,game_map.Get_Map_From_Type(11),None,None,game_map.Get_Map_From_Type(2),game_map.GRASS(5),game_map.Get_Map_From_Type(19)],
              [game_map.GRASS(2),game_map.Get_Map_From_Type(12),None,None,game_map.GRASS(7),game_map.Get_Map_From_Type(4),None,None],
              [game_map.Get_Map_From_Type(11),None,None,game_map.Get_Map_From_Type(21),game_map.Get_Map_From_Type(1),game_map.Get_Map_From_Type(10),None,None]]

def Game_Render():
    global Status, player, Bottyamons

    os.system("cls")

    if Status == "PREGAME":

        file_path = "save.json"

        if not os.path.exists(file_path):
            player.x = 9
            player.y = 25
            player.mapx = 4
            player.mapy = 0
            player.inventory = {"Bottyaball": 5}
            player.money = 1000
            Bottyamons = []

            print("What would you like to name your Bottyamon?: ")
            name = input()

            while(name == ''):
                print("You didnt choose a name")
                name = input()

            #Fajták: Villám, Föld, Víz, Gáz, Sötétség, Árny, Kő, Tűz
            Types = ["Thunder","Earth","Water","Gas","Dark","Shadow","Rock","Fire"]

            Chooseable_Types = []

            for i in range(0,3):
                tipus = random.randint(0, len(Types) - 1)
                Chooseable_Types.append(Types[tipus])

                Types.remove(Types[tipus])

            print(" ".join(Chooseable_Types))

            Bottyamon_type = input("Choose a type: ")

            Vane = False

            while (Vane == False):
                for i in Chooseable_Types:
                    if(i == Bottyamon_type):
                        Vane = True
                if (Vane == False):
                    print("You didnt choose the correct type")
                    Bottyamon_type = input()

            hp = random.randint(10,50)

            Bottyamons.append(Bottyamon(name, Bottyamon_type, hp, hp,random.randint(1,10),random.randint(1,10),random.randint(1,10),100,1))

            print("Your first bottyamon stats are:")

            print(Bottyamons[0].hp)
            print(Bottyamons[0].attack)
            print(Bottyamons[0].defense)
            print(Bottyamons[0].speed)
            print(Bottyamons[0].lvl)

            input("Would you like to start your adventure?")
        else:
            from saves import read_save
            player, Bottyamons = read_save()

        Status = "GAME"



    if Status == "GAME":
        grid = actual_map[player.mapx][player.mapy]
        if grid is None:
            # Safety fallback: the current world cell has no map assigned
            print("Hiba: üres térképrészre kerültél (None). Visszaraklak a kezdőpontra.")
            player.x = 9
            player.y = 25
            player.mapx = 4
            player.mapy = 0
            grid = actual_map[player.mapx][player.mapy]

        for x, row in enumerate(grid):
            rendered_row = row.copy()

            if x == player.x:
                if 0 <= player.y < len(rendered_row):
                    rendered_row[player.y] = '🧑'

            print("".join(rendered_row))

    if Status == "SHOP":
        print("What would you like to buy?")

        print("-------------------------------")
        print("Your money:", player.money)
        print("-------------------------------")
        print("1 - Map - 100 Forint")
        print("2 - Perm. Stat up - 500 Forint")
        print("3 - Heal candy - 50 Forint")
        print("4 - Bottyaball - 25 Forint")
        print("5 - Back")

        UserInput = int(input())

        match(UserInput):
            case 1:
                if player.money > 100:
                    player.money -= 100
                    if('Map' in player.inventory):
                        player.inventory["Map"] += 1
                    else:
                        player.inventory["Map"] = 1
                else:
                    print("Ur a poor man get some money")
            case 2:
                if player.money > 500:
                    player.money -= 500
                    if ('Perm. Stat up' in player.inventory):
                        player.inventory["Perm. Stat up"] += 1
                    else:
                        player.inventory["Perm. Stat up"] = 1
                else:
                    print("Ur a poor man get some money")
            case 3:
                if player.money > 50:
                    player.money -= 50
                    if ('Heal candy' in player.inventory):
                        player.inventory["Heal candy"] += 1
                    else:
                        player.inventory["Heal candy"] = 1
                else:
                    print("Ur a poor man get some money")
            case 4:
                if player.money > 25:
                    player.money -= 25
                    if ('Bottyaball' in player.inventory):
                        player.inventory["Bottyaball"] += 1
                    else:
                        player.inventory["Bottyaball"] = 1
                else:
                    print("Ur a poor man get some money")
            case 5:
                Status = "GAME"
            case _:
                print("Invalid Input")

        Game_Render()




def tile_at(x, y):
    grid = actual_map[player.mapx][player.mapy]
    if grid is None:
        return None
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[x]):
        return None
    return grid[x][y]

def can_move(x, y):
    grid = actual_map[player.mapx][player.mapy]
    if grid is None:
        return False
    # bounds check
    if x < 0 or x >= len(grid):
        return False
    if y < 0 or y >= len(grid[x]):
        return False
    tile = grid[x][y]
    # allow walking only on these tiles
    return tile in (' ', '🟩', '⬜')
