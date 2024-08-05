"""
Solicita al usuario ingresar un número entero del 1 al 10. Luego, utiliza un bucle for para imprimir la tabla de multiplicar de ese número, desde el 1 hasta el 10.

"""

print("Ingrese un numero entero del 1 hasta el 10")
num = int(input())

if(num >= 1 and num <= 10):
    lista = [1,2,3,4,5,6,7,8,9,10]
    
    for multiplo in lista:
        print(f"{num} * {multiplo} = {num * multiplo}")
else:
    print("Ingrese un numero entre 1 y 10")