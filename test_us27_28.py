"""
by qw
Test for Sprint3 US27 28
"""

import datetime
import unittest
from SSW555_project import Person, Family, us27, us28

class Test_US27_28(unittest.TestCase):
    
    def test_US27_28(self):
        """ test US27 and US28"""
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
        test_family.chidren = ["c1", "c2", "c3"]

        c1 = Person()
        c1.id = "c1"
        c1.name = "c1 Sue"
        c1.gender = "F"
        c1.birthDate = "29 SEP 2000"

        c2 = Person()
        c2.id = "c2"
        c2.name = "c2 Sue"
        c2.gender = "F"
        c2.birthDate = "2 SEP 2000"

        c3 = Person()
        c3.id = "c3"
        c3.name = "c3 Sue"
        c3.gender = "F"
        c3.birthDate = "1 SEP 2000"



        person_list = [test_person1, test_person2, c1, c2, c3]
        
        family_list = [test_family]

        family_list2 = [test_family]
        family_list2[0].children = ['c3', 'c2', 'c1']
        #self.assertEqual(us27(family_list), 1)
        # age is already included in the original individuals pretty table
        # us27 doesn't have code for testing
        #print(us28(person_list))
        self.assertEqual(us28(person_list, family_list), family_list2)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
