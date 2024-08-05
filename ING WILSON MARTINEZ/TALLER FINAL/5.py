kilometros = int(input("Ingrese los kilometros recorridos: "))
if kilometros <= 300:
    valor = 300000
elif kilometros > 300 and kilometros <= 1000:
    valor = 300000 + 15000 * (kilometros - 300)
elif kilometros > 1000:
    valor = 300000 + 10000 * (kilometros - 1000)

IVA = valor * 0.20


print(f"El valor total a pagar es de {valor}, incluyendo un impuesto de {IVA}")