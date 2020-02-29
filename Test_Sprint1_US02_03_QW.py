"""
by qw
Test for Sprint1_US02_03
"""

import datetime
import unittest
from Sprint1_US02_03_QW import US02, US03
from Project import Person, Family

class Test_US02_03(unittest.TestCase):
    
    def test_US02_03(self):
        """ test US02 and US03"""
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
        test_family.chidren = []

        person_list = [test_person1, test_person2]
        family_list = [test_family]

        self.assertEqual(US02("test_output.txt", person_list, family_list, False), 0)
        self.assertEqual(US03("test_output.txt", person_list, False), 0)
        
        person_list[0].birthDate = "29 SEP 2021"
        self.assertEqual(US02("test_output.txt", person_list, family_list, False), 1)
        self.assertEqual(US03("test_output.txt", person_list, False), 1)
                
        person_list[1].birthDate = "29 SEP 2021"
        self.assertEqual(US02("test_output.txt", person_list, family_list, False), 2)
        self.assertEqual(US03("test_output.txt", person_list, False), 2)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
