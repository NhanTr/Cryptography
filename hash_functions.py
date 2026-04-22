import hashlib


def hash_md5(text):
    """Tính hash MD5 của chuỗi văn bản đầu vào.
    
    MD5 tạo ra giá trị hash 128-bit (32 ký tự hex).
    Lưu ý: MD5 hiện không còn an toàn cho mục đích bảo mật,
    chỉ sử dụng cho mục đích học tập.
    """
    return hashlib.md5(text.encode('utf-8')).hexdigest()


def hash_sha256(text):
    """Tính hash SHA-256 của chuỗi văn bản đầu vào.
    
    SHA-256 tạo ra giá trị hash 256-bit (64 ký tự hex).
    SHA-256 là thuật toán hash an toàn, được sử dụng rộng rãi
    trong các ứng dụng bảo mật hiện đại.
    """
    return hashlib.sha256(text.encode('utf-8')).hexdigest()
