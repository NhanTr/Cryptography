import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def encrypt_3des(key, message):
    """Mã hóa 3DES với mode CBC"""
    # key phải là 24 bytes (192 bits) cho 3DES
    key_bytes = key.encode() if isinstance(key, str) else key
    if len(key_bytes) < 24:
        key_bytes = key_bytes.ljust(24, b'\x00')
    else:
        key_bytes = key_bytes[:24]
    
    iv = os.urandom(8)  # DES3 block size là 8 bytes
    cipher = Cipher(
        algorithms.TripleDES(key_bytes),
        modes.CBC(iv),
        backend=default_backend()
    )
    encryptor = cipher.encryptor()
    
    # Thêm padding
    message_bytes = message.encode()
    block_size = 8
    padding_length = block_size - (len(message_bytes) % block_size)
    padded_message = message_bytes + bytes([padding_length]) * padding_length
    
    ciphertext = iv + encryptor.update(padded_message) + encryptor.finalize()
    return ciphertext.hex()

def decrypt_3des(key, ciphertext_hex):
    """Giải mã 3DES với mode CBC"""
    # key phải là 24 bytes (192 bits) cho 3DES
    key_bytes = key.encode() if isinstance(key, str) else key
    if len(key_bytes) < 24:
        key_bytes = key_bytes.ljust(24, b'\x00')
    else:
        key_bytes = key_bytes[:24]
    
    ciphertext = bytes.fromhex(ciphertext_hex)
    iv = ciphertext[:8]  # Lấy IV từ phần đầu của ciphertext
    actual_ciphertext = ciphertext[8:]
    
    cipher = Cipher(
        algorithms.TripleDES(key_bytes),
        modes.CBC(iv),
        backend=default_backend()
    )
    decryptor = cipher.decryptor()
    
    decrypted_padded = decryptor.update(actual_ciphertext) + decryptor.finalize()
    
    # Loại bỏ padding
    padding_length = decrypted_padded[-1]
    decrypted = decrypted_padded[:-padding_length]
    
    return decrypted.decode()