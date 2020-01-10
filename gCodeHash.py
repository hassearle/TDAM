'''
    author:    Ash Searle    kss0024@auburn.edu
    created:   12/27/19
    updated:   1/9/20
    
    purpose:   validate the integrity of a STL file
'''

import subprocess

ERROR_HEADER = "ERROR: "
STATUS_KEY = "status"
STATUS_POSITIVE = "ok"

ERROR01 = "hash file missing"
ERROR02 = "STL file missing"
ERROR03 = "V3DPConfig file missing"
ERROR04 = "GCTests file missing"
ERROR05 = "sliced STL GCode failed GCTests"
ERROR06 = "slicer could not slice stl file"

PYTHON_EXE = "python3"
PERL_EXE = "perl"
SLIC3R_EXE = "/home/has/Slic3r/slic3r.pl"

# FILE_NAME = "stl"
FILE_NAME = "testSTL"
STL_EXTENSION = ".stl"
GCODE_EXTENSION = ".gcode"

SLIC3R_PATH = "/home/has/Documents/Thesis/code/stlFiles/"
GCTESTS_PATH = "config/gCTests.py"
HASH_PATH = 'inputFiles/hash'
STL_PATH = 'inputFiles/stl.stl'
V3DP_CONFIG_PATH = 'config/v3dpConfig'
GCODE_TESTS_PATH = 'config/gCTests.py'

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



def gch():
	# if flag != 0:
	result = validateParms()
	rtn = {STATUS_KEY:result.objStatus,
		"stl":result.objStl,
		"hash":result.objHash, 
		"v3dpConfig":result.objV3dpConfig,
		"gCTests":result.objGCTests}
	return rtn
	# else:
	# 	return result

def validateParms():
	try:
		try:
			hashInput = ""
			with open(HASH_PATH, 'r') as f:
				hashInput = f.read()
		except:
			raise ValueError(ERROR01)
		try:
			stlInput = ""
			with open(STL_PATH, 'rb') as f:
				stlInput = f.read()
		except:
			raise ValueError(ERROR02)
		try:
			v3dpConfigInput = ""
			with open(V3DP_CONFIG_PATH, 'r') as f:
				v3dpConfigInput = f.read()
		except:
			raise ValueError(ERROR03)
		try:
			gCTestsInput = ""
			with open(GCODE_TESTS_PATH, 'r') as f:
				gCTestsInput = f.read()
		except:
			raise ValueError(ERROR04)
	except Exception as e:
		result = ERROR_HEADER + e.args[0]
		return result
	else:
		status = STATUS_POSITIVE

	result = V3dpos(status,STL_PATH,HASH_PATH,V3DP_CONFIG_PATH,GCODE_TESTS_PATH)
	# result = {"status":rtn.objStatus,
	# 	"stl":rtn.objStl,
	# 	"hash":rtn.objHash, 
	# 	"v3dpConfig":rtn.objV3dpConfig,
	# 	"gCTests":rtn.objGCTests}

	return result

def validateGCode(v3dpos):
	testsOutput = subprocess.run([PYTHON_EXE, GCTESTS_PATH], universal_newlines=True, 
		stdout=subprocess.PIPE, stderr=subprocess.PIPE)#, v3dpos.objGCode])
	if "FAILED" in testsOutput.stderr:
		status = ERROR_HEADER + ERROR05
		v3dpos.objStatus = status
		result = v3dpos
		return result
	else:
		result = v3dpos
		return result

def sliceSTLToGCode(stl_):
	result = {STATUS_KEY: "n/a", 'gcode': "n/a"}
	test = [PERL_EXE, SLIC3R_EXE, SLIC3R_PATH + FILE_NAME + STL_EXTENSION]
	print(test)
	slic3r = subprocess.run(test, universal_newlines=True, 
		stdout=subprocess.PIPE, stderr=subprocess.PIPE)#, v3dpos.objGCode])
	if "Done." not in slic3r.stdout:
		status = ERROR_HEADER + ERROR06
		result[STATUS_KEY] = status
		return result
	else:
		result[STATUS_KEY] = STATUS_POSITIVE
		result['gcode'] = stl_ + GCODE_EXTENSION
		return result

def dev():
	ash = validateParms()
	has = sliceSTLToGCode(ash.objStl)
	print(has)