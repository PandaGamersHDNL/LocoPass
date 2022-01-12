from genericpath import isfile
from Cryptodome.Cipher import AES
from error import error
from dataStruct import dataHandling
import hashlib
import json
import re
import os
#https://devrescue.com/simple-python-aes-encryption-example/

class Crypto:
    def __init__(self, path, key):
        self.path = path
        hash = hashlib.sha256(key.encode())
        self.key = hash.digest()

    def encryptData(self, data):
        try:
            cipher = AES.new(self.key, AES.MODE_EAX)
            jsonData = json.dumps(data, indent = 4)
            encrypted, tag = cipher.encrypt_and_digest(
                bytes(jsonData, "utf-8")
                )
            outfile = open(self.path, "wb+")
            [outfile.write(x) for x in (cipher.nonce, tag, encrypted)]
            outfile.close()
            return True
        except:
            error("encrypt error")
            return False

    
    def decryptData(self):
        try:
            #TODO if file doesn't exist ask user to make new file
            if(not os.path.isfile(self.path)):
                error("not a valid path")
                return False
            file = open(self.path, "rb")
            path = "./temp.json"
            nonce, tag, encrypted = [ file.read(x) for x in (16, 16, -1) ]
            cipher = AES.new(self.key, AES.MODE_EAX, nonce)
            decrypted = cipher.decrypt_and_verify(encrypted, tag)
            temp = open(path, "w+")
            temp.write(decrypted.decode())
            temp = open(path, "r")
            data = json.load(temp)
            temp.close()
            os.remove(path)
            return data
        except:
            error("decrypt error")
            return False
        


        #return json.loads(decrypted)

    