'''
    author:    Ash Searle    kss0024@auburn.edu
    created:   12/27/19
    updated:   1/9/20
    
    purpose:   validate the integrity of a STL file
'''

import subprocess

#temp
from pprint import pprint
#

ERROR_HEADER = "ERROR: "
STATUS_KEY = "status"
GCODE_KEY = "gcode"
STATUS_POSITIVE = "ok"

ERROR01 = "hash file missing"
ERROR02 = "STL file missing"
ERROR03 = "V3DPConfig file missing"
ERROR04 = "GCTests file missing"
ERROR05 = "sliced STL GCode failed GCTests"
ERROR06 = "slicer could not slice stl file"
ERROR07 = "input not a GCode file"

PYTHON_EXE = "python3"
PERL_EXE = "perl"
SLIC3R_EXE = "/home/has/Slic3r/slic3r.pl"

# FILE_NAME = "stl"
FILE_NAME = "testSTL"
STL_EXTENSION = ".stl"
GCODE_EXTENSION = ".gcode"

SLIC3R_PATH = "/home/has/Documents/Thesis/code/stlFiles/"
GCTESTS_PATH = "/home/has/Documents/Thesis/code/config/gCTests.py"
HASH_PATH = '/home/has/Documents/Thesis/code/inputFiles/hash'
STL_PATH = '/home/has/Documents/Thesis/code/inputFiles/stl.stl'
V3DP_CONFIG_PATH = '/home/has/Documents/Thesis/code/config/v3dpConfig'
GCODE_TESTS_PATH = '/home/has/Documents/Thesis/code/config/gCTests.py'

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

def validateGCode(v3dpos_):
	result = v3dpos_
	inputSTL = result.objStl
	
	# getGCode = sliceSTLToGCode(inputSTL)
	# gcodeStatus = getGCode[STATUS_KEY]
	# gCode = getGCode[GCODE_KEY]
	# gCodeTestResults = gCodeTests(gCode)
	
	# if gcodeStatus != STATUS_POSITIVE:
	# 	result.objStatus = gcodeStatus
	# elif gCodeTestResults != STATUS_POSITIVE:
	# 	result.objStatus = gCodeTestResults
	# else:
	# 	result.objStatus = gcodeStatus
	# 	result.objGCode = gCode

	try:
		getGCode = sliceSTLToGCode(inputSTL)
		gcodeStatus = getGCode[STATUS_KEY]
		gCode = getGCode[GCODE_KEY]
		gCodeTestResults = gCodeTests(gCode)
	except Exception as e:
		result.objStatus = ERROR_HEADER + e.args[0]
	else:
		result.objStatus = gcodeStatus
		result.objGCode = gCode

	return result

def sliceSTLToGCode(stl_):
	result = {STATUS_KEY: "n/a", GCODE_KEY: "n/a"}
	test = [PERL_EXE, SLIC3R_EXE, stl_]
	slic3r = subprocess.run(test, universal_newlines=True, 
		stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if "Done." not in slic3r.stdout:
		# status = ERROR_HEADER + ERROR06
		# result[STATUS_KEY] = status
		# return result
		raise ValueError(ERROR06)
	else:
		result[STATUS_KEY] = STATUS_POSITIVE
		result[GCODE_KEY] = stl_[:-4] + GCODE_EXTENSION
		return result

def gCodeTests(objGCode_):
	status = "n/a"

	try:
		gCTestsInput = ""
		with open(objGCode_, 'rb') as f:
			gCTestsInput = f.read()
	except:
		raise ValueError(ERROR04)

	if not objGCode_.lower().endswith(('.gcode')):
		raise ValueError(ERROR07)

	testsOutput = subprocess.run([PYTHON_EXE, GCTESTS_PATH, gCTestsInput],
		universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	
	# print(objGCode_)
	# print(testsOutput.stdout)

	if "OK" not in testsOutput.stderr:
		# error = ERROR_HEADER + ERROR05
		# status = error
		# return status
		print("stdout:\n" + testsOutput.stdout)
		print("stderr:\n" + testsOutput.stderr)		
		raise ValueError(testsOutput.stdout + ERROR05)
	else:
		status = STATUS_POSITIVE #testsOutput.stdout
		return status

def dev():
	ash = validateParms()
	pprint(vars(ash))
	badGCode = '/home/has/Documents/Thesis/code/stl.stl'
	ash.objGCode = badGCode
	has = gCodeTests(ash.objGCode)
	pprint(vars(has))

	# badGCode = ""
	gcode = has.objGCode
	# result = gCodeTests(gcode)
	expectedResult = ERROR_HEADER + ERROR05
	# actualResult = result[STATUS_KEY]
	print("expected result:\n" + expectedResult)
	# print("actual result:\n" + actualResult)