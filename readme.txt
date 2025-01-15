# Inventario API

Esta es una API para gestionar un inventario de productos. La API permite consultar, agregar y actualizar productos en el inventario.

## Requisitos

- Python 3.x
- Flask

## Instalación

1. Clona este repositorio en tu máquina local.
2. Navega al directorio del proyecto.


Instala las dependencias necesarias.
pip install flask

Ejecución de la API
Para ejecutar la API, sigue estos pasos:

Asegúrate de estar en el directorio del proyecto.
Ejecuta el archivo app.py.

python app.py

La API estará disponible en http://127.0.0.1:5000.

Endpoints
Consultar un producto
URL: /producto/<id_producto>
Método: GET
Descripción: Consulta un producto por su ID.
Respuesta exitosa: 200 OK
Respuesta de error: 404 Not Found o 400 Bad Request
Agregar un producto
URL: /producto
Método: POST
Descripción: Agrega un nuevo producto al inventario.
Cuerpo de la solicitud:


{
  "nombre": "Nombre del producto",
  "cantidad": 100
}

Respuesta exitosa: 200 OK
Respuesta de error: 400 Bad Request

Actualizar el stock de un producto
URL: /producto/<id_producto>
Método: PUT
Descripción: Actualiza la cantidad de un producto existente.
Cuerpo de la solicitud:

{
  "nueva_cantidad": 150
}

Respuesta exitosa: 200 OK
Respuesta de error: 404 Not Found o 400 Bad Request
Ejecución de pruebas
Para ejecutar las pruebas unitarias, utiliza el siguiente comando:

python -m unittest discover

Esto ejecutará todas las pruebas definidas en los archivos testInventario.py y testAPI.py.

Autor
Alejandro Alvarez


