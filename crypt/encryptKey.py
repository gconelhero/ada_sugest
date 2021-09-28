from cryptography.fernet import Fernet
import os

# ENCRYPT API KEY! (txt)

class EncryptKey():

    def __init__(self):
        self.crypt_key = os.getenv('CRYPT_KEY')
        self.api_key = input("API KEY: ")
        
    def encryptKey(self):
        fernet_key = Fernet(self.crypt_key.encode())
        self.api_key = fernet_key.encrypt(self.api_key.encode())
        os.system(f'setx OPEN_API_KEY {self.api_key.decode()}')
        
        print("""REBOOT YOUR COMMAND PROMPT !
                \nREBOOT YOUR TEXT EDITOR CODE !""")