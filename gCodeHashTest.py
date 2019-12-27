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
		fSTL =  open("stl", "w")
		fSTL.write("i")
		fSTL.close()
		# fHash = open("hash", "w")
		# fHash.write("i")
		# fHash.close()
		fV3dpConfig = open("v3dpConfig", "w")
		fV3dpConfig.write("i")
		fV3dpConfig.close()
		fGCTests =  open("gCTests", "w")
		fGCTests.write("i")
		fGCTests.close()

	def tearDown(self):
		rm("stl")
		# rm("hashTemp")
		rm("v3dpConfig")
		rm("gCTests")

	def test100_500_hashFileMissing(self):
		expectedResult = "output: ERROR: hash file missing"
		actualResult = gch()
		self.assertEqual(expectedResult, actualResult)

if __name__ == '__main__':
    unittest.main()