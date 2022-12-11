from Sandpile import Sandpile
import numpy as np

# np.set_printoptions(formatter={'int': color_int})

twozero = Sandpile(3, 2, [[2, 2], [2, 2]])

threes_3 = Sandpile(3, 3, [[3, 3, 3], [3, 3, 3], [3, 3, 3]])
threezero = Sandpile(3, 3, [[2, 1, 2], [1, 0, 1], [2, 1, 2]])

# 3 + 0 = 3
(threes_3 + threezero).topple().print()

sp = Sandpile(3, 4, [[2, 1, 2, 2], [1, 2, 1, 3], [3, 1, 3, 3], [3, 3, 3, 2]])
fourzero = Sandpile(3, 4, [[2, 3, 3, 2], [3, 2, 2, 3], [3, 2, 2, 3], [2, 3, 3, 2]])

# sp + 0 = sp
(sp + fourzero).topple().print()

threeinverse = Sandpile(3, 3, [[3, 3, 3], [3, 1, 3], [3, 3, 3]])

# 3 + (-3) = 0
(threes_3 + threeinverse).topple().print()

blank = Sandpile(3, 5, [[], [], [], [], []])
fivezero = blank.readFile("fivezero.csv")

fivezero.print()