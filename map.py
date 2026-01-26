class Map:
    def Get_Map_From_Type(self,type_index):
        bettermap = []
        temp = []

        with open("types.txt", "r", encoding="UTF-8") as file:
            for i in file:
                row = i.strip().split("@")
                temp.append(row)

                if row.count('') == 2:
                    bettermap.append(temp)
                    temp = []

        return bettermap[type_index]
