import unittest
from Circle import Circle
import math

class TestCircle(unittest.TestCase):
    def test_area(self):
        c = Circle(0.0)
        self.assertEqual(c.compute_area(), 0.0)
        c = Circle(5.0)
        self.assertEqual(c.compute_area(), math.pi*5.0**2)

    def test_smart(self):
        c = Circle(5)
        self.assertGreaterEqual(c.compute_circumference(), 0.0)


if __name__ == "__main__":
    unittest.main()
