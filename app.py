from langchain_community.llms import Ollama

# Load model
llm = Ollama(model="llama3.2")

# Simple conversation
question = "Explain LangChain in one sentence."
answer = llm.invoke(question)

print(f"Q: {question}")
print(f"A: {answer}")
# ollama_test.py