import unittest as unittest
from unittest.mock import AsyncMock
from main import _latex, generate_graph, send_graph

class TestBotCommands(unittest.TestCase):
    # Testa se a função _latex é executada corretamente
    def test_latex_command(self):
        ctx_mock = AsyncMock()  # Mock do contexto Discord
        ctx_mock.defer.return_value = None  # Configura o retorno do método defer
        
        # Testa se a função _latex não levanta exceção
        try:
            _latex(ctx_mock)
        except Exception as e:
            self.fail(f"_latex raised exception: {e}")
        
        # Testa se a função send_graph é chamada
        send_graph.assert_called_once_with(ctx_mock)

    # Testa se a função generate_graph gera uma imagem
    def test_generate_graph(self):
        try:
            generate_graph()  # Gera o gráfico
        except Exception as e:
            self.fail(f"generate_graph raised exception: {e}")

    # Testa se a função send_graph envia uma imagem
    def test_send_graph(self):
        ctx_mock = AsyncMock()  # Mock do contexto Discord
        ctx_mock.send.return_value = None  # Configura o retorno do método send
        
        # Testa se a função send_graph não levanta exceção
        try:
            send_graph(ctx_mock)  # Envia a imagem
        except Exception as e:
            self.fail(f"send_graph raised exception: {e}")

if __name__ == '__main__':
    unittest.main()
