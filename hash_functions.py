import hashlib


def hash_md5(text):
    """Tính hash MD5 của chuỗi văn bản đầu vào.
    
    MD5 tạo ra giá trị hash 128-bit (32 ký tự hex).
    Lưu ý: MD5 hiện không còn an toàn cho mục đích bảo mật,
    chỉ sử dụng cho mục đích học tập.
    """
    return hashlib.md5(text.encode('utf-8')).hexdigest()
