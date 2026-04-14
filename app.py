from flask import Flask, render_template, request, jsonify
from generateKey import generate_key_symmetric
from DES3 import encrypt_3des, decrypt_3des

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
    # Sinh khóa dựa trên thuật toán được chọn
    key = generate_key_symmetric(algorithm)
    return jsonify({"status": "success", "key": key})


#Encrypt API
@app.route('/encrypt-symmetric', methods=['POST'])
def encrypt_endpoint():
    print("Received request:", request.json)
    data = request.json
    
    key = data.get("key")
    message = data.get("message")
    algorithm = data.get("algorithm")

    try:
        result = encrypt_3des(key, message)
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

    try:
        result = decrypt_3des(key, ciphertext)
        return jsonify({"status": "success", "result": result})
    except Exception as e:
        print(f"Error decrypting: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)