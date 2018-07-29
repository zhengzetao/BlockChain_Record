import contract

if __name__ == "__main__":
    INS = contract.deploy("storage.sol", "FileHashStorage")
    contract.upload(INS, '0a123','zetao',36,'zetao','D')
