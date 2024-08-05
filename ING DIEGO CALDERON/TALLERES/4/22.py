cadena = input("Ingrese la cadena de texto a  analizar: ")

cadMin = cadena.lower()
eliminarEspacios = cadMin.replace(" ", "")
invertir = eliminarEspacios[::-1]

print(eliminarEspacios == invertir)
