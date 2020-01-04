'''
    author:    Ash Searle    kss0024@auburn.edu
    created:   1/3/20
    updated:   1/3/20
    
    purpose:   gCodeHash unit tests
'''

import unittest
from os import remove as rm
import gCodeHash
from gCodeHash import V3dpos
from hashlib import sha512

#100: V3dpos
#200: GCodeTests
#300: validateParams

# 1##:	happy path test case
# 1#1:	similarly grouped test case
# 2##:	refactor (blue light) test case
# 5##:	dev (temp) test case
# 9##:	sad path test case

class GCodeHashTestNominalSetup(unittest.TestCase):

	maxDiff = None

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
		fGCTests =  open("gCTests", "w")
		fGCTests.write("i")
		fGCTests.close()

	def tearDown(self):
		rm("stl")
		rm("hash")
		rm("v3DPConfig")
		rm("gCTests")

		# def test100_540_hashFileCorrupted(self):
		# 	expectedResult = "output: ERROR: hash file corrupted or cant be opened"
		# 	actualResult = gCodeHash.gch()
		# 	self.assertEqual(expectedResult, actualResult)

	@unittest.SkipTest
	def test100_500_NominalSTL(self):
		expectedResult = ""
		with open('stlFiles/testSTL.stl', 'r') as f:
			expectedResult += f.read()

		result = gCodeHash.gch(5)
		actualResult = result["stl"]
		self.assertEqual(expectedResult, actualResult)

	@unittest.SkipTest
	def test100_510_NominalHash(self):
		expectedResult = "e7c1d1d8c8d8f377889b8ecad6a5f5f0e4e98362980a8905b708f10ae84f6a91d607377713e4ed0d7bcfee4dc3a1242c7a3e4dc81c9f3bc1c27a548dfd7b6b12  stl.stl"
		result = gCodeHash.gch(5)
		actualResult = result["hash"]
		self.assertEqual(expectedResult, actualResult)

	@unittest.SkipTest
	def test100_520_NominalV3DPConfig(self):
		expectedResult = ""
		with open('stlFiles/testV3dpConfig', 'r') as f:
			expectedResult += f.read()

		result = gCodeHash.gch(5)
		actualResult = result["v3dpConfig"]
		self.assertEqual(expectedResult, actualResult)

	@unittest.SkipTest
	def test100_530_NominalGCTests(self):
		expectedResult = ""
		with open('stlFiles/testGCTests.py', 'r') as f:
			expectedResult += f.read()

		result = gCodeHash.gch(5)
		actualResult = result["gCTests"]
		self.assertEqual(expectedResult, actualResult)

	# def test200_931_FailsGCTests(self):
	# 	expectedResult = "output: ERROR: sliced STL GCode failed GCTests"
	# 	gcode = 
	# 	actualResult = gCTests()

	def test300_200_validateParms(self):
		stl_ = ""
		with open('stlFiles/testSTL.stl', 'r') as f:
			stl_ += f.read()

		hash_ = "e7c1d1d8c8d8f377889b8ecad6a5f5f0e4e98362980a8905b708f10ae84f6a91d607377713e4ed0d7bcfee4dc3a1242c7a3e4dc81c9f3bc1c27a548dfd7b6b12  stl.stl"
		
		v3dpConfig_ = ""
		with open('stlFiles/testV3dpConfig', 'r') as f:
			v3dpConfig_ += f.read()

		gcTests_ = ""
		with open('stlFiles/testGCTests.py', 'r') as f:
			gcTests_ += f.read()

		expectedResult = {"status":'ok',
			"stl":stl_,
			"hash":hash_, 
			"v3dpConfig":v3dpConfig_,
			"gCTests":gcTests_}
		actualResult = gCodeHash.validateParms(stl_,hash_,v3dpConfig_,gcTests_)
		self.assertEqual(expectedResult, actualResult)


#class method to slice gcode

		# h = sha512()
		# h.update(stl)
		# hash_ = h.hexdigest()
		# print(hash_)

		# fHash = open("hash", "r")
		# fV3dpConfig = open("v3DPConfig", "r")
		# fGCTests =  open("gCTests", "r")

if __name__ == '__main__':
    unittest.main()