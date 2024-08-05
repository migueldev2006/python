print("Ingrese el valor total de la compra :")
total_compra = int(input())

print("Ingrese el porcentaje de descuento :")
porcentaje = int(input())

equivalencia = porcentaje/100
descuento = total_compra * equivalencia
valortotal = total_compra - descuento

print("El descuento es de :",descuento)
print("El valor total a pagar es de :",valortotal)