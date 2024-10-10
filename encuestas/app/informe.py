class Informe:
    def __init__(self, encuesta, grupo):
        self.encuesta = encuesta
        self.grupo = grupo

    def generar_informe(self):
        total_usuarios = len(self.grupo.usuarios)
       
        respuestas = self.obtener_respuestas()

        tasa_respuesta = len(respuestas) / total_usuarios * 100

        distribucion_respuestas = self.calcular_distribucion(respuestas)

        return {
            "tasa_respuesta": tasa_respuesta,
            "distribucion_respuestas": distribucion_respuestas
        }

    def obtener_respuestas(self):
        """Simula la obtención de respuestas."""
        return []  

    def calcular_distribucion(self, respuestas):
        """Distribución de respuestas por pregunta."""
        return {}
