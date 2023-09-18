#!/usr/bin/python3

"""Tests for Rectangle module."""


import unittest
from models.rectangle import Rectangle

class RectangleTests(unittest.TestCase):
	"""Tests for Rectangle class."""
	def setUp(self):
    	self.rect = Rectangle(15, 20)

	def test_width(self):
    	"""Testing width"""
    	self.assertEqual(self.rect.width, 15)

	def test_height(self):
    	"""Testing height"""
    	self.assertEqual(self.rect.height, 20)

	def test_x_val(self):
    	"""testing the x value"""
    	self.rect.x = 0
    	self.assertEqual(self.rect.x, 0)

	def test_y_val(self):
    	"""testing the x value"""
    	self.rect.y = 0
    	self.assertEqual(self.rect.y, 0)

	def test_x_neg(self):
    	"""testing assigning neg to x"""
    	with self.assertRaises(ValueError):
        	self.rect.x = -1

	def test_y_neg(self):
    	"""testing assigning neg to y"""
    	with self.assertRaises(ValueError):
        	self.rect.y = -1

	def test_width_zero(self):
    	"""testing assigning 0 to width"""
    	with self.assertRaises(ValueError):
        	self.rect.width = 0

	def test_height_zero(self):
    	"""testing assigning 0 to height"""
    	with self.assertRaises(ValueError):
        	self.rect.height = 0

	def test_string_assign_width(self):
    	"""test assigning string to width"""
    	with self.assertRaises(TypeError):
        	self.rect.width = "4"

	def test_string_assign_height(self):
    	"""test assigning string to height"""
    	with self.assertRaises(TypeError):
        	self.rect.height = "4"

	def test_bool_assign_width(self):
    	"""test assigning bool to width"""
    	with self.assertRaises(TypeError):
        	self.rect.width = True

	def test_bool_assign_height(self):
    	"""test assigning bool to height"""
    	with self.assertRaises(TypeError):
        	self.rect.height = True

	def test_none_assign_width(self):
    	"""test assigning None to width"""
    	with self.assertRaises(TypeError):
        	self.rect.width = None

	def test_none_assign_height(self):
    	"""test assigning None to height"""
    	with self.assertRaises(TypeError):
        	self.rect.height = None

	def test_float_assign_width(self):
    	"""testing assigning float value to width"""
    	with self.assertRaises(TypeError):
        	self.rect.width = 7.8
    
	def test_float_assign_height(self):
    	"""testing assigning float value to height"""
    	with self.assertRaises(TypeError):
        	self.rect.height = 7.8

	def test_list_assign_width(self):
    	"""testing assigning float value to width"""
    	with self.assertRaises(TypeError):
        	self.rect.width = [8, 9]

	def test_list_assign_height(self):
    	"""testing assigning float value to height"""
    	with self.assertRaises(TypeError):
        	self.rect.height = [8, 9]

	def test_string_assign_x(self):
    	"""test assigning string to x"""
    	with self.assertRaises(TypeError):
        	self.rect.x = "4"

	def test_string_assign_y(self):
    	"""test assigning string to y"""
    	with self.assertRaises(TypeError):
        	self.rect.y = "4"

	def test_bool_assign_x(self):
    	"""test assigning bool to x"""
    	with self.assertRaises(TypeError):
        	self.rect.x = True

	def test_bool_assign_y(self):
    	"""test assigning bool to y"""
    	with self.assertRaises(TypeError):
        	self.rect.y = True

	def test_none_assign_x(self):
    	"""test assigning None to x"""
    	with self.assertRaises(TypeError):
        	self.rect.x = None

	def test_none_assign_y(self):
    	"""test assigning None to y"""
    	with self.assertRaises(TypeError):
        	self.rect.y = None

	def test_float_assign_x(self):
    	"""testing assigning float value to x"""
    	with self.assertRaises(TypeError):
        	self.rect.x = 7.8
    
	def test_float_assign_y(self):
    	"""testing assigning float value to y"""
    	with self.assertRaises(TypeError):
        	self.rect.y = 7.8

	def test_list_assign_x(self):
    	"""testing assigning float value to x"""
    	with self.assertRaises(TypeError):
        	self.rect.x = [8, 9]

	def test_list_assign_y(self):
    	"""testing assigning float value to y"""
    	with self.assertRaises(TypeError):
        	self.rect.y = [8, 9]

	def test_id(self):
    	"""test checking id"""
    	r = Rectangle(1, 2, 3, 4, 27)
    	self.assertEqual(r.id, 27)

	def test_area(self):
    	"""testing area"""
    	self.assertEqual(self.rect.area(), self.rect.height * self.rect.width)

	def test_normal_update(self):
    	"""normal testing of the update function"""
    	self.rect.update(12, 67, 22, 1, 9)
    	self.assertEqual(self.rect.id, 12)
    	self.assertEqual(self.rect.width, 67)
    	self.assertEqual(self.rect.height, 22)
    	self.assertEqual(self.rect.x, 1)
    	self.assertEqual(self.rect.y, 9)

	def tearDown(self):
    	del self.rect
	def test_id_update(self):
    	"""updating the id using update"""
    	self.rect.update(77)
    	self.assertEqual(self.rect.id, 77)

	def test_string_id_update(self):
    	"""updating the id using update"""
    	with self.assertRaises(TypeError):
        	self.rect.update("77")

	def test_list_id_update(self):
    	"""test to assigning list to update"""
    	with self.assertRaises(TypeError):
        	self.rect.update([1, 2, 3, 4])

	def test_float_id_update(self):
    	"""test to assigning float to update"""
    	with self.assertRaises(TypeError):
        	self.rect.update(8.9)

	def test_str_str_update(self):
    	"""test assigning string to update"""
    	with self.assertRaises(TypeError):
        	self.rect.update(69, "haha", "nice")

	def test_overload_update(self):
    	"""test passing more than 5 values to update"""
    	with self.assertRaises(IndexError):
        	self.rect.update(12, 67, 22, 1, 9, 234, 12, 395, 45945)

	def test_kwargs_update(self):
    	"""test to check the kwargs values are assigned"""
    	self.rect.update(y=54, height=65, x=12, width=89, id=89)
    	self.assertEqual(self.rect.id, 89)
    	self.assertEqual(self.rect.width, 89)
    	self.assertEqual(self.rect.height, 65)
    	self.assertEqual(self.rect.x, 12)
    	self.assertEqual(self.rect.y, 54)

	def test_kwargs_args_update(self):
    	"""test to put kwargs and args together"""
    	self.rect.update(1, 2, 3, height=45)
    	self.assertEqual(self.rect.id, 1)
    	self.assertEqual(self.rect.width, 2)
    	self.assertEqual(self.rect.height, 3)

	def test_display(self):
    	self.rect.update(4, 4, 5)

	def tearDown(self):
    	del self.rect

class TestRectangleDisplay(unittest.TestCase):

	def setUp(self):
    	"""Redirect stdout to capture the printed output"""
    	self.saved_stdout = sys.stdout
    	self.output = StringIO()
    	sys.stdout = self.output

	def tearDown(self):
    	"""Restore the original stdout"""
    	sys.stdout = self.saved_stdout

	def test_display_no_offset(self):
    	"""tesing no display offset"""
    	r = Rectangle(3, 2)
    	r.display()
    	expected_output = "###\n###\n"
    	self.assertEqual(self.output.getvalue(), expected_output)

	def test_display_with_offset(self):
    	"""testing display offset"""
    	r = Rectangle(3, 2, 2, 1)
    	r.display()
    	expected_output = "\n  ###\n  ###\n"
    	self.assertEqual(self.output.getvalue(), expected_output)

	def test_display_empty_rectangle(self):
    	"""testing empty rectangle"""
    	with self.assertRaises(ValueError):
        	r = Rectangle(0, 0)
        	r.display()



class Testrectangle_updating_args(unittest.TestCase):
    """Unittests for args attribute of class rectangle"""

    def test_update_args_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_args_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))

    def test_update_args_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_args_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_args_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))

    def test_update_args_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_more_than_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_None_id_and_more(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None, 4, 5, 2)
        correct = "[Rectangle] ({}) 2/10 - 4/5".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        r.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(r))

    def test_update_args_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid")

    def test_update_args_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, 0)

    def test_update_args_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, -5)

    def test_update_args_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 2, "invalid")

    def test_update_args_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, 0)

    def test_update_args_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, -5)

    def test_update_args_invalid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, 3, "invalid")

    def test_update_args_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(89, 1, 2, -6)

    def test_update_args_invalid_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 2, 3, 4, "invalid")

    def test_update_args_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(89, 1, 2, 3, -6)

    def test_update_args_width_before_height(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", "invalid")

    def test_update_args_width_before_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, "invalid")

    def test_update_args_width_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, 2, "invalid")

    def test_update_args_height_before_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", "invalid")

    def test_update_args_height_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", 1, "invalid")

    def test_update_args_x_before_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 1, 2, "invalid", "invalid")

class Testrectangle_updating_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of the Rectangle class."""

    def test_update_kwargs_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    def test_update_kwargs_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def test_update_kwargs_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_kwargs_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))

    def test_update_kwargs_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(r))

    def test_update_kwargs_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_None_id_and_more(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None, height=7, y=9)
        correct = "[Rectangle] ({}) 10/9 - 10/7".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2)
        r.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(r))

def test_update_kwargs_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid")

    def test_update_kwargs_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_update_kwargs_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-5)

    def test_update_kwargs_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_update_kwargs_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-5)

    def test_update_kwargs_inavlid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def test_update_args_and_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_kwargs_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_kwargs_some_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(r))


class Testrectangle_to_dict(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Rectangle class."""

    def test_to_dictionary_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg(self):
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()

