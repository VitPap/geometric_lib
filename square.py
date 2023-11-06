import unittest
def area(a):
    return a * a


def perimeter(a):
    return 4 * a

class SquareTestcase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_calculation_area(self):
        res = area(4)
        self.assertEqual(res, 16)

    def test_calculation_perimeter(self):
        res = perimeter(4)
        self.assertEqual(res, 16)
