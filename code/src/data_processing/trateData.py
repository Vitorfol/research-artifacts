import pandas as pd
import matplotlib.pyplot as plt

def convert_comma_and_percent_columns(df):
    """
    Converte colunas com valores percentuais no formato 'x,y%' para números decimais.

    Parâmetros:
    - df: DataFrame do Pandas contendo os dados.

    Retorno:
    - DataFrame com as colunas devidamente convertidas.
    """ 
    for col in df.columns:
        if df[col].dtype == object:
            df[col] = df[col].str.replace(',', '.', regex=True)  
            if df[col].str.contains('%').any():
                try:
                    df[col] = df[col].str.replace('%', '', regex=True)  
                    df[col] = df[col].astype(float) / 100  
                except ValueError:
                    pass  
    return df

def find_correlations(df, threshold=0.69, start_index=3):
    """
    Encontra pares de colunas que possuem correlação forte (positiva ou negativa).
    
    Parâmetros:
    - df: DataFrame do Pandas contendo os dados.
    - threshold: Valor mínimo absoluto da correlação para considerar como relação forte.
    - start_index: Índice a partir do qual as colunas serão consideradas.
    
    Retorno:
    - Um dicionário indexado onde cada chave representa um par de colunas altamente correlacionadas.
    """
    # Seleciona as colunas a partir do índice start_index
    df = df.iloc[:, start_index:]
    
    correlation_matrix = df.corr()  # Calcula a matriz de correlação
    pairs = []  # Lista para armazenar as colunas correlacionadas
    seen_pairs = set()  # Conjunto para armazenar pares já vistos

    for col1 in df.columns:  # Percorre todas as colunas
        for col2 in df.columns:
            if col1 != col2 and (col2, col1) not in seen_pairs:  # Evita a correlação de uma coluna com ela mesma e duplicações
                correlation = correlation_matrix.loc[col1, col2]  # Obtém a correlação entre col1 e col2
                
                # Se a correlação for maior que o threshold ou menor que -threshold, adiciona à lista
                if correlation > threshold or correlation < -threshold:
                    relation = "direta" if correlation > 0 else "inversa"
                    pairs.append((col1, col2, correlation, relation))
            seen_pairs.add((col1, col2))  # Marca o par como visto
            seen_pairs.add((col2, col1))  # Marca o par como visto

    # Retorna um dicionário onde a chave é um índice e o valor é um par de colunas correlacionadas
    return {i+1: pair for i, pair in enumerate(pairs)}

def convert_df_columns_to_float(df, column_indices=[16,17]):
    """
    Converte colunas específicas do DataFrame para valores numéricos.

    Parâmetros:
    - df: DataFrame do Pandas contendo os dados.
    - column_indices: Lista de índices das colunas a serem convertidas.
    """
    for column_index in column_indices:
        df[df.columns[column_index]] = pd.to_numeric(df[df.columns[column_index]], errors='coerce')
    return df

def calculate_medians_df(df):
    medians = df.iloc[:, 3:].median()
    return medians

def series_median_comparator(series1, series2):
    if series1.shape[0] != series2.shape[0]:
        return None
    
    series1_higher_medians = pd.DataFrame({
        'series1': series1[series1 > series2].round(5),
        'series2': series2[series1 > series2].round(5),
        'difference': (series1[series1 > series2] - series2[series1 > series2]).round(5),
        'series2/series1': (series2[series1 > series2] / series1[series1 > series2]).round(2)
    }).sort_values(by='difference', ascending=False)
    
    series2_higher_medians = pd.DataFrame({
        'series1': series1[series2 > series1].round(5),
        'series2': series2[series2 > series1].round(5),
        'difference': (series2[series2 > series1] - series1[series2 > series1]).round(5),
        'series1/series2': (series1[series2 > series1] / series2[series2 > series1]).round(2)
    }).sort_values(by='difference', ascending=False)
    
    series1_equals_series2 = pd.DataFrame({
        'series1': series1[series1 == series2].round(5),
        'series2': series2[series1 == series2].round(5),
        'difference': (series1[series1 == series2] - series2[series1 == series2]).round(5)
    }).sort_values(by='difference', ascending=False)

    return [series1_higher_medians, series2_higher_medians, series1_equals_series2] 

def calculate_kurtosis(df):
    kurtosis = df.iloc[:, 3:].kurtosis().sort_values(ascending=False)
    return kurtosis

def calculate_skewness(df):
    skewness = df.iloc[:, 3:].skew().sort_values(ascending=False)
    return skewness