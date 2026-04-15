from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import binascii

# DES (Data Encryption Standard) là:
# Thuật toán mã hóa đối xứng → dùng cùng 1 key để mã hóa & giải mã
# Là block cipher → xử lý dữ liệu theo khối 64 bit (8 byte)

def to_hex(data):
    return binascii.hexlify(data).decode('utf-8')
def to_bytes(data_hex):
    return binascii.unhexlify(data_hex)

def generate_des_key():
    return to_hex(get_random_bytes(8))


def generate_des_iv():
    return to_hex(get_random_bytes(8))

def pad(data, block_size):
    pad_len = block_size - (len(data) % block_size)
    padding = bytes([pad_len] * pad_len)
    return data + padding

def encrypt_des(plaintext, key_hex, iv_hex): 

    data_bytes = plaintext.encode('utf-8')

    key = to_bytes(key_hex)
    iv = to_bytes(iv_hex)

    cipher = DES.new(key, DES.MODE_ECB)
    block_size = DES.block_size
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
# 4. Giải mã DES CBC
def decrypt_des(ciphertext_hex, key_hex, iv_hex):
    print("in des.py: ", ciphertext_hex, key_hex, iv_hex)
    ciphertext = to_bytes(ciphertext_hex)  

    key = to_bytes(key_hex)
    iv = to_bytes(iv_hex)

    cipher = DES.new(key, DES.MODE_ECB)
    block_size = DES.block_size

    result = b''
    prev_block = iv

    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i : i + block_size]

        decrypted = cipher.decrypt(block)
        plain_block = bytes(b1 ^ b2 for b1, b2 in zip(decrypted, prev_block))

        result += plain_block
        prev_block = block

    result = unpad(result)
    print("result: ", result.decode('utf-8'))
    return result.decode('utf-8')
    





# ==============================
# 6. Demo chạy thử
# ==============================
# if __name__ == "__main__":
#     # Sinh key và IV
#     key = generate_des_key()
#     iv = generate_iv()

#     print("Key (hex):", to_hex(key))
#     print("IV  (hex):", to_hex(iv))

#     plaintext = "Hello DES CBC Mode!"

#     print("\nPlaintext:", plaintext)

#     # Mã hóa
#     ciphertext = encrypt_des_cbc(plaintext, key, iv)
#     print("Ciphertext (hex):", ciphertext)

#     # Giải mã
#     decrypted = decrypt_des_cbc(ciphertext, key, iv)
#     print("Decrypted:", decrypted)


plaintext = "nhan thien"
key = "495f95499c52171e"
iv = "4dfca20048f6d46f"
result = encrypt_des(plaintext, key, iv)
