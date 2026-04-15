import matplotlib.pyplot as plt
from matplotlib.widgets import Button

class Dashboard:

    def __init__(self, hist_nsga, hist_hibrido, frente):
        self.hist_nsga = hist_nsga
        self.hist_hibrido = hist_hibrido
        self.frente = frente

        self.fig, self.ax = plt.subplots()
        plt.subplots_adjust(bottom=0.3)

        # Botones
        ax_btn1 = plt.axes([0.1, 0.05, 0.25, 0.1])
        ax_btn2 = plt.axes([0.4, 0.05, 0.25, 0.1])
        ax_btn3 = plt.axes([0.7, 0.05, 0.25, 0.1])

        self.btn1 = Button(ax_btn1, 'Convergencia')
        self.btn2 = Button(ax_btn2, 'Comparación')
        self.btn3 = Button(ax_btn3, 'Pareto')

        self.btn1.on_clicked(self.mostrar_convergencia)
        self.btn2.on_clicked(self.mostrar_comparacion)
        self.btn3.on_clicked(self.mostrar_pareto)

        self.mostrar_convergencia(None)

        plt.show()

    def limpiar(self):
        self.ax.clear()

    def mostrar_convergencia(self, event):
        self.limpiar()
        self.ax.plot(self.hist_hibrido)
        self.ax.set_title("Convergencia Híbrido")
        self.ax.set_xlabel("Iteraciones")
        self.ax.set_ylabel("Fitness")
        self.fig.canvas.draw()

    def mostrar_comparacion(self, event):
        self.limpiar()
        self.ax.plot(self.hist_nsga, label="NSGA-II")
        self.ax.plot(self.hist_hibrido, label="Híbrido")
        self.ax.set_title("Comparación de Convergencia")
        self.ax.legend()
        self.fig.canvas.draw()

    def mostrar_pareto(self, event):
        self.limpiar()
        x = [f[0] for f in self.frente]
        y = [f[1] for f in self.frente]
        self.ax.scatter(x, y)
        self.ax.set_title("Frente de Pareto")
        self.ax.set_xlabel("Distancia")
        self.ax.set_ylabel("Costo")
        self.fig.canvas.draw()