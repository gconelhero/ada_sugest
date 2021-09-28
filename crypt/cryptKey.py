import os
from cryptography.fernet import Fernet

# Generate a Fernet KEY! (txt)

class CryptKey():
    
    def __init__(self):
        self.crypt_key = Fernet.generate_key()

    def createKey(self):
        os.system(f"setx CRYPT_KEY {self.crypt_key.decode()}")
