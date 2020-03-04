"""
by tx
Test for us07
"""

import datetime
import unittest
from SSW555_project import Person, Family, us07, us08

class test_us07(unittest.TestCase):
    def test_us07(self):
        """test for us07"""
        test_person1 = Person()
        test_person1.id = "I01"
        test_person1.name = "Marry Sue"
        test_person1.gender = "F"
        test_person1.birthDate = "29 SEP 1800"
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

        test_person3 = Person()
        test_person3.id = "I03"
        test_person3.name = "Haizi"
        test_person3.gender = "M"
        test_person3.birthDate = "12 Jan 1996"
        test_person3.age = 10
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
        test_family.chidren = []

        person_list = [test_person1, test_person2]
        family_list = [test_family]

        self.assertEqual(us07(person_list,family_list),'Error')
        self.assertEqual(us08(person_list,family_list),'Correct')

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)    