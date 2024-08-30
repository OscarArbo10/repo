# Lista para almacenar los paquetes turísticos como diccionarios
paquetes = []

# Función para agregar un paquete turístico a la lista
def agregar_paquete(id_paquete, nombre, destino, duracion, duracion2, precio, descripcion):
    paquete = {
        'id_paquete': id_paquete,
        'nombre': nombre,
        'destino': destino,
        'duracion': duracion,  # Duración en días
        'duracion2': duracion2,  # Duración en noches
        'precio': precio,
        'descripcion': descripcion
    }
    paquetes.append(paquete)

# Función para mostrar todos los paquetes turísticos
def mostrar_paquetes():
    if paquetes:
        print("Elige el paquete que más se adapte a tus gustos y necesidades.")
        print("Estos son los paquetes turísticos disponibles:")
        for i, paquete in enumerate(paquetes, 1):
            print(f"{i}. {paquete['nombre']} a {paquete['destino']} por {paquete['duracion']} días y {paquete['duracion2']} noches - Precio: ${paquete['precio']}")

# Función para que el usuario escoja un paquete y mostrarlo
def escoger_paquete():
    mostrar_paquetes()
    opcion = int(input("Introduce el número del paquete que deseas escoger: "))
    
    if  opcion <= len(paquetes):
        paquete_seleccionado = paquetes[opcion -1]
        print("\nHas seleccionado el siguiente paquete:")
        print(f"Nombre: {paquete_seleccionado['nombre']}")
        print(f"Destino: {paquete_seleccionado['destino']}")
        print(f"Duración: {paquete_seleccionado['duracion']} días y {paquete_seleccionado['duracion2']} noches")
        print(f"Precio: ${paquete_seleccionado['precio']}")
        print(f"Descripción: {paquete_seleccionado['descripcion']}")
    else:
        print("Opción inválida. Por favor, selecciona un número de la lista.")

# Función para agregar los paquetes
agregar_paquete(1, "Escapada Romántica", "San Andrés", 5, 4, 1500000, "Incluye hotel y visitas guiadas")
agregar_paquete(2, "Ruta del sol", "Barranquilla", 4, 3, 900000, "Incluye hotel, ski y tours guiados")
agregar_paquete(3, "Aventura costera", "Santa Marta", 3, 2, 850000, "Incluye hotel, ski y tours guiados")
agregar_paquete(4, "Costa dorada", "Panamá", 3, 2, 1000000, "Incluye hotel y tours guiados")
agregar_paquete(5, "Tesoros cariocas", "Río de Janeiro", 7, 6, 2100000, "Incluye hotel")

# Llamado a la función para que el usuario escoja un paquete
escoger_paquete()