import requests

def chat_with_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "llama3.2",  # Change to any model you have
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print(response.json().get("response", "No response"))
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    chat_with_ollama("Hello from Ollama + LangChain setup!")
