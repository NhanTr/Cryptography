import random
import math

# 1. Hàm tạo khóa Public Key và Private Key
def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Chọn e sao cho 1 < e < phi và e đồng nguyên tố với phi
    e = random.randrange(2, phi)
    while math.gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    # Tính d là nghịch đảo modulo của e theo phi
    # (Tìm d sao cho (d * e) % phi == 1)
    d = pow(e, -1, phi)

    # Trả về: Khóa công khai (e, n) và Khóa riêng tư (d, n)
    return (e, n), (d, n)

# 2. Hàm mã hóa
def encrypt(public_key, plaintext):
    e, n = public_key
    # Công thức: C = M^e mod n
    # Chuyển từng ký tự của chuỗi thành số (ASCII) rồi mã hóa
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

# 3. Hàm giải mã
def decrypt(private_key, ciphertext):
    d, n = private_key
    # Công thức: M = C^d mod n
    # Giải mã từng số về lại ký tự ASCII
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext

# # ==========================================
# # CHẠY THỬ CHƯƠNG TRÌNH
# # ==========================================
# if __name__ == '__main__':
#     # Hai số nguyên tố (Trong thực tế p, q phải rất lớn, cỡ 1024-2048 bit)
#     p = 61
#     q = 53
    
#     print("Đang tạo khóa RSA...")
#     public, private = generate_keypair(p, q)
#     print(f"- Khóa công khai (e, n): {public}")
#     print(f"- Khóa riêng tư (d, n): {private}")
    
#     # Tin nhắn cần mã hóa
#     message = "HELLO RSA!"
#     print(f"\nTin nhắn gốc: {message}")
    
#     # Mã hóa
#     encrypted_msg = encrypt(public, message)
#     print(f"Bản mã (Ciphertext): {encrypted_msg}")
    
#     # Giải mã
#     decrypted_msg = decrypt(private, encrypted_msg)
#     print(f"Tin nhắn sau khi giải mã: {decrypted_msg}")