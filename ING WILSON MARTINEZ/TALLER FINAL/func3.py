print("Recuperar contraseña")
print("Ingrese su correo electronico")
correo = input()
print("Ingrese al nueva contrasena")
nueva_contrasena = input()
print("Confirmar contrasena")
confirmar = input()

if (nueva_contrasena == confirmar):
    print("Contrasena cambiada correctamente")
else:
    print("Las contrasenas no coinciden")