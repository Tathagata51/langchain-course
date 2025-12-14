from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

llm_gemini = ChatGoogleGenerativeAI(
    model="models/gemini-robotics-er-1.5-preview", temperature=0)

llm_groq = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0
)
