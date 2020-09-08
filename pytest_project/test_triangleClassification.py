# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016

This file shows some simple (and buggy) python code to solve the Triangles assignment.   
The primary goal of this file is to demonstrate a simple python program and the use of the
unittest package.

Note that this code includes intentional errors for you to find.


@author: jrr
"""

import unittest     # this makes Python unittest module available

def classifyTriangle(a,b,c):
	"""
	
	This function returns a string with the type of triangle from three  values
	corresponding to the lengths of the three sides of the Triangle.
	
	return:
		If all three sides are equal, return 'Equilateral'
		If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
        
        
	"""
	if a+b<=c or a+c<=b or b+c<=a:
		return 'NotATriangle'
	elif a == b and b == c:
		return 'Equilateral'
	elif a*a+b*b == c*c or c*c+b*b== a*a or a*a+c*c==b*b:
		return 'Right'
	elif a == b or b == c or a==c:
		return 'Isoceles'
	else:
		return 'Scalene'
    
        
        
def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c))#,sep="")


# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
	# define multiple sets of tests as functions with names that begin
	# with 'test'.  Each function may include multiple tests
	def testSet1(self): # test invalid inputs
		# your tests go here.  Include as many tests as you'd like
		self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
		self.assertEqual(classifyTriangle(4,3,5),'Right','3,4,5 is a Right triangle')
		self.assertEqual(classifyTriangle(5,4,3),'Right','3,4,5 is a Right triangle')
		self.assertNotEqual(classifyTriangle(3,4,6),'Right','3,4,6 is not a Right triangle')
		
	def testMyTestSet2(self): 
		# define multiple test sets to test different aspects of the code
		# notice that tests can have bugs too! (Fixed!)
		self.assertEqual(classifyTriangle(10,10,6),'Isoceles','10,10,6 is a Isoceles triangle')
		self.assertEqual(classifyTriangle(6,10,10),'Isoceles','10,10,6 is a Isoceles triangle')
		self.assertEqual(classifyTriangle(10,6,10),'Isoceles','10,10,6 is a Isoceles triangle')
		self.assertNotEqual(classifyTriangle(10,6,7),'Isoceles','10,6,7 is not a Isoceles triangle')

	def testSet3(self):
		self.assertEqual(classifyTriangle(21,20,19),'Scalene','21,20,19 is a Scalene triangle')
		self.assertEqual(classifyTriangle(20,21,19),'Scalene','21,20,19 is a Scalene triangle')
		self.assertEqual(classifyTriangle(21,19,20),'Scalene','21,20,19 is a Scalene triangle')
		self.assertNotEqual(classifyTriangle(21,21,21),'Scalene','21,21,21 is Not a Scalene triangle')
	
	def testSet4(self):
		self.assertEqual(classifyTriangle(2,2,2),'Equilateral','2,2,2 is a Equilateral triangle')
		self.assertEqual(classifyTriangle(3,3,3),'Equilateral','3,3,3 is a Equilateral triangle')
		self.assertEqual(classifyTriangle(4,4,4),'Equilateral','4,4,4 is a Equilateral triangle')
		self.assertNotEqual(classifyTriangle(1,2,2),'Equilateral','1,2,2 is Not Equilateral triangle')
	
	def testSet5(self):
		self.assertEqual(classifyTriangle(1,5,2),'NotATriangle','1,5,2 is Not a triangle')
		self.assertEqual(classifyTriangle(6,5,1),'NotATriangle','6,5,1 is Not a triangle')
		self.assertEqual(classifyTriangle(30,10,10),'NotATriangle','30,10,10 is Not a triangle')
		self.assertNotEqual(classifyTriangle(4,3,2),'NotATriangle','4,3,2 is a triangle')
		
		
if __name__ == '__main__':
    # examples of running the code
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)
    runClassifyTriangle(3,4,5)
    runClassifyTriangle(3,3,5)
    #unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line  