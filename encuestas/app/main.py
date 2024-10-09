import os
from grupo import Grupo
from banco_encuestas import cargar_banco_encuestas
from informe import Informe

def main():
    # Obtener la ruta actual del script
    ruta_actual = os.path.dirname(__file__)
    ruta_csv = os.path.join(ruta_actual, '../data/usuarios.csv')
    
    # Cargar el grupo de usuarios
    grupo = Grupo(nombre="Clientes Encuestados")
    grupo.cargar_usuarios_desde_csv(ruta_csv)

    print(f"\n{len(grupo.usuarios)} usuarios cargados en el grupo '{grupo.nombre}'")

    # Cargar las encuestas
    encuestas_disponibles = cargar_banco_encuestas()
    print("\nEncuestas disponibles:")
    for i, encuesta in enumerate(encuestas_disponibles, start=1):
        print(f"{i}. {encuesta.titulo} (Creada el: {encuesta.fechaCreacion})")

    # Seleccionar una encuesta y aplicarla
    encuesta_seleccionada = encuestas_disponibles[0]
    encuesta_seleccionada.aplicar_a_grupo(grupo)
    
    # Generar un informe de la encuesta aplicada
    informe = Informe(encuesta_seleccionada, grupo)
    resultado_informe = informe.generar_informe()

    # Mostrar el resultado del informe
    print(f"\nTasa de respuesta: {resultado_informe['tasa_respuesta']}%")
    print("Distribución de respuestas:", resultado_informe['distribucion_respuestas'])

if __name__ == "__main__":
    main()


#     # Crear una encuesta
#     encuesta = Encuesta(titulo="Encuesta de Satisfacción", fechaCreacion="2024-10-03")
#     print(f"Creada encuesta: {encuesta.titulo} el {encuesta.fechaCreacion}")
    
#     # Agregar preguntas a la encuesta
#     pregunta1 = Pregunta(texto="¿Cómo calificaría el servicio?")
#     pregunta2 = Pregunta(texto="¿Recomendaría el servicio?")
#     encuesta.agregar_pregunta(pregunta1)
#     encuesta.agregar_pregunta(pregunta2)
#     print(f"Preguntas agregadas: {[pregunta.texto for pregunta in encuesta.preguntas]}")

#     # Crear un grupo de personas
#     grupo = Grupo(nombre="Clientes VIP", criterios={"edad": ">= 30"})
#     print(f"Grupo creado: {grupo.nombre} con criterios {grupo.criterios}")
    
#     # Asignar encuesta al grupo
#     encuesta.aplicar_a_grupo(grupo)
#     print(f"La encuesta '{encuesta.titulo}' ha sido asignada al grupo '{encuesta.grupo.nombre}'")

#     # Crear un usuario
#     usuario = Usuario(nombre="Ana García", email="ana@example.com")
#     print(f"Usuario creado: {usuario.nombre}, email: {usuario.email}")

#     # Crear una respuesta a la pregunta
#     respuesta = Respuesta(pregunta=pregunta1, usuario=usuario, valor="Excelente")
#     print(f"Respuesta creada: Usuario {respuesta.usuario.nombre} respondió '{respuesta.valor}' a la pregunta '{respuesta.pregunta.texto}'")

    # Crear una respuesta para el primer usuario en la lista del grupo
#     if grupo.usuarios:
#         usuario = grupo.usuarios[1]
#         respuesta = Respuesta(pregunta=pregunta1, usuario=usuario, valor="Excelente")
#         print(f"Usuario {respuesta.usuario.nombre} respondió '{respuesta.valor}' a la pregunta '{respuesta.pregunta.texto}'")

# if __name__ == "__main__":
#     main()




# def main():
#     # Crear una encuesta
#     encuesta = Encuesta(titulo="Encuesta de Satisfacción", fechaCreacion="2024-10-03")
#     print(f"Creada encuesta: {encuesta.titulo} el {encuesta.fechaCreacion}")
    
#     # Agregar preguntas a la encuesta
#     pregunta1 = Pregunta(texto="¿Cómo calificaría el servicio?")
#     pregunta2 = Pregunta(texto="¿Recomendaría el servicio?")
#     encuesta.agregar_pregunta(pregunta1)
#     encuesta.agregar_pregunta(pregunta2)
#     print(f"Preguntas agregadas: {[pregunta.texto for pregunta in encuesta.preguntas]}")

#     # Crear un grupo de personas
#     grupo = Grupo(nombre="Clientes VIP", criterios={"edad": ">= 30"})
#     print(f"Grupo creado: {grupo.nombre} con criterios {grupo.criterios}")
    
#     # Asignar encuesta al grupo
#     encuesta.aplicar_a_grupo(grupo)
#     print(f"La encuesta '{encuesta.titulo}' ha sido asignada al grupo '{encuesta.grupo.nombre}'")

#     # Crear un usuario
#     usuario = Usuario(nombre="Ana García", email="ana@example.com")
#     print(f"Usuario creado: {usuario.nombre}, email: {usuario.email}")

#     # Crear una respuesta a la pregunta
#     respuesta = Respuesta(pregunta=pregunta1, usuario=usuario, valor="Excelente")
#     print(f"Respuesta creada: Usuario {respuesta.usuario.nombre} respondió '{respuesta.valor}' a la pregunta '{respuesta.pregunta.texto}'")

# if __name__ == "__main__":
#     main()
