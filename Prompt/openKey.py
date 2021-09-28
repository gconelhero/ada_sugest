from cryptography.fernet import Fernet
import os

# DECRYPT API KEY!

class OpenKey():
    
    def __init__(self):
        self.crypt_key = os.getenv('CRYPT_KEY')
        #open(".\\crypt\\crypt_key.txt", "r")
        self.api_file = os.getenv('OPEN_API_KEY')
        #open(".\\crypt\\APIKEY.txt")
        
    
    def openKey(self):
        key = Fernet(self.crypt_key.encode())
        open_key = key.decrypt(self.api_file.encode())
        #self.crypt_key.close()
        #self.api_file.close()

        return open_key.decode()
