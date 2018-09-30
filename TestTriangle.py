# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    """
    Module to run unittests for the Triangle python code
    """

    def test_right_triangle_a(self):
        """Tests to determine that program can correctly associate Right Triangles"""
        self.assertEqual(classify_triangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')
        self.assertEqual(classify_triangle(6, 8, 10), 'Right', '6,8,10 is a Right triangle')
        self.assertEqual(classify_triangle(30, 40, 50), 'Right', '30,40,50 is a Right triangle')
        self.assertEqual(classify_triangle(69, 92, 115), 'Right', '69,92,115 is a Right triangle')

    def test_right_triangle_b(self):
        """Tests to determine that program can correctly associate Right Triangles"""
        self.assertEqual(classify_triangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')
    def test_equilateral_triangles(self):
        """Tests to determine that program can correctly associate Equilateral Triangles"""
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral', '1,1,1 is equil')
        self.assertEqual(classify_triangle(4, 4, 4), 'Equilateral', '4,4,4 is equil')
        self.assertEqual(classify_triangle(199, 199, 199), 'Equilateral', '199,199,199 is equil')
        self.assertEqual(classify_triangle(42, 42, 42), 'Equilateral', '42,42,42 is equil')
        self.assertEqual(classify_triangle(111, 111, 111), 'Equilateral', '111,111,111 is equil')

    def test_isoceles_triangles(self):
        """Tests to determine that program can correctly associate Isoceles Triangles"""
        self.assertEqual(classify_triangle(6, 6, 10), 'Isoceles', '6,6,10 is Isoceles')
        self.assertEqual(classify_triangle(36, 60, 36), 'Isoceles', '6,6,10 is Isoceles')
        self.assertEqual(classify_triangle(12, 12, 20), 'Isoceles', '12,12,20 is Isoceles')
        self.assertEqual(classify_triangle(180, 40, 180), 'Isoceles', '6,6,10 is Isoceles')
        self.assertEqual(classify_triangle(6, 45, 45), 'Isoceles', '6,45,45 is Isoceles')

    def test_scalene_triangles(self):
        """Tests to determine that program can correctly associate Scalene Triangles"""
        self.assertEqual(classify_triangle(6, 8, 9), 'Scalene', '6,8,9 is Scalene')
        self.assertEqual(classify_triangle(12, 88, 99), 'Scalene', '12,88,99 is Scalene')
        self.assertEqual(classify_triangle(6, 12, 10), 'Scalene', '6,12,10 is Scalene')
        self.assertEqual(classify_triangle(40, 30, 60), 'Scalene', '40,30,60 is Scalene')
        self.assertEqual(classify_triangle(9, 4, 10), 'Scalene', '9,4,10 is Scalene')
        self.assertEqual(classify_triangle(120, 150, 125), 'Scalene', '120,150,125 is Scalene')


    def test_not_a_triangle(self):
        """Tests to determine that program can correctly associate NON Triangles"""
        self.assertEqual(classify_triangle(2, 4, 46), 'NotATriangle', '2,4,46 is NOT a Triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
