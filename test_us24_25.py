"""
Boyang Li
Test for Sprint2 US24 25
"""

import datetime
import unittest
from SSW555_project import Person, Family, us24, us25


class Test_US24_25(unittest.TestCase):


    def test_US24_25(self):
        test_person1 = Person()
        test_person1.id = "d1"
        test_person1.name = "Jack Sue"
        test_person1.gender = "M"
        test_person1.birthDate = "1 JAN 1986"
        test_person1.age = 34
        test_person1.alive = True
        test_person1.death = "N/A"
        test_person1.child = []
        test_person1.spouse = ["d2"]

        test_person2 = Person()
        test_person2.id = "d2"
        test_person2.name = "Rose Sue"
        test_person2.gender = "F"
        test_person2.birthDate = "1 JAN 1987"
        test_person2.age = 33
        test_person2.alive = True
        test_person2.death = "N/A"
        test_person2.child = []
        test_person2.spouse = ["d1"]

        test_person3 = Person()
        test_person3.id = "d3"
        test_person3.name = "Jack Sue"
        test_person3.gender = "M"
        test_person3.birthDate = "1 JAN 1986"
        test_person3.age = 34
        test_person3.alive = True
        test_person3.death = "N/A"
        test_person3.child = []
        test_person3.spouse = ["d4"]

        test_person4 = Person()
        test_person4.id = "d4"
        test_person4.name = "Rose Sue"
        test_person4.gender = "F"
        test_person4.birthDate = "1 JAN 1987"
        test_person4.age = 33
        test_person4.alive = True
        test_person4.death = "N/A"
        test_person4.child = []
        test_person4.spouse = ["d3"]

        test_person5 = Person()
        test_person5.id = "US25C"
        test_person5.name = "Mary Zhang"
        test_person5.gender = "M"
        test_person5.birthDate = "1 JAN 2019"
        test_person5.age = 34
        test_person5.alive = True
        test_person5.death = "N/A"
        test_person5.child = []
        test_person5.spouse = []

        test_person6 = Person()
        test_person6.id = "US25D"
        test_person6.name = "Mary Zhang"
        test_person6.gender = "F"
        test_person6.birthDate = "1 JAN 2019"
        test_person6.age = 34
        test_person6.alive = True
        test_person6.death = "N/A"
        test_person6.child = []
        test_person6.spouse = []





        test_family = Family()
        test_family.id = "f4"
        test_family.married = "DATE 1 JAN 2018"
        test_family.divorce = "NA"
        test_family.husbandID = "d1"
        test_family.husbandName = "Jack Sue"
        test_family.wifeID = "d2"
        test_family.wifeName = "Rose Sue"
        test_family.chidren = []

        test_family2 = Family()
        test_family2.id = "f5"
        test_family2.married = "DATE 1 JAN 2018"
        test_family2.divorce = "NA"
        test_family2.husbandID = "d3"
        test_family2.husbandName = "Jack Sue"
        test_family2.wifeID = "d4"
        test_family2.wifeName = "Rose Sue"
        test_family2.chidren = ["US25C", "US25D"]





        person_list = [test_person1, test_person2, test_person3, test_person4, test_person5, test_person6]
        family_list = [test_family, test_family2]

        self.assertEqual(us24(family_list), None)
        self.assertEqual(us25(person_list, family_list), None)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
