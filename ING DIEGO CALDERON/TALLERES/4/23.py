anio = int(input("Ingrese el anio: "))

op1 = anio % 4
op2 = anio % 100
op3 = anio % 400

if op1 == 0 or op2 == 0 or op3 == 0:
    print("Es un anio bisiesto")
else:
    print("No es un año bisiesto")