import matplotlib.pyplot as plt
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_processing.trateData import calculate_kurtosis, calculate_skewness
from matplotlib.widgets import Button, TextBox

class HistogramNavigator:
    def __init__(self, df, start_index=3):
        self.df = df
        self.index = start_index

        self.kurtosis_series = calculate_kurtosis(df)
        self.skewness_series = calculate_skewness(df)

        self.fig, self.ax = plt.subplots(figsize=(8, 4), dpi=150)
        plt.subplots_adjust(bottom=0.3, right=0.75)  # Ajusta espaço para o texto ao lado

        # Botões
        axprev = plt.axes([0.6, 0.05, 0.15, 0.075])
        axnext = plt.axes([0.76, 0.05, 0.15, 0.075])
        self.btn_prev = Button(axprev, 'Anterior')
        self.btn_next = Button(axnext, 'Próximo')

        self.btn_prev.on_clicked(self.prev_plot)
        self.btn_next.on_clicked(self.next_plot)

        # Caixa de texto para índice
        axtext = plt.axes([0.2, 0.05, 0.2, 0.075])
        self.text_box = TextBox(axtext, 'Índice', initial=str(self.index))
        axok = plt.axes([0.42, 0.05, 0.1, 0.075])
        self.btn_ok = Button(axok, 'OK')
        self.btn_ok.on_clicked(self.go_to_index)

        self.plot_histogram()
        plt.show()

    def plot_histogram(self):
        """Plota o histograma da coluna atual e exibe os valores de curtose e assimetria."""
        self.ax.clear()

        col_name = self.df.columns[self.index]
        data = self.df[col_name].dropna()  # Removendo valores NaN para evitar problemas no histograma
        kurt_value = self.kurtosis_series.get(col_name, 0)
        skew_value = self.skewness_series.get(col_name, 0)

        # Plota o histograma da distribuição da coluna
        self.ax.hist(data, bins=20, color='blue', alpha=0.7, edgecolor='black')
        self.ax.set_title(f'{col_name}')
        self.ax.set_xlabel('Valores')
        self.ax.set_ylabel('Frequência')

        # Exibir os valores ao lado
        text_x = self.ax.get_xlim()[1] * 1.05  # Ajusta posição para ficar ao lado
        text_y = self.ax.get_ylim()[1] * 0.8
        self.ax.text(text_x, text_y, f'Curtose: {kurt_value:.3f}\nAssimetria: {skew_value:.3f}', 
                     fontsize=10, bbox=dict(facecolor='white', alpha=0.6))

        self.fig.canvas.draw()

    def next_plot(self, event):
        """Avança para a próxima coluna do DataFrame."""
        if self.index < len(self.df.columns) - 1:
            self.index += 1
            self.text_box.set_val(str(self.index))
            self.plot_histogram()

    def prev_plot(self, event):
        """Volta para a coluna anterior do DataFrame."""
        if self.index > 0:
            self.index -= 1
            self.text_box.set_val(str(self.index))
            self.plot_histogram()

    def go_to_index(self, event):
        """Permite selecionar um índice específico digitando na caixa de texto."""
        try:
            new_index = int(self.text_box.text)
            if 0 <= new_index < len(self.df.columns):
                self.index = new_index
                self.plot_histogram()
            else:
                print("Índice fora do intervalo.")
        except ValueError:
            print("Por favor, insira um número válido.")
