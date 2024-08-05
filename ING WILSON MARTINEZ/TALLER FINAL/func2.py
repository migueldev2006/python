datos = ['Luis Miguel Giron Orozco', 1081729282, 'gironorozcoluisniguel3@gmail.com', 'Aprendiz', 'Luismi321', 3132642980]

print("Inicio de sesión o autenticación")
print("Ingrese su identificación:")
ID = int(input())
print("Digite su contrasena:")
contrasena = input()

if contrasena == datos[4] and ID == datos[1]:
    print(datos[0], "sus datos son correctos") 
    print("Iniciando sesión...")
else:
    print("Lo siento, los datos son incorrectos")
    print("Cargando pagina nuevamente...")