from langchain_groq import ChatGroq
from dotenv import load_dotenv

class GroqLLM:
    def __init__(self):
        load_dotenv()

    def get_llm(self):
        try:
            llm = ChatGroq(model="llama-3.3-70b-versatile")
            return llm
        except Exception as e:
            return e
