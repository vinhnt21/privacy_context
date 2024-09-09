from langchain_cohere import CohereEmbeddings, ChatCohere
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()
embeddings = CohereEmbeddings(
    model="embed-english-v3.0"
)
llm = ChatCohere(
    model="command-r-plus",
    temperature=0,
    max_tokens=None,
    timeout=None,
)

local_llm = ChatOllama(
    model="llama3.1",
    temperature=0.7,  # Giảm một chút để đảm bảo câu trả lời chính xác hơn
    num_predict=256,  # Giữ nguyên để tạo câu trả lời đủ dài
    top_p=0.9,  # Đảm bảo câu trả lời đa dạng nhưng không quá ngẫu nhiên
    top_k=50,  # Giới hạn số lượng từ xem xét để tăng độ kiểm soát
    repetition_penalty=1.2,  # Tránh lặp lại câu trả lời
    use_gpu=True,  # Sử dụng GPU nếu có để tăng tốc độ
)


import spacy
# Load a pre-trained NER model (e.g., en_core_web_sm)
nlp = spacy.load('en_core_web_sm')