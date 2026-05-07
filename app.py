from flask import Flask, render_template, request, jsonify
from AES import *
from DES3 import *
from DES import *
from hash_functions import hash_md5, hash_sha256, hash_all
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
    if(algorithm == "AES"):
        key = generate_aes_key()
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
    if(algorithm == "AES"):
        iv = generate_aes_iv()
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
            result = encrypt_aes(message, key, iv)
        elif algorithm == "DES":
            result = encrypt_des(message, key, iv)
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
            result = decrypt_aes(ciphertext, key, iv)
        elif algorithm == "DES":
            result = decrypt_des(ciphertext, key, iv)
    
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


if __name__ == '__main__':
    app.run(debug=True)