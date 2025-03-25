from google import genai

client = genai.Client(api_key="AIzaSyB9jyZloZl9J8y_RHrFLk0cFPdGlWsJqKo")

# Định nghĩa ngữ cảnh cho AI
context = """
Bạn là một trợ lý AI thân thiện và hữu ích. Bạn có thể giao tiếp bằng tiếng Việt và tiếng Anh.
Bạn nên trả lời ngắn gọn, rõ ràng và thân thiện.
"""

# Khởi tạo lịch sử chat
chat_history = []

def print_chat_history():
    print("\n=== Lịch sử trò chuyện ===")
    for i, (role, message) in enumerate(chat_history, 1):
        print(f"{i}. {role}: {message}")
    print("========================\n")

def chat():
    print("Chào mừng đến với Gemini Chat! (Gõ 'thoát' để kết thúc)")
    print("Gõ 'lịch sử' để xem lại lịch sử trò chuyện")
    
    while True:
        user_input = input("\nBạn: ").strip()
        
        if user_input.lower() == 'thoát':
            print("Tạm biệt!")
            break
        elif user_input.lower() == 'lịch sử':
            print_chat_history()
            continue
            
        # Thêm câu hỏi của người dùng vào lịch sử
        chat_history.append(("Người dùng", user_input))
        
        # Tạo prompt với context và lịch sử
        history_text = "\n".join([f"{role}: {message}" for role, message in chat_history])
        prompt = f"{context}\n\nLịch sử trò chuyện:\n{history_text}"
        
        try:
            # Gửi yêu cầu
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            
            # Thêm câu trả lời của AI vào lịch sử
            ai_response = response.text
            chat_history.append(("AI", ai_response))
            
            print(f"\nAI: {ai_response}")
            
        except Exception as e:
            print(f"\nLỗi: {str(e)}")

if __name__ == "__main__":
    chat()