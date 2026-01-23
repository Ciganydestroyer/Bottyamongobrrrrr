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
    def __init__(self,x,y,mapx,mapy,inventory,money):
        self.x = x
        self.y = y
        self.mapx = mapx
        self.mapy = mapy
        self.inventory = inventory
        self.money = money

player = Player(16, 24, 0, 0, None, 0)

def Game_Start():
    print("Before anything starts what will your Bottyamon name will be?")
    name = input()

    Game_Render()

    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'w':
                player.x -= 1
            if key == b'a':
                player.y -= 1
            if key == b's':
                player.x += 1
            if key == b'd':
                player.y += 1

            Game_Render()




def Game_Render():
    clear = lambda: os.system('cls')
    clear()

    game_map = Map()
    grid = game_map.Parse_Map_Electric_Bogoloo()[0]

    for row_index, row in enumerate(grid):
        line = row[0]  # extract the actual string

        if row_index == player.x:
            line = line[:player.y] + '🧑' + line[player.y + 1:]

        print(line)