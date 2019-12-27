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
		fV3dpConfig = open("v3DPConfig", "w")
		fV3dpConfig.write("i")
		fV3dpConfig.close()
		fGCTests =  open("gCTests", "w")
		fGCTests.write("i")
		fGCTests.close()

	def tearDown(self):
		rm("stl")
		# rm("hash")
		rm("v3DPConfig")
		rm("gCTests")

	def test100_500_hashFileMissing(self):
		expectedResult = "output: ERROR: hash file missing"
		actualResult = gch()
		self.assertEqual(expectedResult, actualResult)


class GCodeHashTestMissingSTL(unittest.TestCase):
	def setUp(self):
		# fSTL =  open("stl", "w")
		# fSTL.write("i")
		# fSTL.close()
		fHash = open("hash", "w")
		fHash.write("i")
		fHash.close()
		fV3dpConfig = open("v3DPConfig", "w")
		fV3dpConfig.write("i")
		fV3dpConfig.close()
		fGCTests =  open("gCTests", "w")
		fGCTests.write("i")
		fGCTests.close()

	def tearDown(self):
		# rm("stl")
		rm("hash")
		rm("v3DPConfig")
		rm("gCTests")

	def test100_510_STLFileMissing(self):
		expectedResult = "output: ERROR: STL file missing"
		actualResult = gch()
		self.assertEqual(expectedResult, actualResult)


class GCodeHashTestMissingV3DPConfig(unittest.TestCase):
	def setUp(self):
		fSTL =  open("stl", "w")
		fSTL.write("i")
		fSTL.close()
		fHash = open("hash", "w")
		fHash.write("i")
		fHash.close()
		# fV3dpConfig = open("v3DPConfig", "w")
		# fV3dpConfig.write("i")
		# fV3dpConfig.close()
		fGCTests =  open("gCTests", "w")
		fGCTests.write("i")
		fGCTests.close()

	def tearDown(self):
		rm("stl")
		rm("hash")
		# rm("v3dpConfig")
		rm("gCTests")

	def test100_520_V3DPConfigFileMissing(self):
		expectedResult = "output: ERROR: V3DPConfig file missing"
		actualResult = gch()
		self.assertEqual(expectedResult, actualResult)


class GCodeHashTestMissingGCTests(unittest.TestCase):
	def setUp(self):
		fSTL =  open("stl", "w")
		fSTL.write("i")
		fSTL.close()
		fHash = open("hash", "w")
		fHash.write("i")
		fHash.close()
		fV3dpConfig = open("v3DPConfig", "w")
		fV3dpConfig.write("i")
		fV3dpConfig.close()
		# fGCTests =  open("gCTests", "w")
		# fGCTests.write("i")
		# fGCTests.close()

	def tearDown(self):
		rm("stl")
		rm("hash")
		rm("v3DPConfig")
		# rm("gCTests")

	def test100_530_GCTestsFileMissing(self):
		expectedResult = "output: ERROR: GCTests file missing"
		actualResult = gch()
		self.assertEqual(expectedResult, actualResult)

if __name__ == '__main__':
    unittest.main()