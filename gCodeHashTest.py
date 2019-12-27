'''
    author:    Ash Searle    kss0024@auburn.edu
    created:   12/27/19
    updated:   12/27/19
    
    purpose:   gCodeHash test cases
'''

import unittest
import gGodeHash
from os import remove as rm


class GCodeHashTestNominalSetup(unittest.TestCase):
	def setup():
		pass
		
	# def test100_500_hashFileMissing(self):
	# 	expectedResult = "output: ERROR: hash file misssing"
	# 	actualResult = gCodeHash.gch()
	# 	self.assertEqual(expectedResult, actualResult)

class GCodeHashTestMissingHash(unittest.TestCase):
	def setup(self):
		fSTL =  open("sTLTemp", "w+")
		# fHash = open("hashTemp", "w+")
		fV3dpConfig = open("v3dpConfigTemp", "w+")
		fGCTests =  open("gCTestsTemp", "w+")

	def tearDown(self):
		rm("sTLTemp")
		# rm("hashTemp")
		rm("v3dpConfigTemp")
		rm("gCTestsTemp")

	def test100_500_hashFileMissing(self):
		expectedResult = "output: ERROR: hash file misssing"
		actualResult = gCodeHash.gch()
		self.assertEqual(expectedResult, actualResult)

if __name__ == '__main__':
    unittest.main()