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
    size = -1
    values = []

    def __init__(self, Max, size, values):
        self.Max = Max
        self.size = size
        self.values = values

    def getMax(self):
        return self.Max
        
    def getSize(self):
        return self.size

    def getValues(self):
        return self.values

    def __add__(self, o):
        try:
            if self.Max != o.Max:
                raise UnequalMaxesException
            elif self.Max != o.Max:
                raise UnequalSizesException
            else:
                array = []
                for i in range(self.size):
                    row = []
                    array.append(row)
                    for j in range(self.size):
                        array[i].append(self.values[i][j] + o.values[i][j])
                return Sandpile(self.Max, self.size, array)
        except UnequalMaxesException:
            print("Exception occurred: Maxes not equal. Cannot add sandpiles")
        except UnequalSizesException:
            print("Exception occurred: Sizes not equal. Cannot add sandpiles")
    
    def checkValues(self):
        array = []
        for i in range(self.size):
            for j in range(self.size):
                if (self.values[i][j] > self.Max):
                    array.append((i, j))
        return array

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
            elif self.size != o.size:
                raise UnequalSizesException
            else:
                for i in range(self.size):
                    for j in range(self.size):
                        if self.values[i][j] != o.values[i][j]:
                            return False
                return True
        except UnequalMaxesException:
            print("Exception occurred: Maxes not equal. Cannot compare sandpiles")
        except UnequalSizesException:
            print("Exception occurred: Sizes not equal. Cannot compare sandpiles")

    def print(self):
        for i in range(int(self.size)):
            print("\n", end='')
            for j in range(int(self.size)):
                print(self.color_int(int(self.values[i][j])), end = ' ')
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
        sandpile.append(data[1])
        values = []
        for i in range(2, len(data)):
            values.append(data[i].split(","))
        sandpile.append(values)
        self.Max = sandpile[0]
        self.size = sandpile[1]
        self.values = sandpile[2]
        return self

    def topple(self):
        while self.checkValues():
            array = self.checkValues()
            for p in array:
                self.values[p[0]][p[1]] -= 4
                if p[0] == 0:
                    if p[1] == 0: # top left
                        self.values[p[0] + 1][p[1]] += 1
                        self.values[p[0]][p[1] + 1] += 1
                    elif p[1] < self.size - 1: # top
                        self.values[p[0] + 1][p[1]] += 1
                        self.values[p[0]][p[1] - 1] += 1
                        self.values[p[0]][p[1] + 1] += 1
                    else: # top right
                        self.values[p[0] + 1][p[1]] += 1
                        self.values[p[0]][p[1] - 1] += 1
                elif p[0] < self.size - 1 :
                    if p[1] == 0: # left
                        self.values[p[0] - 1][p[1]] += 1
                        self.values[p[0] + 1][p[1]] += 1
                        self.values[p[0]][p[1] + 1] += 1
                    elif p[1] < self.size - 1: # center
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
                    elif p[1] < self.size - 1: # bottom
                        self.values[p[0] - 1][p[1]] += 1
                        self.values[p[0]][p[1] - 1] += 1
                        self.values[p[0]][p[1] + 1] += 1
                    else: # bottom right
                        self.values[p[0] - 1][p[1]] += 1
                        self.values[p[0]][p[1] - 1] += 1
        return self