import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

instrucoes = "Responda sempre de forma empática, em português do Brasil, como se fosse uma amiga que entende de tecnologia. Nunca use inglês. Use emojis e linguagem informal."

chat = model.start_chat(history=[
    {
        "role": "user",
        "parts": [{"text": instrucoes}]
    }
])

tarefas = []
metas = []

print("🤖 Olá! Sou sua assistente digital! Digite 'sair' para encerrar.\n")

while True:
    entrada = input("Você: ").strip()

    if entrada.lower() in ["sair", "exit", "tchau"]:
        print("Assistente: Até logo, poderosa! 💖✨")
        break

    # Detecta comandos da assistente
    comando = entrada.lower()
    if comando.startswith("adicionar tarefa"):
        try:
            partes = entrada.replace("adicionar tarefa:", "").strip().split(" às ")
            descricao = partes[0].strip().capitalize()
            horario = partes[1].strip()
            tarefas.append({"descricao": descricao, "horario": horario})
            print(f"Assistente: Anotado, miga! 📝 '{descricao}' às {horario} foi adicionado com sucesso!")
        except:
            print("Assistente: Eita, não entendi direitinho 😅 Tenta assim: 'Adicionar tarefa: lavar roupa às 10h'")

    elif comando in ["mostrar tarefas", "ver tarefas"]:
        if tarefas:
            print("Assistente: Olha só o que tem na sua listinha hoje 📋✨")
            for i, t in enumerate(tarefas, 1):
                print(f"{i}. {t['descricao']} às {t['horario']}")
        else:
            print("Assistente: Nenhuma tarefa ainda! Quer adicionar uma? 😄")

    elif comando.startswith("definir meta") or comando.startswith("criar meta"):
        try:
            meta = entrada.replace("definir meta:", "").replace("criar meta:", "").strip().capitalize()
            metas.append(meta)
            print(f"Assistente: Meta criada com sucesso! 💪 '{meta}' vai ser moleza pra você!")
        except:
            print("Assistente: Não consegui entender direito a meta 😅 Tenta assim: 'Definir meta: aprender Git até sexta'")

    elif comando in ["ver metas", "mostrar metas"]:
        if metas:
            print("Assistente: Suas metas brilhantes da semana 💡💖")
            for i, m in enumerate(metas, 1):
                print(f"{i}. {m}")
        else:
            print("Assistente: Nenhuma meta ainda! Vamos sonhar alto juntas? 🎯")

    else:
        # Se não for comando, pergunta pro GeminiBot
        try:
            print("GeminiBot está pensando... 🤔")
            resposta = chat.send_message(entrada)
            print(f"GeminiBot: {resposta.text}\n")
        except Exception as e:
            print(f"⚠️ Ocorreu um erro: {e}\n")
