"""
Boyang Li
Test for Sprint2 US35 36
"""

import datetime
import unittest
from SSW555_project import Person, us35, us36


class Test_US35_36(unittest.TestCase):


    def test_US35_36(self):
        test_person1 = Person()
        test_person1.id = "d1"
        test_person1.name = "Jack Sue"
        test_person1.gender = "M"
        test_person1.birthDate = "1 APR 2020"
        test_person1.age = 0
        test_person1.alive = True
        test_person1.death = "N/A"
        test_person1.child = []
        test_person1.spouse = []

        test_person2 = Person()
        test_person2.id = "d2"
        test_person2.name = "Rose Sue"
        test_person2.gender = "F"
        test_person2.birthDate = "1 JAN 1987"
        test_person2.age = 33
        test_person2.alive = False
        test_person2.death = "16 APR 2020"
        test_person2.child = []
        test_person2.spouse = []

        person_list = [test_person1, test_person2]

        self.assertEqual(us35(person_list), None)
        self.assertEqual(us36(person_list), None)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
