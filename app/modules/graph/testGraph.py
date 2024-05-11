import unittest
from modules.graph.graph import Graph
import os


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph(0, 0, 0)

    def testGenerateFirstDegreeGraph(self):
        self.graph = Graph(0, 7, 5)
        legend, degree = self.graph.generate_graph_legend()
        # apaga o arquivo se existir
        if os.path.isfile(f'grafico_funcao_{degree}_grau.png'):
            os.remove(f'grafico_funcao_{degree}_grau.png')
        # gera o grafico
        legend, degree = self.graph.generate_graph()
        # verifica se o arquivo foi criado
        self.assertTrue(os.path.isfile(f'grafico_funcao_{degree}_grau.png'))

    def testGenerateSecondDegreeGraph(self):
        self.graph = Graph(2, 3, 8)
        legend, degree = self.graph.generate_graph_legend()
        # apaga o arquivo se existir
        if os.path.isfile(f'grafico_funcao_{degree}_grau.png'):
            os.remove(f'grafico_funcao_{degree}_grau.png')
        # gera o grafico
        legend, degree = self.graph.generate_graph()
        # verifica se o arquivo foi criado
        self.assertTrue(os.path.isfile(f'grafico_funcao_{degree}_grau.png'))

    def testLegendZero(self):
        self.graph = Graph(0, 0, 0)
        legend, degree = self.graph.generate_graph_legend()
        self.assertEqual(legend, 'y = 0')

    def testLegendFirstDegree(self):
        self.graph = Graph(0, 7, 5)
        legend, degree = self.graph.generate_graph_legend()
        self.assertEqual(degree, "primeiro")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Graph('testGenerateFirstDegreeGraph'))
    suite.addTest(Graph('testGenerateSecondDegreeGraph'))
    suite.addTest(Graph('testLegendZero'))
    suite.addTest(Graph('testLegendFirstDegree'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())