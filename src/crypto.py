from io import StringIO
from typing import Text
from cryptography.fernet import Fernet
from Cryptodome import Cipher
from Cryptodome.Cipher import AES
import hashlib
import json
import os
#https://devrescue.com/simple-python-aes-encryption-example/

class crypto:
    def __init__(self):
        hash = hashlib.sha256(b"hey")
        print(hash.hexdigest())
        self.key = hash.digest()
        self.path = "LocoPass\data.bin"

    def encryptData(self, data):
        cipher = AES.new(self.key, AES.MODE_EAX)
        jsonData = json.dumps(data, indent = 4)
        encrypted, tag = cipher.encrypt_and_digest(
            bytes(jsonData, "utf-8")
            )
        outfile = open(self.path, "wb+")
        [outfile.write(x) for x in (cipher.nonce, tag, encrypted)]
        outfile.close()
    #use hash as key   
    
    def decryptData(self):
        file = open(self.path, "rb")
        nonce, tag, encrypted = [ file.read(x) for x in (16, 16, -1) ]
        cipher = AES.new(self.key, AES.MODE_EAX, nonce)
        decrypted = cipher.decrypt_and_verify(encrypted, tag)
        temp = open("./temp.json", "w+")
        temp.write(decrypted.decode())
        temp = open("./temp.json", "r")
        data = json.load(temp)
        temp.close()
        os.remove("./temp.json")
        return data
        


        #return json.loads(decrypted)

    