import matplotlib.pyplot as plt
import numpy as np
import os

class Graph:
    def __init__(self, a=0, b=0, c=0, trigonometric="sin"):
        self.a = a
        self.b = b
        self.c = c
        self.trigonometric = trigonometric

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
            return f"y = {self.b}x + ({self.c})", "primeiro"
        if self.b == 0:
            return f"y = {self.a}x² + ({self.c})", "segundo"
        if self.c == 0:
            return f"y = {self.a}x² + ({self.b}x)", "segundo"
        return f"y = {self.a}x² + ({self.b}x) + ({self.c})" , "segundo"

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

    def generate_trigonometric_graph(self):

        intervalo = (-2*np.pi, 2*np.pi)
        pontos = 1000
        # Define o intervalo para o eixo x
        x = np.linspace(intervalo[0], intervalo[1], pontos)
        
        # Calcula os valores correspondentes para as funções seno, cosseno e tangente
        seno = np.sin(x)
        cosseno = np.cos(x)
        tangente = np.tan(x)
        # apaga o arquivo se existir
        if os.path.isfile(f'grafico_funcao_{self.trigonometric}.png'):
            os.remove(f'grafico_funcao_{self.trigonometric}.png')
        
        # Cria o gráfico
        plt.figure(figsize=(10, 6))
        if self.trigonometric == 'sin':
            plt.plot(x, seno, label='Seno', color='blue')
        elif self.trigonometric == 'cos':
            plt.plot(x, cosseno, label='Cosseno', color='red')
        elif self.trigonometric == 'tan':
            plt.plot(x, tangente, label='Tangente', color='green')
        else:
            raise ValueError("O tipo de trigonometria informado não é reconhecido. Por favor, informe 'sin', 'cos' ou 'tan'.")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Graph of the {self.trigonometric} trigonometric function')
        plt.legend()
        plt.grid(True)
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)
        plt.savefig(f'grafico_funcao_{self.trigonometric}.png')

