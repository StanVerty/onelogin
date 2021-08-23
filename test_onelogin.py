import unittest
import onelogin
from fractions import Fraction


class TestOnelogin(unittest.TestCase):

    def test_input_number(self):
        self.assertEqual(onelogin.input_number("1/2"), Fraction(1, 2))
        self.assertEqual(onelogin.input_number("2_1/2"), Fraction(5, 2))
        self.assertEqual(onelogin.input_number("1/1"), Fraction(1))
        self.assertEqual(onelogin.input_number("0/1"), Fraction(0))


    def test_output_result(self):
        self.assertEqual(onelogin.output_result(Fraction(1, 2)), "1/2")
        self.assertEqual(onelogin.output_result(Fraction(5, 2)), "2_1/2")
        self.assertEqual(onelogin.output_result(Fraction(3)), "3")




# if __name__ == '__mane__':
#     unittest.main()
