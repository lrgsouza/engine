import unittest
from graph import Graph
import os


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph(3, 7, 5)

    def testGenerateFirstDegreeGraph(self):
        # apaga o arquivo se existir
        if os.path.isfile('grafico_funcao.png'):
            os.remove('grafico_funcao.png')
        # gera o grafico
        self.graph.generate_first_degree_graph()
        # verifica se o arquivo foi criado
        self.assertTrue(os.path.isfile('grafico_funcao.png'))

    def testGenerateSecondDegreeGraph(self):
        # apaga o arquivo se existir
        if os.path.isfile('grafico_funcao_segundo_grau.png'):
            os.remove('grafico_funcao_segundo_grau.png')
        # gera o grafico
        self.graph.generate_second_degree_graph()
        # verifica se o arquivo foi criado
        self.assertTrue(os.path.isfile('grafico_funcao_segundo_grau.png'))