# Sandpile unequal maxes exception
class UnequalMaxesException(Exception):
    "Raised when two combined sandpiles have different maxes"
    pass

class Sandpile:
    Max = -1
    n1 = -1
    n2 = -1
    n3 = -1
    n4 = -1
    n5 = -1
    n6 = -1
    n7 = -1
    n8 = -1
    n9 = -1

    def __init__(self, Max, n1, n2, n3, n4, n5, n6, n7, n8, n9):
        self.Max = Max
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.n5 = n5
        self.n6 = n6
        self.n7 = n7
        self.n8 = n8
        self.n9 = n9

    def getMax(self):
        return self.Max

    def getn1(self):
        return self.n1

    def getn2(self):
        return self.n2

    def getn3(self):
        return self.n3

    def getn4(self):
        return self.n4

    def getn5(self):
        return self.n5

    def getn6(self):
        return self.n6

    def getn7(self):
        return self.n7

    def getn8(self):
        return self.n8

    def getn9(self):
        return self.n9
    
    def checkValues(self):
        values = []
        if (self.n1 > self.Max):
            values.append(1)
        if (self.n2 > self.Max):
            values.append(2)
        if (self.n3 > self.Max):
            values.append(3)
        if (self.n4 > self.Max):
            values.append(4)
        if (self.n5 > self.Max):
            values.append(5)
        if (self.n6 > self.Max):
            values.append(6)
        if (self.n7 > self.Max):
            values.append(7)
        if (self.n8 > self.Max):
            values.append(8)
        if (self.n9 > self.Max):
            values.append(9)
        return values

    def topple(self):
        while self.checkValues():
            values = self.checkValues()
            if 1 in values:
                self.n1 -= 4
                self.n2 += 1
                self.n4 += 1
            if 2 in values:
                self.n2 -= 4
                self.n1 += 1
                self.n3 += 1
                self.n5 += 1
            if 3 in values:
                self.n3 -= 4
                self.n2 += 1
                self.n6 += 1
            if 4 in values:
                self.n4 -= 4
                self.n1 += 1
                self.n5 += 1
                self.n7 += 1
            if 5 in values:
                self.n5 -= 4
                self.n2 += 1
                self.n4 += 1
                self.n6 += 1
                self.n8 += 1
            if 6 in values:
                self.n6 -= 4
                self.n3 += 1
                self.n5 += 1
                self.n9 += 1
            if 7 in values:
                self.n7 -= 4
                self.n4 += 1
                self.n8 += 1
            if 8 in values:
                self.n8 -= 4
                self.n7 += 1
                self.n5 += 1
                self.n9 += 1
            if 9 in values:
                self.n9 -= 4
                self.n6 += 1
                self.n8 += 1
        return self

    def print(self):
        print(
            "\n",self.n1," ", self.n2, " ", self.n3,"\n", 
            self.n4," ", self.n5, " ", self.n6,"\n", 
            self.n7," ", self.n8, " ", self.n9
        )

    def __add__(self, o):
        try:
            if self.Max != o.Max:
                raise UnequalMaxesException
            else:
                N1 = self.n1 + o.n1
                N2 = self.n2 + o.n2
                N3 = self.n3 + o.n3
                N4 = self.n4 + o.n4
                N5 = self.n5 + o.n5
                N6 = self.n6 + o.n6
                N7 = self.n7 + o.n7
                N8 = self.n8 + o.n8
                N9 = self.n9 + o.n9
                return Sandpile(self.Max, N1, N2, N3, N4, N5, N6, N7, N8, N9)
        except UnequalMaxesException:
            print("Exception occurred: Maxes not equal. Cannot add sandpiles")

    def __eq__(self, o):
        try:
            if self.Max != o.Max:
                raise UnequalMaxesException
            else:
                if (
                    self.Max == o.Max and 
                    self.n1 == o.n1 and
                    self.n2 == o.n2 and
                    self.n3 == o.n3 and
                    self.n4 == o.n4 and
                    self.n5 == o.n5 and
                    self.n6 == o.n6 and
                    self.n7 == o.n7 and
                    self.n8 == o.n8 and
                    self.n9 == o.n9
                    ):
                    return True
                else:
                    return False
        except UnequalMaxesException:
            print("Exception occurred: Maxes not equal. Cannot compare sandpiles")