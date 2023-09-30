from re import findall

def regular(text): 
    template = r".{"+str(BLOCK)+"}"
    return findall(template, text)

def addition(text):
	while len(text) % BLOCK != 0: 
		text += '0'
	return text

def toMatrix(text, matrix = []):
	for three in regular(text): 
		matrix.append(list(three))
	return matrix

def createMatrix(matrix):
	final = []
	for _ in range(len(matrix)): 
		final.append([])
	return final

def encodeMatrix(matrix):
	final = createMatrix(matrix)
	for block in range(len(matrix)):
		for cell in range(len(matrix[block])):
			final[block].append(ord(matrix[block][cell]))
	return final

def decodeMatrix(matrix):
	final = createMatrix(matrix)
	for block in range(len(matrix)):
		for cell in range(len(matrix[block])):
			final[block].append(chr(matrix[block][cell]))
	return final

def encodeVector(vector):
	for cell in range(len(vector)):
		vector[cell] = ord(vector[cell])
	return vector

def toVectorXOR(text):
	text = encodeVector(list(text))
	vecXOR = text[0]
	for index in range(1,BLOCK): 
		vecXOR ^= text[index]
	return vecXOR

def toString(matrix, final = ""):
	for block in range(len(matrix)):
		for cell in range(len(matrix[block])):
			final += matrix[block][cell]
	return final

def encrypt(message, vector, key):
	matrix = encodeMatrix(toMatrix(addition(message)))
	key, vector = toVectorXOR(key), toVectorXOR(vector)
	final = createMatrix(matrix)
	for cell in range(BLOCK):
		final[0].append(matrix[0][cell] ^ vector ^ key)
	for block in range(1,len(matrix)):
		vecInit = final[block-1][0]
		for index in range(1, BLOCK): vecInit ^= final[block-1][index]
		for cell in range(BLOCK):
			final[block].append(matrix[block][cell] ^ vecInit ^ key)
	return final

def decrypt(matrix, vector, key):
	key, vector = toVectorXOR(key), toVectorXOR(vector)
	final = createMatrix(matrix)
	for cell in range(BLOCK):
		final[0].append(matrix[0][cell] ^ vector ^ key)
	for block in range(1,len(matrix)):
		vecInit = matrix[block-1][0]
		for index in range(1, BLOCK): vecInit ^= matrix[block-1][index]
		for cell in range(BLOCK):
			final[block].append(matrix[block][cell] ^ vecInit ^ key)
	return toString(decodeMatrix(final))

try:
	cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
	if cryptMode not in ['E','D']:
		print("Error: mode is not Found"); raise SystemExit
except KeyboardInterrupt: 
	print(); raise SystemExit

try:
	BLOCK = int(input("Set BLOCK size: "))
	startMessage = input("Write the message: ")
	keyVectInit = input("Write the key & vector init: ").split()
except KeyboardInterrupt: 
	print(); raise SystemExit
except ValueError: 
	print("Error: BLOCK is not int value"); raise SystemExit

def encryptDecrypt(mode, message, key_vector):
	if mode == 'E':
		return encrypt(message, key_vector[1], key_vector[0])
	else:
		try:
			return decrypt(eval(message), key_vector[1], key_vector[0])
		except NameError: 
			print("Error: message is not list"); raise SystemExit
print("Final message:",encryptDecrypt(cryptMode, startMessage, keyVectInit))
