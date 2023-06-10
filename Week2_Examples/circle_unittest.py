import unittest
from Circle import Circle

class TestCircle(unittest.TestCase):
    def test_area(self):
        c = Circle(0.0)
        self.assertEqual(c.compute_area(), 0.0)
        c = Circle(5.0)
        self.assertEqual(c.compute_area(), 78.5398)

    def test_stupid(self):
        c = Circle(5)
        self.assertLess(c.compute_circumference(), 0.0)


if __name__ == "__main__":
    unittest.main()
