"""
by zw
Test for Sprint1 US01 06
"""
import unittest
from SSW555_project import Person, Family, us01, us06


class TestUs0106(unittest.TestCase):
    """ test case for us0106 """
    def test_us01_06(self):
        """ test whether us01 and us06 work well """
        test_person1 = Person()
        test_person1.id = "I01"
        test_person1.name = "Marry Sue"
        test_person1.gender = "F"
        test_person1.birthDate = "29 SEP 2022"
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
        test_family.divorce = "25 JAN 2020"
        test_family.husbandID = "I02"
        test_family.husbandName = "Morgan Sue"
        test_family.wifeID = "I01"
        test_family.wifeName = "Marry Sue"
        test_family.chidren = []

        person_list = [test_person1, test_person2]
        family_list = [test_family]

        self.assertEqual(us01(person_list, family_list), "Not all dates happen before current date.")
        self.assertEqual(us06(person_list, family_list), "Not all divorces happen before one is dead.")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)