'''
    author:    Ash Searle    kss0024@auburn.edu
    created:   12/27/19
    updated:   7/12/20
    
    purpose:   validate the integrity of a STL file
'''

import unittest
import sys
import re
import ieeeConverter
import targetPrinter as p

class V3DPTestCases(unittest.TestCase):
	GCODE_PATH = ""
	GCODE_INPUT = ""
	SKIP_TEST = None
	BED_TEMP_HEADER1 = 'M140 S(\d+)'
	BED_TEMP_HEADER2 = 'M190 S(\d+)'
	BED_TEMP_VAR = p.BED_TEMP_VAR
	MAX_BED_TEMP_VAR = p.MAX_BED_TEMP_VAR


	@classmethod
	def setUpClass(cls):
		if ".gcode" in cls.GCODE_PATH:
			cls.SKIP_TEST = False
			with open(cls.GCODE_PATH, 'r') as f:
				cls.GCODE_INPUT = f.read()
		else:
			cls.SKIP_TEST = True

	def setUp(self):
		if self.SKIP_TEST == True:
			self.skipTest("Not G-Code file")

	def test100_920_bedTemp(self):
		expectedResult = True
		actualResult = False
		
		m = re.findall(self.BED_TEMP_HEADER1, self.GCODE_INPUT)
		if len(m) == 0:
			actualResult = True
		else:
			for element in m:
				current = float(element)
				if current != 0 and current != self.BED_TEMP_VAR:
					actualResult = "Bed Temp Error: value(" + str(current) + ") != value(" + str(self.BED_TEMP_VAR) + ")"
					break
				else:
					actualResult = True
		self.assertEqual(expectedResult, actualResult)

	def test100_921_bedTemp(self):
		expectedResult = True
		actualResult = False
		
		m = re.findall(self.BED_TEMP_HEADER2, self.GCODE_INPUT)
		if len(m) == 0:
			actualResult = True
		else:
			for element in m:
				current = float(element)
				if current != 0 and current != self.BED_TEMP_VAR:
					actualResult = "Bed Temp Error: value(" + str(current) + ") != value(" + str(self.BED_TEMP_VAR) + ")"
					break
				else:
					actualResult = True
		self.assertEqual(expectedResult, actualResult)

	def test100_930_bedTempMax(self):
		expectedResult = True
		actualResult = False
		
		m = re.findall(self.BED_TEMP_HEADER1, self.GCODE_INPUT)
		if len(m) == 0:
			actualResult = True
		else:
			for element in m:
				current = float(element)
				if current > self.MAX_BED_TEMP_VAR:
					actualResult = "Bed Temp Error: value(" + str(current) + ") > bounds(" + str(self.MAX_BED_TEMP_VAR) + ")" 
					break
				else:
					actualResult = True
		self.assertEqual(expectedResult, actualResult)

	def test100_931_bedTempMax(self):
		expectedResult = True
		actualResult = False
		
		m = re.findall(self.BED_TEMP_HEADER2, self.GCODE_INPUT)
		if len(m) == 0:
			actualResult = True
		else:
			for element in m:
				current = float(element)
				if current > self.MAX_BED_TEMP_VAR:
					actualResult = "Bed Temp Error: value(" + str(current) + ") > bounds(" + str(self.MAX_BED_TEMP_VAR) + ")" 
					break
				else:
					actualResult = True
		self.assertEqual(expectedResult, actualResult)


if __name__ == '__main__':
	if len(sys.argv) > 1:
		filePath = sys.argv.pop()
		V3DPTestCases.GCODE_PATH = filePath
	unittest.main()

