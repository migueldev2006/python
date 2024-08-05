votacion = input("Elija a su candidato (A,B o C): ")

mayus = votacion.upper()

if (mayus == "A"):
    print("Usted ha votado por el partido rojo.")
    
elif (mayus == "B"):
    print("Usted ha votado por el partido verde.")
    
elif (mayus == "C"):
    print("Usted ha votado por el partido azul.")
    
else:
    print("Opción errónea")