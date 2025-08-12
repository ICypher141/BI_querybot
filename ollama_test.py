from langchain_community.chat_models import ChatOllama

def test_ollama():
    llm = ChatOllama(model="llama3.2")
    response = llm.invoke("Hello! Can you confirm you are working?")
    print(response.content)

if __name__ == "__main__":
    test_ollama()
