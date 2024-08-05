print("Ingreses nombre del usuario")
usuario = input()

print("Ingrese cantidad en la cuenta de ahorros")
ahorrosiniciales = input()

an1 = float(ahorrosiniciales) * 0.04
total1 = round(float(ahorrosiniciales) - float(an1), 2)

an2 = float(total1) * 0.04
total2 = round(float(total1) - an2, 2)

an3 = float(total2) * 0.04
total3 = round(float(total2) -an3, 2)


print("En el primer an la cuenta de ",usuario, "cerro con ",total1, " en ahorros.")
print("En el segundo an la cuenta de ",usuario, "cerro con ",total2, "en ahorros.")
print("En el tercer an la cuenta de ",usuario, "cerro con ",total3, " en ahorros.")