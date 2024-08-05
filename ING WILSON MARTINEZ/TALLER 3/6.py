num = int(input("Ingrese un numero: "))

factorial = 1

for i in range(1,num + 1):
    factorial *=i
    
print(f"El factorial  del numero {num} es : {factorial}")