import os
import google.generativeai as genai
from dotenv import load_dotenv

# Carrega a chave do .env
load_dotenv()
api_key = os.getenv("API_KEY")

# Configura a API
genai.configure(api_key=api_key)

# Lista os modelos disponíveis
models = genai.list_models()

print("📦 Modelos disponíveis:")
for model in models:
    print(f"- {model.name}")
