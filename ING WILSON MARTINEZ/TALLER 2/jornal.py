jornada = input("Ingrese la jornada de trabajo: ")
horas_trabajadas = input("Digite las horas trabajadas: ")

if jornada == ('Diurna'):
    tarifa = 10
    total_pagar_diu = int(horas_trabajadas) * int(tarifa)
    
    print(f"El jornal de un trabajador de jornada diurna es de $ {total_pagar_diu}")

elif jornada == ('Nocturna'):
    tarifa2 = 15
    total_pagar_noc = int(horas_trabajadas) * int(tarifa2)
    print(f"El jornal de un trabajador de jornada nocturna es de $ {total_pagar_noc}")

else: 
    print("No hay coincidencias")