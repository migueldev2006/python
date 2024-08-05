"""
Escribe un programa que solicite al usuario ingresar un número entero positivo. Luego, utiliza un bucle while para imprimir todos los números pares desde 0 hasta ese número, seguido de todos los números impares hasta ese número.

"""

print("Digite un numero entero:")
lim = int(input())
aux = 0
while(aux <= lim):
    if(aux % 2 == 0):
        print("NUMERO PARES")
        print(aux)
        aux = aux +1
    else:
        print("NUMERO IMPARES")
        print(aux)
        aux = aux +1