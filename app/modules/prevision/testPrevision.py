import unittest
from unittest.mock import patch, Mock
from prevision import Prevision 

class TestPrevision(unittest.TestCase):
    @patch('prevision.requests.get')
    @patch('prevision.Translator.translate')
    def test_prevision_success(self, mock_translate, mock_get):
        # Mock da resposta da API do OpenWeatherMap
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'weather': [{'description': 'clear sky'}],
            'main': {'temp': 25}
        }
        mock_get.return_value = mock_response
        
        # Mock da resposta do Google Translate (se usado)
        mock_translate.return_value = Mock(text='céu limpo')

        # Instancia a classe Prevision e chama o método prevision
        previsao = Prevision(city_id="3449847")  
        result = previsao.prevision()

        # Verifica o resultado esperado
        expected_result = 'Condition: clear sky, Temperature: 25ºC'
        self.assertEqual(result, expected_result)

    @patch('prevision.requests.get')
    def test_prevision_failure(self, mock_get):
        # Mock de uma resposta de falha da API
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Instancia a classe Prevision e chama o método prevision
        previsao = Prevision(city_id="3449847")  
        result = previsao.prevision()

        # Verifica o resultado esperado
        expected_result = '\n Não foi possível obter a previsão do tempo.\n'
        self.assertEqual(result, expected_result)
    
    @patch('prevision.requests.get')
    def test_prevision_invalid_city(self, mock_get):
        # Mock de uma resposta indicando que a cidade é inválida
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.json.return_value = {
            'cod': '404',
            'message': 'city not found'
        }
        mock_get.return_value = mock_response

        # Instancia a classe Prevision e chama o método prevision
        previsao = Prevision(city_id="invalid_city") 
        result = previsao.prevision()

        # Verifica o resultado esperado
        expected_result = '\n Não foi possível obter a previsão do tempo.\n'
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
