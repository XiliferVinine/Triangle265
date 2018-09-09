# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(6, 8, 10), 'Right', '6,8,10 is a Right triangle')
        self.assertEqual(classifyTriangle(30, 40, 50), 'Right', '30,40,50 is a Right triangle')
        self.assertEqual(classifyTriangle(69, 92, 115), 'Right', '69,92,115 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')
        self.assertEqual(classifyTriangle(4, 4, 4), 'Equilateral', '4,4,4 should be equilateral')
        self.assertEqual(classifyTriangle(199, 199, 199), 'Equilateral', '199,199,199 should be equilateral')
        self.assertEqual(classifyTriangle(42, 42, 42), 'Equilateral', '42,42,42 should be equilateral')
        self.assertEqual(classifyTriangle(111, 111, 111), 'Equilateral', '111,111,111 should be equilateral')

    def testIsocelesTriangles(self):
        self.assertEqual(classifyTriangle(6, 6, 10), 'Isoceles', '6,6,10 should be Isoceles')
        self.assertEqual(classifyTriangle(36, 60, 36), 'Isoceles', '6,6,10 should be Isoceles')
        self.assertEqual(classifyTriangle(12, 12, 20), 'Isoceles', '12,12,20 should be Isoceles')
        self.assertEqual(classifyTriangle(180, 40, 180), 'Isoceles', '6,6,10 should be Isoceles')
        self.assertEqual(classifyTriangle(6, 45, 45), 'Isoceles', '6,45,45 should be Isoceles')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(6, 8, 9), 'Scalene', '6,8,9 should be Scalene')
        self.assertEqual(classifyTriangle(12, 88, 99), 'Scalene', '12,88,99 should be Scalene')
        self.assertEqual(classifyTriangle(6, 12, 10), 'Scalene', '6,12,10 should be Scalene')
        self.assertEqual(classifyTriangle(40, 30, 60), 'Scalene', '40,30,60 should be Scalene')
        self.assertEqual(classifyTriangle(9, 4, 10), 'Scalene', '9,4,10 should be Scalene')
        self.assertEqual(classifyTriangle(120, 150, 125), 'Scalene', '120,150,125 should be Scalene')


    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(2, 4, 46), 'NotATriangle', '2,4,46 is NOT a Triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

