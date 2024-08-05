dinero = input("Ingrese la cantidad de dinero incial depositada en la cuenta de ahorros: ")

interes = 0.02

incremento = int(dinero) * (1+interes)
incremento2 = incremento * (1+interes)
incremento3 = incremento2 *(1+interes)

sacar = round(incremento3 * 0.10)
saldocuenta = round(incremento3 - sacar) 

print(f"Dado el incremento del tercer año usted va a retirar {sacar} y su saldo en la cuenta luego de esto es de {saldocuenta}.")
