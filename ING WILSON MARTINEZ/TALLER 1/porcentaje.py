print("Digite numero de mujeres")
nmujeres = int(input())
print("Digite numero de hombres")
nhombres = int(input())

totalalumnos = nmujeres + nhombres
porcentajemujeres =(int(nmujeres/totalalumnos))*100
porcentajehombres =(int(nhombres/totalalumnos))*100

print("El total de alumnos es de :",totalalumnos)
print("El porcentaje de mujeres es de :",porcentajemujeres, "%")
print("El porcentaje de hombres es de :",porcentajehombres, "%")