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

player = Player(9, 25, 4, 0, None, 0)

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

            grid = len(actual_map[player.mapx][player.mapy])

            #TODO: Add the fucking movement im tired

            Game_Render()
            print(grid)


game_map = Map()
actual_map = [[None,game_map.Get_Map_From_Type(15),game_map.Get_Map_From_Type(8),None,None,game_map.Get_Map_From_Type(7),game_map.Get_Map_From_Type(17),None],
              [game_map.Get_Map_From_Type(7),game_map.Get_Map_From_Type(1),game_map.Get_Map_From_Type(16),game_map.Get_Map_From_Type(5),game_map.Get_Map_From_Type(5),game_map.Get_Map_From_Type(18),None,game_map.Get_Map_From_Type(13)],
              [game_map.Get_Map_From_Type(20),None,game_map.Get_Map_From_Type(11),None,None,game_map.Get_Map_From_Type(2),game_map.Get_Map_From_Type(5),game_map.Get_Map_From_Type(19)],
              [game_map.Get_Map_From_Type(2),game_map.Get_Map_From_Type(12),None,None,game_map.Get_Map_From_Type(7),game_map.Get_Map_From_Type(4),None,None],
              [game_map.Get_Map_From_Type(11),None,None,game_map.Get_Map_From_Type(21),game_map.Get_Map_From_Type(1),game_map.Get_Map_From_Type(10),None,None]]

def Game_Render():
    clear = lambda: os.system('cls')
    clear()
    grid = actual_map[player.mapx][player.mapy]

    for row_index, row in enumerate(grid):
        line = row[0]  # extract the actual string

        if row_index == player.x:
            line = line[:player.y] + '🧑' + line[player.y + 1:]

        print(line)