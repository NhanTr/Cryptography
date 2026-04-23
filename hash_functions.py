import hashlib


def validate_input(text):
    """Kiểm tra đầu vào có hợp lệ hay không.
    
    Raises:
        ValueError: Nếu đầu vào là None
        TypeError: Nếu đầu vào không phải chuỗi
    """
    if text is None:
        raise ValueError("Input text cannot be None")
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return True

def hash_md5(text):
    """Tính hash MD5 của chuỗi văn bản đầu vào.
    
    MD5 tạo ra giá trị hash 128-bit (32 ký tự hex).
    Lưu ý: MD5 hiện không còn an toàn cho mục đích bảo mật,
    chỉ sử dụng cho mục đích học tập.
    
    Hỗ trợ: chuỗi rỗng, ký tự đặc biệt, Unicode (tiếng Việt)
    """
    validate_input(text)
    return hashlib.md5(text.encode('utf-8')).hexdigest()


def hash_sha256(text):
    """Tính hash SHA-256 của chuỗi văn bản đầu vào.
    
    SHA-256 tạo ra giá trị hash 256-bit (64 ký tự hex).
    SHA-256 là thuật toán hash an toàn, được sử dụng rộng rãi
    trong các ứng dụng bảo mật hiện đại.
    
    Hỗ trợ: chuỗi rỗng, ký tự đặc biệt, Unicode (tiếng Việt)
    """
    validate_input(text)
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def hash_all(text):
    """Tính cả MD5 và SHA-256 để so sánh kết quả.
    
    Hàm này giúp người dùng thấy được sự khác biệt về độ dài output
    giữa MD5 (128-bit) và SHA-256 (256-bit), phục vụ mục đích giáo dục.
    
    Returns:
        dict: Chứa hash MD5, SHA-256 và độ dài tương ứng
    """
    validate_input(text)
    md5_result = hash_md5(text)
    sha256_result = hash_sha256(text)
    return {
        "md5": md5_result,
        "sha256": sha256_result,
        "md5_length": len(md5_result),        # 32 ký tự (128 bits)
        "sha256_length": len(sha256_result)    # 64 ký tự (256 bits)
    }
