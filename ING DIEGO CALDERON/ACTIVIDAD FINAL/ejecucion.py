from menu_biblioteca import *

libros_biblioteca = {}
libros_prestados = []
historial_prestamos = [] 


while True:
    
    print("Oprima 1 para agregar libros")
    print("Oprima 2 para buscar libros")
    print("Oprima 3 para prestar libros")
    print("Oprima 4 para devolver libros")
    print("Oprima 5 para ver libros prestados")
    print("Oprima 6 para ver historial de prestamos")
    print("Oprima 7 para salir")
    
    op = int(input())
    
    if (op == 1):
        agregar_libros(libros_biblioteca)
    elif (op == 2):
        buscar_libros(libros_biblioteca)
    elif (op == 3):
        prestar_libros(libros_biblioteca, libros_prestados, historial_prestamos)
    elif (op == 4):
        devolver_libros(libros_biblioteca, libros_prestados, historial_prestamos)
    elif (op == 5):
        ver_libros_prestados(libros_prestados)
    elif (op == 6):
        ver_historial_de_prestamos(historial_prestamos)
    elif (op == 7):
        print("Saliendo de la biblioteca...")
        break
    else:
        print("Lo siento, no es posible ejecutar. Debes seleccionar una opción valida.")
        