import unittest
from us01 import us01
import Project

Project.main()


class TestUs01(unittest.TestCase):
    def test_us01(self):
        self.assertEqual(us01(), "Not all dates happen before current date.")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)