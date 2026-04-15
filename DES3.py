import binascii
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

def to_hex(byte_data):
    return binascii.hexlify(byte_data).decode('utf-8')

def to_bytes(hex_data):
    return binascii.unhexlify(hex_data)

def generate_3des_key():
    # 3DES cần 24 bytes (192 bits)
    return to_hex(get_random_bytes(24))

def generate_3des_iv():
    # 3DES sử dụng khối 64 bit (8 byte)
    return to_hex(get_random_bytes(8))


def pad(data, block_size):
    pad_len = block_size - (len(data) % block_size)
    padding = bytes([pad_len] * pad_len)
    return data + padding

def encrypt_3des(plaintext, key_hex, iv_hex):
    data_bytes = plaintext.encode('utf-8')

    key = to_bytes(key_hex)
    iv = to_bytes(iv_hex)

    cipher = DES3.new(key, DES3.MODE_ECB)
    block_size = DES3.block_size
    padded_data = pad(data_bytes, block_size)
    
    result = b''
    prev_block = iv
    
    for i in range(0, len(padded_data), block_size):
        block = padded_data[i : i + block_size]

        xored = bytes(b1 ^ b2 for b1, b2 in zip(block, prev_block))
        encrypted_block = cipher.encrypt(xored)
        result += encrypted_block
        prev_block = encrypted_block

    return to_hex(result)

def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

def decrypt_3des(ciphertext_hex, key_hex, iv_hex):
    ciphertext = to_bytes(ciphertext_hex)  

    key = to_bytes(key_hex)
    iv = to_bytes(iv_hex)

    cipher = DES3.new(key, DES3.MODE_ECB)
    block_size = DES3.block_size
    
    result = b''
    prev_block = iv
    
    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i : i + block_size]

        decrypted_block = cipher.decrypt(block)
        xored = bytes(b1 ^ b2 for b1, b2 in zip(decrypted_block, prev_block))
        result += xored
        prev_block = block

    unpadded_result = unpad(result)
    return unpadded_result.decode('utf-8')