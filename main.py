from Sandpile import Sandpile

s1 = Sandpile(3, 2, 2, 0, 2, 1, 1, 0, 1, 3)
s2 = Sandpile(3, 2, 1, 3, 1, 0, 1, 0, 1, 0)

s1.print()
s2.print()
s1.add(s2).print()
s1.add(s2).topple().print()

zero = Sandpile(3, 2, 1, 2, 1, 0, 1, 2, 1, 2)