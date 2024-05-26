import requests
from googletrans import Translator

translator = Translator()

# Substitua 'sua_chave_api_aqui' pela chave de API que você obteve do OpenWeather
API_KEY = '47252a9b54a83e7bf4da95c7505c5d02'
# city_id = '3449847' #Cidade de Santa Rita

def prevision(city_id):
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
  else:
      print(f'\n Não foi possível obter a previsão do tempo.\n')