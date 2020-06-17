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
	BED_TEMP_HEADER1 = '[M][1][4][0] [S][0-9]{2}'
	BED_TEMP_HEADER2 = '[M][1][9][0] [S][0-9]{2}'
	BED_TEMP_VAR = 25
	MAX_BED_TEMP_VAR = 65
	LAYER_HEIGHT = 0.3
	LAYER_HEIGHT_HEADER = "G1 Z"
	Z_REPOSITION_VAR = 0.5
	DIGITS = '([0-9+].[0-9+]|[0-9+])'

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
				actualResult = "exceeded max temp"	
			self.assertEqual(expectedResult, actualResult)

	def test100_110_bedTemp(self):
		expectedResult = True
		actualResult = False
		with open(self.GCODE_INPUT, 'r') as f:
			gCodeInput = f.read()
		m = re.findall(self.BED_TEMP_HEADER1, gCodeInput)
		for index, element in enumerate(m):
			i = re.search('(?<=S)(.*)', element)
			current = float(i.group(0))
			if current != 0 and current != self.BED_TEMP_VAR:
				actualResult = "incorrect bed temp: index(" + str(index) + ")"
				break
			else:
				actualResult = True
		self.assertEqual(expectedResult, actualResult)

	def test100_111_bedTemp(self):
		expectedResult = True
		actualResult = False
		with open(self.GCODE_INPUT, 'r') as f:
			gCodeInput = f.read()
		m = re.findall(self.BED_TEMP_HEADER2, gCodeInput)
		for index, element in enumerate(m):
			i = re.search('(?<=S)(.*)', element)
			current = float(i.group(0))
			if current != 0 and current != self.BED_TEMP_VAR:
				actualResult = "incorrect bed temp: index(" + str(index) + ")"
				break
			else:
				actualResult = True
		self.assertEqual(expectedResult, actualResult)

	def test100_920_bedTempMax(self):
		expectedResult = True
		actualResult = False
		with open(self.GCODE_INPUT, 'r') as f:
			gCodeInput = f.read()
		m = re.findall(self.BED_TEMP_HEADER1, gCodeInput)
		for index, element in enumerate(m):
			i = re.search('(?<=S)(.*)', element)
			current = float(i.group(0))
			if current > self.MAX_BED_TEMP_VAR:
				actualResult = "exceded max bed temp: index(" + str(index) + ")"
				break
			else:
				actualResult = True
		self.assertEqual(expectedResult, actualResult)

	def test100_921_bedTempMax(self):
		expectedResult = True
		actualResult = False
		with open(self.GCODE_INPUT, 'r') as f:
			gCodeInput = f.read()
		m = re.findall(self.BED_TEMP_HEADER2, gCodeInput)
		for index, element in enumerate(m):
			i = re.search('(?<=S)(.*)', element)
			current = float(i.group(0))
			if current > self.MAX_BED_TEMP_VAR:
				actualResult = "exceded max bed temp: index(" + str(index) + ")"
				break
			else:
				actualResult = True
		self.assertEqual(expectedResult, actualResult)

	def test200_100_fanNeverEngaged(self):
		expectedResult = True
		actualResult = False
		with open(self.GCODE_INPUT, 'r') as f:
			gCodeInput = f.read()

		m = re.search('(?<=M106)(.*)', gCodeInput)
		actualResult = True if m != None else "fan never engaged"
		self.assertEqual(expectedResult, actualResult)

	def test300_100_layerHeight(self):
		expectedResult = True
		actualResult = False
		reLayerHeight = '[G][1] [Z]([0-9+].[0-9+]|[0-9+])[\n][G][1] [E]'

		with open(self.GCODE_INPUT, 'r') as f:
			gCodeInput = f.read()
		m = re.findall(reLayerHeight, gCodeInput)
		
		previous = next_ = None
		mLength = len(m)
		for index, element in enumerate(m):
			i = re.search(self.DIGITS, element)
			current = float(i.group(0))

			if index > 0:
				j = re.search(self.DIGITS, m[index - 1])
				previous = float(j.group(0))
				diff1 = round(current - previous, 3)
				if diff1 != 0.0 and diff1 != self.LAYER_HEIGHT:
					actualResult = "layer height error: index(" + str(index) + ")"
					break

			if index < (mLength -1):
				k = re.search(self.DIGITS, m[index + 1])
				next_ = float(k.group(0))
				diff2 = round(next_ - current, 3)
				if diff2 != 0.0 and diff2 != self.LAYER_HEIGHT:
					actualResult = "layer height error: index(" + str(index) + ")"
					break
			actualResult = True
		self.assertEqual(expectedResult, actualResult)


if __name__ == '__main__':
	if len(sys.argv) > 1:
		V3DPTestCases.GCODE_INPUT = sys.argv.pop()
		# print(V3DPTestCases.GCODE_INPUT)
	unittest.main()
