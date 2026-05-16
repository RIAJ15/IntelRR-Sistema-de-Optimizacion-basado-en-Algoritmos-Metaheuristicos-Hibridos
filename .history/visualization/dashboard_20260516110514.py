import matplotlib.pyplot as plt
from matplotlib.widgets import Button


class Dashboard:
    """
    Dashboard interactivo para visualizar resultados del proyecto.

    Parámetros:
        hist_nsga (list): Historial de convergencia de NSGA-II.
        hist_hibrido (list): Historial de convergencia del modelo híbrido.
        frente (list): Soluciones del frente de Pareto.
        ciudades (list): Coordenadas de las ciudades.
    """

    def __init__(self, hist_nsga, hist_hibrido, frente, ciudades):
        self.hist_nsga = hist_nsga
        self.hist_hibrido = hist_hibrido
        self.frente = frente
        self.ciudades = ciudades

        # Figura principal
        self.fig, self.ax = plt.subplots()
        plt.subplots_adjust(bottom=0.3)

        # =========================
        # BOTONES
        # =========================
        ax_btn1 = plt.axes([0.05, 0.05, 0.18, 0.1])
        ax_btn2 = plt.axes([0.25, 0.05, 0.18, 0.1])
        ax_btn3 = plt.axes([0.45, 0.05, 0.18, 0.1])
        ax_btn4 = plt.axes([0.65, 0.05, 0.18, 0.1])

        self.btn1 = Button(ax_btn1, 'Convergencia')
        self.btn2 = Button(ax_btn2, 'Comparación')
        self.btn3 = Button(ax_btn3, 'Pareto')
        self.btn4 = Button(ax_btn4, 'Ruta')

        # Eventos
        self.btn1.on_clicked(self.mostrar_convergencia)
        self.btn2.on_clicked(self.mostrar_comparacion)
        self.btn3.on_clicked(self.mostrar_pareto)
        self.btn4.on_clicked(self.mostrar_ruta)

        # Vista inicial
        self.mostrar_convergencia(None)

        plt.show()

    def limpiar(self):
        """
        Limpia el área de dibujo actual.
        """
        self.ax.clear()

    def mostrar_convergencia(self, event):
        """
        Muestra la convergencia del modelo híbrido.
        """
        self.limpiar()

        self.ax.plot(self.hist_hibrido)
        self.ax.set_title("Convergencia del Modelo Híbrido")
        self.ax.set_xlabel("Iteraciones")
        self.ax.set_ylabel("Fitness")

        self.fig.canvas.draw()

    def mostrar_comparacion(self, event):
        """
        Compara convergencia entre NSGA-II y modelo híbrido.
        """
        self.limpiar()

        self.ax.plot(self.hist_nsga, label="NSGA-II")
        self.ax.plot(self.hist_hibrido, label="Híbrido")

        self.ax.set_title("Comparación de Convergencia")
        self.ax.set_xlabel("Iteraciones")
        self.ax.set_ylabel("Fitness")
        self.ax.legend()

        self.fig.canvas.draw()

    def mostrar_pareto(self, event):
        """
        Muestra el frente de Pareto.
        """
        self.limpiar()

        x = [f[0] for f in self.frente]
        y = [f[1] for f in self.frente]

        self.ax.scatter(x, y)

        for i, (xi, yi) in enumerate(zip(x, y)):
            self.ax.text(xi, yi, f"S{i}", fontsize=8)

        self.ax.set_title("Frente de Pareto")
        self.ax.set_xlabel("Distancia")
        self.ax.set_ylabel("Costo")

        self.fig.canvas.draw()

    def mostrar_ruta(self, event):
        """
        Muestra visualmente una ruta optimizada entre ciudades.
        """
        self.limpiar()

        ruta = self.frente[0]["ruta"]

        x = [self.ciudades[i][0] for i in ruta]
        y = [self.ciudades[i][1] for i in ruta]

        # cerrar ciclo
        x.append(x[0])
        y.append(y[0])

        self.ax.plot(x, y, marker='o')

        for i, (xi, yi) in enumerate(self.ciudades):
            self.ax.text(xi, yi, str(i))

        self.ax.set_title("Ruta Optimizada entre Ciudades")
        self.ax.set_xlabel("Coordenada X")
        self.ax.set_ylabel("Coordenada Y")

        self.fig.canvas.draw()