n = int(input("Ingresa un numero: "))

cont = 0
for i in range(1,n + 1):
    if i % 3 == 0:
        cont += 1
        print(i)

print(f"Entre 1 y {n} hay {cont} multipos de 3.")