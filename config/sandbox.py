
test = ["665d6a40","69f16e40","39fe553c","33669440","331c9240","10508a3e"]
binaries = []

for element in test:
	binary = "{0:08b}".format(int(element, 16))
	while len(binary) != 32:
		binary = "0" + binary
	print(str(binary))
	
	sign = int(binary[0])
	exponent = binary[1:9]
	fraction = binary[10:]
	# print(sign)
	# print(exponent)
	# print(fraction + "\n")

	exponent = int(exponent, 2) -127

	exponent_ = -1
	remainder = 0
	for bit in fraction:
		remainder += int(bit) * (2**exponent_)
		exponent_ -= 1

	sign = (-1)**sign
	print(sign)
	remainder = 1 + remainder
	print(exponent)
	exponent = 2**exponent
	print(remainder)


	answer = sign * remainder * exponent

	print(answer)
	print("\n")
