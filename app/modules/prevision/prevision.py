import requests
from googletrans import Translator
import os


translator = Translator()

tempo_api_key = os.getenv('TEMPO_API_KEY', "")

class Prevision:
    def __init__(self, city_id: str):
        self.city_id = city_id

    def prevision(self):
    # Construa o URL da API com sua chave e a cidade desejada
        url = f'https://api.openweathermap.org/data/2.5/weather?id={self.city_id}&appid={tempo_api_key}&units=metric'
        print(url)
        # Faça a requisição à API
        res = requests.get(url)

        # Verifique se a requisição foi bem-sucedida
        if res.status_code == 200:
            # Converta a resposta em JSON
            dados = res.json()
                
            # Extraia as informações desejadas
            description = dados['weather'][0]['description']
            temperature = dados['main']['temp']
            # description_pt = translator.translate(description, dest='pt', src='en').text
            
            
            print(f'Condição: {description}, Temperatura: {temperature}ºC')
            return (f'Condition: {description}, Temperature: {temperature}ºC')
        else:
            print(f'\n Não foi possível obter a previsão do tempo.\n')
            return (f'\n Não foi possível obter a previsão do tempo.\n')
      