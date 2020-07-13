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

class CMBTestCases(unittest.TestCase):
	CMB_PATH = ""
	CMB_INPUT = ""
	SKIP_TEST = None

	CMB_MAX_X_SIZE = p.CMB_MAX_X_SIZE
	CMB_MAX_Y_SIZE = p.CMB_MAX_Y_SIZE
	CMB_MAX_Z_SIZE = p.CMB_MAX_Z_SIZE

	expectedResult = False
	actualResult = True

	@classmethod
	def setUpClass(cls):
		if ".cmb" in cls.CMB_PATH:
			cls.SKIP_TEST = False
			with open(cls.CMB_PATH, 'rb') as f:
				cls.CMB_INPUT = f.read().hex()
		else:
			cls.SKIP_TEST = True

	def setUp(self):
		if self.SKIP_TEST == True:
			self.skipTest("Not CMB file")
		self.expectedResult = False
		self.actualResult = True

	def test700_900_cmb_exceedsMaxXSize(self):
		index_ = 0
		part_max_X = ""
		temp = ""
		hexList = []
		for line in self.CMB_INPUT:
			for element in line:
				temp += element
				if (index_ + 1) % 2 == 0:
					hexList.append(temp)
					temp = ""
				index_ += 1
				if index_ == 200:
					break

		for index, value in enumerate(hexList):
			if index >= 50 and index <= 53:
				part_max_X = value + part_max_X
			elif index > 53:
				break
			index += 1

		floatMaxX_in = ieeeConverter.hex2Float(part_max_X)
		floatMaxX_mm = floatMaxX_in / 0.0393700787
		if floatMaxX_mm > self.CMB_MAX_X_SIZE:
			self.actualResult = " X value(" + str(floatMaxX_mm) + ") > X-axis bounds(" + str(self.CMB_MAX_X_SIZE) + ")"
		else:
			self.actualResult = False

		self.assertEqual(self.expectedResult, self.actualResult)

	def test700_910_cmb_exceedsMaxYSize(self):
		index_ = 0
		part_max_Y = ""
		temp = ""
		hexList = []
		for line in self.CMB_INPUT:
			for element in line:
				temp += element
				if (index_ + 1) % 2 == 0:
					hexList.append(temp)
					temp = ""
				index_ += 1
				if index_ == 200:
					break

		for index, value in enumerate(hexList):
			if index >= 54 and index <= 57:
				part_max_Y = value + part_max_Y
			elif index > 58:
				break
			index += 1

		floatMaxY_in = ieeeConverter.hex2Float(part_max_Y)
		floatMaxY_mm = floatMaxY_in / 0.0393700787
		if floatMaxY_mm > self.CMB_MAX_Y_SIZE:
			self.actualResult = " Y value(" + str(floatMaxY_mm) + ") > Y-axis bounds(" + str(self.CMB_MAX_Y_SIZE) + ")"
		else:
			self.actualResult = False

		self.assertEqual(self.expectedResult, self.actualResult)

	def test700_920_cmb_exceedsMaxZSize(self):
		index_ = 0
		part_max_Z = ""
		temp = ""
		hexList = []
		for line in self.CMB_INPUT:
			for element in line:
				temp += element
				if (index_ + 1) % 2 == 0:
					hexList.append(temp)
					temp = ""
				index_ += 1
				if index_ == 200:
					break

		for index, value in enumerate(hexList):
			if index >= 58 and index <= 61:
				part_max_Z = value + part_max_Z
			elif index > 62:
				break
			index += 1

		floatMaxZ_in = ieeeConverter.hex2Float(part_max_Z)
		floatMaxZ_mm = floatMaxZ_in / 0.0393700787
		floatMaxZ_mm = round(floatMaxZ_mm)
		if floatMaxZ_mm > self.CMB_MAX_Z_SIZE:
			self.actualResult = " Z value(" + str(floatMaxZ_mm) + ") > Z-axis bounds(" + str(self.CMB_MAX_Z_SIZE) + ")"
		else:
			self.actualResult = False

		self.assertEqual(self.expectedResult, self.actualResult)

if __name__ == '__main__':
	if len(sys.argv) > 1:
		filePath = sys.argv.pop()
		CMBTestCases.CMB_PATH = filePath
	unittest.main()

