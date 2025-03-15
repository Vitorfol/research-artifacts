import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from plot_navigator.boxPlot import BoxplotNavigator
# from processData import process_csv_path

def show_box(df_path, start_index=3):
    BoxplotNavigator(df_path, start_index)

# original_robo = 'C:/Users/necta/Downloads/robo.csv'
# final_robo = process_csv_path(original_robo)
# show_box(final_robo)
