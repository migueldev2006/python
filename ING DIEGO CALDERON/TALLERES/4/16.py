monto = int(input("Ingrese el total de la compra: "))

descuento1 = 0.10
descuento2 = 0.05

if (monto >= 1000):
    descuento = monto * descuento1
    total = monto - descuento
    print(f"Querido cliente, por la compra mayor a $1000 se le hace un descuento de 10% de su monto total {monto}, siendo un descuento de {descuento} y pagando un total de ${total} por la compra.")
    
elif (monto < 1000 and monto >= 500):
    descuento = monto * descuento2
    total = monto - descuento
    print(f"Querido cliente, por la compra mayor a $500 se le hace un descuento de 5% de su monto total {monto}, siendo un descuento de {descuento} y pagando un total de ${total} por la compra.")
    
else:
    print(f"Querido cliente, por la compra no se efectuara descuento ya que es menor a $500  y debe pagar un total de ${monto} por la compra.")