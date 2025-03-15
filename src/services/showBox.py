import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from plot_navigator.boxPlot import BoxplotNavigator

def show_box(df_path, start_index=3):
    BoxplotNavigator(df_path, start_index)
