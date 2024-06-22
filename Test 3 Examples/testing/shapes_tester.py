import unittest

from shapes import Shape, Circle, Rectangle

class TestShapes(unittest.TestCase):
    currentResult = None  # holds last result object passed to run method

    @classmethod
    def setResult(cls, amount, errors, failures, skipped):
        cls.amount, cls.errors, cls.failures, cls.skipped = \
            amount, errors, failures, skipped

    def tearDown(self):
        amount = self.currentResult.testsRun
        errors = self.currentResult.errors
        failures = self.currentResult.failures
        skipped = self.currentResult.skipped
        self.setResult(amount, errors, failures, skipped)

    @classmethod
    def tearDownClass(cls):
        print("\ntests run: " + str(cls.amount))
        print("errors: " + str(len(cls.errors)))
        print("failures: " + str(len(cls.failures)))
        print("success: " + str(cls.amount - len(cls.errors) - len(cls.failures)))
        print("skipped: " + str(len(cls.skipped)))

    def run(self, result=None):
        self.currentResult = result  # remember result for use in tearDown
        unittest.TestCase.run(self, result)  # call superclass run method


    def test_r_area(self):
        rectangle = Rectangle(4, 4.1, 2.3)
        self.assertEqual(rectangle.calculate_area(), 9.429999999999998)
        rectangle = Rectangle(4, 4, 2)
        self.assertEqual(rectangle.calculate_area(), 8)

    def test_r_perimeter(self):
        rectangle = Rectangle(4, 4.1, 2.3)
        self.assertEqual(rectangle.calculate_perimeter(), 12.799999999999999)

    def test_r_set_width(self):
        rectangle = Rectangle(4, 4.1, 2.3)
        rectangle.set_width(3)
        self.assertEqual(rectangle.get_width(), 3)

    def test_r_get_width(self):
        rectangle = Rectangle(4, 4.1, 2.3)
        self.assertEqual(rectangle.get_width(), 2.3)

    def test_r_set_height(self):
        rectangle = Rectangle(4, 4.1, 2.3)
        rectangle.set_height(3)
        self.assertEqual(rectangle.get_height(), 3)

    def test_r_get_height(self):
        rectangle = Rectangle(4, 4.1, 2.3)
        self.assertEqual(rectangle.get_height(), 4.1)

    def test_r_eq(self):
        rectangle = Rectangle(4, 4.1, 2.3)
        self.assertEqual(rectangle == Rectangle(4, 4.1, 2.3), True)

    def test_r_str(self):
        rectangle = Rectangle(4, 4.1, 2.3)
        self.assertEqual(str(rectangle), 'A rectangle has 4 sides | Area = 9.429999999999998 | Perimeter = 12.799999999999999')

    def test_c_area(self):
        circle = Circle(1, 3.5)
        self.assertEqual(circle.calculate_area(), 38.48451000647496)

    def test_c_perimeter(self):
        circle = Circle(1, 3.5)
        self.assertEqual(circle.calculate_perimeter(), 21.991148575128552)

    def test_c_set_radius(self):
        circle = Circle(1, 3.5)
        circle.set_radius(2)
        self.assertEqual(circle.get_radius(), 2)

    def test_c_get_radius(self):
        circle = Circle(1, 3.5)
        self.assertEqual(circle.get_radius(), 3.5)

    def test_c_eq(self):
        circle = Circle(1, 3.5)
        self.assertEqual(circle == Circle(1, 3.5), True)

    def test_c_str(self):
        circle = Circle(1, 3.5)
        self.assertEqual(str(circle), 'A circle has 1 sides | Area = 38.48451000647496 | Perimeter = 21.991148575128552')

if __name__ == '__main__':
    unittest.main()



