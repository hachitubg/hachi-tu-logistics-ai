# Hachi Tu Logistics AI Assistant

Ứng dụng chatbot AI chuyên về Logistics và Chuỗi cung ứng, được xây dựng bằng Python và Google Generative AI.

## Tính năng

- Chat với AI về các vấn đề logistics
- Hỗ trợ các chủ đề:
  - Vận chuyển và Phân phối
  - Quản lý Kho bãi
  - Quản lý Chuỗi cung ứng
  - Quy trình và Tiêu chuẩn Logistics
  - Hệ thống CELLO của Samsung
- Giao diện web thân thiện với người dùng
- Hỗ trợ định dạng Markdown trong tin nhắn
- Lưu trữ lịch sử chat

## Cài đặt

1. Clone repository:
```bash
git clone https://github.com/yourusername/hachi-tu-logistics-ai.git
cd hachi-tu-logistics-ai
```

2. Tạo môi trường ảo và kích hoạt:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

4. Tạo file `.env` và thêm API key của Google:
```
GOOGLE_API_KEY=your_api_key_here
```

## Chạy ứng dụng

```bash
python app.py
```

Truy cập http://localhost:5000 để sử dụng ứng dụng.

## Công nghệ sử dụng

- Python
- Flask
- Google Generative AI
- HTML/CSS/JavaScript
- Markdown-it

## License

MIT License 