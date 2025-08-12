from scripts.parser import load_data

if __name__ == "__main__":
    file_path = input("Enter CSV or JSON file path: ")
    df = load_data(file_path)
    print("Data Loaded Successfully!")
    print(df.head())
