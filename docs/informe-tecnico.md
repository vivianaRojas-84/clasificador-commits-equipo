<<<<<<< HEAD
# INFORME TÉCNICO – ENTORNO DE DESARROLLO IA

# INFORME TÉCNICO – CARACTERIZACIÓN DEL ENTORNO Y MODELOS LOCALES

## 1. Información del entorno

- Sistema operativo: Ubuntu 24.04 LTS.
- Entorno de ejecución: WSL2.
- Perfil de hardware: A.
- Memoria RAM asignada a WSL: 7.8 GiB.
- Espacio disponible en disco: 951 GB.
- Procesador utilizado: CPU.

## 2. Herramientas de inteligencia artificial

- Herramienta de ejecución: Ollama.
- Versión de Ollama: 0.40.11.

### Modelo qwen2.5-coder:1.5b

- Tamaño del modelo instalado: 986 MB.

### Modelo qwen2.5:0.5b

- Tamaño del modelo instalado: 397 MB.
- Tamaño reportado durante la ejecución: 486 MB.
- Contexto: 4096.

## 3. Mediciones de rendimiento

### Modelo qwen2.5-coder:1.5b

| Ejecución | Tiempo |
|---|---:|
| 1 | 4957 ms |
| 2 | 209 ms |
| 3 | 206 ms |
| 4 | 230 ms |
| 5 | 202 ms |
| **Promedio** | **1161 ms** |

La primera ejecución presentó un tiempo mayor debido a la carga inicial del modelo. Las siguientes respuestas fueron considerablemente más rápidas.

### Modelo qwen2.5:0.5b

| Ejecución | Respuesta del modelo | Tiempo |
|---|---|---:|
| 1 | Clases | 0.324 s |
| 2 | Desarrollo, Entorno, Documentación | 0.543 s |
| 3 | Desarrollo | 0.194 s |
| 4 | git commit: completar descripcion del proyecto | 0.377 s |
| 5 | Git | 0.306 s |
| **Promedio** | | **0.349 s** |

## 4. Consumo de memoria

### Modelo qwen2.5-coder:1.5b

- Memoria total asignada: 7.8 GiB.
- Memoria disponible durante la prueba: 6.2 GiB.
- Uso de swap: 0 B.

Nota: estos datos corresponden al consumo general de Ubuntu durante la prueba, no exclusivamente al modelo.

### Modelo qwen2.5:0.5b

- Memoria reportada por Ollama: 486 MB.
- Procesador: 100% CPU.
- Contexto: 4096.

## 5. Evaluación de calidad

### Modelo qwen2.5-coder:1.5b

- Calificación: 4/5.

El modelo ofrece respuestas claras, comprende las instrucciones y proporciona ejemplos útiles. Sin embargo, algunas respuestas pueden necesitar revisión para asegurar que la información sea completamente correcta.

### Modelo qwen2.5:0.5b

- Calificación: 3/5.

El modelo presenta un tiempo de respuesta rápido y puede generar resultados relacionados con el mensaje de commit. Sin embargo, sus respuestas no siempre corresponden exactamente a la categoría esperada, por lo que su desempeño se considera regular.

## 6. Conclusiones

La instalación y configuración del entorno de inteligencia artificial se realizó correctamente. Docker, Docker Compose, Git, Python y Ollama funcionan adecuadamente.

Se probaron los modelos qwen2.5-coder:1.5b y qwen2.5:0.5b. Ambos pudieron ejecutarse y responder. Las pruebas permitieron observar diferencias en sus tiempos de respuesta y en la calidad de sus resultados.## 1. Información del entorno

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
=======
# Informe técnico: Caracterización del modelo local

## 1. Perfil de hardware
- Sistema operativo: Ubuntu en WSL2.
- Memoria RAM total: 7.4 GiB.
- Procesador utilizado: CPU.

## 2. Modelo utilizado
- Nombre del modelo: qwen2.5:0.5b.
- Tamaño del modelo instalado: 397 MB.
- Tamaño reportado durante la ejecución: 486 MB.
- Contexto: 4096.

## 3. Pruebas de inferencia

| Ejecución | Respuesta del modelo | Tiempo real |
|---|---|---:|
| 1 | Clases | 0.324 s |
| 2 | Desarrollo, Entorno, Documentación | 0.543 s |
| 3 | Desarrollo | 0.194 s |
| 4 | git commit: completar descripcion del proyecto | 0.377 s |
| 5 | Git | 0.306 s |

### Tiempo promedio
El tiempo promedio de las cinco ejecuciones fue de 0.349 segundos.

## 4. Memoria durante la inferencia
- Memoria reportada por Ollama: 486 MB.
- Procesador: 100% CPU.
- Contexto: 4096.

## 5. Calidad percibida
- Calificación: 3/5.
- Justificación: El modelo presenta un tiempo de respuesta rápido y puede generar resultados relacionados con el mensaje de commit. Sin embargo, sus respuestas no siempre corresponden exactamente a la categoría esperada, por lo que su desempeño se considera regular.
>>>>>>> 98b8981 (docs: caracterizacion del modelo local)
