from Sandpile import Sandpile

s1 = Sandpile(3, 2, 2, 0, 2, 1, 1, 0, 1, 3)
s2 = Sandpile(3, 2, 1, 3, 1, 0, 1, 0, 1, 0)

threes = Sandpile(3, 3, 3, 3, 3, 3, 3, 3, 3, 3)
zero = Sandpile(3, 2, 1, 2, 1, 0, 1, 2, 1, 2)

threes.add(zero).topple().print()

s1.add(zero).topple().print()
s2.add(zero).topple().print()

a = Sandpile(3, 1, 3, 1, 3, 3, 3, 1, 3, 1)

threes.add(a).topple().print()