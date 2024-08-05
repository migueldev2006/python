"Escriba un programa en Python que determine si un año ingresado por el usuario es bisiesto o no. Un año es bisiesto si es divisible por 4 pero no por 100, o si es divisible por 400."

año = 2024

op1 = año % 4 #ser divisible
op2 = año % 100 #NO divisible
op3 = año % 400 #ser divisible

print(f"El res de la op1 es: {op1}")
print(f"El res de la op2 es: {op2}")
print(f"El res de la op3 es: {op3}")
