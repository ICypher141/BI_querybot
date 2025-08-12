import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from langchain_community.chat_models import ChatOllama

import os

def generate_m(file_path):
    llm = ChatOllama(model="llama3.2", temperature=0)

    abs_path = os.path.abspath(file_path)
    prompt = f"""
You are a Power Query M language expert.
Write an M script to load the dataset from the following path:
{abs_path}

Ensure the M script includes:
- Correct file loading (Csv.Document or Json.Document)
- Promoting headers
- Basic type detection

Return ONLY valid M code without any explanation or markdown.
    """

    response = llm.invoke(prompt)
    return response.content.strip()
