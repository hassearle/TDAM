'''
    author:    Ash Searle    kss0024@auburn.edu
    created:   12/27/19
    updated:   1/14/20
    
    purpose:   validate the integrity of a STL file
'''

import unittest
import sys
import re
import statistics 

class V3DPTestCases(unittest.TestCase):
	GCODE_INPUT = ""
	TEMP_HEADER1 = '(?<=M104)(.*)'
	TEMP_HEADER2 = '(?<=M109)(.*)'
	TEMP_DIGITS = '(?<=S)([0-9]{3}|[0])'
	TEMP_VAR = 210
	MAX_TEMP_VAR = 220
	BED_TEMP_HEADER1 = '[M][1][4][0] [S][0-9]{2}'
	BED_TEMP_HEADER2 = '[M][1][9][0] [S][0-9]{2}'
	BED_TEMP_VAR = 25
	MAX_BED_TEMP_VAR = 65
	LAYER_HEIGHT = 0.3
	FAN_HEADER = '(?<=M106)(.*)'
	LAYER_HEIGHT_HEADER = '[G][1] [Z]([0-9+].[0-9+]|[0-9+])[\n][G][1] [E]'
	# MAX_X_SIZE = 228.0
	# MIN_X_SIZE = 2.0
	MAX_X_SIZE = 200.0
	MIN_X_SIZE = 10.0
	X_SIZE_HEADER = 'G1 X(-*\d+\.*\d*)'
	# MAX_Y_SIZE = 254.0
	# MIN_Y_SIZE = 2.0
	MAX_Y_SIZE = 200.0
	MIN_Y_SIZE = 10.0
	Y_SIZE_HEADER = 'G1 X*\d*\.*\d* *[Y](-*\d+.\d+|\d+)'
	# MAX_Z_SIZE = 254.0
	# MIN_Z_SIZE = 2.0
	MAX_Z_SIZE = 200.0
	MIN_Z_SIZE = 0.1
	Z_SIZE_HEADER = 'G1 *X*\d* *Y*\d* Z(-*\d+\.*\d+)'


	DIGITS = '([0-9+].[0-9+]|[0-9+])'

	def setUp(self):
		pass

	def test100_900_maxTemp(self):
		expectedResult = True
		actualResult = False
		with open(self.GCODE_INPUT, 'r') as f:
			gCodeInput = f.read()
		m = re.findall(self.TEMP_HEADER1, gCodeInput)
		for index, element in enumerate(m):
			i = re.search(self.TEMP_DIGITS, element)
			current = float(i.group(0))
			if current > self.MAX_TEMP_VAR:
				actualResult = "exceeded max temp: index(" + str(index) + ")"
				break
			else:
				actualResult = True
		self.assertEqual(expectedResult, actualResult)

	def test100_901_maxTemp(self):
		expectedResult = True
		actualResult = False
		with open(self.GCODE_INPUT, 'r') as f:
			gCodeInput = f.read()
		m = re.findall(self.TEMP_HEADER2, gCodeInput)
		for index, element in enumerate(m):
			i = re.search(self.TEMP_DIGITS, element)
			current = float(i.group(0))
			if current > self.MAX_TEMP_VAR:
				actualResult = "exceeded max temp: index(" + str(index) + ")"
				break
			else:
				actualResult = True
		self.assertEqual(expectedResult, actualResult)

	def test100_110_temp(self):
		expectedResult = True
		actualResult = False
		with open(self.GCODE_INPUT, 'r') as f:
			gCodeInput = f.read()
		m = re.findall(self.TEMP_HEADER1, gCodeInput)
		for index, element in enumerate(m):
			i = re.search(self.TEMP_DIGITS, element)
			current = float(i.group(0))
			if current != 0 and current != self.TEMP_VAR:
				actualResult = "exceeded max temp: index(" + str(index) + ")"
				break
			else:
				actualResult = True
		self.assertEqual(expectedResult, actualResult)

	def test100_111_temp(self):
		expectedResult = True
		actualResult = False
		with open(self.GCODE_INPUT, 'r') as f:
			gCodeInput = f.read()
		m = re.findall(self.TEMP_HEADER2, gCodeInput)
		for index, element in enumerate(m):
			i = re.search(self.TEMP_DIGITS, element)
			current = float(i.group(0))
			if current != 0 and current != self.TEMP_VAR:
				actualResult = "exceeded max temp: index(" + str(index) + ")"
				break
			else:
				actualResult = True
		self.assertEqual(expectedResult, actualResult)

	def test100_120_bedTemp(self):
		expectedResult = True
		actualResult = False
		with open(self.GCODE_INPUT, 'r') as f:
			gCodeInput = f.read()
		m = re.findall(self.BED_TEMP_HEADER1, gCodeInput)
		for index, element in enumerate(m):
			i = re.search('(?<=S)(.*)', element)
			current = float(i.group(0))
			if current != 0 and current != self.BED_TEMP_VAR:
				actualResult = "incorrect bed temp: index(" + str(index) + ")"
				break
			else:
				actualResult = True
		self.assertEqual(expectedResult, actualResult)

	def test100_121_bedTemp(self):
		expectedResult = True
		actualResult = False
		with open(self.GCODE_INPUT, 'r') as f:
			gCodeInput = f.read()
		m = re.findall(self.BED_TEMP_HEADER2, gCodeInput)
		for index, element in enumerate(m):
			i = re.search('(?<=S)(.*)', element)
			current = float(i.group(0))
			if current != 0 and current != self.BED_TEMP_VAR:
				actualResult = "incorrect bed temp: index(" + str(index) + ")"
				break
			else:
				actualResult = True
		self.assertEqual(expectedResult, actualResult)

	def test100_930_bedTempMax(self):
		expectedResult = True
		actualResult = False
		with open(self.GCODE_INPUT, 'r') as f:
			gCodeInput = f.read()
		m = re.findall(self.BED_TEMP_HEADER1, gCodeInput)
		for index, element in enumerate(m):
			i = re.search('(?<=S)(.*)', element)
			current = float(i.group(0))
			if current > self.MAX_BED_TEMP_VAR:
				actualResult = "exceded max bed temp: index(" + str(index) + ")"
				break
			else:
				actualResult = True
		self.assertEqual(expectedResult, actualResult)

	def test100_931_bedTempMax(self):
		expectedResult = True
		actualResult = False
		with open(self.GCODE_INPUT, 'r') as f:
			gCodeInput = f.read()
		m = re.findall(self.BED_TEMP_HEADER2, gCodeInput)
		for index, element in enumerate(m):
			i = re.search('(?<=S)(.*)', element)
			current = float(i.group(0))
			if current > self.MAX_BED_TEMP_VAR:
				actualResult = "exceded max bed temp: index(" + str(index) + ")"
				break
			else:
				actualResult = True
		self.assertEqual(expectedResult, actualResult)

	def test200_900_fanNeverEngaged(self):
		expectedResult = True
		actualResult = False
		with open(self.GCODE_INPUT, 'r') as f:
			gCodeInput = f.read()

		m = re.search(self.FAN_HEADER, gCodeInput)
		actualResult = True if m != None else "fan never engaged"
		self.assertEqual(expectedResult, actualResult)

	def test300_100_layerHeight(self):
		expectedResult = True
		actualResult = False

		with open(self.GCODE_INPUT, 'r') as f:
			gCodeInput = f.read()
		m = re.findall(self.LAYER_HEIGHT_HEADER, gCodeInput)
		
		previous = next_ = None
		mLength = len(m)
		for index, element in enumerate(m):
			i = re.search(self.DIGITS, element)
			current = float(i.group(0))

			if index > 0:
				j = re.search(self.DIGITS, m[index - 1])
				previous = float(j.group(0))
				diff1 = round(current - previous, 3)
				if diff1 != 0.0 and diff1 != self.LAYER_HEIGHT:
					actualResult = "layer height error: index(" + str(index) + ")"
					break

			if index < (mLength -1):
				k = re.search(self.DIGITS, m[index + 1])
				next_ = float(k.group(0))
				diff2 = round(next_ - current, 3)
				if diff2 != 0.0 and diff2 != self.LAYER_HEIGHT:
					actualResult = "layer height error: index(" + str(index) + ")"
					break
			actualResult = True
		self.assertEqual(expectedResult, actualResult)

	def test400_100_feedRate(self):
		pass
		#112.5

	# swap 0 and 0.0
	INFILL = 	'[G][1] [X]([0-9]+|[0-9]+.[0-9]+) ([E][0-9]+.[0-9]+ [F][0-9]+|[E][0-9]+.[0-9]+)'

	# '[G][1] [X]([0-9]+|[0-9]+.[0-9]+) [Y]([0-9]+|[0-9]+.[0-9]+) ([E][0-9]+.[0-9]+ [F][0-9]+|[E][0-9]+.[0-9]+)'

	def test500_100_infill(self):
		pass
		# expectedResult = True
		# actualResult = False

		# # with open(self.GCODE_INPUT, 'r') as f:
		# 	# 	gCodeInput = f.read()
		# 	# m = re.findall(self.INFILL, gCodeInput)
		# 	# n = []
		# 	# for element in m:
		# 	# 	n.append(float(element[0]))
		# 	# xxDiff = n[6] - n[5]
		# 	# print(xxDiff)
		# 	# n.sort()
		# 	# highestX = n[-1]
		# 	# lowestX = n[0]
		# 	# print(highestX)
		# 	# print(lowestX)
		# 	# xDiff = highestX - lowestX
		# 	# print(xDiff)
		# 	# xxxDiff = xDiff / xxDiff
		# 	# print(xxxDiff)
		# infill = []
		# tempInfillList = ""
		# skipHeader = 'LAYER_HEIGHT'
		# infillHeader = 'TYPE:FILL'
		# stopHeader = '; '
		# skip = False
		# cont = False
		# with open(self.GCODE_INPUT, 'r') as f:
		# 	for index, line in enumerate(f):
		# 		if skipHeader in line:
		# 			skip = True
		# 			f.readline()
		# 			# print("two " + str(index) + " " + f.readline())
		# 		elif infillHeader in line:
		# 			cont = True
		# 			# print("three " + str(index) + " " + f.readline())
		# 			while cont == True:
		# 				nextLine = f.readline()
		# 				nextLine = nextLine

		# 				if stopHeader in nextLine:
		# 					# print("four " + str(index) + " " + f.readline())
		# 					cont = False
		# 					infill.append(tempInfillList)
		# 					tempInfillList = ""
		# 					break
		# 				else:
		# 					tempInfillList += nextLine
		# 					# print("five " + str(index) + " " + nextLine)

		# # for index, element in enumerate(infill):
		# 	# print(index)
		# 	# print("[ " + element + "]")

		# avgInfill = []
		# for element in infill:
		# # 	for element_ in list_:
		# 	m = re.findall(self.INFILL, element)
		# 	# print("[ " + str(m) + "]")
		# 	n = []
		# 	index_ = -1
		# 	for index, item in enumerate(m):
		# 		index_ = index
		# 		n.append(float(item[0]))
		# 	if len(n) == 0: continue
		# 	if n[0] > n[3]: spaceBetweenX_1 = n[0] - n[3]
		# 	else: spaceBetweenX_1 = n[3] - n[0]
			
		# 	if n[-1] > n[-4]: spaceBetweenX_2 = n[-1] - n[-4]
		# 	else: spaceBetweenX_2 = n[-4] - n[-1]

		# 	if spaceBetweenX_1 > spaceBetweenX_2:
		# 		spaceBetweenX = spaceBetweenX_1
		# 	else:
		# 		spaceBetweenX = spaceBetweenX_2


		# 	print("space b/w x: " + str(spaceBetweenX))
			
		# 	n.sort()
		# 	highestX = n[-1]
		# 	lowestX = n[0]
		# 	print("highest X: " + str(highestX))
		# 	print("lowest X: " + str(lowestX))

		# 	totalXSpace = highestX - lowestX
		# 	# totalXSpace = index * spaceBetweenX
		# 	print("total X Space: " + str(totalXSpace))

		# 	# percentNotInfill = totalXSpace / spaceBetweenX
		# 	# percentInfill = totalXSpace / percentNotInfill
		# 	percentInfill = totalXSpace / spaceBetweenX
		# 	print("percent infill: " + str(percentInfill))
		# 	if percentInfill <= 100:
		# 		avgInfill.append(percentInfill)
			
		# 	print(index_)
		# 	# print(element)

		# # print(statistics.mean(avgInfill))
		# print("\n")


# if wrong type:fill continue and skip
# if type:fill: save to list
# if ; in line stop saving to list

	def test600_900_exceedsMaxXSize(self):
		expectedResult = False
		actualResult = True
		with open(self.GCODE_INPUT, 'r') as f:
			gCodeInput = f.read()

		m = re.findall(self.X_SIZE_HEADER, gCodeInput)
		elementX = None
		for index, element in enumerate(m):
			elementX = element
			if float(element) > self.MAX_X_SIZE:
				actualResult = " X value(" + str(elementX) + ") over mas X-axis bounds(" + str(self.MAX_X_SIZE) + ")"
				break
			elif index == len(m)-1:
				actualResult = False

		self.assertEqual(expectedResult, actualResult)

	def test600_910_exceedsMinXSize(self):
		expectedResult = False
		actualResult = True
		with open(self.GCODE_INPUT, 'r') as f:
			gCodeInput = f.read()

		m = re.findall(self.X_SIZE_HEADER, gCodeInput)
		elementX = None
		for index, element in enumerate(m):
			elementX = element
			if float(element) < self.MIN_X_SIZE:
				if index == 0: continue
				actualResult = " X value(" + str(elementX) + ") under min X-axis bounds(" + str(self.MIN_X_SIZE) + ")"
				break
			elif index == len(m)-1:
				actualResult = False

		self.assertEqual(expectedResult, actualResult)

	def test600_920_exceedsMaxYSize(self):
		expectedResult = False
		actualResult = True
		with open(self.GCODE_INPUT, 'r') as f:
			gCodeInput = f.read()
		m = re.findall(self.Y_SIZE_HEADER, gCodeInput)
		elementY = None
		for index, element in enumerate(m):
			elementY = element
			if float(element) > self.MAX_Y_SIZE:
				actualResult = " Y value(" + str(elementY) + ") over mas Y-axis bounds(" + str(self.MAX_Y_SIZE) + ")"
				break
			elif index == len(m)-1:
				actualResult = False

		self.assertEqual(expectedResult, actualResult)

	def test600_930_exceedsMinYSize(self):
		expectedResult = False
		actualResult = True
		with open(self.GCODE_INPUT, 'r') as f:
			gCodeInput = f.read()

		m = re.findall(self.Y_SIZE_HEADER, gCodeInput)
		elementY = None
		for index, element in enumerate(m):
			elementY = element
			if float(element) < self.MIN_Y_SIZE:
				if index == 0: continue
				actualResult = " Y value(" + str(elementY) + ") under min Y-axis bounds(" + str(self.MIN_Y_SIZE) + ")"
				break
			elif index == len(m)-1:
				actualResult = False

		self.assertEqual(expectedResult, actualResult)

	def test600_940_exceedsMaxZSize(self):
		expectedResult = False
		actualResult = True
		with open(self.GCODE_INPUT, 'r') as f:
			gCodeInput = f.read()
		m = re.findall(self.Z_SIZE_HEADER, gCodeInput)
		print(m)
		elementZ = None
		for index, element in enumerate(m):
			elementZ = element
			print(element)
			if float(element) > self.MAX_Z_SIZE:
				actualResult = "Z value(" + str(elementZ) + ") over mas Z-axis bounds(" + str(self.MAX_Z_SIZE) + ")"
				break
			elif index == len(m)-1:
				actualResult = False

		self.assertEqual(expectedResult, actualResult)

	def test600_950_exceedsMinZSize(self):
		expectedResult = False
		actualResult = True
		with open(self.GCODE_INPUT, 'r') as f:
			gCodeInput = f.read()

		m = re.findall(self.Z_SIZE_HEADER, gCodeInput)
		elementZ = None
		for index, element in enumerate(m):
			elementZ = element
			if float(element) < self.MIN_Z_SIZE:
				if index == 0: continue
				actualResult = "Z value(" + str(elementZ) + ") under min Z-axis bounds(" + str(self.MIN_Z_SIZE) + ")"
				break
			elif index == len(m)-1:
				actualResult = False

		self.assertEqual(expectedResult, actualResult)

if __name__ == '__main__':
	if len(sys.argv) > 1:
		V3DPTestCases.GCODE_INPUT = sys.argv.pop()
		# print(V3DPTestCases.GCODE_INPUT)
	unittest.main()

