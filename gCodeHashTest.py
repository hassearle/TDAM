'''
    author:    Ash Searle    kss0024@auburn.edu
    created:   12/27/19
    updated:   12/27/19
    
    purpose:   gCodeHash test cases
'''

import unittest
import gCodeHash

class GCodeHashTest(unittest.TestCase):
	def setup():
		pass
		
	def test100_900_hashFileMissing(self):
		expectedResult = "hello world"
		actualResult = gCodeHash.gch()
		self.assertEqual(expectedResult, actualResult)

if __name__ == '__main__':
    unittest.main()