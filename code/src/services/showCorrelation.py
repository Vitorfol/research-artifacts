import sys
import os
import inspect

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from data_processing.trateData import find_correlations
from plot_navigator.scatterPlot import ScatterPlotNavigator
from services.util import print_purple

def show_correlation(df_path, threshold=None):
    if threshold is None:
        threshold = inspect.signature(find_correlations).parameters['threshold'].default

    correlations = find_correlations(df_path, threshold=threshold)
    for index, (col1, col2, correlation, relation) in correlations.items():
        print_purple(f"{index}: {col1} e {col2} têm uma correlação {relation} de {correlation:.2f}")
    
    ScatterPlotNavigator(df_path, correlations)

def show_correlation_between_files(df_path1, df_path2, threshold=None):
    if threshold is None:
        threshold = inspect.signature(find_correlations).parameters['threshold'].default

    correlations1 = find_correlations(df_path1, threshold=threshold)
    correlations2 = find_correlations(df_path2, threshold=threshold)   

    correlated_pairs1 = {(col1, col2) for _, (col1, col2, _, _) in correlations1.items()}
    correlated_pairs2 = {(col1, col2) for _, (col1, col2, _, _) in correlations2.items()}    

    common_pairs = correlated_pairs1.intersection(correlated_pairs2)
    print_purple("\nPares de colunas com correlação em ambos os arquivos:")
    for index, (col1, col2) in enumerate(common_pairs, start=1):
        corr1 = next(corr for _, (c1, c2, corr, _) in correlations1.items() if (c1, c2) == (col1, col2))
        corr2 = next(corr for _, (c1, c2, corr, _) in correlations2.items() if (c1, c2) == (col1, col2))

        print_purple(f"{index}. {col1} e {col2}: Correlação no primeiro arquivo = {corr1:.2f}, no segundo arquivo = {corr2:.2f}")

