# BI-RealTime

Análisis de criptomonedas en tiempo real.

En este proyecto nos vamos a estar conectando a la API de [***coincap.io***](https://docs.coincap.io/), desde allí se tomarán los datos en tiempo real para ser procesados. 

Lo primero será tener instalado Kafka, en mi caso estoy trabajando con WSL. Para hacerlo, puedes seguir las instruciones de este [repositorio](https://github.com/Ivan-Cepeda/Kafka-Python/blob/main/install.sh). Una vez instaldo, se creo la carpeta del proyecto, y se inicializó kafka. 

En mi caso, he creado un archivo arranque_kafka.sh, que tiene las instrucciones de inicio con solo ejecutar el comando.

```shell
./arranque_kafka.sh
```
Una vez inicializado Kafka, se puede crear el topic dónde van a llegar nuestros datos. 

Creación del "topic": 
```shell
kafka-topics.sh --bootstrap-server localhost:9092 --topic cryptodata --create --partitions 3
```
Ahora bien, ahora corresponde crear el fichero dónde se va a configurar el Producer, con los datos de la API de coincap. 

Para ello vamos a crear 2 script, el de producer.py y el de consumer.py, una que extraerá los datos a traves de la API de coincap, y los enviará al topic creado. El de consumer, tomará los datos del topic y los cargará a un archivo csv. 

Para la visualización y análisis de los datos, se conecta el csv a Power Bi. 
