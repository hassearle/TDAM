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

class GCodeHashTestNominalSetup(unittest.TestCase):
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

	def test100_100_NominalSTL(self):
		expectedResult = ""
		with open('stlFiles/testSTL.stl', 'r') as f:
			expectedResult += f.read()

		result = gCodeHash.gch(5)
		actualResult = result["stl"]
		self.assertEqual(expectedResult, actualResult)


		# h = sha512()
		# h.update(stl)
		# hash_ = h.hexdigest()
		# print(hash_)

		# fHash = open("hash", "r")
		# fV3dpConfig = open("v3DPConfig", "r")
		# fGCTests =  open("gCTests", "r")

if __name__ == '__main__':
    unittest.main()