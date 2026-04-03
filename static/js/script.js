function openTab(tabName) {
    // Ẩn tất cả nội dung
    document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
    
    // Hiện tab được chọn
    document.getElementById(tabName).classList.add('active');
    event.currentTarget.classList.add('active');
}

function generateKey() {
    const randomKey = Math.random().toString(36).substring(2, 10).toUpperCase();
    document.getElementById('sym-key').value = randomKey;
}

function handleAction(type) {
    const output = document.getElementById('result-output');
    output.innerText = "Đang xử lý...";

    // Ở đây bạn sẽ dùng fetch() để gửi dữ liệu lên Flask app.py
    // Ví dụ giả lập:
    setTimeout(() => {
        output.innerText = `[${type}] Thao tác thành công. (Đây là kết quả demo)`;
    }, 500);
}