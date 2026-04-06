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

### 3. Hàm băm (Hash Functions)
* **Thuật toán:** MD5, SHA-256.
* **Chức năng:** Tính toán giá trị băm (Digest) của một chuỗi văn bản đầu vào. Không yêu cầu khóa.

---
