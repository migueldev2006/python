dinero =  2000000
impuestoAnual = 0.02
anios = 3
retiro = 10

incremento = dinero * (1+impuestoAnual)

incremento3 = incremento * anios

sacar = incremento3 - (incremento3*0.10)


print(incremento)
print (f"El valor acumulado por 3 años es de: {incremento3} y su retiro luego de 3 años es de : {sacar}")

