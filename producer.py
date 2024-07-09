#importa librerias
from confluent_kafka import Producer
import requests
import json
import time

#cryptos para seguir y analizar.
cryptos_to_track = ['bitcoin', 'ethereum', 'ripple', 'litecoin', 'cardano', 'polkadot', 'stellar', 'eos', 'tron', 'dogecoin']

#URL de la API de coincap
api_url = 'https://api.coincap.io/v2/assets'

#configuración Kafka
producer_conf = {'bootstrap.servers':'localhost:9092'}
producer = Producer(producer_conf)
topic_name = 'cryptodata'

#Bucle para conectarse a la API, y traer los datos
while True:
    response = requests.get(api_url)
    #Verifca el estatus de la conexión para traer la data
    if response.status_code == 200:
        data = response.json()
    
    else:
        print(f"Error al realizar la solicitud a la API. Código de estado: {response.status_code}")

    #controlar el tiempo en el que se realizan solicitudes a la API. 
    time.sleep(30)