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
                self.n4 -= 4
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
    def add(self, s):
        self.n1 += s.n1
        self.n2 += s.n2
        self.n3 += s.n3
        self.n4 += s.n4
        self.n5 += s.n5
        self.n6 += s.n6
        self.n7 += s.n7
        self.n8 += s.n8
        self.n9 += s.n9
        return self