import unittest
from math import pi
from shapes import Circle, Triangle, calculate_area


class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(1)
        self.assertAlmostEqual(circle.area(), pi)
        self.assertAlmostEqual(calculate_area(1), pi)
        self.assertAlmostEqual(calculate_area(circle), pi)

    def test_circle_validation(self):
        with self.assertRaises(ValueError):
            Circle(-1)
        with self.assertRaises(ValueError):
            Circle(0)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6)
        self.assertAlmostEqual(calculate_area((3, 4, 5)), 6)
        self.assertAlmostEqual(calculate_area(triangle), 6)

    def test_triangle_validation(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)  # 1+1 < 3
        with self.assertRaises(ValueError):
            Triangle(-1, 2, 2)
        with self.assertRaises(ValueError):
            Triangle(0, 0, 0)

    def test_right_angled(self):
        self.assertTrue(Triangle(3, 4, 5).is_right_angled())
        self.assertTrue(Triangle(5, 12, 13).is_right_angled())
        self.assertTrue(Triangle(8, 15, 17).is_right_angled())
        self.assertFalse(Triangle(5, 5, 5).is_right_angled())

    def test_invalid_shape(self):
        with self.assertRaises(ValueError):
            calculate_area("not a shape")
        with self.assertRaises(ValueError):
            calculate_area((1, 2))  # needs exactly 3 sides


if __name__ == "__main__":
    unittest.main()