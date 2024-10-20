# API de Scraping Corona Chile

Este proyecto es una API desarrollada con Django que realiza web scraping en la página de ropa Corona de Chile. La API proporciona un pequeño CRUD para mostrar los productos obtenidos, incluyendo una sección de favoritos y todos los productos disponibles.

## Requisitos previos

- Python 3.x
- pip (gestor de paquetes de Python)

## Instalación

1. Clona este repositorio en tu máquina local:
   ```
   git clone <URL_DEL_REPOSITORIO>
   ```

2. Navega al directorio del proyecto:
   ```
   cd <NOMBRE_DEL_DIRECTORIO>
   ```

3. Crea un entorno virtual (opcional, pero recomendado):
   ```
   python -m venv venv
   ```

4. Activa el entorno virtual:
   - En Windows:
     ```
     venv\Scripts\activate
     ```
   - En macOS y Linux:
     ```
     source venv/bin/activate
     ```

5. Instala las dependencias del proyecto utilizando el archivo `requirements.txt`:
   ```
   pip install -r requirements.txt
   ```

## Ejecución del proyecto

Para ejecutar el servidor de desarrollo de Django, utiliza el siguiente comando:

```
python manage.py runserver
```

El servidor se iniciará en `http://127.0.0.1:8000/`.
Puedes acceder a la API con `http://127.0.0.1:8000/api/corona/`.
