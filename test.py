import unittest
from main import *

class MyTestCase(unittest.TestCase):
    def args(self):
        self.assertEqual(adder(2,2),4)
    def test_kwargs(self):
        self.assertEqual(adder(a=10,b=11),21)
    def test_mixed(self):
        self.assertEqual(adder(1,b=2),3)

if __name__ == '__main__':
    unittest.main()