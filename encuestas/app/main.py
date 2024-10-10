import os
from grupo import Grupo
from banco_encuestas import cargar_banco_encuestas
from encuesta import Encuesta
from pregunta import Pregunta
from respuesta import Respuesta
from informe import Informe

def main():
    # 1. Cargar el grupo de usuarios desde un archivo CSV
    ruta_actual = os.path.dirname(__file__)
    ruta_csv = os.path.join(ruta_actual, '../data/usuarios.csv')
    
    grupo = Grupo(nombre="Clientes Encuestados")
    grupo.cargar_usuarios_desde_csv(ruta_csv)

    print(f"\n{len(grupo.usuarios)} usuarios cargados en el grupo '{grupo.nombre}'")

    # 2. Crear una encuesta manualmente
    encuesta = Encuesta(titulo="Encuesta de Satisfacción", fechaCreacion="2024-10-03")
    print(f"\nCreada encuesta: {encuesta.titulo} el {encuesta.fechaCreacion}")
    
    # 3. Agregar preguntas a la encuesta
    pregunta1 = Pregunta(texto="¿Cómo calificaría el servicio?")
    pregunta2 = Pregunta(texto="¿Recomendaría el servicio?")
    encuesta.agregar_pregunta(pregunta1)
    encuesta.agregar_pregunta(pregunta2)
    print(f"Preguntas agregadas: {[pregunta.texto for pregunta in encuesta.preguntas]}")

    # 4. Seleccionar una encuesta de un banco de encuestas
    encuestas_disponibles = cargar_banco_encuestas()
    print("\nEncuestas disponibles:")
    for i, enc in enumerate(encuestas_disponibles, start=1):
        print(f"{i}. {enc.titulo} (Creada el: {enc.fechaCreacion})")

    encuesta_seleccionada = encuestas_disponibles[0] if encuestas_disponibles else encuesta
    print(f"\nEncuesta seleccionada: {encuesta_seleccionada.titulo}")

    # 5. Asignar la encuesta al grupo de usuarios
    encuesta_seleccionada.aplicar_a_grupo(grupo)
    print(f"La encuesta '{encuesta_seleccionada.titulo}' ha sido asignada al grupo '{grupo.nombre}'")

    # 6. Crear una respuesta para el primer usuario en el grupo
    if grupo.usuarios:
        primer_usuario = grupo.usuarios[0]
        respuesta = Respuesta(pregunta=pregunta1, usuario=primer_usuario, valor="Excelente")
        print(f"\nUsuario {respuesta.usuario.nombre} respondió '{respuesta.valor}' a la pregunta '{respuesta.pregunta.texto}'")

    # 7. Generar un informe de la encuesta aplicada
    informe = Informe(encuesta_seleccionada, grupo)
    resultado_informe = informe.generar_informe()

    # 8. Mostrar el resultado del informe
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
