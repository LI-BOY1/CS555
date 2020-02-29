import unittest
from us08 import us08
import Project

Project.main()

class test_us08(unittest.TestCase):
    def test_us08(self):
        self.assertEqual(us08(), 'Correct')
        # self.assertEqual(us08(), 'The data in ged_file is Wrong. (us08)')

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)    