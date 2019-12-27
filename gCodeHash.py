'''
    author:    Ash Searle    kss0024@auburn.edu
    created:   12/27/19
    updated:   12/27/19
    
    purpose:   validate the integrity of a STL file
'''

ERROR_HEADER = "ERROR: "
OUTPUT_HEADER = "output: "
ERROR01 = "hash file missing"
ERROR02 = "STL file missing"
ERROR03 = "V3DPConfig file missing"

def gch():
	try:
		try:
			fHash = open("hash", "r")
		except:
			raise ValueError(ERROR01)
		try:
			fSTL = open("stl", "r")
		except:
			raise ValueError(ERROR02)
		try:
			fV3DPConfig = open("v3DPConfig", "r")
		except:
			raise ValueError(ERROR03)
	except Exception as e:
		result = OUTPUT_HEADER + ERROR_HEADER + e.args[0]



	return result
