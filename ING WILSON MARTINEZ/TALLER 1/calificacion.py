#Inicio
calificacion1 = 0
calificacion2 = 0
calificacion3 = 0
#datos de entrada
print("Digite calificacion1")
calificacion1 = float(input())

print("Digite calificacion2")
calificacion2 = float(input())

print("Digite calificacion3")
calificacion3 = float(input())
#procesos
resultado1 = calificacion1 * 0.30
resultado2 = calificacion2 * 0.30
resultado3 = calificacion3 * 0.40
resultadofinal = resultado1 + resultado2 + resultado3
#salida
print("El primer examen equivale a :",resultado1)
print("El segundo examen equivale a :",resultado2)
print("El tercer examen equivale a :",resultado3)
print("La calificacion final del alumn es :",resultadofinal)