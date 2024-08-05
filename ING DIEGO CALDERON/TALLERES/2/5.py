n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

if (n1 > 10 and n2 > 10):
    print("Ambos numeros son mayores que 10")

elif (n1 > 10 or n2 > 10):
    print("Solo uno de los numeros es mayor que 10")
    
else:
    print("Ninguno de los números es mayor que 10") 