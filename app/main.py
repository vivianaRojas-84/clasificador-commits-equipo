import os
import time
import psycopg2
import requests

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

app = FastAPI(title="Clasificador de Commits con IA")

# Configuración de la base de datos
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD")
}

OLLAMA_URL = os.getenv("OLLAMA_URL")
MODELO_OLLAMA = os.getenv("MODELO_OLLAMA")
MOTOR_POR_DEFECTO = os.getenv("MOTOR_POR_DEFECTO", "eco")


# Modelo de entrada
class Commit(BaseModel):
    mensaje: str
    motor: str = "eco"


# Conexión a PostgreSQL
def obtener_conexion():
    return psycopg2.connect(**DB_CONFIG)


# Motor de clasificación por reglas
def clasificar_eco(mensaje):
    mensaje = mensaje.lower()

    reglas = {
        "docs": ["docs:", "documentación", "readme"],
        "test": ["test:", "tests:", "prueba"],
        "fix": ["fix:", "bug:", "corregir"],
        "feat": ["feat:", "feature:", "agregar"],
        "refactor": ["refactor:", "refactorización"]
    }

    for categoria, palabras in reglas.items():
        if any(palabra in mensaje for palabra in palabras):
            return categoria

    return "otros"


# Motor de clasificación con Ollama
def clasificar_ollama(mensaje):
    prompt = (
        "Clasifica este mensaje de commit en una sola categoría: "
        "feat, fix, docs, test, refactor, otros. "
        "Responde únicamente con la categoría.\n"
        f"Mensaje: {mensaje}"
    )

    respuesta = requests.post(
        OLLAMA_URL,
        json={
            "model": MODELO_OLLAMA,
            "prompt": prompt,
            "stream": False
        },
        timeout=60
    )

    respuesta.raise_for_status()

    return respuesta.json()["response"].strip().lower()


# Ruta principal de verificación
@app.get("/health")
def health():
    return {"estado": "API funcionando correctamente"}


# Ruta para clasificar commits
@app.post("/clasificar")
def clasificar(commit: Commit):
    inicio = time.time()

    motor = commit.motor or MOTOR_POR_DEFECTO

    try:
        if motor == "eco":
            salida = clasificar_eco(commit.mensaje)
            modelo = "reglas"
        elif motor == "ollama":
            salida = clasificar_ollama(commit.mensaje)
            modelo = MODELO_OLLAMA
        else:
            raise HTTPException(
                status_code=400,
                detail="Motor no válido. Use eco u ollama."
            )

        latencia = int((time.time() - inicio) * 1000)

        conexion = obtener_conexion()

        try:
            with conexion.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO inferencias
                    (motor, modelo, entrada, salida, latencia_ms)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (motor, modelo, commit.mensaje, salida, latencia)
                )
            conexion.commit()
        finally:
            conexion.close()

        return {
            "mensaje": commit.mensaje,
            "categoria": salida,
            "motor": motor,
            "modelo": modelo,
            "latencia_ms": latencia
        }

    except requests.RequestException as error:
        raise HTTPException(
            status_code=502,
            detail=f"Error al comunicarse con Ollama: {error}"
        )
    except psycopg2.Error as error:
        raise HTTPException(
            status_code=500,
            detail=f"Error en la base de datos: {error}"
        )


# Ruta para consultar las inferencias
@app.get("/inferencias")
def listar_inferencias():
    try:
        conexion = obtener_conexion()

        try:
            with conexion.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id, fecha, motor, modelo,
                           entrada, salida, latencia_ms
                    FROM inferencias
                    ORDER BY id DESC
                    """
                )

                columnas = [desc[0] for desc in cursor.description]
                resultados = [
                    dict(zip(columnas, fila))
                    for fila in cursor.fetchall()
                ]

            return resultados

        finally:
            conexion.close()

    except psycopg2.Error as error:
        raise HTTPException(
            status_code=500,
            detail=f"Error en la base de datos: {error}"
        )
