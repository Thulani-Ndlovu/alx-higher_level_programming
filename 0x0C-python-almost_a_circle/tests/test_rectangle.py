#!/usr/bin/python3
# rectangleTests.py
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)  

    def test_rectangleIsBase(self):
        self.assertIsInstance(Rectangle(5, 4), Base)

    def test_zeroArguments(self):
        self.assertRaises(TypeError, Rectangle)

    def test_oneArgument(self):
        self.assertRaises(TypeError, Rectangle, 1)

    def test_twoArguments(self):
        self.assertEqual(self.r1.id, self.r2.id - 1)

    def test_threeArguments(self):
        self.assertEqual(self.r1.id, self.r2.id - 1)

    def test_fourArguments(self):
        self.assertEqual(self.r1.id, self.r2.id - 1)

    def test_fiveArguments(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_ArgumentOverflow(self):
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_widthGetter(self):
        r1 = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r1.width)

    def test_widthSetter(self):
        r1 = Rectangle(5, 7, 7, 5, 1)
        r1.width = 10
        self.assertEqual(10, r1.width)

    def test_height_getter(self):
        r1 = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r1.height)

    def test_heightSetter(self):
        r1 = Rectangle(5, 7, 7, 5, 1)
        r1.height = 10
        self.assertEqual(10, r1.height)

    def test_xGetter(self):
        r1 = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r1.x)

    def test_xSetter(self):
        r1 = Rectangle(5, 7, 7, 5, 1)
        r1.x = 10
        self.assertEqual(10, r1.x)

    def test_yGetter(self):
        r1 = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r1.y)

    def test_ySetter(self):
        r1 = Rectangle(5, 7, 7, 5, 1)
        r1.y = 10
        self.assertEqual(10, r1.y)

if __name__ == "__main__":
    unittest.main()
