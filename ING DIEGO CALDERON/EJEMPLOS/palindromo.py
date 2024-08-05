print("Ingrese la cadena de texto para analizar")
cadena = input()

cadeMin = cadena.lower()
eliminaEspacio = cadeMin.replace(" ", "")
invertir = eliminaEspacio[::-1]

print( eliminaEspacio == invertir)