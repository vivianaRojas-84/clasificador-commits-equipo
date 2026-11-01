# INFORME TÉCNICO – ENTORNO DE DESARROLLO IA

## 1. Información del entorno

- Sistema operativo: Ubuntu 24.04 LTS.
- Entorno de ejecución: WSL2.
- Perfil de hardware: A.
- Memoria RAM asignada a WSL: 7.8 GiB.
- Espacio disponible en disco: 951 GB.

## 2. Modelo de inteligencia artificial

- Modelo instalado: qwen2.5-coder:1.5b.
- Herramienta de ejecución: Ollama.
- Versión de Ollama: 0.40.11.
- Tamaño del modelo: 986 MB.

## 3. Mediciones de rendimiento

### Tiempos de respuesta

| Ejecución | Tiempo |
|---|---:|
| 1 | 4957 ms |
| 2 | 209 ms |
| 3 | 206 ms |
| 4 | 230 ms |
| 5 | 202 ms |
| **Promedio** | **1161 ms** |

La primera ejecución presentó un tiempo mayor debido a la carga inicial del modelo. Las siguientes respuestas fueron considerablemente más rápidas.

### Consumo de memoria

- Memoria total asignada: 7.8 GiB.
- Memoria disponible durante la prueba: 6.2 GiB.
- Uso de swap: 0 B.

Nota: estos datos corresponden al consumo general de Ubuntu durante la prueba, no exclusivamente al modelo.

## 4. Evaluación de calidad

- Calificación: 4/5.

El modelo ofrece respuestas claras, comprende las instrucciones y proporciona ejemplos útiles. Sin embargo, algunas respuestas pueden necesitar revisión para asegurar que la información sea completamente correcta.

## 5. Conclusiones

La instalación y configuración del entorno de inteligencia artificial se realizó correctamente. Docker, Docker Compose, Git, Python y Ollama funcionan adecuadamente. El modelo Qwen2.5-Coder:1.5b pudo ejecutarse y responder tanto desde la terminal como mediante la API REST.
