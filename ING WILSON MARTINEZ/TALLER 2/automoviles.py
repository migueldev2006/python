salario = 450000
valor_compra = input("Ingrese el valor de la compra: ")
vehiculos_vendidos = input("Digite el número de vehiculos vendidos: ")

equivalencia_venta = int(valor_compra) * (5/100)
aumento = int(vehiculos_vendidos) * 50000 
salario_total = int(salario) + equivalencia_venta + aumento

print(f"La comision del 5%  del valor de la venta que recibe el empleado es de {equivalencia_venta}.")
print(f"El aumento por vehiculos vendidos es de {aumento}.")
print(f"El salario total del empleado es de $ {salario_total}.")