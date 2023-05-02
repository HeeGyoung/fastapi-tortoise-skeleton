from base64 import b64decode, b64encode

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

UTF_8 = "utf-8"


def _get_aes_cbc(key: str, iv: str):
    b_key = bytes(key[:16], UTF_8)
    b_iv = bytes(iv[:16], UTF_8)
    return AES.new(b_key, AES.MODE_CBC, b_iv)


def encrypt_aes_cbc(key: str, iv: str, data: str):
    cipher = _get_aes_cbc(key, iv)
    b_data = bytes(data, UTF_8)
    ct_bytes = cipher.encrypt(pad(b_data, AES.block_size))
    return b64encode(ct_bytes).decode(UTF_8)


def decrypt_aes_cbc(key: str, iv: str, data: str):
    cipher = _get_aes_cbc(key, iv)
    b_data = bytes(data, UTF_8)
    return unpad(cipher.decrypt(b64decode(b_data)), AES.block_size)
