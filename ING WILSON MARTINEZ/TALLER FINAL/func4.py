print("Ajustes")
print("¿A donde desea dirigirse?")
print("Opcion 1 para configurar la cuenta")                              
print("Opcion 2 para  las notificaciones de la cuenta")                 
print("Opcion 3 para cerrar sesion")
op = int(input())

if (op == 1):
    print("Cofiguarcion de la cuenta")
    print("¿Que desea hacer?")
    print("Opcion 1 para configurar login")
    print("Opcion 2 para ingresar a las opciones del sistema")
    print("Opcion 3 para regresar a ajustes")
    seleccion = int(input())
    
    if(seleccion == 1):
        print("Configurar login")
    elif(seleccion == 2):
        print("Opciones del sistema")
    elif(seleccion == 3):
        print("Regresando a ajustes...")
    else:
        print("Debe ingresar una opción válida")

elif (op == 2):
    print("Notificaciones de la cuenta")
    print("No hay notificaciones")

elif (op == 3):
    print("Cerrar sesión")
    print("¿Seguro que deseas cerrar sesión?")
    cerrar_sesion = input()
    if (cerrar_sesion.lower() == "si"):
        print("Cerrando sesión...")
    else:
        print("Regresando a ajustes...")

else:
    print("Opcion inválida.")