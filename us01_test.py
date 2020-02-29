import unittest
import Project
Project.main(False)


class TestUs01(unittest.TestCase):
    def test_us01(self):
        self.assertEqual(Project.us01(), "Not all dates happen before current date.")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
