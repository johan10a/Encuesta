import csv
from usuario import Usuario

class Grupo:
    def __init__(self, nombre, criterios=None):
        self.nombre = nombre
        self.criterios = criterios if criterios is not None else {}
        self.usuarios = []

    def agregar_usuario(self, usuario):
        """Agrega un usuario al grupo."""
        self.usuarios.append(usuario)

    def cargar_usuarios_desde_csv(self, ruta_csv):
        """Carga usuarios desde un archivo CSV."""
        try:
            with open(ruta_csv, newline='', encoding='utf-8') as archivo_csv:
                lector_csv = csv.DictReader(archivo_csv)
                for fila in lector_csv:
                    print(f"Filas cargadas: {fila}")  # Muestra las filas cargadas
                    usuario = Usuario(
                        nombre=fila['Nombre'],
                        email=fila.get('Correo electrónico'),
                        celular=fila.get('Número celular'),
                        edad=fila.get('Edad'),
                        genero=fila.get('Género')
                    )
                    self.agregar_usuario(usuario)
            print(f"{len(self.usuarios)} usuarios cargados en el grupo '{self.nombre}'")
        except FileNotFoundError:
            print(f"No se encontró el archivo: {ruta_csv}")
        except KeyError as e:
            print(f"Error: la clave '{e}' no se encontró en el archivo CSV. Verifica los nombres de las columnas.")
