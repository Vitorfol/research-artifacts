import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox

class BoxplotNavigator:
    def __init__(self, df, start_index=3):
        self.df = df
        self.index = start_index
        
        self.fig, self.ax = plt.subplots(figsize=(4, 3.5), dpi=150)
        plt.subplots_adjust(bottom=0.3)
        
        axprev = plt.axes([0.6, 0.05, 0.15, 0.075])
        axnext = plt.axes([0.76, 0.05, 0.15, 0.075])
        
        self.btn_prev = Button(axprev, 'Anterior')
        self.btn_next = Button(axnext, 'Próximo')
        
        self.btn_prev.on_clicked(self.prev_plot)
        self.btn_next.on_clicked(self.next_plot)
        
        axtext = plt.axes([0.2, 0.05, 0.2, 0.075])
        self.text_box = TextBox(axtext, 'Índice', initial=str(self.index))
        axok = plt.axes([0.42, 0.05, 0.1, 0.075])
        self.btn_ok = Button(axok, 'OK')
        self.btn_ok.on_clicked(self.go_to_index)
        
        self.box_plot()
        plt.show()
    
    def box_plot(self):
        """
        Gera um boxplot para a coluna atual do DataFrame.
        """
        self.ax.clear()  
        self.df[self.df.columns[self.index]].plot.box(ax=self.ax)  
        self.ax.set_title(f'Boxplot de {self.df.columns[self.index]}')
        self.fig.canvas.draw()  
    
    def next_plot(self, event):
        if self.index < len(self.df.columns) - 1:
            self.index += 1
            self.text_box.set_val(str(self.index))  
            self.box_plot()

    def prev_plot(self, event):
        if self.index > 0:
            self.index -= 1
            self.text_box.set_val(str(self.index))  
            self.box_plot()
    
    def go_to_index(self, event):
        try:
            new_index = int(self.text_box.text)
            if 0 <= new_index < len(self.df.columns):
                self.index = new_index
                self.box_plot()
            else:
                print("Índice fora do intervalo.")
        except ValueError:
            print("Por favor, insira um número válido.")