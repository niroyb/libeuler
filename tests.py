#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author niroyb

import unittest
from libeuler import *


class TestLibEuler(unittest.TestCase):

    def test_factorial(self):
        self.assertEquals(1, factorial(0))
        self.assertEquals(1, factorial(1))
        self.assertEquals(2, factorial(2))
        self.assertEquals(2432902008176640000, factorial(20))

    def test_is_permutation(self):
        self.assertEquals(True, is_permutation(0, 0))
        self.assertEquals(True, is_permutation(123, 231))
        self.assertEquals(True, is_permutation(222, 222))
        
        self.assertEquals(False, is_permutation(0, 1))
        self.assertEquals(False, is_permutation(1, 10))
        self.assertEquals(False, is_permutation(1234, 5678))
        

    def test_is_palindromic(self):
        self.assertEquals(True, is_palindromic(0))
        self.assertEquals(True, is_palindromic(12321))
        self.assertEquals(True, is_palindromic(123321))
        
        self.assertEquals(False, is_palindromic(123))
        self.assertEquals(False, is_palindromic(10))
        self.assertEquals(False, is_palindromic(123123))

    def test_is_pandigital(self):
        self.assertEquals(True, is_pandigital(0, min=0, max=0))
        self.assertEquals(False, is_pandigital(0, min=0, max=1))
        self.assertEquals(True, is_pandigital(10, min=0, max=1))
        
        self.assertEquals(True, is_pandigital(123456789, 1, 9))
        self.assertEquals(False, is_pandigital(1234567891, 1, 9))
        self.assertEquals(False, is_pandigital(12345, 1, 9))
        
        self.assertEquals(True, is_pandigital(1234567890))
        self.assertEquals(True, is_pandigital(9087634521))
        self.assertEquals(False, is_pandigital(12345))
        self.assertEquals(False, is_pandigital(123456789))

if __name__ == '__main__':
    unittest.main()
