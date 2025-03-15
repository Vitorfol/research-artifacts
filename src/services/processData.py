import sys
import os

# Adiciona o diretório src ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data_processing.csvReader import load_csv_as_df
from data_processing.trateData import convert_comma_and_percent_columns, convert_df_columns_to_float

def process_csv_path(file_path):
    original_csv_df = load_csv_as_df(file_path)
    temp_csv_df = convert_comma_and_percent_columns(original_csv_df)
    final_csv_df = convert_df_columns_to_float(temp_csv_df)
    return final_csv_df
