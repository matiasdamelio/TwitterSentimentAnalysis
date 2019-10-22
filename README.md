# Twitter Sentiment Analysis

Enlace de referencia [Twitter Sentiment Python-Docker-Elasticsearch-Kibana](https://realpython.com/twitter-sentiment-python-docker-elasticsearch-kibana/)

## Docker Environment

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


