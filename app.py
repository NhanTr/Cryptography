from flask import Flask, render_template, request, jsonify
from DES3 import *
from DES import *
from hash_functions import hash_md5, hash_sha256, hash_all
from RSA import *
import base64
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Placeholder cho các API xử lý sau này
@app.route('/process', methods=['POST'])
def process():
    data = request.json
    # Logic mã hóa/giải mã/hash sẽ nằm ở đây
    return jsonify({"status": "success", "result": "Kết quả mẫu từ Server"})

#Generate key API for algorithms (DES, AES, 3DES)
@app.route('/generate-key-symmetric', methods=['POST'])
def generate_key_symmetric_endpoint():
    print("Received request:", request.json)
    data = request.json
    algorithm = data.get("algorithm")

    key = ""
    if(algorithm == "DES"): 
        key = generate_des_key()
    elif(algorithm == "3DES"): 
        key = generate_3des_key()  # 3DES cần 24 bytes (192 bits)
    print(key)
    return jsonify({"status": "success", "key": key})

@app.route('/generate-iv-symmetric', methods=['POST'])
def generate_iv_symmetric_endpoint():
    print("Received request:", request.json)
    data = request.json
    algorithm = data.get("algorithm")

    iv = ""
    if(algorithm == "DES"): 
        iv = generate_des_iv()
    elif(algorithm == "3DES"): 
        iv = generate_3des_iv()
    print("iv: ", iv)
    return jsonify({"status": "success", "iv": iv})

#Encrypt API
@app.route('/encrypt-symmetric', methods=['POST'])
def encrypt_endpoint():
    data = request.json
    
    key = data.get("key")
    message = data.get("message")
    iv = data.get("iv")
    algorithm = data.get("algorithm")
    result = ""
    

    try:
        if algorithm == "3DES":
            result = encrypt_3des(message, key, iv)
        elif algorithm == "AES":
            # result = encrypt_aes(key, message)  # Placeholder cho AES
            pass
        elif algorithm == "DES":
            result = encrypt_des(message, key, iv)
            pass
        return jsonify({"status": "success", "result": result})
    except Exception as e:
        print(f"Error encrypting: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

#Decrypt API
@app.route('/decrypt-symmetric', methods=['POST'])
def decrypt_endpoint():
    print("Received request:", request.json)
    data = request.json
    
    key = data.get("key")
    ciphertext = data.get("ciphertext")
    algorithm = data.get("algorithm")
    iv = data.get("iv")
    result = ""
    
    print(ciphertext, key, iv)
    try:
        result = None
        if algorithm == "3DES":
            result = decrypt_3des(ciphertext, key, iv)
        elif algorithm == "AES":
            # result = decrypt_aes(key, ciphertext)  # Placeholder cho AES
            pass
        elif algorithm == "DES":
            result = decrypt_des(ciphertext, key, iv)
            pass
    
        return jsonify({"status": "success", "result": result})
    except Exception as e:
        print(f"Error decrypting: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


# Hash API - Tính giá trị hash cho chuỗi văn bản
@app.route('/hash', methods=['POST'])
def hash_endpoint():
    data = request.json
    if not data:
        return jsonify({"status": "error", "message": "Không nhận được dữ liệu"}), 400

    text = data.get("text")
    algorithm = data.get("algorithm", "MD5")

    if text is None:
        return jsonify({"status": "error", "message": "Vui lòng nhập chuỗi văn bản"}), 400

    try:
        if algorithm == "MD5":
            result = hash_md5(text)
        elif algorithm == "SHA-256":
            result = hash_sha256(text)
        else:
            return jsonify({"status": "error", "message": "Thuật toán không được hỗ trợ"}), 400

        return jsonify({"status": "success", "result": result})
    except Exception as e:
        print(f"Error hashing: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


# Hash All API - Tính cả MD5 và SHA-256 cùng lúc để so sánh
@app.route('/hash-all', methods=['POST'])
def hash_all_endpoint():
    data = request.json
    if not data:
        return jsonify({"status": "error", "message": "Không nhận được dữ liệu"}), 400

    text = data.get("text")

    if text is None:
        return jsonify({"status": "error", "message": "Vui lòng nhập chuỗi văn bản"}), 400

    try:
        result = hash_all(text)
        return jsonify({"status": "success", "result": result})
    except Exception as e:
        print(f"Error hashing: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

#RSA
# Cập nhật 3 hàm RSA trong app.py để sử dụng thuật toán từ file RSA.py của bạn

@app.route('/generate-keys-rsa', methods=['POST'])
def generate_keys_rsa():
    try:
        # Chọn 2 số nguyên tố p, q (Trong thực tế là số rất lớn, demo dùng số nhỏ)
        p = 61
        q = 53
        
        # Gọi hàm từ file RSA.py của bạn
        public_key, private_key = generate_keypair(p, q)
        
        # public_key là dạng tuple (e, n), chuyển thành chuỗi "e,n" để gửi lên web
        pub_str = f"{public_key[0]},{public_key[1]}"
        priv_str = f"{private_key[0]},{private_key[1]}"
        
        return jsonify({
            'status': 'success',
            'public_key': pub_str,
            'private_key': priv_str
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/encrypt-rsa', methods=['POST'])
def encrypt_rsa():
    try:
        data = request.json
        pub_key_str = data.get('public_key') # Dạng "e,n"
        message = data.get('message')
        
        # Tách chuỗi thành số e và số n
        e_str, n_str = pub_key_str.split(',')
        public_key = (int(e_str), int(n_str))
        
        # Gọi hàm encrypt từ file RSA.py (kết quả trả về là 1 list các số nguyên)
        encrypted_list = encrypt(public_key, message)
        
        # Ghép mảng số thành chuỗi cách nhau bởi dấu phẩy để hiển thị trên HTML
        encrypted_str = ','.join(map(str, encrypted_list))
        
        return jsonify({'status': 'success', 'result': encrypted_str})
    except Exception as e:
        return jsonify({'status': 'error', 'message': "Lỗi mã hóa! Kiểm tra lại Public Key."})

@app.route('/decrypt-rsa', methods=['POST'])
def decrypt_rsa():
    try:
        data = request.json
        priv_key_str = data.get('private_key') # Dạng "d,n"
        ciphertext_str = data.get('ciphertext') # Dạng "123,456,789"
        
        # Tách chuỗi thành số d và số n
        d_str, n_str = priv_key_str.split(',')
        private_key = (int(d_str), int(n_str))
        
        # Chuyển chuỗi mã hóa về lại thành mảng các số nguyên
        ciphertext_list = list(map(int, ciphertext_str.split(',')))
        
        # Gọi hàm decrypt từ file RSA.py
        decrypted_msg = decrypt(private_key, ciphertext_list)
        
        return jsonify({'status': 'success', 'result': decrypted_msg})
    except Exception as e:
        return jsonify({'status': 'error', 'message': "Lỗi giải mã! Khóa Private hoặc chuỗi mã hóa không hợp lệ."})

if __name__ == '__main__':
    app.run(debug=True)