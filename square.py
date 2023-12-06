import unittest
def area(a):
    return a * a


def perimeter(a):
    return 4 * a

class SquareTestcase(unittest.TestCase):
    def test_zero_mul_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_zero_mul_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_calculation_area(self):
        res = area(4)
        self.assertEqual(res, 16)

    def test_calculation_perimeter(self):
        res = perimeter(4)
        self.assertEqual(res, 16)

    def test_string_input_area(self):
        with self.assertRaises(TypeError):
            area('5')

    def test_string_input_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter('10')
