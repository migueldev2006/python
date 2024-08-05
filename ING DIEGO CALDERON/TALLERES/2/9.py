numero = int(input("Ingrese un número: "))

res = numero % 3
res2 = numero % 5

if (res == 0 and res2 == 0):
    print(f"El {numero}, es divisible por 3 y 5.")
    
else:
    print(f"El {numero}, no es divisible por 3 y 5.")