import numpy as np
import colorama

# Sandpile unequal maxes exception
class UnequalMaxesException(Exception):
    "Raised when two combined sandpiles have different maxes"
    pass

# Sandpile unequal sizes exception
class UnequalSizesException(Exception):
    "Raised when two combined sandpiles have different sizes"
    pass

class Sandpile:
    Max = -1
    height = -1
    width = -1
    values = []

    def __init__(self, Max, height, width, values):
        self.Max = Max
        self.height = height
        self.width = width
        self.values = values

    def getMax(self):
        return self.Max
        
    def getHeight(self):
        return self.height
        
    def getWidth(self):
        return self.width

    def getValues(self):
        return self.values

    def __add__(self, o):
        try:
            if self.Max != o.Max:
                raise UnequalMaxesException
            elif self.height != o.height:
                raise UnequalSizesException
            elif self.width != o.width:
                raise UnequalSizesException
            else:
                array = []
                for i in range(self.height):
                    row = []
                    array.append(row)
                    for j in range(self.width):
                        array[i].append(self.values[i][j] + o.values[i][j])
                return Sandpile(self.Max, self.height, self.width, array)
        except UnequalMaxesException:
            print("Exception occurred: Maxes not equal. Cannot add sandpiles")
        except UnequalSizesException:
            print("Exception occurred: Sizes not equal. Cannot add sandpiles")

    def color_int(self, x):
        if x == 0:
            c = colorama.Fore.BLACK
        elif x == 1:
            c = colorama.Fore.YELLOW
        elif x == 2:
            c = colorama.Fore.BLUE
        elif x == 3:
            c = colorama.Fore.RED
        else:
            c = colorama.Fore.GREEN
        return f'{c}{x}'

    def __eq__(self, o):
        try:
            if self.Max != o.Max:
                raise UnequalMaxesException
            elif self.height != o.height:
                raise UnequalSizesException
            elif self.width != o.width:
                raise UnequalSizesException
            else:
                for i in range(self.height):
                    for j in range(self.width):
                        if self.values[i][j] != o.values[i][j]:
                            return False
                return True
        except UnequalMaxesException:
            print("Exception occurred: Maxes not equal. Cannot compare sandpiles")
        except UnequalSizesException:
            print("Exception occurred: Sizes not equal. Cannot compare sandpiles")
    
    def getToppleArray(self):
        array = []
        for i in range(self.height):
            for j in range(self.width):
                if (int(self.values[i][j]) > self.Max):
                    array.append((i, j))
        return array

    # def getToppleArray(self):
    #     return [[[i > self.Max] for i in row] for row in self.values]

    def print(self):
        for i in range(self.height):
            print("\n", end='')
            for j in range(self.width):
                print(self.color_int(self.values[i][j]), end = ' ')
        print("\n", end='')

    def readFile(self, fileName = None):
        if fileName is None:
            fileName = input("Enter a file name: ")
        file = open(fileName, "r")
        data = file.readlines()
        for i in range(len(data)):
            data[i] = data[i].strip("\n")
        sandpile = []
        sandpile.append(data[0])
        size = data[1].split(",")
        sandpile.append(int(size[0]))
        sandpile.append(int(size[1]))
        values = []
        for i in range(2, len(data)):
            values.append(data[i].split(","))
        for i in range(sandpile[1]):
            for j in range(sandpile[2]):
                values[i][j] = int(values[i][j])        
        sandpile.append(values)
        self.Max = int(sandpile[0])
        self.height = int(sandpile[1])
        self.width = int(sandpile[2])
        self.values = sandpile[3]
        return self

    def topple(self):
        while self.getToppleArray():
            topple = self.getToppleArray()
            for p in topple:
                self.values[p[0]][p[1]] -= 4
                if p[0] == 0:
                    if p[1] == 0: # top left
                        self.values[p[0] + 1][p[1]] += 1
                        self.values[p[0]][p[1] + 1] += 1
                    elif p[1] < self.width - 1: # top
                        self.values[p[0] + 1][p[1]] += 1
                        self.values[p[0]][p[1] - 1] += 1
                        self.values[p[0]][p[1] + 1] += 1
                    else: # top right
                        self.values[p[0] + 1][p[1]] += 1
                        self.values[p[0]][p[1] - 1] += 1
                elif p[0] < self.height - 1 :
                    if p[1] == 0: # left
                        self.values[p[0] - 1][p[1]] += 1
                        self.values[p[0] + 1][p[1]] += 1
                        self.values[p[0]][p[1] + 1] += 1
                    elif p[1] < self.width - 1: # center
                        self.values[p[0] - 1][p[1]] += 1
                        self.values[p[0] + 1][p[1]] += 1
                        self.values[p[0]][p[1] - 1] += 1
                        self.values[p[0]][p[1] + 1] += 1
                    else: # right
                        self.values[p[0] - 1][p[1]] += 1
                        self.values[p[0] + 1][p[1]] += 1
                        self.values[p[0]][p[1] - 1] += 1
                else:
                    if p[1] == 0: # bottom left
                        self.values[p[0] - 1][p[1]] += 1
                        self.values[p[0]][p[1] + 1] += 1
                    elif p[1] < self.width - 1: # bottom
                        self.values[p[0] - 1][p[1]] += 1
                        self.values[p[0]][p[1] - 1] += 1
                        self.values[p[0]][p[1] + 1] += 1
                    else: # bottom right
                        self.values[p[0] - 1][p[1]] += 1
                        self.values[p[0]][p[1] - 1] += 1
        return self