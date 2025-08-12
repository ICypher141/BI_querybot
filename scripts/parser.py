from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser

class PowerBIOutput(BaseModel):
    dax_query: str = Field(description="DAX query for Power BI")
    chart_spec: dict = Field(description="Chart specification in JSON format")
    m_language: str = Field(description="M language code for Power BI transformation")

def get_powerbi_parser():
    """Return a LangChain PydanticOutputParser for PowerBIOutput."""
    return PydanticOutputParser(pydantic_object=PowerBIOutput)
