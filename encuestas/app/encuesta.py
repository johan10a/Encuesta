class Encuesta:
    def __init__(self, titulo, fechaCreacion=None):
        self.titulo = titulo
        self.fechaCreacion = fechaCreacion
        self.preguntas = []
        self.grupo = None

    def agregar_pregunta(self, pregunta):
        """Agrega una pregunta a la encuesta."""
        self.preguntas.append(pregunta)

    def aplicar_a_grupo(self, grupo):
        """Asigna la encuesta a un grupo de personas."""
        self.grupo = grupo

    def personalizar_encuesta(self, nuevas_preguntas):
        """Permite agregar o modificar preguntas en la encuesta."""
        self.preguntas = nuevas_preguntas


class Pregunta:
    def __init__(self, texto, opciones=None):
        self.texto = texto
        self.opciones = opciones if opciones else []

    def __str__(self):
        return self.texto
