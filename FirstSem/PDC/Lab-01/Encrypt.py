from cryptography.fernet import Fernet
class Encrypt:
    def encrypt(self,key,fileName,output):
        with open(fileName, 'rb') as f:
            data = f.read()
            
        encrypted = Fernet(key).encrypt(data)
        with open(output_file, 'wb') as f:
            f.write(output)
