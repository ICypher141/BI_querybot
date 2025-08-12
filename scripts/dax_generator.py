import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from langchain_community.chat_models import ChatOllama


def generate_dax(df, file_path):
    llm = ChatOllama(model="llama3.2", temperature=0)

    schema_info = "\n".join([f"{col}: {str(dtype)}" for col, dtype in zip(df.columns, df.dtypes)])
    prompt = f"""
You are a Power BI DAX expert.
Given a dataset located at '{file_path}' with the following schema:
{schema_info}

Generate multiple DAX measures and calculated columns that could be useful for reporting.
Return ONLY the DAX code without any explanations, formatting, or markdown.
    """

    response = llm.invoke(prompt)
    return response.content.strip()
