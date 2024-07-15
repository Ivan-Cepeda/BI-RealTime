#importa librerias
from confluent_kafka import Producer
import requests
import json
import datetime

#cryptos para seguir y analizar.
cryptos_to_track = ['bitcoin', 'ethereum', 'ripple', 'litecoin', 'cardano', 'polkadot', 'stellar', 'eos', 'tron', 'dogecoin']
fecha_hora_actual = datetime.datetime.now()
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
        #Verificar la estructura de la respuesta
        if 'data' in data and isinstance(data['data'], list):

            #Crear una lista de diccionarios con la información que deseamos extraer. 
            rows = [{'date': fecha_hora_actual, 'name': crypto['name'], 'symbol': crypto['symbol'], 'price': crypto['priceUsd']} for crypto in data['data'] if crypto['id'] in cryptos_to_track]

            #Enviar los datos extraidos a Kafka
            for row in rows:
                producer.produce(topic_name, value=json.dumps(row))
            
            #Asegurarnos que se está enviando toda la info
            producer.flush()

            print("Datos enviados exitosamente a Kafka")

        else:
            print('La estructura de la respuesta no es la esperada')

    else:
        print(f"Error al realizar la solicitud a la API. Código de estado: {response.status_code}")

    #controlar el tiempo en el que se realizan solicitudes a la API. 
    time.sleep(30)