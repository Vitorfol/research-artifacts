import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.widgets import Button

class ScatterPlotNavigator:
    def __init__(self, df, pair_dict):
        self.df = df
        self.pair_dict = pair_dict
        self.index = 1
        
        # Criar a figura e os eixos
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        plt.subplots_adjust(bottom=0.2)  # Ajusta espaço para os botões
        
        # Criar os botões
        axprev = plt.axes([0.7, 0.05, 0.1, 0.075])  # Botão Anterior
        axnext = plt.axes([0.81, 0.05, 0.1, 0.075])  # Botão Próximo
        
        self.btn_prev = Button(axprev, 'Anterior')
        self.btn_next = Button(axnext, 'Próximo')
        
        self.btn_prev.on_clicked(self.prev_plot)
        self.btn_next.on_clicked(self.next_plot)
        
        self.plot_scatter()
        plt.show()
    
    def plot_scatter(self):
        self.ax.clear()
        if self.index in self.pair_dict:
            col1, col2, correlation, relation = self.pair_dict[self.index]
            sns.scatterplot(x=self.df[col1], y=self.df[col2], ax=self.ax)
            self.ax.set_title(f"Índice {self.index}: {col1} & {col2} ({relation})\nCorrelação: {correlation:.2f}")
            self.ax.set_xlabel(col1)
            self.ax.set_ylabel(col2)
            self.fig.canvas.draw()
    
    def next_plot(self, event):
        if self.index < len(self.pair_dict):  # Ensure we don't exceed the available pairs
            self.index += 1
            self.plot_scatter()

    def prev_plot(self, event):
        if self.index > 1:  # Ensure we don't go below the first plot
            self.index -= 1
            self.plot_scatter() 