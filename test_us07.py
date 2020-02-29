import unittest
from us07 import us07
import Project

Project.main()

class test_us07(unittest.TestCase):
    def test_us07(self):
        self.assertEqual(us07(), 'Correct')


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)    