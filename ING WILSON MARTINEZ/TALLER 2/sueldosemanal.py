nombre = input("Digite el nombre del trabajador: ")
horas_trabajadas = input("Ingrese el número de horas trabajadas: ")


if int(horas_trabajadas) <= 40:
    valor_hora = 20
    
    total_sueldo = int(horas_trabajadas) * int(valor_hora)
    
    print(f"El sueldo semanal de {nombre} es de $ {total_sueldo}")

elif int(horas_trabajadas) > 40:
    horas_normales = 40
    valor_hora = 20
    valor_hora_extra = 25
    
    total_sueldo_normal = int(horas_normales) * int(valor_hora)
    extra = (int(horas_trabajadas)-40) * int(valor_hora_extra)
    sueldo_total = int(total_sueldo_normal) + int(extra)
    
    print(f"El sueldo semanal de {nombre} es de $ {sueldo_total}")