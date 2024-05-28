import requests
from googletrans import Translator


translator = Translator()

API_KEY = ''

def prevision(city_id: str):
# Construa o URL da API com sua chave e a cidade desejada
    url = f'https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={API_KEY}&units=metric'

    # Faça a requisição à API
    res = requests.get(url)

    # Verifique se a requisição foi bem-sucedida
    if res.status_code == 200:
        # Converta a resposta em JSON
        dados = res.json()
            
        # Extraia as informações desejadas
        description = dados['weather'][0]['description']
        temperature = dados['main']['temp']
        description_pt = translator.translate(description, dest='pt', src='en').text
        
        
        print(f'Condição: {description_pt}, Temperatura: {temperature}ºC')
        return (f'Condição: {description_pt}, Temperatura: {temperature}ºC')
    else:
        print(f'\n Não foi possível obter a previsão do tempo.\n')
        return (res.status_code)
      