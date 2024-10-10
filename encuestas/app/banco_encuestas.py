from encuesta import Encuesta, Pregunta

def cargar_banco_encuestas():
    # Crear algunas encuestas predefinidas para simular un banco de encuestas
    encuesta1 = Encuesta(titulo="Encuesta de Satisfacción", fechaCreacion="2024-01-10")
    encuesta2 = Encuesta(titulo="Encuesta de Clima Laboral", fechaCreacion="2024-02-15")
    encuesta3 = Encuesta(titulo="Encuesta de Marketing", fechaCreacion="2024-03-05")

    # Agregar algunas preguntas
    pregunta1 = Pregunta(texto="¿Cómo calificaría el servicio?")
    pregunta2 = Pregunta(texto="¿Recomendaría el servicio?")
    
    encuesta1.agregar_pregunta(pregunta1)
    encuesta1.agregar_pregunta(pregunta2)

    return [encuesta1, encuesta2, encuesta3]
