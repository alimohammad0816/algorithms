"""
    OneTimePad Cipher
"""


from random import randint


class OneTime:
    @staticmethod
    def encrypt(text: str):
        plain = [ord(i) for i in text]
        key = []
        cipher = []
        for i in plain:
            k = randint(1, 1000)
            c = (i + k) * k
            cipher.append(c)
            key.append(k)
        
        # return {"cipher": cipher, "key": key}
        return cipher, key
    
    def decrypt(cipher, key):
        plain = []
        for i in range(len(key)):
            p = int((cipher[i] - key[i] ** 2) / key[i])
            plain.append(chr(p))

        return "".join(plain)
