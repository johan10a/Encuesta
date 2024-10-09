from encuesta import Encuesta, Pregunta

def cargar_banco_encuestas():
    """Cargar un banco de encuestas predefinidas."""
    encuesta1 = Encuesta("Encuesta de Satisfacción", "2024-01-10")
    encuesta1.agregar_pregunta(Pregunta("¿Cómo calificaría el servicio?"))
    encuesta1.agregar_pregunta(Pregunta("¿Recomendaría nuestro producto?"))
    encuesta1.agregar_pregunta(Pregunta("¿Qué mejorarías en nuestro servicio?"))

    encuesta2 = Encuesta("Encuesta de Clima Laboral", "2024-02-15")
    encuesta2.agregar_pregunta(Pregunta("¿Cómo describiría el ambiente laboral?"))
    encuesta2.agregar_pregunta(Pregunta("¿Se siente valorado en su lugar de trabajo?"))

    encuesta3 = Encuesta("Encuesta de Marketing", "2024-03-05")
    encuesta3.agregar_pregunta(Pregunta("¿Con qué frecuencia utiliza nuestro producto?"))
    encuesta3.agregar_pregunta(Pregunta("¿Qué otras marcas utiliza con frecuencia?"))

    return [encuesta1, encuesta2, encuesta3]
