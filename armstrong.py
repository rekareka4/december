import math

szam = input("A vizsgálni kívánt szám: ")
osszeg = 0

for i in szam:
    osszeg += math.pow(int(i), len(szam))

print(*["A megadott szám Armstrong-szám." if int(szam) == osszeg else "A megadott szám nem Armstrong-szám."])

import unittest

class TesztArmstrong(unittest.TestCase):
    def armstrong(self):
        self.assertTrue(armstrong(153))
        self.assertTrue(armstrong(9474))
        self.assertFalse(armstrong(123))
        self.assertFalse(armstrong(10))
