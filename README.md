# Sistema de Gestión de Encuestas

**Autor:** Johan Alexis Chara  
**Profesor:** Diego Fernando Marín  
**Curso:** Lenguaje de Programación Avanzado 1

## Documentación

[Documentation](docs/REQUERIMIENTOS.MD)
[Diagrama UML](docs/img/DiagramaEncuesta.jpg)

## Descripción
Este sistema de gestión de encuestas permite la creación, distribución y análisis de encuestas. Los usuarios pueden cargar listados de encuestados desde archivos CSV, asignarles encuestas personalizadas. Además, el sistema facilita la segmentación de los encuestados por diversos criterios como edad, género y ubicación.


## Características Principales
- **Gestión de Usuarios:** Carga de usuarios desde archivos CSV o manualmente. Los usuarios se agrupan para aplicarles encuestas.
- **Gestión de Grupos:** Creación de grupos para segmentar usuarios y asignar encuestas.
- **Banco de Encuestas:** Creación de encuestas y almacenamiento de encuestas predefinidas.
- **Asignación de Encuestas:** Aplicación de encuestas a grupos de usuarios.
- **Recopilación de Respuestas:** Registro de respuestas de los usuarios a preguntas específicas de las encuestas.

## Requisitos

### Requisitos de Software
## Instrucciones de Uso

1. **Instalación**: Asegúrate de tener Python 3.12.5 instalado en tu máquina.

2. **Ejecución**: Ejecuta el archivo `main.py` desde la línea de comandos con la siguiente ruta:
   ```bash
$ Encuesta/encuestas/app/main.py
   ```
   Ejecutar las pruebas:

```bash
$ Encuesta\encuestas> pytest
```


### Estructura del Proyecto
```bash

encuestas/
│
├── app/
│   ├── main.py              # Archivo principal para ejecutar el sistema
│   ├── grupo.py             # Gestión de grupos de usuarios
│   ├── usuario.py           # Definición de la clase Usuario
│   ├── encuesta.py          # Gestión de encuestas
│   ├── pregunta.py          # Gestión de preguntas dentro de las encuestas
│   ├── respuesta.py         # Registro de respuestas de usuarios
│   ├── informe.py           # Generación de informes
│   ├── banco_encuestas.py   # Carga de encuestas predefinidas
├── └──test_encuestas.py        # Pruebas unitarias del sistema
│
├── data/
│   └── usuarios.csv         # Archivo CSV de usuarios
│
│
└── README.md                # Archivo con la descripción del proyecto


