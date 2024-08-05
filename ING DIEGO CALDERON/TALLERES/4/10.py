nota = int(input("Ingrese la nota del estudiante: "))

if (nota >= 60 and nota < 90):
    print("El estudiante ha Aprobado.")
    
elif (nota >= 90):
    print("Es un estudiante Sobresaliente.")
    
else:
    print("El estudiante ha Reprobado.")