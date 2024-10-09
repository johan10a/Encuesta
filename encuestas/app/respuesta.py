from  usuario import Usuario
from  pregunta import Pregunta


class Respuesta:
    def __init__(self, pregunta, usuario, valor):
        """
        Inicializa una respuesta para una pregunta hecha por un usuario.
        - pregunta: instancia de Pregunta.
        - usuario: instancia de Usuario.
        - valor: la respuesta dada por el usuario.
        """
        self.pregunta = pregunta
        self.usuario = usuario
        self.valor = valor
