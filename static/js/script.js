function openTab(tabName) {
    // Ẩn tất cả nội dung
    document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
    
    // Hiện tab được chọn
    document.getElementById(tabName).classList.add('active');
    event.currentTarget.classList.add('active');
}


function handleAction(type) {
    const output = document.getElementById('result-output');
    const algorithm = document.getElementById("sym-algo").value;
    console.log(`Thực hiện ${type} với thuật toán ${algorithm}`);
    output.innerText = "Đang xử lý...";

    // Ở đây bạn sẽ dùng fetch() để gửi dữ liệu lên Flask app.py
    // Ví dụ giả lập:
    setTimeout(() => {
        output.innerText = `[${type}] Thao tác thành công. (Đây là kết quả demo)`;
    }, 500);
}

async function generateKey() {
    const output = document.getElementById('sym-key');
    const algorithm = document.getElementById("sym-algo").value;
    console.log(`Tạo khóa cho thuật toán ${algorithm}`);
    output.innerText = "Đang tạo khóa...";

    try {
        const response = await fetch('/generate-key-symmetric', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ algorithm })
        });
        const data = await response.json();
        output.value = data.key;
    } catch (error) {
        console.error('Error generating key:', error);
        output.value = "Lỗi khi tạo khóa.";
    }
}

async function encryptMessage() {
    const output = document.getElementById('result-output');
    const algorithm = document.getElementById("sym-algo").value;
    const key = document.getElementById('sym-key').value;
    const message = document.getElementById('sym-input').value;

    if (!key || !message) {
        output.innerText = "Vui lòng nhập khóa và tin nhắn!";
        return;
    }

    try {
        const response = await fetch('/encrypt-symmetric', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ algorithm, key, message })
        });
        const data = await response.json();
        if (response.ok) {
            output.innerText = data.result;
        } else {
            output.innerText = `Lỗi: ${data.message}`;
        }
    } catch (error) {
        console.error('Error encrypting message:', error);
        output.innerText = "Lỗi khi mã hóa tin nhắn.";
    }
}

async function decryptMessage() {
    const output = document.getElementById('result-output');
    const algorithm = document.getElementById("sym-algo").value;
    const key = document.getElementById('sym-key').value;
    const ciphertext = document.getElementById('sym-input').value;

    if (!key || !ciphertext) {
        output.innerText = "Vui lòng nhập khóa và ciphertext!";
        return;
    }

    try {
        const response = await fetch('/decrypt-symmetric', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ algorithm, key, ciphertext })
        });
        const data = await response.json();
        if (response.ok) {
            output.innerText = data.result;
        } else {
            output.innerText = `Lỗi: ${data.message}`;
        }
    } catch (error) {
        console.error('Error decrypting message:', error);
        output.innerText = "Lỗi khi giải mã tin nhắn.";
    }
}