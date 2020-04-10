import unittest
from SSW555_project import Person, Family, us34, us42


class TestUS2129(unittest.TestCase):
    """ test case for user story 34 and 42 """
    def test_34_42(self):
        """ test whether us34 and us42 work well """
        husband = Person()
        husband.id = "I01"
        husband.name = "Jotaro /Kujo/"
        husband.gender = "M"
        husband.birthDate = "29 SEP 1918"
        husband.age = 101
        husband.alive = True
        husband.death = "N/A"
        husband.child = ["I03"]
        husband.spouse = ["I02"]

        wife = Person()
        wife.id = "I02"
        wife.name = "Marry Sue"
        wife.gender = "F"
        wife.birthDate = "12 Jan 1988"
        wife.age = 80
        wife.alive = False
        wife.death = "32 JAN 2020"
        wife.child = []
        wife.spouse = ["I01"]

        test_family = Family()
        test_family.id = "F01"
        test_family.married = "29 SEP 1993"
        test_family.divorce = "33 JAN 2020"
        test_family.husbandID = "I01"
        test_family.husbandName = "Morgan Sue"
        test_family.wifeID = "I02"
        test_family.wifeName = "Marry Sue"
        test_family.chidren = ["I03"]

        personList = [husband, wife]
        familiList = [test_family]

        self.assertEqual(us34(personList, familiList), "There are some couples who were married when the older spouse was more than twice as old as the younger spouse")
        self.assertEqual(us42(personList, familiList), "Not all dates are legitimate dates for the months specified.")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
