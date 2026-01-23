class Map:
    def Parse_Map(self):
        file = open("types.txt","r")

        map = []

        for i in file:
            map.append(i.replace("\n","").split("@"))


        return map

    def Parse_Map_Electric_Bogoloo(self):
        map = self.Parse_Map()
        bettermap = []
        temp = []

        for i in map:
            temp.append(i)
            if(i.count('') == 2):
                bettermap.append(temp)
                temp = []

        return bettermap
