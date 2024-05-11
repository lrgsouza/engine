import matplotlib.pyplot as plt
import numpy as np
import os

class Graph:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    def generate_first_degree_graph(self):

        x = np.linspace(-10, 10, 400)
        y = self.a*x + self.b

        plt.figure()
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.title(f'Graph of y = {self.a}x + {self.b}')
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)
        plt.savefig('grafico_funcao.png')

    def generate_second_degree_graph(self):
        x = np.linspace(-10, 10, 400)
        
        # Calcula os valores correspondentes para o eixo y usando a função quadrática
        y = self.a * x**2 + self.b * x + self.c
        
        # Cria o gráfico
        plt.plot(x, y, label=f'{self.a}x^2 + {self.b}x + {self.c}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Gráfico da função de segundo grau: y = {self.a}x² + {self.b}x + {self.c}')
        plt.grid(True)
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)
        plt.savefig('grafico_funcao_segundo_grau.png')