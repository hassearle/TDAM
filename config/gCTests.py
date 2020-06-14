'''
    author:    Ash Searle    kss0024@auburn.edu
    created:   12/27/19
    updated:   1/14/20
    
    purpose:   validate the integrity of a STL file
'''

import unittest
import sys
import re

class V3DPTestCases(unittest.TestCase):
	GCODE_INPUT = ""
	TEMP = "M104"
	TEMP_VAR = "210"

	def setUp(self):
		pass

	def test100_100_maxTemp(self):
		expectedResult = True
		actualResult = False
		with open(self.GCODE_INPUT, 'r') as f:
			gCodeInput = f.read()
		m = re.findall('(?<=M104)(.*)', gCodeInput)
		for element in m:
			if self.TEMP_VAR in element:
				actualResult = True
			elif "S0" in element:
				actualResult = True
			else:
				actualResult = False
		
		try:
			self.assertEqual(expectedResult, actualResult)
		except Exception as e:
			raise ValueError("temp wrong")

	def test200_100_fanNeverEngaged(self):
		expectedResult = True
		actualResult = False
		with open(self.GCODE_INPUT, 'r') as f:
			gCodeInput = f.read()

		m = re.search('(?<=M106)(.*)', gCodeInput)
		actualResult = True if m != None else False
		try:
			self.assertEqual(expectedResult, actualResult)
		except Exception as e:
			raise ValueError("fan never engaged")


if __name__ == '__main__':
	if len(sys.argv) > 1:
		V3DPTestCases.GCODE_INPUT = sys.argv.pop()
		# print(V3DPTestCases.GCODE_INPUT)
	unittest.main()
