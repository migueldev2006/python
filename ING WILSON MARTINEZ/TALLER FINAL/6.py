ahorro_total = 0 

for mes in range(1,13):
    Deposito = int(input(f"Ingresa la cantidad de  dinero depositada en el mes {mes}:  "))
    ahorro_total += Deposito
    print(f"El ahorro total del mes {mes} es de: {ahorro_total}")

print(f"El ahorro total  al finalizar un anio es de : {ahorro_total}")