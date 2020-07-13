'''
    author:    Ash Searle    kss0024@auburn.edu
    created:   12/27/19
    updated:   7/12/20
    
    purpose:   validate the integrity of a STL file
'''

	def test100_900_layerHeight(self):
		expectedResult = True
		actualResult = False
		
		header = ''
		skip = False
		if self.SLICER_MATTER_SLICE in self.GCODE_INPUT:
			header = self.LAYER_HEIGHT_HEADER1
		elif self.SLICER_SLIC3R in self.GCODE_INPUT:
			header = self.LAYER_HEIGHT_HEADER2
		else:
			actualResult = "Unknown slicer. Unable to determine infill density"
			skip = True

		if skip == False:
			m = re.findall(header, self.GCODE_INPUT)
			mLength = len(m)
			previous = next_ = None
			for index, element in enumerate(m):
				current = float(element)
				if index < 1:
					# skip because 1st layer height may be different
					continue
				if index < (mLength -1):
					next_ = float(m[index + 1])
					diff2 = round(next_ - current, 3)
					if diff2 != 0.0 and diff2 != self.LAYER_HEIGHT:
						actualResult = "layer height error: value(" + str(next_) + ") != value(" + str(self.LAYER_HEIGHT) + ")"
						break
				actualResult = True
		self.assertEqual(expectedResult, actualResult)

	def test200_900_infill(self):
		expectedResult = True
		actualResult = False
		
		m = re.search(self.SLICER_MATTER_SLICE, self.GCODE_INPUT)
		n = re.search(self.SLICER_SLIC3R, self.GCODE_INPUT)

		if m != None:
			o = re.search(self.INFILL_HEADER1, self.GCODE_INPUT)
			infill1 = float(o.group(1))
			if infill1 != self.INFILL_VAR:
				actualResult = "Infill Error: value(" + str(infill1) + ") != value(" + str(self.INFILL_VAR) + ")"
			else: 
				actualResult = True
		elif n != None:
			p = re.search(self.INFILL_HEADER2, self.GCODE_INPUT)
			infill2 = float(p.group(1))
			if infill2 != self.INFILL_VAR:
				actualResult = "Infill Error: value(" + str(infill2) + ") != value(" + str(self.INFILL_VAR) + ")"
			else:
				actualResult = True
		else:
			actualResult = "Unknown slicer. Unable to determine infill density"

		self.assertEqual(expectedResult, actualResult)