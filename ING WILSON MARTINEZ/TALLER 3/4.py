num = int(input("Ingrese un numero: "))
pares = 0
for i in range(0,num + 1):
   if i % 2 == 0:
    pares += i
    print(i)
    
print(f"Las suma de los numeros pares entre 1 y {num} es: {pares}")