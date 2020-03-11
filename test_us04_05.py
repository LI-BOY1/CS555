# Boyang Li
# Test file for US04 US05

import datetime
import unittest

from SSW555_project import Person, Family, us0405


class Test_US0405(unittest.TestCase):

    def test_US0405(self):

        test_person1 = Person()
        test_person1.id = "P0002"
        test_person1.name = "CCCC"
        test_person1.gender = "F"
        test_person1.birthDate = "29 SEP 1973"
        test_person1.age = 27
        test_person1.alive = True
        test_person1.death = "N/A"
        test_person1.child = []
        test_person1.spouse = ["P0003"]

        test_person2 = Person()
        test_person2.id = "P0003"
        test_person2.name = "DDDD"
        test_person2.gender = "M"
        test_person2.birthDate = "12 Jan 1978"
        test_person2.age = 32
        test_person2.alive = False
        test_person2.death = "23 JAN 2020"
        test_person2.child = []
        test_person2.spouse = ["P0002"]

        test_family2 = Family()
        test_family2.id = "F0002"
        test_family2.married = "23 JAN 2021"
        test_family2.divorce = "NA"
        test_family2.husbandID = "P0003"
        test_family2.husbandName = "DDDD"
        test_family2.wifeID = "P0002"
        test_family2.wifeName = "CCCC"
        test_family2.chidren = []



        test_family1 = Family()
        test_family1.id = "F0001"
        test_family1.married = "29 SEP 1990"
        test_family1.divorce = "29 sep 1988"
        test_family1.husbandID = "P0001"
        test_family1.husbandName = "AAAA"
        test_family1.wifeID = "P0002"
        test_family1.wifeName = "BBB"
        test_family1.chidren = []

        fileName = "Sprint1US0405Output.txt"

        person_list = [test_person1, test_person2]
        family_list = [test_family1, test_family2]

        self.assertEqual(us0405(family_list, person_list), None)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
