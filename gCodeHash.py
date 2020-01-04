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
ERROR04 = "GCTests file missing"

class V3dpos:
	stl = "n/a"
	objHash = "n/a"
	objV3dpConfig = "n/a"
	def __init__ (self, stl_, hash_, v3dpConfig_):
		self.stl = stl_
		self.objHash = hash_
		self.objV3dpConfig = v3dpConfig_

def gch(flag):
	result = 1

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
		try:
			fGCTests = open("gcTests", "r")
		except:
			raise ValueError(ERROR04)
	except Exception as e:
		result = OUTPUT_HEADER + ERROR_HEADER + e.args[0]

	stlInput = ""
	with open('inputFiles/stl.stl', 'r') as f:
		stlInput += f.read()

	hashInput = ""
	with open('inputFiles/hash', 'r') as f:
		hashInput += f.read()

	v3dpConfigInput = ""
	with open('config/v3dpConfig', 'r') as f:
		v3dpConfigInput += f.read()

	v3dpos = V3dpos(stlInput,hashInput,v3dpConfigInput)

	if flag != 0:
		rtn = {"status":result, "stl":v3dpos.stl, "hash":v3dpos.objHash, 
			"v3dpConfig":v3dpos.objV3dpConfig}
		return rtn
	else:
		return result

# stlInput = ""
# with open('inputFiles/stl.stl', 'r') as f:
# 	stlInput += f.read()
# ash = V3dpos(stlInput)
# print(ash.stl)