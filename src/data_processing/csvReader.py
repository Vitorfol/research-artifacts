import pandas as pd

def load_csv_as_df(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"Arquivo {file_path} carregado com sucesso!")
        return df
    except Exception as e:
        print(f"Erro ao carregar CSV: {e}")
        return None

