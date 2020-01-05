'''
    author:    Ash Searle    kss0024@auburn.edu
    created:   12/27/19
    updated:   1/4/20
    
    purpose:   validate the integrity of a STL file
'''

import subprocess

ERROR_HEADER = "ERROR: "
STATUS_HEADER = "status: "
STATUS_POSITIVE = "ok"
ERROR01 = "hash file missing"
ERROR02 = "STL file missing"
ERROR03 = "V3DPConfig file missing"
ERROR04 = "GCTests file missing"
ERROR05 = "sliced STL GCode failed GCTests"
GCTESTS_PATH = "config/gCTests.py"

class V3dpos:
	objStatus = "n/a"
	objStl = "n/a"
	objHash = "n/a"
	objV3dpConfig = "n/a"
	objGCTests = "n/a"
	objGCode = "n/a"
	def __init__ (self, status_, stl_, hash_, v3dpConfig_, gCTests_):
		self.objStatus = status_
		self.objStl = stl_
		self.objHash = hash_
		self.objV3dpConfig = v3dpConfig_
		self.objGCTests = gCTests_

	@classmethod
	def setGCode(cls, gcode_):
		cls.objGCode = gcode_

	@classmethod
	def setStatus(cls, status_):
		cls.objStatus = status_



def gch(flag):
	if flag != 0:
		rtn = {"output":result,
			"stl":v3dpos.objStl,
			"hash":v3dpos.objHash, 
			"v3dpConfig":v3dpos.objV3dpConfig,
			"gCTests":v3dpos.objGCTests}
		return rtn
	else:
		return result

def validateParms():
	try:
		try:
			hashInput = ""
			with open('inputFiles/hash', 'r') as f:
				hashInput = f.read()
		except:
			raise ValueError(ERROR01)
		try:
			stlInput = ""
			with open('inputFiles/stl.stl', 'rb') as f:
				stlInput = f.read()
		except:
			raise ValueError(ERROR02)
		try:
			v3dpConfigInput = ""
			with open('config/v3dpConfig', 'r') as f:
				v3dpConfigInput = f.read()
		except:
			raise ValueError(ERROR03)
		try:
			gCTestsInput = ""
			with open('config/gCTests.py', 'r') as f:
				gCTestsInput = f.read()
		except:
			raise ValueError(ERROR04)
	except Exception as e:
		result = ERROR_HEADER + e.args[0]
		return result
	else:
		status = STATUS_POSITIVE

	result = V3dpos(status,stlInput,hashInput,v3dpConfigInput,gCTestsInput)
	# result = {"status":rtn.objStatus,
	# 	"stl":rtn.objStl,
	# 	"hash":rtn.objHash, 
	# 	"v3dpConfig":rtn.objV3dpConfig,
	# 	"gCTests":rtn.objGCTests}

	return result

def validateGCode(v3dpos):
	try:
		try:
			subprocess.run(["python " + GCTESTS_PATH, v3dpos.objGCode], check=True)
		except:
			raise ValueError(ERROR05)
	except Exception as e:
		status = ERROR_HEADER + e.args[0]
		result = v3dpos.setStatus(status)
		return result
	else:
		result = v3dpos
		return result
# stlInput = ""
# with open('inputFiles/stl.stl', 'r') as f:
# 	stlInput += f.read()
# ash = V3dpos(stlInput)
# print(ash.stl)