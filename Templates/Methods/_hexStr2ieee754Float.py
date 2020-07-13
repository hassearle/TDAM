'''
	author:		Ash Searle	kss0024@auburn.edu
	created:	7/3/20
	updated:	7/3/20
	
	purpose:	convert hex string to IEEE 754 float
'''

def hex2Float(hexValues):
	result = 0.0
	binary = "{0:08b}".format(int(hexValues, 16))
	while len(binary) != 32:
		binary = "0" + binary
	
	sign = int(binary[0])
	exponent = binary[1:9]
	fraction = binary[10:]

	exponent = int(exponent, 2) -127
	exponent_ = -1
	remainder = 0
	for bit in fraction:
		remainder += int(bit) * (2**exponent_)
		exponent_ -= 1

	result = ((-1)**sign) * (1 + remainder) * (2**exponent)
	return result