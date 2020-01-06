'''
    author:    Ash Searle    kss0024@auburn.edu
    created:   12/27/19
    updated:   1/4/20
    
    purpose:   validate the integrity of a STL file
'''

import unittest
import sys

class V3DPTestCases(unittest.TestCase):
	GCODE_INPUT = ""

	def setUp(self):
		pass

	def test100_500_maxTemp(self):
		expectedResult = 0
		actualResult = 1
		self.assertEqual(expectedResult, actualResult)


if __name__ == '__main__':
	# if len(sys.argv) > 1:
	# 	V3DPTestCases.GCODE_INPUT = sys.argv.pop()
	unittest.main()