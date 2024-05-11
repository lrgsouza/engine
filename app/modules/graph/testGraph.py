import unittest
from modules.graph.graph import Graph
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

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Graph('testGenerateFirstDegreeGraph'))
    suite.addTest(Graph('testGenerateSecondDegreeGraph'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())