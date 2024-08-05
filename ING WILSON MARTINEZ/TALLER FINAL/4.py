suma_pares = 0
suma_impares = 0
for i in range(1,100 + 1):
    if i % 2 == 0:
        suma_pares += i
        print(f"Suma de numeros pares: {suma_pares} ")


for i in range(1,100 +1):
    if i % 2 != 0:
        suma_impares+= i
        print(f"Suma de numeros impares: {suma_impares}")