from DES import generate_des_iv
from flask import Flask, render_template, request, jsonify
from generateKey import generate_key_symmetric
from DES3 import encrypt_3des, decrypt_3des
from DES import *
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
    if(algorithm == "DES"): key = generate_des_key()
    print(key)
    return jsonify({"status": "success", "key": key})

@app.route('/generate-iv-symmetric', methods=['POST'])
def generate_iv_symmetric_endpoint():
    print("Received request:", request.json)
    data = request.json
    algorithm = data.get("algorithm")

    iv = ""
    if(algorithm == "DES"): iv = generate_des_iv()
    print("iv DES: ", iv)
    return jsonify({"status": "success", "iv": iv})

#Encrypt API
@app.route('/encrypt-symmetric', methods=['POST'])
def encrypt_endpoint():
    print("Received request:", request.json)
    data = request.json
    
    key = data.get("key")
    message = data.get("message")
    iv = data.get("iv")
    algorithm = data.get("algorithm")
    result = ""
    

    try:
        if(algorithm == "DES"): result = encrypt_des(message, key, iv)
        elif(algorithm == "DES3"): result = encrypt_3des(key, message)
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
        if(algorithm == "DES"): result = decrypt_des(ciphertext, key, iv)
        elif(algorithm == "DES3"): result = decrypt_3des(key, ciphertext)
        return jsonify({"status": "success", "result": result})
    except Exception as e:
        print(f"Error decrypting: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)