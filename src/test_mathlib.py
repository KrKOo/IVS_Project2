# Tests for mathematical library 
# @file mathlib_tests.py
# @brief TDD Tests for the mathematical library
# @author Martin Kozák xkozak18
# Date: 21.3.2021

import unittest
from mathlib import *


class AddTest(unittest.TestCase):
    def test_add_integer(self):
        self.assertEqual(add(0,0), 0)
        self.assertEqual(0, add(-5,5))
        self.assertEqual(3, add(3,0))
        self.assertEqual(321, add(320,1))

    def test_add_float(self):
        self.assertAlmostEqual(0.2, add(0, 0.2))
        self.assertAlmostEqual(4.8, add(1.2, 3.6))
        self.assertAlmostEqual(-2.4, add(-1.2, -1.2))
        self.assertAlmostEqual(1.458321, add(1, 0.458321))
        

class SubTest(unittest.TestCase):
    def test_sub_integer(self):
        self.assertEqual(0, sub(5,5))
        self.assertEqual(-1, sub(5,6))
        self.assertEqual(2, sub(10,8))
        self.assertEqual(-65465, sub(14524, 79989))
    
    def test_sub_test_float(self):
        self.assertAlmostEqual(3.2, sub(5.2, 2))
        self.assertAlmostEqual(2.79, sub(4.25, 1.46))
        self.assertAlmostEqual(-0.5, sub(2, 2.5))
        self.assertAlmostEqual(1000, sub(999.1, -0.9))

class DivTest(unittest.TestCase):

    def test_division_by_zero(self):
        self.assertRaises(ZeroDivisionError, div, 8,0)
        self.assertRaises(ZeroDivisionError, div, -1,0)
        self.assertRaises(ZeroDivisionError, div,42121.1,0)

    def test_division_integer_positive(self):
        self.assertEqual(1, div(2,2))
        self.assertEqual(2, div(8,4))
        self.assertEqual(42, div(195552, 4656))
        

    def test_division_integer_negative(self):
        self.assertEqual(-1, div(-3,3))
        self.assertEqual(4, div(-16, -4))
        self.assertEqual(-3, div(15,-5))

    def test_division_float(self):
        self.assertEqual(2.5, div(5,2))
        self.assertAlmostEqual(-1.7, div(-3.944, 2.32))
        self.assertAlmostEqual(0.666666666, div(2,3), 8)
        self.assertAlmostEqual(3.142857143, div(22,7))

class MulTest(unittest.TestCase):
    
    def test_mul_integer(self):
        self.assertEqual(0, mul(0,5))
        self.assertEqual(8, mul(2,4))
        self.assertEqual(-2, mul(1, -2))
        self.assertEqual(1000, mul(-50,-20))

    def test_mul_float(self):
        self.assertAlmostEqual(0.2, mul(0.1,2))
        self.assertAlmostEqual(-4.5, mul(-1.5, 3))
        self.assertAlmostEqual(-2, mul(0.5, -4))
        self.assertAlmostEqual(-10.2, mul(-2.55,4))

class FractTest(unittest.TestCase):
    
    def test_fact_error(self):
        self.assertRaises(ValueError, fact, -1.2)
        self.assertRaises(ValueError, fact, -5)
        self.assertRaises(ValueError, fact, 1.5)
        self.assertRaises(ValueError, fact, 2.5)

    def test_fact(self):
        self.assertEqual(1, fact(0))
        self.assertEqual(1, fact(1))
        self.assertEqual(2, fact(2))
        self.assertEqual(6, fact(3))
        self.assertEqual(3628800, fact(10))

class PowTest(unittest.TestCase):
    
    def test_pow_error(self):
        self.assertRaises(ValueError, pow, 1, -1)
        self.assertRaises(ValueError, pow, 1, -1.5)
        self.assertRaises(ValueError, pow, 1, 1.5)

    def test_pow_integer(self):
        self.assertEqual(2, pow(2,1)) 
        self.assertEqual(0, pow(0,100))
        self.assertEqual(-64, pow(-4, 3))
        self.assertEqual(256, pow(-4, 4))

    def test_pow_float(self):
        self.assertAlmostEqual(4.41, pow(2.1,2))
        self.assertAlmostEqual(731.1616, pow(5.2,4))
        self.assertAlmostEqual(0.00194481, pow(0.21, 4))
        self.assertAlmostEqual(-31.2079601 ,pow(-1.99,5))


class NthRootTest(unittest.TestCase):
    
    def test_nth_root_error(self):
        self.assertRaises(ValueError, nth_root, -1, 2)
        self.assertRaises(ValueError, nth_root, -1000, -5)
        self.assertRaises(ValueError, nth_root, 5, -2)
        self.assertRaises(ValueError, nth_root, 2, 0)

    def test_nth_root_integer(self):
        self.assertEqual(2, nth_root(4,2))
        self.assertEqual(2, nth_root(8,3))
        self.assertEqual(4, nth_root(256,4))
        self.assertEqual(10, nth_root(10000000000,10))

    def test_nth_root_float(self):
        self.assertAlmostEqual(1.41421356, nth_root(2,2))
        self.assertAlmostEqual(1.14471424, nth_root(1.5,3))
        self.assertAlmostEqual(1.73205080,nth_root(3,2))
        self.assertAlmostEqual(2.17153409, nth_root(3.2,1.5))
        


class ModTest(unittest.TestCase):

    def test_mod_error(self):
        self.assertRaises(ZeroDivisionError, mod, 5,0)

    def test_mod(self):
        self.assertEqual(0 , mod(4,2))
        self.assertEqual(1, mod(4,3))
        self.assertEqual(16, mod(1000, 24))
        self.assertEqual(10, mod(10,11))

if __name__ == '__main__':
    unittest.main()
