import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from plot_navigator.histogramPlot import HistogramNavigator

def show_histogram(df_path, start_index=3):
    HistogramNavigator(df_path, start_index)
    