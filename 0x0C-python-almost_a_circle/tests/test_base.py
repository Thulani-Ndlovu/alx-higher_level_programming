#!/usr/bin/python3
# rectangleTests.py
import io
import sys
import unittest
from models.base import Base

class BaseTesting(unittest.TestCase):
    def test_constructor(self):
        b1 = Base(1)
        self.assertEqual(b1.id, 1)
        self.assertIsNotNone(b1)

    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)
        b3 = Base()
        self.assertEqual(b3.id, b2.id + 1)
