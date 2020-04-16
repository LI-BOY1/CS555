"""
by qw
Test for Sprint4 US 33 41
"""

import datetime
import unittest
from SSW555_project import Person, Family, us33, us41

class Test_US33_41(unittest.TestCase):
    
    def test_US33_41(self):
        """ test US33 and US41"""
        test_person1 = Person()
        test_person1.id = "I01"
        test_person1.name = "Marry Sue"
        test_person1.gender = "F"
        test_person1.birthDate = "29 SEP 1993"
        test_person1.age = 27
        test_person1.alive = False
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
        c1.age = 18
        c1.gender = "F"
        c1.birthDate = "29 SEP 2002"

        c2 = Person()
        c2.id = "c2"
        c2.name = "c2 Sue"
        c2.age = 19
        c2.gender = "F"
        c2.birthDate = "2 SEP 2001"

        c3 = Person()
        c3.id = "c3"
        c3.name = "c3 Sue"
        c3.age = 17
        c3.gender = "F"
        c3.birthDate = "1 SEP 2003"

        person_list = [test_person1, test_person2, c1, c2, c3]
        family_list = [test_family]

        # for us 41 modification made in parser
        # so us41 doesn't have code for testing

        self.assertEqual(us33(person_list, family_list), 1)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
