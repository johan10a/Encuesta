# Requisitos del Sistema de Gestión de Encuestas


## Requisitos Funcionales

1. **Gestión de Usuarios**:
- El sistema debe permitir cargar un listado de usuarios desde un archivo CSV, incluyendo campos como nombre, correo electrónico, número celular, edad y género.
- El sistema debe permitir la creación manual de usuarios, almacenando sus datos en una estructura de grupo para facilitar su asignación a encuestas.
- Los usuarios deben poder pertenecer a uno o varios grupos.


2. **Gestión de Grupos**:
- El sistema debe permitir la creación de grupos de usuarios, que serán usados para segmentar a los encuestados.
- Debe ser posible asignar usuarios existentes a uno o varios grupos.
- Los grupos deben poder ser utilizados para aplicar encuestas específicas.


3. **Gestión de Encuestas**:
- El sistema debe permitir la creación de encuestas, las cuales contendrán un conjunto de preguntas.
- Cada encuesta debe tener un título y una fecha de creación.
- El sistema debe almacenar múltiples encuestas en un banco de encuestas para su reutilización.
- Las encuestas deben poder ser asignadas a grupos de usuarios.


4. **Gestión de Preguntas**:
- Cada encuesta debe poder incluir una o más preguntas.
- El sistema debe permitir agregar preguntas a las encuestas, almacenando el texto de la pregunta.

5. **Recopilación de Respuestas**:
- Los usuarios deben poder proporcionar respuestas a las preguntas asignadas.
- Las respuestas de los usuarios deben estar vinculadas a la pregunta correspondiente y a la encuesta en la que se hicieron.
- El sistema debe registrar las respuestas de cada usuario en una estructura que permita su análisis posterior.

6. **Integración de Datos**:
- El sistema debe permitir la carga de usuarios desde archivos CSV que contienen información variada, asegurando la correcta lectura de campos como nombre, correo electrónico, edad y género.
8. **Personalización y Segmentación**
- El sistema debe permitir la creación de encuestas personalizadas a partir de un banco de preguntas predefinidas.
- Debe ser posible segmentar a los usuarios por criterios como edad, género y ubicación para asignarles encuestas específicas.



## Requisitos No Funcionales


1. **Usabilidad**:
- El sistema debe tener una interfaz de usuario sencilla que permita la carga de usuarios, la creación de encuestas y la visualización de informes de manera intuitiva.
2. **Mantenibilidad**:
- El código del sistema debe ser modular y fácil de mantener, permitiendo la adición de nuevas funciones sin afectar la estabilidad del sistema.
- La documentación del código debe estar disponible para facilitar el mantenimiento y futuras mejoras del sistema.