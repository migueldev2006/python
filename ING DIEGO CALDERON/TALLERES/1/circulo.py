import math

print("Digite el radio del circulo:")
radio = input()

perimetro = 2* math.pi * int(radio)
area = math.pi * (int(radio)**2)

print("El perimetro del circulo es de :",perimetro)
print("El área del circulo es de :",area)