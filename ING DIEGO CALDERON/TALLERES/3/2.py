diccionario = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España":"Madrid"}

pais = input("Ingrese un pais: ")


if (pais in diccionario):
    print(pais in diccionario)
    
else:
    print("El pais no existe.")
    
