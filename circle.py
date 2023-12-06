import math
import unittest

def area(r):
    return math.pi * r * r

def perimeter(r):
    return 2 * math.pi * r

class CircleTestcase(unittest.TestCase):
    def test_zero_mul_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_zero_mul_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_calculation_area(self):
        res = round(area(7), 5)
        self.assertEqual(res, 153.93804)

    def test_calculation_perimeter(self):
        res = round(perimeter(4), 5)
        self.assertEqual(res, 25.13274)

    def test_string_input_area(self):
        with self.assertRaises(TypeError):
            area('2')

    def test_string_input_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter('4')

