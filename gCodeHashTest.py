'''
    author:    Ash Searle    kss0024@auburn.edu
    created:   12/27/19
    updated:   12/27/19
    
    purpose:   gCodeHash test cases
'''

import unittest
from gCodeHash import gch
from os import remove as rm


class GCodeHashTestNominalSetup(unittest.TestCase):
	def setup():
		pass
		
	# def test100_500_hashFileMissing(self):
	# 	expectedResult = "output: ERROR: hash file misssing"
	# 	actualResult = gCodeHash.gch()
	# 	self.assertEqual(expectedResult, actualResult)

class GCodeHashTestMissingHash(unittest.TestCase):
	def setUp(self):
		fSTL =  open("sTLTemp", "w")
		fSTL.write("i")
		fSTL.close()
		# fHash = open("hashTemp", "w+")
		# fHash.write("i")
		# fHash.close()
		fV3dpConfig = open("v3dpConfigTemp", "w")
		fV3dpConfig.write("i")
		fV3dpConfig.close()
		fGCTests =  open("gCTestsTemp", "w")
		fGCTests.write("i")
		fGCTests.close()

	def tearDown(self):
		rm("sTLTemp")
		# rm("hashTemp")
		rm("v3dpConfigTemp")
		rm("gCTestsTemp")

	def test100_500_hashFileMissing(self):
		expectedResult = "output: ERROR: hash file misssing"
		actualResult = gch()
		self.assertEqual(expectedResult, actualResult)

if __name__ == '__main__':
    unittest.main()