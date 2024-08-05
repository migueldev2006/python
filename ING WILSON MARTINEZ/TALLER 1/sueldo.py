print("Digite el nombre del trabajador")
nombre=input()
print("Digite el sueldo base")
SB=int(input())

aumento=int(SB*0.10)
Sueldototal=int(SB+aumento)

print("El aumento es de: ",aumento)
print("El nuevo sueldo de ",nombre, "es: ",Sueldototal)
