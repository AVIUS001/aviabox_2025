# communications/encryption.py
import base64

class Encryption:
    def encrypt(self, plaintext):
        return base64.b64encode(plaintext.encode("utf-8")).decode("utf-8")

    def decrypt(self, ciphertext):
        return base64.b64decode(ciphertext.encode("utf-8")).decode("utf-8")

if __name__ == "__main__":
    enc = Encryption()
    cipher = enc.encrypt("Secret Message")
    print("Encrypted:", cipher)
    print("Decrypted:", enc.decrypt(cipher))
