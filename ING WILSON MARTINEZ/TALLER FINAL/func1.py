datos = []
print("Registro de usuario")
print("Ingrese su nombre completo:")
nombre = input()
print("Ingrese su numero de identificación:")
ID = int(input())
print("Ingrese su correo electronico:")
correo_electronico = input()
print("Ingrese el tipo de usuario:")
tipo_de_usuario = input()
print("Ingrese una conatraseña segura:")
contrasena = input()
print("Ingrse su número de telefono:")
telefono = int(input())
datos.append(nombre)
datos.append(ID)
datos.append(correo_electronico)
datos.append(tipo_de_usuario)
datos.append(contrasena)
datos.append(telefono)
print(datos)
print("Registro exitoso.")