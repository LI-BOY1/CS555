import unittest
from SSW555_project import Person, Family, us21, us29


class TestUS2129(unittest.TestCase):
    """ test case for user story 21 and 29 """
    def test_21_29(self):
        """ test whether us21 and us29 work well """
        husband = Person()
        husband.id = "I01"
        husband.name = "Jotaro /Kujo/"
        husband.gender = "F"
        husband.birthDate = "29 SEP 1918"
        husband.age = 101
        husband.alive = True
        husband.death = "N/A"
        husband.child = ["I03"]
        husband.spouse = ["I02"]

        wife = Person()
        wife.id = "I02"
        wife.name = "Marry Sue"
        wife.gender = "M"
        wife.birthDate = "12 Jan 1988"
        wife.age = 80
        wife.alive = False
        wife.death = "23 JAN 2020"
        wife.child = []
        wife.spouse = ["I01"]

        test_family = Family()
        test_family.id = "F01"
        test_family.married = "29 SEP 1993"
        test_family.divorce = "25 JAN 2020"
        test_family.husbandID = "I01"
        test_family.husbandName = "Morgan Sue"
        test_family.wifeID = "I02"
        test_family.wifeName = "Marry Sue"
        test_family.chidren = ["I03"]

        personList = [husband, wife]
        familiList = [test_family]

        self.assertEqual(us21(personList, familiList), "Husband in family is not male or wife in family is not female")
        self.assertEqual(us29(personList), ['I02'])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
