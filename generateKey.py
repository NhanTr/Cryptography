import os

def generate_key_symmetric(algorithm):
    if algorithm == "AES":
        # Sinh khóa AES (ví dụ 256-bit)
        key = os.urandom(32)  # 32 bytes = 256 bits
    elif algorithm == "DES":
        # Sinh khóa DES (ví dụ 64-bit)
        key = os.urandom(8)  # 8 bytes = 64 bits
    elif algorithm == "3DES":
        # Sinh khóa 3DES (ví dụ 192-bit)
        key = os.urandom(24)  # 24 bytes = 192 bits

    return key.hex()  # Trả về khóa dưới dạng hex string