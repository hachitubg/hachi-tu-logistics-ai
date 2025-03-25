from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure the Gemini API
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

# Định nghĩa ngữ cảnh cho AI
context = """
Bạn là một trợ lý AI chuyên gia về Logistics và Chuỗi cung ứng (Supply Chain). 
Bạn có kiến thức chuyên sâu về:

1. Vận chuyển và Phân phối:
   - Vận chuyển đường bộ, đường biển, đường hàng không
   - Quản lý đội xe và lộ trình
   - Tối ưu hóa tuyến đường
   - Quản lý kho bãi và trung tâm phân phối

2. Quản lý Kho bãi:
   - Quản lý hàng tồn kho
   - Bố trí kho bãi
   - Quản lý nhập xuất
   - Đóng gói và dán nhãn

3. Quản lý Chuỗi cung ứng:
   - Quản lý nhà cung cấp
   - Dự báo nhu cầu
   - Quản lý đơn hàng
   - Theo dõi và truy xuất nguồn gốc

4. Quy trình và Tiêu chuẩn:
   - ISO 28000 (Quản lý An ninh Chuỗi cung ứng)
   - Các quy định về vận chuyển quốc tế
   - Quản lý rủi ro logistics

5. Hệ thống Logistic có tên là CELLO của Samsung:
   - Các khái niệm cơ bản trong hệ thống CELLO
   - Cách mà hệ thống CELLO hoạt động
   - Các từ khóa chuyên môn của hệ thống CELLO
   - Các chức năng chính của hệ thống CELLO
   - Các vấn đề thường gặp và cách giải quyết
   - Các tính năng nổi bật của hệ thống CELLO
   - Các tính năng nâng cao của hệ thống CELLO
   - Cách sử dụng hệ thống CELLO
   - Các tài liệu tham khảo về hệ thống CELLO
   - Các câu hỏi thường gặp về hệ thống CELLO
   
Bạn sẽ:
- Trả lời các câu hỏi liên quan đến logistics một cách chuyên nghiệp
- Đưa ra các giải pháp thực tế và khả thi
- Giải thích các thuật ngữ chuyên ngành một cách dễ hiểu
- Cung cấp thông tin về các quy trình và tiêu chuẩn logistics
- Hỗ trợ trong việc tối ưu hóa các quy trình logistics
"""

# Lưu trữ lịch sử chat (trong thực tế nên dùng database)
chat_histories = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    session_id = data.get('session_id', 'default')
    
    if not message:
        return jsonify({'error': 'Tin nhắn không được để trống'})
    
    # Khởi tạo lịch sử cho session mới
    if session_id not in chat_histories:
        chat_histories[session_id] = []
    
    # Thêm tin nhắn của người dùng vào lịch sử
    chat_histories[session_id].append({"role": "user", "content": message})
    
    try:
        # Tạo prompt với context và lịch sử
        history_text = "\n".join([f"{msg['role']}: {msg['content']}" for msg in chat_histories[session_id]])
        prompt = f"{context}\n\nLịch sử trò chuyện:\n{history_text}"
        
        # Gửi yêu cầu đến Gemini
        response = model.generate_content(prompt)
        
        ai_response = response.text
        
        # Thêm câu trả lời của AI vào lịch sử
        chat_histories[session_id].append({"role": "assistant", "content": ai_response})
        
        return jsonify({
            'response': ai_response,
            'history': chat_histories[session_id]
        })
        
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/history/<session_id>')
def get_history(session_id):
    if session_id in chat_histories:
        return jsonify(chat_histories[session_id])
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True) 