sueldo_inicial = int(input("Ingrese el sueldo inicial :"))

if sueldo_inicial <= 500000:
    
    descuento = sueldo_inicial * (12/100)
    sueldo_total = sueldo_inicial - descuento
    print(f"El descuento es de {descuento}")
    print(f"El tarbajador recibe un sueldo total de $ {sueldo_total}")

elif sueldo_inicial > 500000 and sueldo_inicial <= 1000000:
    
    descuento = sueldo_inicial * (15/100)
    sueldo_total = sueldo_inicial - descuento
    print(f"El descuento es de {descuento}")
    print(f"El tarbajador recibe un sueldo total de $ {sueldo_total}")
    
elif sueldo_inicial > 1000000: 
       
    descuento = sueldo_inicial * (18/100)
    sueldo_total = sueldo_inicial - descuento
    print(f"El descuento es de {descuento}")
    print(f"El tarbajador recibe un sueldo total de $ {sueldo_total}")