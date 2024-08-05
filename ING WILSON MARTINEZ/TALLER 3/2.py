print("Igrese un numero:")
num = int(input())

cont = 0

if num > 1:
  
  for i in range(2,num):
    resto = num % i
    
    if (resto == 0):
      cont+= 1
      print(i)
      
  if cont == 0:
    print(f"El {num} es un número primo")
  
  else:
    print(f"El {num} no es un número primo")

else:
  print("Numero invalido")