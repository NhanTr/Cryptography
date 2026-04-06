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