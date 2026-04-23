# 🔐 Cryptography Toolkit (Flask Web App)

Dự án này là một bộ công cụ mật mã học chạy trên nền tảng Web, được xây dựng bằng **Python (Flask)**. Ứng dụng cung cấp giao diện trực quan để người dùng tìm hiểu và thực hiện các thao tác mã hóa đối xứng, bất đối xứng và các hàm băm phổ biến.

---

## ✨ Các Chức năng Chính

### 1. Mã hóa Đối xứng (Symmetric Encryption)
* **Thuật toán hỗ trợ:** DES, 3DES, AES.
* **Chức năng mã hóa:** Người dùng nhập Plaintext, có thể tự nhập khóa hoặc nhấn nút **"Generate Random Key"** để hệ thống tạo khóa ngẫu nhiên.
* **Chức năng giải mã:** Nhập Ciphertext và khóa tương ứng để lấy lại dữ liệu gốc.

### 2. Mã hóa Bất đối xứng (Asymmetric Encryption)
* **Thuật toán:** RSA.
* **Quản lý khóa:** Tính năng tạo cặp khóa (Key Pair Generation) tự động tạo ra Public Key và Private Key.
* **Mã hóa/Giải mã:** Cho phép người dùng tùy chọn khóa để mã hóa và sử dụng khóa còn lại trong cặp để giải mã.

### 3. Hàm băm (Hash Functions) — `hash_functions.py`
* **Thuật toán:** MD5 (128-bit), SHA-256 (256-bit).
* **Chức năng chính:**
  * Nhập chuỗi văn bản bất kỳ (hỗ trợ Unicode / tiếng Việt)
  * Tính và hiển thị giá trị Hash (Digest)
  * **So sánh MD5 & SHA-256** song song để thấy sự khác biệt về độ dài output
  * **Copy kết quả** vào clipboard
  * **Thử lại / Xóa** để reset form
* **Thư viện:** `hashlib` (thư viện chuẩn Python, không cần cài thêm)
* **Lưu ý:** MD5 chỉ dùng cho mục đích học tập — không an toàn trong thực tế.

---

## 🚀 Cách Chạy Ứng Dụng

```bash
# 1. Cài đặt thư viện
pip install -r requirements.txt

# 2. Chạy server Flask
python app.py

# 3. Mở trình duyệt tại
http://127.0.0.1:5000
```

---

## 📦 Thư Viện Sử Dụng

| Thư viện | Mục đích |
|----------|----------|
| `flask` | Web framework |
| `pycryptodome` | DES, 3DES, AES encryption |
| `cryptography` | RSA encryption |
| `hashlib` | MD5, SHA-256 hashing (built-in) |

---

## 👥 Phân Công Nhóm

| Thành viên | Phần đảm nhận |
|------------|---------------|
| Thành viên 1 | AES |
| Thành viên 2 | DES |
| Thành viên 3 | 3DES |
| Thành viên 4 | RSA |
| Thành viên 5 | MD5 & SHA-256 (Hash Functions) |
