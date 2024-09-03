#Libros

#Declaro clase

class Libro:
    def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion

    def __str__(self):
        return f"'{self.titulo}' by {self.autor} - Genre: {self.genero}, Rating: {self.puntuacion}"

def agregar_libro(lista_libros):
    titulo = input("Ingresa el título del libro: ")
    autor = input("Ingresa el autor del libro: ")
    genero = input("Ingresa el género del libro: ")
    puntuacion = float(input("Ingresa la puntuación del libro (0-10): "))
    
    nuevo_libro = Libro(titulo, autor, genero, puntuacion)
    lista_libros.append(nuevo_libro)
    print(f"Libro '{titulo}' agregado correctamente.\n")

def buscar_libros_por_genero(lista_libros):
    genero = input("Ingresa el género que deseas buscar: ")
    libros_en_genero = [libro for libro in lista_libros if libro.genero.lower() == genero.lower()]
    
    if libros_en_genero:
        print(f"Libros en el género '{genero}':")
        for libro in libros_en_genero:
            print(f"- {libro.titulo}")
    else:
        print(f"No se encontraron libros en el género '{genero}'.\n")


def recomienda_libro(lista_libros):
    genero = input("Ingresa el género que te interesa: ")
    libros_en_genero = [libro for libro in lista_libros if libro.genero.lower() == genero.lower()]
    
    if libros_en_genero:
        mejor_libro = max(libros_en_genero, key=lambda libro: libro.puntuacion)
        print(f"Te recomendamos leer '{mejor_libro.titulo}', con una puntuación de {mejor_libro.puntuacion}.\n")
    else:
        print(f"No se encontraron libros en el género '{genero}'.\n")

def ranking_libros(lista_libros):
    libros_por_genero = {}

    # Agrego genero por si no existe

    for libro in lista_libros:
        if libro.genero not in libros_por_genero: 
            libros_por_genero[libro.genero] = []
        libros_por_genero[libro.genero].append(libro)

    # Ranking

    for genero, libros in libros_por_genero.items():
        libros.sort(key=lambda libro: libro.puntuacion, reverse=True)

    # Muestro ranking

    for genero, libros in libros_por_genero.items():
        print(f"Ranking de libros en el género: {genero}:")
        for i, libro in enumerate(libros, start = 1):
            print(f"{i}. {libro.titulo} - Puntuación: {libro.puntuacion}")
        print()

import pandas as pd

def cargar_desde_csv(ruta_csv, lista_libros):
    datos = pd.read_csv(ruta_csv)

    for _, row in datos.iterrows():
        titulo = row['titulo']
        autor = row['autor']
        genero = row['genero']
        puntuacion = row['puntuacion']
        nuevo_libro = Libro(titulo, autor, genero, puntuacion)
        lista_libros.append(nuevo_libro)

def menu():
    lista_libros = []

    lista_libros.extend([
    Libro('CIEN AÑOS DE SOLEDAD','GABRIEL GARCÍA MÁRQUEZ','FICCIÓN',4.5),
    Libro('1984','GEORGE ORWELL','CIENCIA FICCIÓN',4.3),
    Libro('EL HOBBIT','J.R.R. TOLKIEN','FANTASÍA',4.7),
    Libro('ORGULLO Y PREJUICIO','JANE AUSTEN','ROMANCE',4.2),
    Libro('CRIMEN Y CASTIGO','FIÓDOR DOSTOYEVSKI','CLÁSICO',4.4),
    Libro('LOS JUEGOS DEL HAMBRE','SUZANNE COLLINS','JUVENIL',4.11),
    Libro('DON QUIJOTE DE LA MANCHA','MIGUEL DE CERVANTES','CLÁSICO',4.6),
    Libro('HARRY POTTER Y LA PIEDRA FILOSOFAL','J.K. ROWLING','FANTASÍA',4.8),
    Libro('LOS PILARES DE LA TIERRA','KEN FOLLETT','HISTÓRICA',4.4),
    Libro('CAZADORES DE SOMBRAS: CIUDAD DE HUESO','CASSANDRA CLARE','FANTASÍA',4.0)])
    
    while True:
        print("Menú de opciones:")
        print("1. Agregar Libro")
        print("2. Buscar Libros por Género")
        print("3. Recomendar Libro")
        print("4. Ranking de libros por Genero")
        print("5. Cargar csv")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            agregar_libro(lista_libros)
        elif opcion == '2':
            buscar_libros_por_genero(lista_libros)
        elif opcion == '3':
            recomienda_libro(lista_libros)
        elif opcion == '4':
            ranking_libros(lista_libros)
        elif opcion == '5':
            ruta_csv = input("Ingresa la ruta del archivo: ")
            cargar_desde_csv(ruta_csv, lista_libros)
        elif opcion == '6':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.\n")


# Ejecutar el menú
menu()
