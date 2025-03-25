# Hachi Tu Logistics AI Assistant

Ứng dụng chatbot AI chuyên gia về Logistics và Chuỗi cung ứng, sử dụng Google Gemini AI.

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
git clone https://github.com/hachitubg/hachi-tu-logistics-ai.git
cd hachi-tu-logistics-ai
```

2. Tạo môi trường ảo và kích hoạt:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Cài đặt dependencies:
```bash
pip install -r requirements.txt
```

4. Tạo file `.env` và thêm API key:
```
GOOGLE_API_KEY=your_api_key_here
```

## Chạy ứng dụng

```bash
python app.py
```

Ứng dụng sẽ chạy tại `http://localhost:5000`

## Deployment trên Render.com

1. Push code lên GitHub repository
2. Tạo Web Service mới trên Render.com
3. Connect với GitHub repository
4. Thêm biến môi trường `GOOGLE_API_KEY` trong cài đặt của service
5. Deploy!

## Công nghệ sử dụng

- Python 3.9
- Flask
- Google Gemini AI
- Gunicorn (cho production)

## License

MIT License 