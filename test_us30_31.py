"""
by tx
Test for us30 us31
"""

import datetime
import unittest
from SSW555_project import Person, Family, us30, us31

class test_us30_31(unittest.TestCase):
    def test_us30_31(self):
        test_person1 = Person()
        test_person1.id = "I01"
        test_person1.name = "child"
        test_person1.gender = "F"
        test_person1.birthDate = "29 SEP 1900"
        test_person1.age = 44
        test_person1.alive = True
        test_person1.death = "23 JAN 2020"
        test_person1.child = []
        test_person1.spouse = ["I02"]
        
        test_person2 = Person()
        test_person2.id = "I02"
        test_person2.name = "Morgan Sue"
        test_person2.gender = "M"
        test_person2.birthDate = "12 Jan 1988"
        test_person2.age = 55
        test_person2.alive = False
        test_person2.death = "23 JAN 2020"
        test_person2.child = []
        test_person2.spouse = ["I01"]

        test_person3 = Person()
        test_person3.id = "I03"
        test_person3.name = "Haizi"
        test_person3.gender = "M"
        test_person3.birthDate = "12 Jan 1996"
        test_person3.age = 45
        test_person3.alive = True
        test_person3.death = "23 JAN 2020"
        test_person3.child = []
        test_person3.spouse = []

        person_list = [test_person1, test_person2, test_person3]
        
        self.assertEqual(us30(person_list), ["I01"])
        self.assertEqual(us31(person_list), ["I03"])


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)    