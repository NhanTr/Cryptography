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
        // console.log(data.key);
        output.value = data.key;
    } catch (error) {
        console.error('Error generating key:', error);
        output.value = "Lỗi khi tạo khóa.";
    }
}
async function generateIV() {
    const output = document.getElementById('sym-iv');
    const algorithm = document.getElementById("sym-algo").value;
    console.log(`Tạo IV cho thuật toán ${algorithm}`);
    output.innerText = "Đang tạo IV...";

    try {
        const response = await fetch('/generate-iv-symmetric', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ algorithm })
        });
        const data = await response.json();
        output.value = data.iv;
    } catch (error) {
        console.error('Error generating IV:', error);
        output.value = "Lỗi khi tạo IV.";
    }
}

async function encryptMessage() {
    const output = document.getElementById('result-output');
    const algorithm = document.getElementById("sym-algo").value;
    const key = document.getElementById('sym-key').value;
    const message = document.getElementById('sym-input').value;
    const iv = document.getElementById('sym-iv').value;
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
            body: JSON.stringify({ algorithm, key, message, iv })
        });
        const data = await response.json();
        console.log('Response status:', response.status, 'Response body:', data.result);
        output.innerText = data.result;
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
    const iv = document.getElementById('sym-iv').value;
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
            body: JSON.stringify({ algorithm, key, ciphertext, iv})
        });
        const data = await response.json();
        console.log('Response status:', response.status, 'Response body:', data.result);
        output.innerText = data.result;
    } catch (error) {
        console.error('Error decrypting message:', error);
        output.innerText = "Lỗi khi giải mã tin nhắn.";
    }
}

// ========== HASH FUNCTIONS ==========

/**
 * Tính giá trị hash cho chuỗi văn bản
 * Gọi API /hash với thuật toán được chọn (MD5 hoặc SHA-256)
 */
async function performHash() {
    const text = document.getElementById('hash-input').value;
    const algorithm = document.getElementById('hash-algo').value;
    const resultArea = document.getElementById('hash-result-area');
    const resultBox = document.getElementById('hash-result');
    const compareArea = document.getElementById('hash-compare-area');

    if (!text) {
        resultArea.style.display = 'block';
        resultBox.innerText = '⚠️ Vui lòng nhập chuỗi văn bản!';
        compareArea.style.display = 'none';
        return;
    }

    resultBox.innerText = 'Đang tính toán...';
    resultArea.style.display = 'block';
    compareArea.style.display = 'none';

    try {
        const response = await fetch('/hash', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text, algorithm })
        });
        const data = await response.json();

        if (data.status === 'success') {
            resultBox.innerText = data.result;
        } else {
            resultBox.innerText = '❌ Lỗi: ' + data.message;
        }
    } catch (error) {
        console.error('Error hashing:', error);
        resultBox.innerText = '❌ Lỗi kết nối server.';
    }
}

/**
 * Copy kết quả hash vào clipboard
 * Hiển thị thông báo "Đã copy!" trong 2 giây
 */
function copyHashResult() {
    const result = document.getElementById('hash-result').innerText;
    if (!result || result.startsWith('⚠️') || result.startsWith('❌')) {
        return;
    }

    navigator.clipboard.writeText(result).then(() => {
        const notification = document.getElementById('copy-notification');
        notification.style.display = 'inline';
        setTimeout(() => {
            notification.style.display = 'none';
        }, 2000);
    }).catch(err => {
        console.error('Failed to copy:', err);
    });
}

/**
 * So sánh kết quả hash MD5 và SHA-256 cùng lúc
 * Gọi API /hash-all để tính cả hai thuật toán đồng thời
 */
async function compareHash() {
    const text = document.getElementById('hash-input').value;
    const resultArea = document.getElementById('hash-result-area');
    const compareArea = document.getElementById('hash-compare-area');
    const md5Box = document.getElementById('compare-md5');
    const sha256Box = document.getElementById('compare-sha256');

    if (!text) {
        resultArea.style.display = 'block';
        document.getElementById('hash-result').innerText = '⚠️ Vui lòng nhập chuỗi văn bản!';
        compareArea.style.display = 'none';
        return;
    }

    resultArea.style.display = 'none';
    compareArea.style.display = 'block';
    md5Box.innerText = 'Đang tính toán...';
    sha256Box.innerText = 'Đang tính toán...';

    try {
        const response = await fetch('/hash-all', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text })
        });
        const data = await response.json();

        if (data.status === 'success') {
            md5Box.innerText = data.result.md5;
            sha256Box.innerText = data.result.sha256;
        } else {
            md5Box.innerText = '❌ Lỗi: ' + data.message;
            sha256Box.innerText = '❌ Lỗi: ' + data.message;
        }
    } catch (error) {
        console.error('Error comparing hash:', error);
        md5Box.innerText = '❌ Lỗi kết nối server.';
        sha256Box.innerText = '❌ Lỗi kết nối server.';
    }
}

/**
 * Xóa toàn bộ input và kết quả hash - chức năng "Thử lại"
 * Reset form về trạng thái ban đầu
 */
function clearHash() {
    // Xóa input
    document.getElementById('hash-input').value = '';
    document.getElementById('hash-algo').selectedIndex = 0;

    // Ẩn kết quả
    document.getElementById('hash-result-area').style.display = 'none';
    document.getElementById('hash-compare-area').style.display = 'none';

    // Xóa nội dung kết quả
    document.getElementById('hash-result').innerText = '';
    document.getElementById('compare-md5').innerText = '';
    document.getElementById('compare-sha256').innerText = '';
    document.getElementById('copy-notification').style.display = 'none';
}