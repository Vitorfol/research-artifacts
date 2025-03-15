import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data_processing.trateData import calculate_medians_df, series_median_comparator, calculate_kurtosis, calculate_skewness
from services.util import print_purple

def show_median_comparator(df1, df2):
    medians_df1 = calculate_medians_df(df1)
    medians_df2 = calculate_medians_df(df2)
    
    result = series_median_comparator(medians_df1, medians_df2)
    
    if result is None:
        print_purple("Os DataFrames possuem tamanhos diferentes.")
    else:
        print_purple("Medians of df1 higher than medians of df2:")
        print_purple(result[0])
        print_purple("\nMedians of df2 higher than medians of df1:")
        print_purple(result[1])
        print_purple("\nMedians of df1 equals to medians of df2:")
        print_purple(result[2])

def show_kurtosis_and_skewness(df1, df2):

    kurtosis_df1 = calculate_kurtosis(df1)
    skewness_df1 = calculate_skewness(df1)
    kurtosis_df2 = calculate_kurtosis(df2)
    skewness_df2 = calculate_skewness(df2)

    kurtosis = pd.DataFrame({
        "df1": kurtosis_df1,
        "df2": kurtosis_df2
    })

    skewness = pd.DataFrame({
        "df1": skewness_df1,
        "df2": skewness_df2
    })

    print_purple("Kurtosis:")
    print_purple(kurtosis)
    print_purple("\nSkewness:")
    print_purple(skewness)

def df_describe_and_info(df):
    df.info()
    print_purple("\n")
    for i in df.columns[3:]:
        print_purple(df[i].describe().round(2))
        print_purple("\n")
