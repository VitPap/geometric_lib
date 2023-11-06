import unittest

def area(a, b):
    return a * b 

def perimeter(a, b): 
    return (a + b) * 2

class RectangleTestcase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0, 5)
        self.assertEqual(res, 0)
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_calculation_area(self):
        res = area(5, 6)
        self.assertEqual(res, 30)

    def test_calculation_perimeter(self):
        res = perimeter(5, 6)
        self.assertEqual(res, 22)