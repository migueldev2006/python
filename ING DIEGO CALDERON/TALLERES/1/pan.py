print("Digite la cantidad de panes vendidos que no son del dia :")
panes = int(input())

print("Valor por barra de chocolate es :")
valor = float(input())

total = round(panes * valor, 2)
descuento = round(total * 0.60, 2)
final = round(total - descuento, 2)

print("El valor total inicial a pagar es de :",total, " USD.")
print("El descuento es de :",descuento, " USD.")
print("El valor final a pagar es de :",final, " USD.")