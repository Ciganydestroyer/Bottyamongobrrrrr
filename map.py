import regex

class Map:
    def Get_Map_From_Type(self, type_index):
        maps = []
        current = []

        with open("types.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.rstrip("\n")

                if line == "@":
                    maps.append(current)
                    current = []
                else:
                    # split into REAL emoji tiles
                    tiles = regex.findall(r"\X", line)
                    current.append(tiles)

        return maps[type_index]

    def GRASS(self, type_index):
        map = self.Get_Map_From_Type(type_index)

        return self.fill_from_center(map)

    def fill_from_center(self,grid):
        rows = len(grid)
        cols = len(grid[0])

        start_r = rows // 2
        start_c = cols // 2

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            if grid[r][c] == "|" or grid[r][c] == "🟩" or grid[r][c] == "-" or grid[r][c] == "+" or grid[r][c] == "⬜":
                return

            grid[r][c] = "🟩"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(start_r, start_c)
        return grid
