class Encuesta:
    def __init__(self, titulo, fechaCreacion=None):
        self.titulo = titulo
        self.fechaCreacion = fechaCreacion
        self.preguntas = []
        self.respuestas = []
        self.grupo = None  

    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)

    def registrar_respuesta(self, respuesta):
        self.respuestas.append(respuesta)

    def obtener_respuestas(self):
        """Devuelve la lista de respuestas registradas."""
        return self.respuestas

    def aplicar_a_grupo(self, grupo):
        """Asigna la encuesta a un grupo de personas."""
        self.grupo = grupo

class Pregunta:
    def __init__(self, texto):
        self.texto = texto
