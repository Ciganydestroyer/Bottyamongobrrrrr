import math

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
                print(" " * self.alignment + "|" + " " * math.ceil(self.x / 2) + self.text + " " * math.floor(self.x / 2) + "|")
            else:
                print(" " * self.alignment + "|" + " " * (self.x + len(self.text))  + "|")

        print("\n")

    def Align_Center(self):
        total_lenght = len("+" + "-" * (self.x + len(self.text)) + "+")
        self.alignment = math.floor((self.screenlength - total_lenght) / 2)

    def Align_Right(self):
        total_lenght = len("+" + "-" * (self.x + len(self.text)) + "+")
        self.alignment = self.screenlength - total_lenght