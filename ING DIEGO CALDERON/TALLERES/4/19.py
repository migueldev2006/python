import math

radio = input("Digite el radio: ")

area = math.pi * int(radio) ** 2
perimetro = 2 * math.pi * int(radio)

print(f"El área del circulo es {area}.")
print(f"El perimetro del circulo es {perimetro}.")