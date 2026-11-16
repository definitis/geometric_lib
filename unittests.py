import unittest
import math
import circle
import rectangle
import square
import triangle

class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_perimeter_zero(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_area_float(self):
        res = circle.area(2.5)
        self.assertEqual(res, 6.25 * math.pi)

    def test_perimeter_float(self):
        res = circle.perimeter(1.2)
        self.assertEqual(res, 2.4 * math.pi)

    def test_area_regular(self):
        res = circle.area(5)
        self.assertEqual(res, 25 * math.pi)

    def test_perimeter_regular(self):
        res = circle.perimeter(5)
        self.assertEqual(res, 10 * math.pi)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            circle.area("abc")


class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = rectangle.area(0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_zero(self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_area_float(self):
        res = rectangle.area(2.5, 3)
        self.assertEqual(res, 7.5)

    def test_perimeter_float(self):
        res = rectangle.perimeter(1.2, 1.5)
        self.assertEqual(res, 5.4)

    def test_area_regular(self):
        res = rectangle.area(5, 3)
        self.assertEqual(res, 15)

    def test_perimeter_regular(self):
        res = rectangle.perimeter(5, 1)
        self.assertEqual(res, 12)


class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_perimeter_zero(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_area_float(self):
        res = square.area(2.5)
        self.assertEqual(res, 6.25)

    def test_perimeter_float(self):
        res = square.perimeter(1.2)
        self.assertEqual(res, 4.8)

    def test_area_regular(self):
        res = square.area(5)
        self.assertEqual(res, 25)

    def test_perimeter_regular(self):
        res = square.perimeter(5)
        self.assertEqual(res, 20)

    def test_perimeter_string(self):
        res = square.perimeter("abc")
        self.assertEqual(res, "abcabcabcabc")

class TriangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = triangle.area(0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_zero(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_area_float(self):
        res = triangle.area(2.5, 3)
        self.assertEqual(res, 3.75)

    def test_perimeter_float(self):
        res = triangle.perimeter(1.2, 1.2, 1.5)
        self.assertEqual(res, 3.9)

    def test_area_regular(self):
        res = triangle.area(5, 3)
        self.assertEqual(res, 7.5)

    def test_perimeter_regular(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)
