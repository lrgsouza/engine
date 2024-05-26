import requests
import unittest
from unittest.mock import patch
from googletrans import Translator
import prevision  # substitua 'prevision' pelo nome do seu arquivo de código

class TestPrevisaoDoTempo(unittest.TestCase):
  @patch('prevision.requests.get')
  @patch.object(Translator, 'translate')
  def test_prevision_sucesso(self, mock_translate, mock_get):
      # Configura a resposta mockada para requests.get
      mock_response = mock_get.return_value
      mock_response.status_code = 200
      mock_response.json.return_value = {
          'weather': [{'description': 'clear sky'}],
          'main': {'temp': 25}
      }

      # Configura a resposta mockada para Translator.translate
      mock_translate.return_value.text = 'céu claro'

      # Chame a função a ser testada
      resultado = prevision('fake_city_id')

      # Verifique se o resultado está correto
      self.assertEqual(resultado, 'Condição: céu claro, Temperatura: 25ºC')

  @patch('prevision.requests.get')
  def test_prevision_falha(self, mock_get):
      # Configura a resposta mockada para requests.get
      mock_response = mock_get.return_value
      mock_response.status_code = 404
      mock_response.text = 'City not found'

      # Chame a função a ser testada
      resultado = prevision('100000100000000000')

      # Verifique se o resultado está correto para a falha
      self.assertEqual(resultado, '\n Não foi possível obter a previsão do tempo.\n',)

if __name__ == '__main__':
    unittest.main()
