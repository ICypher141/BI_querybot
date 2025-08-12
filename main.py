import sys
import os
import pandas as pd
from scripts.dax_generator import generate_dax
from scripts.m_generator import generate_m

def detect_file_type(file_path):
    if file_path.lower().endswith(".csv"):
        return "csv"
    elif file_path.lower().endswith(".json"):
        return "json"
    else:
        raise ValueError("Only CSV and JSON files are supported.")

def load_dataset(file_path):
    file_type = detect_file_type(file_path)
    if file_type == "csv":
        return pd.read_csv(file_path)
    elif file_type == "json":
        return pd.read_json(file_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        sys.exit(1)

    df = load_dataset(file_path)

    print("\nGenerating DAX formulas...")
    dax_code = generate_dax(df, file_path)
    with open("output_dax.txt", "w", encoding="utf-8") as f:
        f.write(dax_code)
    print("✅ DAX formulas saved to output_dax.txt")

    print("\nGenerating M scripts...")
    m_code = generate_m(file_path)
    with open("output_m.txt", "w", encoding="utf-8") as f:
        f.write(m_code)
    print("✅ M scripts saved to output_m.txt")
