numero = int(input("Ingrese un numero del 1 al 10: "))
lista = [1,2,3,4,5,6]

if (numero >= 1 and numero <= 10):
    for multiplo in tabla:
        print(f"{numero} * {multiplo} = {numero * multiplo}")
else:
    print("Ingrese un numero enter 1 y 10")
    