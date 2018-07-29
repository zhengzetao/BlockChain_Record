import contract
import sys

if __name__ == "__main__":
	filehash  = sys.argv[1]
	filename = sys.argv[2]
	filesize = sys.argv[3]
	owner = sys.argv[4]
	operation = sys.argv[5]
	# print(type(filehash),type(filename),type(float(filesize)),type(owner),type(operation))
	# exit()
	INS = contract.deploy("storage.sol", "FileHashStorage")
	# contract.upload(INS, '0a123','zetao',36,'zetao','D')
	contract.upload(INS,filehash,filename,int(filesize),owner,operation)
