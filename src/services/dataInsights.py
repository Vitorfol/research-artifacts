import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data_processing.trateData import calculate_medians_df, series_median_comparator, calculate_kurtosis, calculate_skewness

def show_median_comparator(df1, df2):
    medians_df1 = calculate_medians_df(df1)
    medians_df2 = calculate_medians_df(df2)
    
    result = series_median_comparator(medians_df1, medians_df2)
    
    if result is None:
        print("Os DataFrames possuem tamanhos diferentes.")
    else:
        print("Medians of df1 higher than medians of df2:")
        print(result[0])
        print("\nMedians of df2 higher than medians of df1:")
        print(result[1])
        print("\nMedians of df1 equals to medians of df2:")
        print(result[2])

def show_kurtosis_and_skewness(df1, df2):

    kurtosis_df1 = calculate_kurtosis(df1)
    skewness_df1 = calculate_skewness(df1)
    kurtosis_df2 = calculate_kurtosis(df2)
    skewness_df2 = calculate_skewness(df2)

    kurtosis= pd.DataFrame({
        "df1": kurtosis_df1,
        "df2": kurtosis_df2
    })

    skewness = pd.DataFrame({
        "df1": skewness_df1,
        "df2": skewness_df2
    })

    print("Kurtosis:")
    print(kurtosis)
    print("\nSkewness:")
    print(skewness)

def df_describe_and_info(df):
    df.info()
    print("\n")
    for i in df.columns[3:]:
        print(df[i].describe().round(2))
        print("\n")

