import unittest
from modules.graph.graph import Graph
import os
import xmlrunner

class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph(0, 0, 0,'sin')

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

    def testTrigonometricSinGraph(self):
        self.graph = Graph(0,0,0,"sin")
        self.graph.generate_trigonometric_graph()
        self.assertTrue(os.path.isfile(f'grafico_funcao_{self.graph.trigonometric}.png'))
    
    def testTrigonometricCosGraph(self):
        self.graph = Graph(0,0,0,"cos")
        self.graph.generate_trigonometric_graph()
        self.assertTrue(os.path.isfile(f'grafico_funcao_{self.graph.trigonometric}.png'))

    def testTrigonometricTanGraph(self):
        self.graph = Graph(0,0,0,"tan")
        self.graph.generate_trigonometric_graph()
        self.assertTrue(os.path.isfile(f'grafico_funcao_{self.graph.trigonometric}.png'))

    def testTrigonometricInvalidGraph(self):
        self.graph = Graph(0,0,0,"invalid")
        with self.assertRaises(ValueError):
            self.graph.generate_trigonometric_graph()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Graph('testGenerateFirstDegreeGraph'))
    suite.addTest(Graph('testGenerateSecondDegreeGraph'))
    suite.addTest(Graph('testLegendZero'))
    suite.addTest(Graph('testLegendFirstDegree'))
    suite.addTest(Graph('testTrigonometricSinGraph'))
    suite.addTest(Graph('testTrigonometricCosGraph'))
    suite.addTest(Graph('testTrigonometricTanGraph'))
    suite.addTest(Graph('testTrigonometricInvalidGraph'))
    return suite

if __name__ == '__main__':
    # Ensure the directory exists
    output_dir = 'test-reports'
    os.makedirs(output_dir, exist_ok=True)
    
    # Run the tests
    runner = xmlrunner.XMLTestRunner(output=output_dir)
    runner.run(suite())