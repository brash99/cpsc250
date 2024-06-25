import unittest
from Circle import Circle # Import the Circle class from Circle.py in the current folder

import math

class TestCircle(unittest.TestCase):

    # We will write test cases for the following methods:
    # 1. compute_area
    # 2. compute_circumference
    # 3. get_radius
    # 4. set_radius
    # 5. __str__
    # 6. __eq__
    #
    # The test case functions MUST start with the word "test"

    def test_area(self):
        c = Circle(0.0)
        self.assertEqual(c.compute_area(), 0.0)
        c = Circle(5.0)
        self.assertEqual(c.compute_area(), math.pi*5.0**2)

    def test_positive_circumference(self):
        c = Circle(5.0)
        self.assertGreaterEqual(c.compute_circumference(), 0.0)
        #c = Circle(-5.0)
        #self.assertGreaterEqual(c.compute_circumference(), 0.0)

    def test_get_radius(self):
        c = Circle(5.0)
        self.assertEqual(c.get_radius(), 5.0)

    def test_set_radius(self):
        c = Circle(5.0)
        c.set_radius(10.0)
        self.assertEqual(c.get_radius(), 10.0)
        c.set_radius(0.0)
        self.assertEqual(c.get_radius(), 0.0)
        c.set_radius(-5.0)
        self.assertEqual(c.get_radius(), -5.0)

    def test_str(self):
        c = Circle(5.0)
        self.assertEqual(str(c), "Circle with radius: 5.0")
        c = Circle(0.0)
        self.assertEqual(str(c), "Circle with radius: 0.0")
        c = Circle(-5.0)
        self.assertEqual(str(c), "Circle with radius: -5.0")

    def test_eq(self):
        c1 = Circle(5.0)
        c2 = Circle(5.0)
        self.assertTrue(c1 == c2)
        c2 = Circle(10.0)
        self.assertFalse(c1 == c2)
        c2 = Circle(0.0)
        self.assertFalse(c1 == c2)
        c2 = Circle(-5.0)
        self.assertFalse(c1 == c2)

if __name__ == "__main__":
    unittest.main()
