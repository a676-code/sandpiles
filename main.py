from Sandpile import Sandpile

twozero = Sandpile(3, 2, [[2, 2], [2, 2]])

threes = Sandpile(3, 3, [[3, 3, 3], [3, 3, 3], [3, 3, 3]])
threezero = Sandpile(3, 3, [[2, 1, 2], [1, 0, 1], [2, 1, 2]])

a = Sandpile(3, 3, [[0, 0, 0], [0, 0, 0], [0, 0, 1]])
b = Sandpile(3, 3, [[1, 0, 0], [0, 0, 0], [0, 0, 0]])

(a + b).topple().print()

(threes + threezero).topple().print()

sp = Sandpile(3, 4, [[2, 1, 2, 2], [1, 2, 1, 3], [3, 1, 3, 3], [3, 3, 3, 2]])
fourzero = Sandpile(3, 4, [[2, 3, 3, 2], [3, 2, 2, 3], [3, 2, 2, 3], [2, 3, 3, 2]])

(sp + fourzero).topple().print()

threeinverse = Sandpile(3, 3, [[3, 3, 3], [3, 1, 3], [3, 3, 3]])

threezero.print()

(threes + threeinverse).topple().print()


if (threezero == (threes + threeinverse).topple()):
    print("EQUAL!")
else:
    print("NOT EQUAL!")

blank = Sandpile(3, 3, [[], [], []])
blank.readFile("threes_3.csv")

blank2 = Sandpile(3, 5, [[], [], [], [], []])
blank2.readFile("fivezero.csv")