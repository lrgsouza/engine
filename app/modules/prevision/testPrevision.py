import unittest
from unittest.mock import patch, Mock
import requests
from prevision import prevision 

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
        
        # Mock da resposta do Google Translate
        mock_translate.return_value = Mock(text='céu limpo')

        # Chamada da função
        with patch('builtins.print') as mock_print:
            prevision(123456)  # Substitua 123456 por um ID de cidade válido de teste

            # Verifique se a tradução foi chamada corretamente
            mock_translate.assert_called_once_with('clear sky', dest='pt', src='en')
            
            # Verifique se a função print foi chamada com os valores esperados
            mock_print.assert_called_once_with('Condição: céu limpo, Temperatura: 25ºC')

    @patch('prevision.requests.get')
    def test_prevision_failure(self, mock_get):
        # Mock de uma resposta de falha da API
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Chamada da função
        with patch('builtins.print') as mock_print:
            prevision(123456)  # Substitua 123456 por um ID de cidade válido de teste

            # Verifique se a função print foi chamada com a mensagem de erro esperada
            mock_print.assert_called_once_with('\n Não foi possível obter a previsão do tempo.\n')

if __name__ == '__main__':
    unittest.main()
