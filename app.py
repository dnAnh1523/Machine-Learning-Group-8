from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Tải mô hình đã huấn luyện
model_path = 'model/random_forest.pkl'
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

# Tạo route cho trang chính
@app.route('/')
def home():
    return render_template('index.html')

# Route để xử lý khi người dùng gửi email cần phân loại
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Lấy dữ liệu từ form
        email_data = request.form['email_text']
        
        # Tiền xử lý dữ liệu email (giả định rằng bạn có các bước xử lý này)
        email_vector = preprocess_email(email_data)
        
        # Chuẩn hóa dữ liệu
        scaler = StandardScaler()
        email_vector = scaler.fit_transform(email_vector)
        
        # Dự đoán
        prediction = model.predict(email_vector)
        
        # Hiển thị kết quả
        result = 'Spam' if prediction == 1 else 'Not Spam'
        
        return render_template('index.html', prediction=result)

def preprocess_email(email_text):
    # Placeholder cho việc tiền xử lý email thành vector đặc trưng
    email_vector = np.array([0])  # Thay thế bằng mã thực tế
    return email_vector.reshape(1, -1)

if __name__ == '__main__':
    app.run(debug=True)