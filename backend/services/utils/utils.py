import random
import string
import base64
from Crypto.Cipher import AES
from Crypto import Random

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os


def GetToken():
    MIN_NUM_CHAR = 5
    MAX_NUM_CHAR = 5
    num_char = random.randint(MIN_NUM_CHAR, MAX_NUM_CHAR)

    rand_string = ""
    for i in range(num_char):
        rand_string += random.choice(string.ascii_letters)

    print(rand_string)
    return rand_string

class bgcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class CryptoHandler2:

    def __init__(self):
        pass

    def encrypt(self, text):
        encryption_key = base64.b64decode('FoCKvdLslUuB4y3EZlKate7XGottHski1LmyqJHvUhs=')
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(encryption_key, AES.MODE_CTR, iv)
        encrypted = cipher.encrypt(text.encode())
        return iv.hex() + ':' + encrypted.hex()

    def decrypt(self, text):
        encryption_key = base64.b64decode('FoCKvdLslUuB4y3EZlKate7XGottHski1LmyqJHvUhs=')
        iv, encrypted = text.split(':')
        iv = bytes.fromhex(iv)
        encrypted = bytes.fromhex(encrypted)
        cipher = AES.new(encryption_key, AES.MODE_CTR, iv)
        decrypted = cipher.decrypt(encrypted)
        return decrypted.decode('utf-8')


class CryptoHandler:
    def __init__(self):
        self.algorithm = 'aes-256-ctr'
        self.encryption_key = base64.b64decode('FoCKvdLslUuB4y3EZlKate7XGottHski1LmyqJHvUhs=')
        self.iv_length = 16

    def encrypt(self, text):
        iv = os.urandom(self.iv_length)
        cipher = Cipher(algorithms.AES(self.encryption_key), modes.CTR(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted = encryptor.update(text.encode()) + encryptor.finalize()
        return f"{iv.hex()}:{encrypted.hex()}"

    def decrypt(self, text):
        text_parts = text.split(':')
        iv = bytes.fromhex(text_parts[0])
        encrypted_text = bytes.fromhex(text_parts[1])
        cipher = Cipher(algorithms.AES(self.encryption_key), modes.CTR(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted = decryptor.update(encrypted_text) + decryptor.finalize()
        return decrypted.decode()
