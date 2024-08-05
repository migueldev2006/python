precioCompu = 700

compraCompu = int(input("Ingrese el  número de computadores que va a llevar: "))

descuento1 = 0.1
descuento2 = 0.2
descuento3 = 0.4

if (compraCompu > 0):
   if (compraCompu < 5):
        totalCompra = precioCompu * compraCompu
        descuentoCompra = totalCompra * descuento1
        resultado = totalCompra - descuentoCompra
        print(f"El precio de los {compraCompu} computadores es de: {resultado} USD")
        
   elif (compraCompu >= 5 and compraCompu < 10 ):
        totalCompra = precioCompu * compraCompu
        descuentoCompra = totalCompra * descuento2
        resultado = totalCompra - descuentoCompra
        print(f"El precio de los {compraCompu} computadores es de: {resultado} USD")
        
   elif (compraCompu >= 10):
        totalCompra = precioCompu * compraCompu
        descuentoCompra = totalCompra * descuento3
        resultado = totalCompra - descuentoCompra
        print(f"El precio de los {compraCompu} computadores es de: {resultado} USD")
        
