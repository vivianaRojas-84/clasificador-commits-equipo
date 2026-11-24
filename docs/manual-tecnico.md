# MANUAL TÉCNICO
## Clasificador de Commits con Inteligencia Artificial

### 1. Descripción general

El proyecto consiste en desarrollar un sistema que permite clasificar mensajes de commits utilizando dos motores: ECO, basado en reglas, y Ollama, que utiliza inteligencia artificial.

El backend fue desarrollado con FastAPI y utiliza PostgreSQL para almacenar las clasificaciones realizadas.

### 2. Arquitectura del sistema

El sistema está compuesto por los siguientes elementos:

- Cliente: permite enviar mensajes de commits mediante Swagger o solicitudes HTTP.
- API FastAPI: recibe las solicitudes y coordina el proceso de clasificación.
- Motor ECO: clasifica los mensajes mediante reglas y palabras clave.
- Motor Ollama: utiliza el modelo qwen2.5:0.5b.
- Base de datos PostgreSQL: almacena las inferencias realizadas.

### 3. Endpoints de la API

- GET /health: verifica el estado de la API y la conexión con la base de datos.
- POST /clasificar: recibe un mensaje de commit y devuelve su clasificación.
- GET /inferencias: consulta el historial de clasificaciones almacenadas.

### 4. Tecnologías utilizadas

- Python 3.12.
- FastAPI.
- Uvicorn.
- PostgreSQL 16.
- Docker.
- Ollama.
- Modelo qwen2.5:0.5b.
- psycopg2-binary.
- python-dotenv.
- Requests.

### 5. Configuración y seguridad

Las variables de configuración y las credenciales se almacenan en el archivo .env.

Este archivo está excluido del repositorio mediante .gitignore para evitar publicar información confidencial.

El proyecto utiliza PostgreSQL para almacenar los resultados de las clasificaciones.

### 6. Puesta en marcha del proyecto

1. Abrir Ubuntu y ubicarse en la carpeta del proyecto.
2. Iniciar PostgreSQL si está detenido:

   docker start db-ia

3. Activar el entorno virtual:

   source .venv/bin/activate

4. Para utilizar Ollama, verificar que esté ejecutándose. Si no está iniciado, abrir otra terminal y ejecutar:

   ollama serve

5. Iniciar FastAPI:

   uvicorn app.main:app --reload

6. Abrir Swagger en el navegador:

   http://127.0.0.1:8000/docs

### 7. Pruebas realizadas

**Prueba 1. Estado de la API**

- Endpoint: GET /health.
- Resultado: HTTP 200.
- Estado: ok.
- Base de datos: ok.

**Prueba 2. Motor ECO**

- Mensaje: fea: agregar inicio de sesion.
- Motor: eco.
- Modelo: reglas.
- Categoría: feat.
- Latencia: 0 ms.
- Resultado: clasificación exitosa.

**Prueba 3. Motor Ollama**

- Mensaje: feat: agregar inicio de reportes.
- Motor: ollama.
- Modelo: qwen2.5:0.5b.
- Categoría: feat.
- Latencia: 3334 ms.
- Resultado: HTTP 200.

**Prueba 4. Consulta de inferencias**

- Endpoint: GET /inferencias.
- Resultado: HTTP 200.
- Se verificó el almacenamiento de las clasificaciones en PostgreSQL.
- Registro ID 16 correspondiente a la prueba de Ollama.

### 8. Conclusión

El proyecto cuenta con un backend funcional que permite clasificar mensajes de commits mediante un motor basado en reglas y otro de inteligencia artificial.

Además, utiliza PostgreSQL para guardar el historial de inferencias y permite consultar los resultados mediante los endpoints de FastAPI.

Las pruebas realizadas permitieron comprobar el funcionamiento de la API, la conexión con la base de datos y la clasificación mediante ambos motores.
