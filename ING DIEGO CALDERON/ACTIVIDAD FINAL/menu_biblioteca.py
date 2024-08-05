def  agregar_libros(libros_biblioteca):
    continua = "si"
    
    while (continua == "si"):
        print("¿desea agregar libros?")
        continua = input()
        if (continua == "si"):
            print("Ingrese el nombre del libro:")
            clave = input()
            print("Ingrese el estado del libro")
            valor = input()
            libros_biblioteca[clave] = valor
            
    print("Libros en la biblioteca:")
    for clave, valor in libros_biblioteca.items():
        libros_biblioteca[clave] = valor
        print(f"{clave} : {valor}")
        
    return libros_biblioteca

def buscar_libros(libros_biblioteca):
    print("Ingrese el nombre del libro a buscar")
    nombre = input()
    if nombre in libros_biblioteca:
        print(f"El libro {nombre} se encuentra en estado {libros_biblioteca[nombre]}")
    else:
        print("El libro no se encuentra en la biblioteca")

def prestar_libros(libros_biblioteca,libros_prestados,historial_prestamos):
    print("Ingrese el nombre del libro a prestar ")
    nombre = input()
    if nombre in libros_biblioteca:
        if libros_biblioteca[nombre] == "activo":
            libros_biblioteca[nombre] = "inactivo"
            libros_prestados.append(nombre)
            historial_prestamos.append((nombre, "inactivo"))
            print(f"El libro {nombre} has sido prestado exitosamente.")
        else:
            print(f"El libro {nombre} no esta disponible.")
    else:
        print("Estimado cliente lo sentimos pero su libro no se ha encontrado registrado en la biblioteca.")

def devolver_libros(libros_biblioteca,libros_prestados,historial_prestamos):
        print("Ingrese el nombre del libro a devolver")
        nombre = input()
        if nombre in libros_prestados:
            libros_biblioteca[nombre] = "activo"
            libros_prestados.remove(nombre)
            historial_prestamos.append((nombre, "activo"))
            print(f"El libro {nombre} ha sido devuelto exitosamente.")
        else:
            print(f"No tiene prestado el libro {nombre}.")

def ver_libros_prestados(libros_prestados):
    if libros_prestados:
        print("los libros prestados son:")
        for clave in libros_prestados:
            print (clave)
    else:
        print("No tiene libros prestados.")

def ver_historial_de_prestamos (historial_prestamos):
    print("Historial de prestamos:")
    for clave,valor in historial_prestamos:
        print(f"{clave} : {valor}")