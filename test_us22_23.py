"""
Boyang Li
Test for Sprint2 US22 23
"""

import datetime
import unittest
from SSW555_project import Person, Family, us22, us23

class Test_US22_23(unittest.TestCase):
    
    def test_US22_23(self):


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
        test_person2.id = "I01"
        test_person2.name = "Morgan Sue"
        test_person2.gender = "M"
        test_person2.birthDate = "12 Jan 1988"
        test_person2.age = 32
        test_person2.alive = False
        test_person2.death = "23 JAN 2020"
        test_person2.child = []
        test_person2.spouse = ["I01"]

        test_person3 = Person()
        test_person3.id = "I02"
        test_person3.name = "Morgan Sue"
        test_person3.gender = "M"
        test_person3.birthDate = "12 Jan 1988"
        test_person3.age = 32
        test_person3.alive = False
        test_person3.death = "23 JAN 2020"
        test_person3.child = []
        test_person3.spouse = []


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
        test_family2.id = "F01"
        test_family2.husbandID = "c1"
        test_family2.wifeID = "c2"


        person_list = [test_person1, test_person2, test_person3]
        family_list = [test_family, test_family2]

        self.assertEqual(us22(person_list, family_list), None)
        self.assertEqual(us23(person_list), None)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
