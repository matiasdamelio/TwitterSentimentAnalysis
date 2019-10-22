# Twitter Sentiment Analysis [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![PyPI status](https://img.shields.io/pypi/status/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE) [![GitHub release](https://img.shields.io/github/release/Naereen/StrapDown.js.svg)](https://GitHub.com/Naereen/StrapDown.js/releases/)

Enlace de referencia [Twitter Sentiment Python-Docker-Elasticsearch-Kibana](https://realpython.com/twitter-sentiment-python-docker-elasticsearch-kibana/)

## Prerequisites

### Docker Environment

1. Crear directorio del proyecto
2. Copiar el archivo **_Dockerfile_**
3. Construir la imagen:
```
docker pull nshou/elasticsearch-kibana
```
4. Correr el contenedor:
```
docker run -d -p 9200:9200 -p 5601:5601 nshou/elasticsearch-kibana
```
5. Acceder a Elasticsearch y Kibana:
```
http://localhost:9200 (Elasticsearch)
http://localhost:5601 (Kibana)
```

### Twitter Streaming API

Para acceder al servicio de **Streaming API de Twitter**, es necesario registrar una aplicación en [Twitter Apps](http://apps.twitter.com).
Una vez creada la app, crear un archivo *config.py* con el siguiente formato:
```
consumer_key = "consumer_key"
consumer_secret = "consumer_secret"
access_token = "access_token"
access_token_secret = "access_token_secret"
```

### Packages

Instalar librerias:
```
pip install --requirement requirements.txt
```

### Tracking Keywords

En *sentiment.py* modificar en la linea 62 las palabras claves a buscar.

## Run

Correr primero el *listener* de streaming tweets:
```
python sentiment.py
```

En Kibana importar el archivo **dashboard_twitter.json** desde Management -> Saved Objects -> Import

## Task List

- [x] Armar Dashboard
- [ ] Modificar tabla de Tweets para ordenar ascendentemente por fecha
- [ ] Modificar el criterio de categorias de sentiment
