# SLQAlchemy template

Template con los archivos principales para conectarse a la base de datos y unos ejemplos de modelos de datos

## Estructura del Proyecto

Este proyecto utiliza SQLAlchemy para modelar datos y está estructurado de la siguiente manera:

- `main.py`: Contiene métodos de ejemplo para la carga de bases de datos.
- `applications/`
  - `settings.py`: Script con configuraciones necesarias para la conexión a la base de datos.
- `infrastructure/`
  - `db/`
    - `conexion.py`: Clase para conectarse a la base de datos.
    - `models/`
      - `usuario.py`: Modelo de datos para usuarios.
      - `venta.py`: Modelo de datos para ventas.
      - `base_model.py`: Modelo base para SQLAlchemy.
- `requirements.txt`: Dependencias necesarias para ejecutar el proyecto.

## Instalación

Para instalar este proyecto, sigue estos pasos:

1. Clona este repositorio.
2. Instala las dependencias ejecutando `pip install -r requirements.txt`.

## Configuración

Configura la conexión a tu base de datos editando el archivo `settings.py` en la carpeta `applications`.

## Uso

Para usar este proyecto:

0. Instalar Postgres [https://www.postgresql.org/download/windows/]
1. inicializa Postgres
2. Instalar DBeaver o DataGrip para administrar las bases de datos
3. Ejecuta `main.py` para ver los ejemplos de carga de datos.
4. Utiliza los modelos en `infrastructure/db/models` para interactuar con tu base de datos.

## Contribuir

Agreguemos features relevantes

## Firma

Equipo de datos de Rurall Latam.
