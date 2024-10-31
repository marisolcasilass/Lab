#!/bin/bash
# Construir la imagen de Docker
docker build -t flask-api .

# Ejecutar el contenedor en el puerto 5000
docker run -p 5000:5000 flask-api
