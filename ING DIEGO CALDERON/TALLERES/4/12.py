calificacion = int(input("Ingrese la calificación: "))


if calificacion >= 0 and calificacion <= 59:
    print("Por su calificación Reprobo")
    
elif calificacion >= 60 and calificacion <= 69:
    print("Por su calificación ha Aprobado")

elif calificacion >= 70 and calificacion <= 79:
    print("Su calificación es Regular")

elif calificacion >= 80 and calificacion <= 89:
    print("Su calificación es Buena")

elif calificacion >= 90 and calificacion <= 100:
    print("Su calificación es Excelente")
    
else:
    print("Nota invalida")
