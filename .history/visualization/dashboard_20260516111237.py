import matplotlib.pyplot as plt
from matplotlib.widgets import Button


class Dashboard:
    def __init__(self, hist_nsga, hist_hibrido, frente, ciudades):
        self.hist_nsga = hist_nsga
        self.hist_hibrido = hist_hibrido
        self.frente = frente
        self.ciudades = ciudades

        self.fig, self.ax = plt.subplots(figsize=(10, 7))
        plt.subplots_adjust(bottom=0.25)

        # Botones
        ax_btn1 = plt.axes([0.05, 0.05, 0.18, 0.1])
        ax_btn2 = plt.axes([0.27, 0.05, 0.18, 0.1])
        ax_btn3 = plt.axes([0.49, 0.05, 0.18, 0.1])
        ax_btn4 = plt.axes([0.71, 0.05, 0.18, 0.1])

        self.btn1 = Button(ax_btn1, 'Convergencia')
        self.btn2 = Button(ax_btn2, 'Comparación')
        self.btn3 = Button(ax_btn3, 'Pareto')
        self.btn4 = Button(ax_btn4, 'Rutas')

        self.btn1.on_clicked(self.mostrar_convergencia)
        self.btn2.on_clicked(self.mostrar_comparacion)
        self.btn3.on_clicked(self.mostrar_pareto)
        self.btn4.on_clicked(self.mostrar_rutas)

        self.mostrar_convergencia(None)

        plt.show()

    def limpiar(self):
        self.ax.clear()

    def mostrar_convergencia(self, event):
        self.limpiar()

        self.ax.plot(self.hist_hibrido, linewidth=2)
        self.ax.set_title("Convergencia del Modelo Híbrido")
        self.ax.set_xlabel("Iteraciones")
        self.ax.set_ylabel("Fitness")
        self.ax.grid(True)

        self.fig.canvas.draw()

    def mostrar_comparacion(self, event):
        self.limpiar()

        self.ax.plot(self.hist_nsga, label="NSGA-II", linewidth=2)
        self.ax.plot(self.hist_hibrido, label="Híbrido", linewidth=2)

        self.ax.set_title("Comparación de Convergencia")
        self.ax.set_xlabel("Iteraciones")
        self.ax.set_ylabel("Fitness")
        self.ax.legend()
        self.ax.grid(True)

        self.fig.canvas.draw()

    def mostrar_pareto(self, event):
        """
        Pareto corregido.
        """
        self.limpiar()

        if not self.frente:
            return

        x = [sol["fitness"][0] for sol in self.frente]
        y = [sol["fitness"][1] for sol in self.frente]

        self.ax.scatter(x, y, s=100)

        for i, (xi, yi) in enumerate(zip(x, y)):
            self.ax.text(xi, yi, f"S{i}", fontsize=8)

        self.ax.set_title("Frente de Pareto")
        self.ax.set_xlabel("Distancia")
        self.ax.set_ylabel("Costo")
        self.ax.grid(True)

        self.fig.canvas.draw()

    def ruta_ortogonal(self, ruta):
        """
        Convierte una ruta en trazos tipo calles (horizontal + vertical).
        """
        xs = []
        ys = []

        for i in range(len(ruta) - 1):
            x1, y1 = self.ciudades[ruta[i]]
            x2, y2 = self.ciudades[ruta[i + 1]]

            xs.extend([x1, x2, x2])
            ys.extend([y1, y1, y2])

        return xs, ys

    def mostrar_rutas(self, event):
        """
        Muestra múltiples rutas y resalta la mejor.
        """
        self.limpiar()

        # dibujar ciudades
        x_ciudades = [c[0] for c in self.ciudades]
        y_ciudades = [c[1] for c in self.ciudades]

        self.ax.scatter(x_ciudades, y_ciudades, s=120)

        for i, (x, y) in enumerate(self.ciudades):
            self.ax.text(x, y, str(i), fontsize=9)

        # rutas candidatas
        for sol in self.frente[:5]:
            xs, ys = self.ruta_ortogonal(sol["ruta"])
            self.ax.plot(xs, ys, alpha=0.3)

        # mejor solución
        mejor = min(self.frente, key=lambda s: sum(s["fitness"]))
        xs, ys = self.ruta_ortogonal(mejor["ruta"])

        self.ax.plot(xs, ys, linewidth=3, label="Mejor ruta")

        self.ax.set_title("Rutas Candidatas y Mejor Solución")
        self.ax.legend()
        self.ax.grid(True)

        self.fig.canvas.draw()