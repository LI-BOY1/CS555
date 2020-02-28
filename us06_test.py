import unittest
from us06 import us06
import Project

Project.main()


class TestUs06(unittest.TestCase):
    def test_us06(self):
        self.assertEqual(us06(), "Not all divorces happen before one is dead.")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)