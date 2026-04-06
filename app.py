from flask import Flask, render_template, request, jsonify
from generateKey import generate_key_symmetric

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
@app.route('/encrypt', methods=['POST'])
def encrypt_endpoint():
    print("Received request:", request.json)
    data = request.json
    # Logic mã hóa sẽ nằm ở đây
    return jsonify({"status": "success", "result": "Kết quả mã hóa từ Server"})

#Decrypt API
@app.route('/decrypt', methods=['POST'])
def decrypt_endpoint():
    print("Received request:", request.json)
    data = request.json
    # Logic giải mã sẽ nằm ở đây
    return jsonify({"status": "success", "result": "Kết quả giải mã từ Server"})


if __name__ == '__main__':
    app.run(debug=True)