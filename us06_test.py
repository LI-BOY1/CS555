import unittest
import Project
Project.main(False)


class TestUs06(unittest.TestCase):
    def test_us06(self):
        self.assertEqual(Project.us06(), "Not all divorces happen before one is dead.")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
