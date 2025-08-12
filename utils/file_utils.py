import pandas as pd
import json
from pathlib import Path

def load_csv(file_path: str) -> str:
    """Load CSV file and return its first few rows as a string for LLM context."""
    df = pd.read_csv(file_path)
    # Limit size for prompt efficiency
    return df.head(10).to_csv(index=False)

def load_json(file_path: str) -> dict:
    """Load JSON file and return dict."""
    path = Path(file_path)
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    raise FileNotFoundError(f"{file_path} not found")
