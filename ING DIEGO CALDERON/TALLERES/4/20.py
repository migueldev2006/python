dinero = input("Ingrese la cantidad inicial de dinero para abrir la cuenta de ahorro: ")

interes = 0.015

incremento = int(dinero) * (1+interes)

anio2 = incremento * 2
anio3 = incremento * 3
anio12 = incremento * 12

print(f"El saldo en la cuenta cuenta de ahorros despues del primer año es de {incremento}")
print(f"El saldo en la cuenta cuenta de ahorros despues de dos años es de {anio2}")
print(f"El saldo en la cuenta cuenta de ahorros despues de tres años es de {anio3}")
print(f"El saldo en la cuenta cuenta de ahorros despues de doce años es de {anio12}")