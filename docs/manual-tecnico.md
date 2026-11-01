# Manual técnico

## Clasificador de Commits con Inteligencia Artificial

### 1. Descripción general

El proyecto consiste en desarrollar un sistema para clasificar mensajes de commits utilizando dos motores: un motor basado en reglas llamado ECO y un motor de inteligencia artificial mediante Ollama.

El backend fue desarrollado con FastAPI y utiliza PostgreSQL para almacenar las clasificaciones realizadas.

### 2. Arquitectura del sistema

El sistema está compuesto por los siguientes elementos:

* **Cliente:** permite enviar los mensajes de commits mediante Swagger o solicitudes HTTP.
* **API FastAPI:** recibe las solicitudes y coordina el proceso de clasificación.
* **Motor ECO:** clasifica los mensajes mediante reglas y palabras clave.
* **Motor Ollama:** utiliza el modelo qwen2.5:0.5b para clasificar los mensajes mediante inteligencia artificial.
* **Base de datos PostgreSQL:** almacena las inferencias realizadas, incluyendo el mensaje, la categoría, el motor utilizado y el tiempo de respuesta.

### 3. Diagrama de arquitectura

```text
              CLIENTE
           (Swagger / HTTP)
                  |
                  v
           API FASTAPI
           Puerto 8000
                  |
          +-------+-------+
          |               |
          v               v
      MOTOR ECO       MOTOR OLLAMA
      (Reglas)        (qwen2.5:0.5b)
                          |
                          v
                    API Ollama
                    Puerto 11434
          |
          v
      POSTGRESQL
      Puerto 5432
          |
          v
       TABLA
     inferencias
```

### 4. Endpoints disponibles

| Método | Endpoint     | Descripción                               |
| ------ | ------------ | ----------------------------------------- |
| GET    | /health      | Verifica el funcionamiento de la API.     |
| POST   | /clasificar  | Clasifica un mensaje de commit.           |
| GET    | /inferencias | Consulta las clasificaciones almacenadas. |

### 5. Tecnologías utilizadas

* Python 3.12.
* FastAPI.
* Uvicorn.
* PostgreSQL 16.
* Docker.
* Ollama.
* Modelo qwen2.5:0.5b.
* psycopg2-binary.
* python-dotenv.
* Requests.

### 6. Seguridad del sistema

El proyecto implementa las siguientes medidas de seguridad:

* Las credenciales de conexión a PostgreSQL se almacenan en el archivo `.env`.
* El archivo `.env` está excluido de Git mediante `.gitignore`.
* Se creó un usuario de aplicación llamado `app_ia` con permisos limitados.
* El usuario de aplicación tiene permisos de conexión, consulta e inserción en la tabla de inferencias.
* Las dependencias de Python están registradas en `requirements.txt`.
* Se utiliza Docker para ejecutar PostgreSQL en un contenedor independiente.

### 7. Pruebas realizadas

Se realizaron pruebas para verificar el funcionamiento de los dos motores de clasificación.

**Prueba con el motor ECO:**

* Entrada: `docs: completar descripcion del proyecto`.
* Resultado: `docs`.
* Motor: `eco`.

**Prueba con Ollama:**

* Entrada: `feat: agregar modulo de usuarios`.
* Resultado: `feat`.
* Modelo: `qwen2.5:0.5b`.
* Tiempo de respuesta: 3188 ms.

Las pruebas confirmaron que las clasificaciones se almacenan correctamente en PostgreSQL.

### 8. Conclusión

Se logró implementar un backend funcional que permite clasificar mensajes de commits mediante reglas e inteligencia artificial. Además, se integró PostgreSQL para conservar el historial de inferencias y se establecieron medidas básicas para proteger las credenciales y controlar los permisos de acceso a la base de datos.
