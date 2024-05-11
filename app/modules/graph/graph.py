import matplotlib.pyplot as plt
import numpy as np
import os

class Graph:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    def generate_graph_legend(self):
        if self.a == 0 and self.b == 0 and self.c == 0:
            return "y = 0", "primeiro"
        if self.a == 0 and self.b == 0:
            return f"y = {self.c}", "primeiro"
        if self.a == 0 and self.c == 0:
            return f"y = {self.b}x", "primeiro"
        if self.b == 0 and self.c == 0:
            return f"y = {self.a}x²", "segundo"
        if self.a == 0:
            return f"y = {self.b}x + {self.c}", "primeiro"
        if self.b == 0:
            return f"y = {self.a}x² + {self.c}", "segundo"
        if self.c == 0:
            return f"y = {self.a}x² + {self.b}x", "segundo"
        return f"y = {self.a}x² + {self.b}x + {self.c}" , "segundo"

    def generate_graph(self):
        x = np.linspace(-10, 10, 400)
        
        # Calcula os valores correspondentes para o eixo y usando a função quadrática
        y = self.a * x**2 + self.b * x + self.c

        legend, degree = self.generate_graph_legend()
        # apaga o arquivo se existir
        if os.path.isfile(f'grafico_funcao_{degree}_grau.png'):
            os.remove(f'grafico_funcao_{degree}_grau.png')
            
        # Cria o gráfico
        plt.figure()
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Graph of the function: {legend}')
        plt.grid(True)
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)
        plt.savefig(f'grafico_funcao_{degree}_grau.png')

        return legend, degree