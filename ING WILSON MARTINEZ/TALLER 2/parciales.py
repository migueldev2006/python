parcial1 = input("Ingrese la calificación del primer parcial: ")
parcial2 = input("Ingrese la calificación del segundo parcial: ")
parcial3 = input("Ingrese la calificación del tercer parcial: ")
examen_final = input("Ingrese la calificaión del examen final: ")
trabajo_final = input("Ingrese la calificación del trabajo final: ")

equivalencia_promedio = ((int(parcial1) + int(parcial2) + int(parcial3))/3) * (35/100)
equvalencia_examen_final = int(examen_final) * (35/100)
equivalencia_trabajo_final = int(trabajo_final) * (30/100)

calificacion_final = equivalencia_promedio + equvalencia_examen_final +equivalencia_trabajo_final
print(f"La calificacion final del estudiante es {calificacion_final}")

if calificacion_final >= 3:
    print("El estudiante Aprobo.")
    
else:
    print("El estudiante No Aprobo.")