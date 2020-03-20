"""
by qw
Test for Sprint1 US15 18
"""

import datetime
import unittest
from SSW555_project import Person, Family, us15, us18

class Test_US15_18(unittest.TestCase):
    
    def test_US15_18(self):
        """ test US15 and US18"""
        test_person1 = Person()
        test_person1.id = "I01"
        test_person1.name = "Marry Sue"
        test_person1.gender = "F"
        test_person1.birthDate = "29 SEP 1993"
        test_person1.age = 27
        test_person1.alive = True
        test_person1.death = "23 JAN 2020"
        test_person1.child = []
        test_person1.spouse = ["I02"]
        
        test_person2 = Person()
        test_person2.id = "I02"
        test_person2.name = "Morgan Sue"
        test_person2.gender = "M"
        test_person2.birthDate = "12 Jan 1988"
        test_person2.age = 32
        test_person2.alive = False
        test_person2.death = "23 JAN 2020"
        test_person2.child = []
        test_person2.spouse = ["I01"]

        test_family = Family()
        test_family.id = "F01"
        test_family.married = "29 SEP 1993"
        test_family.divorce = "NA"
        test_family.husbandID = "I02"
        test_family.husbandName = "Morgan Sue"
        test_family.wifeID = "I01"
        test_family.wifeName = "Marry Sue"
        test_family.chidren = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12", "c13", "c14", "c15", "c16"]

        test_family2 = Family()
        test_family.id = "F02"
        test_family.husbandID = "c1"
        test_family.wifeID = "c2"


        person_list = [test_person1, test_person2]
        family_list = [test_family, test_family2]

        self.assertEqual(us15(family_list), 1)
        self.assertEqual(us18(family_list), 1)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
