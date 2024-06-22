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
        self.assertEqual(rectangle.get_width(), 4.1)

    def test_r_set_height(self):
        rectangle = Rectangle(4, 4.1, 2.3)
        height_op = getattr(rectangle, 'set_height', None)
        if callable(height_op):
            rectangle.set_height(3)
            self.assertEqual(rectangle.get_height(), 3)
        else:
            rectangle.set_length(3) 
            self.assertEqual(rectangle.get_length(), 3)

    def test_r_get_height(self):
        rectangle = Rectangle(4, 4.1, 2.3)
        height_op = getattr(rectangle, 'get_height', None)
        if callable(height_op):
            self.assertEqual(rectangle.get_height(), 2.3)
        else:
            self.assertEqual(rectangle.get_length(), 2.3)

    def test_r_eq(self):
        rectangle = Rectangle(4, 4.1, 2.3)
        self.assertEqual(rectangle == Rectangle(4, 4.1, 2.3), True)

    def test_r_noteq(self):
        rectangle = Rectangle(4, 4.1, 2.3)
        self.assertEqual(rectangle == Rectangle(4, 4.1, 2), False)

    def test_r_str(self):
        rectangle = Rectangle(4, 4.1, 2.3)
        nsides = rectangle.get_number_of_sides()
        area = rectangle.calculate_area()
        perimeter = rectangle.calculate_perimeter()
        comparison_list = []
        comparison1 = f'A rectangle has {nsides} sides | Area = {area} | Perimeter = {perimeter}'
        comparison2 = f'A rectangle has {nsides} sides | Area = {area:.2f} | Perimeter = {perimeter:.2f}'
        comparison3 = f'A rectangle has {nsides:.2f} sides | Area = {area:.2f} | Perimeter = {perimeter:.2f}'
        comparison_list.append(comparison1)
        comparison_list.append(comparison2)
        comparison_list.append(comparison3)
        self.assertIn(str(rectangle), comparison_list)

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

    def test_c_noteq(self):
        circle = Circle(1, 3.5)
        self.assertEqual(circle == Circle(1, 2), False)

    def test_c_str(self):
        circle = Circle(1, 3.5)
        nsides = circle.get_number_of_sides()
        area = circle.calculate_area()
        perimeter = circle.calculate_perimeter()
        comparison_list = []
        comparison1 = f'A circle has {nsides} sides | Area = {area} | Perimeter = {perimeter}'
        comparison2 = f'A circle has {nsides} sides | Area = {area:.2f} | Perimeter = {perimeter:.2f}'
        comparison3 = f'A circle has {nsides:.2f} sides | Area = {area:.2f} | Perimeter = {perimeter:.2f}'
        comparison4 = f'A circle has {nsides} side | Area = {area} | Perimeter = {perimeter}'
        comparison5 = f'A circle has {nsides} side | Area = {area:.2f} | Perimeter = {perimeter:.2f}'
        comparison6 = f'A circle has {nsides:.2f} side | Area = {area:.2f} | Perimeter = {perimeter:.2f}'
        comparison7 = f'A circle has {nsides} side | Area = {area} | Perimeter = {perimeter} '
        comparison8 = f'A circle has {nsides} side | Area = {area:.2f} | Perimeter = {perimeter:.2f} '
        comparison9 = f'A circle has {nsides:.2f} side | Area = {area:.2f} | Perimeter = {perimeter:.2f} '
        comparison10 = f'A circle has {nsides} sides | Area = {area} | Perimeter = {perimeter} '
        comparison11 = f'A circle has {nsides} sides | Area = {area:.2f} | Perimeter = {perimeter:.2f} '
        comparison12 = f'A circle has {nsides:.2f} sides | Area = {area:.2f} | Perimeter = {perimeter:.2f} '
        comparison_list.append(comparison1)
        comparison_list.append(comparison2)
        comparison_list.append(comparison3)
        comparison_list.append(comparison4)
        comparison_list.append(comparison5)
        comparison_list.append(comparison6)
        comparison_list.append(comparison7)
        comparison_list.append(comparison8)
        comparison_list.append(comparison9)
        comparison_list.append(comparison10)
        comparison_list.append(comparison11)
        comparison_list.append(comparison12)

        self.assertIn(str(circle), comparison_list)

    def test_set_number_of_sides(self):
        shape = Shape(3)
        shape.set_number_of_sides(4)
        self.assertEqual(shape.number_of_sides, 4)

    def test_get_number_of_sides(self):
        shape = Shape(3)
        self.assertEqual(shape.get_number_of_sides(), 3)

    def test_s_calculate_area(self):
        shape = Shape(3)
        self.assertEqual(shape.calculate_area(), None)

    def test_s_calculate_perimeter(self):
        shape = Shape(3)
        self.assertEqual(shape.calculate_perimeter(), None)

if __name__ == '__main__':
    unittest.main()



