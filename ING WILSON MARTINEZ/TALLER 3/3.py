print("Igrese un numero:")
num = int(input())

cont = 0
suma = 0

for i in range(1,num + 1):
    cont = 0
    for j in range(1,i + 1):
        if i%j == 0:
            cont += 1
    
    if cont == 2:
        suma += i
        print(i)
print(f"La suma de los numeros primos entre 1 y {num} es de {suma}")