#!/usr/bin/python3
"""
This is the "test_square" module
Thes test_square module supplies a class to test class Square
"""

from re import S
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from os.path import exists
import io
from contextlib import redirect_stdout


class TestSquare(unittest.TestCase):
    """
    test classe square
    """

    def setUp(self):
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        pass

    def test_subclass(self):
        """fuction that test if Rectangle is a subclass of Base"""
        self.assertTrue(issubclass(Square, Base))

    def test_subclass(self):
        """fuction that test if Rectangle is a subclass of Base"""
        self.assertTrue(issubclass(Square, Rectangle))

    # test correct values

    def test_correct_values(self):
        r1 = Square(2, 4, 6)
        self.assertEqual(r1.size, 2)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 6)
        self.assertEqual(r1.id, 1)

        r2 = Square(2, 4, 6, 50)
        self.assertEqual(r2.size, 2)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.y, 6)
        self.assertEqual(r2.id, 50)

        r3 = Square(2)
        self.assertEqual(r3.size, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        self.assertEqual(r3.id, 2)


    def test_priority_width_height(self):
        """fuction that test for TypeError"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("str", "str", 3, None)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("str", -2, 3, None)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, -2, 3, None)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, "str", 3, None)

    # tests getters

    def test_getter_width(self):
        r4 = Square(2, 4, 6)
        self.assertEqual(r4.size, 2)

    def test_getter_x(self):
        r4 = Square(2, 4, 6)
        self.assertEqual(r4.x, 4)

    def test_getter_y(self):
        r4 = Square(2, 4, 6)
        self.assertEqual(r4.y, 6)

    # tests setters #

    def test_setter_width(self):
        r4 = Square(2, 4, 6)
        r4.size = 100
        self.assertEqual(r4.size, 100)

    def test_setter_x(self):
        r4 = Square(2, 4, 6)
        r4.x = 10
        self.assertEqual(r4.x, 10)

    def test_setter_y(self):
        r4 = Square(2, 4, 6)
        r4.y = 12
        self.assertEqual(r4.y, 12)

    # tests ValueError

    def test_negative_size(self):
        with self.assertRaises(ValueError):
            Square(-5, 10, 8)

    def test_zero_size(self):
        with self.assertRaises(ValueError):
            Square(0, 10, 8)

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            Square(6, -8, 8)

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            Square(5, 8, -7)

    # tests TypeError

    def test_too_many_arguments(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 6)

    # str :

    def test_string_size(self):
        with self.assertRaises(TypeError):
            Square("hello", 10, 8)

    def test_string_x(self):
        with self.assertRaises(TypeError):
            Square(10, "hello", 8)

    def test_string_y(self):
        with self.assertRaises(TypeError):
            Square(10, 5, "hello")

    # list :

    def test_list_size(self):
        with self.assertRaises(TypeError):
            Square([0, 1, 2], 10, 8)

    def test_list_x(self):
        with self.assertRaises(TypeError):
            Square(10, 10, [0, 1, 2], 8)

    def test_list_y(self):
        with self.assertRaises(TypeError):
            Square(10, 5, [0, 1, 2])

    # tuple :

    def test_tuple_size(self):
        with self.assertRaises(TypeError):
            Square((0, 1, 2), 10, 8, 8)

    def test_tuple_x(self):
        with self.assertRaises(TypeError):
            Square(10, (0, 1, 2), 8)

    def test_tuple_y(self):
        with self.assertRaises(TypeError):
            Square(10, 5, (0, 1, 2))

    # float :

    def test_float_size(self):
        with self.assertRaises(TypeError):
            Square(3.5, 10, 8)

    def test_float_x(self):
        with self.assertRaises(TypeError):
            Square(10, 3.5, 8)

    def test_float_y(self):
        with self.assertRaises(TypeError):
            Square(10, 5, 3.5)

    def test_float_nan_size(self):
        with self.assertRaises(TypeError):
            Square(float('nan'), 10, 8)

    def test_float_nan_x(self):
        with self.assertRaises(TypeError):
            Square(10, float('nan'), 8)

    def test_float_nan_y(self):
        with self.assertRaises(TypeError):
            Square(10, 5, float('nan'))

    def test_float_inf_size(self):
        with self.assertRaises(TypeError):
            Square(float('inf'), 10, 8, 8)

    def test_float_inf_x(self):
        with self.assertRaises(TypeError):
            Square(10, float('inf'), 8)

    def test_float_inf_y(self):
        with self.assertRaises(TypeError):
            Square(10, 5, float('inf'))

    # Bool :

    def test_Bool_size(self):
        with self.assertRaises(TypeError):
            Square(True, 10, 8)

    def test_Bool_x(self):
        with self.assertRaises(TypeError):
            Square(10, True, 8)

    def test_Bool_y(self):
        with self.assertRaises(TypeError):
            Square(10, 5, True)

    # None :

    def test_None_size(self):
        with self.assertRaises(TypeError):
            Square(None, 10, 8)

    def test_None_x(self):
        with self.assertRaises(TypeError):
            Square(10, None, 8)

    def test_None_y(self):
        with self.assertRaises(TypeError):
            Square(10, 5, None)

    # tests Area

    def test_aera(self):
        r1 = Square(10, 0, 0)
        self.assertEqual(r1.area(), 100)

    # tests Display
    def test_diplay(self):
        """Check display func"""
        s1 = Square(2)
        s2 = Square(4, 2, 2)
        with io.StringIO() as buf, redirect_stdout(buf):
            s1.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 2 + "\n")*2)
        with io.StringIO() as buf, redirect_stdout(buf):
            s2.display()
            output = buf.getvalue()
            self.assertEqual(
                output, (2 * "\n" + (" " * 2 + "#" * 4 + "\n") * 4))
    # tests __str___

    def test_str(self):
        r1 = Square(10, 10, 0)
        r2 = Square(10)
        r3 = Square(10, 10, 10, 50)
        self.assertEqual(r1.__str__(), "[Square] (1) 10/0 - 10")
        self.assertEqual(r2.__str__(), "[Square] (2) 0/0 - 10")
        self.assertEqual(r3.__str__(), "[Square] (50) 10/10 - 10")

    # test to_dictionary

    def test_to_dictionnary(self):
        r1 = Square(10, 10, 0)
        # test return type
        self.assertTrue(type(r1.to_dictionary()), dict)
        # test return
        self.assertEqual(r1.to_dictionary(), {
                         'id': 1, 'size': 10, 'x': 10, 'y': 0})

    if __name__ == "__main__":
        unittest.main()
