a = int(input("Digite el primer número: "))
b = int(input("Digite el segundo número: "))
c = int(input("Digite el tercer número: "))

if a<b and a<c:
    print (f"El número menor es {a}")
        
elif b<a and b<c:
    print(f"El numero menor es {b}")

else:
    print(f"El numero menor es {c}")