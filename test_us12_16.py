import unittest
from SSW555_project import Person, Family, us12, us16


class TestUs1216(unittest.TestCase):
    """ test case for user story 12 and 16 """
    def test_us12_16(self):
        """ test whether us12 and us16 work well """
        father = Person()
        father.id = "I01"
        father.name = "Jotaro /Kujo/"
        father.gender = "M"
        father.birthDate = "29 SEP 1918"
        father.age = 101
        father.alive = True
        father.death = "N/A"
        father.child = ["I03"]
        father.spouse = ["I02"]

        mother = Person()
        mother.id = "I02"
        mother.name = "Marry Sue"
        mother.gender = "F"
        mother.birthDate = "12 Jan 1988"
        mother.age = 80
        mother.alive = False
        mother.death = "23 JAN 2020"
        mother.child = []
        mother.spouse = ["I01"]

        child = Person()
        child.id = "I03"
        child.name = "Jolyne /Cujoh/"
        child.gender = "M"
        child.birthDate = "12 Jan 2002"
        child.age = 18
        child.alive = True
        child.death = "N/A"
        child.child = []
        child.spouse = []

        test_family = Family()
        test_family.id = "F01"
        test_family.married = "29 SEP 1993"
        test_family.divorce = "25 JAN 2020"
        test_family.husbandID = "I01"
        test_family.husbandName = "Morgan Sue"
        test_family.wifeID = "I02"
        test_family.wifeName = "Marry Sue"
        test_family.chidren = ["I03"]

        person_list = [father, mother, child]
        family_list = [test_family]
        self.assertEqual(us12(person_list, family_list), "Not all mothers are less than 60 years older than their children, or all fathers are less than 80 years older than their children")
        self.assertEqual(us16(person_list, family_list), "Not all male members of a family have the same last name")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
