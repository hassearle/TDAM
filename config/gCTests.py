'''
    author:    Ash Searle    kss0024@auburn.edu
    created:   12/27/19
    updated:   1/10/20
    
    purpose:   validate the integrity of a STL file
'''

import unittest
import sys

class V3DPTestCases(unittest.TestCase):
	GCODE_INPUT = ""

	def setUp(self):
		pass

	def test100_500_maxTemp(self):
		expectedResult = True
		actualResult = False

		if "M104"  in self.GCODE_INPUT:
			actualResult = True
		self.assertEqual(expectedResult, actualResult)
		# expectedResult = True
		# actualResult = True if "top_solid_layers" in self.GCODE_INPUT else self.GCODE_INPUT

		# self.assertEqual(expectedResult, actualResult)


if __name__ == '__main__':
	if len(sys.argv) > 1:
		V3DPTestCases.GCODE_INPUT = sys.argv.pop()
		# print(V3DPTestCases.GCODE_INPUT)
	unittest.main()