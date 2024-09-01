Email Spam Classification
Giới thiệu
Dự án này là một hệ thống phân loại email spam sử dụng mô hình học máy để phân loại email vào các nhóm spam hoặc ham (không phải spam). Mô hình được huấn luyện trên tập dữ liệu email và được triển khai dưới dạng một ứng dụng web để người dùng có thể phân loại email một cách dễ dàng.

Cài đặt
Clone repository:
bash
git clone https://github.com/yourusername/email-spam-classification.git
cd email-spam-classification

Cài đặt các thư viện cần thiết:
bash
pip install -r requirements.txt

Tải mô hình:

Sử dụng
Chạy ứng dụng web:
bash
python app.py
Ứng dụng sẽ chạy trên http://127.0.0.1:5000/. Bạn có thể truy cập vào địa chỉ này trong trình duyệt của mình.

Gửi email để phân loại:

Mở trình duyệt và truy cập vào http://127.0.0.1:5000/.
Nhập nội dung email vào ô văn bản và nhấn nút "Submit".
Kết quả phân loại sẽ được hiển thị ngay lập tức.
Ví dụ
POST Request Example:

bash

POST http://127.0.0.1:5000/predict
Content-Type: application/json

{
  "text": "Congratulations! You've won a $1000 gift card."
}
Response Example:

json
Sao chép mã
{
  "prediction": "spam"
}
Các tệp trong dự án
app.py: Tệp chính của ứng dụng web, chứa mã nguồn cho API phân loại email.
model.pkl: Tệp chứa mô hình học máy đã huấn luyện.
requirements.txt: Danh sách các thư viện Python cần thiết cho dự án.
README.md: Tài liệu hướng dẫn sử dụng dự án.
Đóng góp
Nếu bạn muốn đóng góp vào dự án này, vui lòng tạo một pull request hoặc mở một issue để thảo luận các thay đổi.

Liên hệ
Nếu bạn có bất kỳ câu hỏi nào về dự án, vui lòng liên hệ với tôi qua email nhatanhdo054@gmail.com