# INFORME TÉCNICO – CLASIFICADOR DE COMMITS CON IA

## 1. Información del entorno

- Sistema operativo: Ubuntu 24.04 LTS.
- Entorno de ejecución: WSL2.
- Memoria RAM asignada a WSL: aproximadamente 7.8 GiB.
- Procesador utilizado: CPU.
- Herramienta de inteligencia artificial: Ollama.
- Versión de Ollama: 0.40.11.

## 2. Modelos de inteligencia artificial evaluados

### Modelo qwen2.5-coder:1.5b

- Tamaño instalado: 986 MB.

### Modelo qwen2.5:0.5b

- Tamaño instalado: 397 MB.
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

## 5. Pruebas de funcionamiento de la API

Se realizaron pruebas mediante Swagger para verificar los endpoints del sistema.

| Endpoint | Resultado |
|---|---|
| GET /health | Correcto. Conexión con PostgreSQL confirmada. |
| POST /clasificar con ECO | Correcto. Clasificación feat. |
| POST /clasificar con Ollama | Correcto. Clasificación feat. |
| GET /inferencias | Correcto. Consulta de registros almacenados. |

### Prueba reciente con Ollama

- Mensaje: feat: agregar inicio de reportes.
- Motor utilizado: ollama.
- Modelo: qwen2.5:0.5b.
- Categoría obtenida: feat.
- Tiempo de respuesta: 3334 ms.
- Código HTTP: 200.
- Registro almacenado en PostgreSQL: ID 16.

Esta prueba confirmó que el modelo puede clasificar mensajes desde la API y guardar los resultados en la base de datos.

## 6. Evaluación de calidad

### Modelo qwen2.5-coder:1.5b

- Calificación: 4/5.

El modelo ofrece respuestas claras, comprende las instrucciones y proporciona ejemplos útiles. Sin embargo, algunas respuestas pueden necesitar revisión para asegurar que la información sea completamente correcta.

### Modelo qwen2.5:0.5b

- Calificación: 3/5.

El modelo presenta un tiempo de respuesta rápido y puede generar resultados relacionados con el mensaje de commit. Sin embargo, sus respuestas no siempre corresponden exactamente a la categoría esperada, por lo que su desempeño se considera regular.

## 7. Conclusiones

La instalación y configuración del entorno de inteligencia artificial se realizó correctamente. Se evaluaron los modelos qwen2.5-coder:1.5b y qwen2.5:0.5b, observando diferencias en sus tiempos de respuesta y calidad.

También se implementó un backend funcional con FastAPI, integrado con PostgreSQL y dos motores de clasificación: ECO, basado en reglas, y Ollama, que utiliza inteligencia artificial.

Las pruebas realizadas confirmaron el funcionamiento de los endpoints, la clasificación de mensajes y el almacenamiento de las inferencias en PostgreSQL.

Finalmente, se establecieron medidas básicas de seguridad para proteger las credenciales y controlar el acceso a la base de datos.
