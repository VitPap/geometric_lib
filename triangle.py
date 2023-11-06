import unittest

def area(a, h):
    return a * h / 2 

def perimeter(a, b, c): 
    return a + b + c

class TriangleTestcase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0, 5)
        self.assertEqual(res, 0)
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_calculation_area(self):
        res = area(8, 6)
        self.assertEqual(res, 24)

    def test_calculation_perimeter(self):
        res = perimeter(5, 6, 8)
        self.assertEqual(res, 19)