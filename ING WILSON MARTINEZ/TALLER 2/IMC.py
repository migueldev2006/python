peso = int(input("Digite su peso: "))
altura = float(input("Digite su altura: "))

IMC = peso / (altura)**2

if IMC < 18.5:
    print(f"El Indice de Masa Corporal es de {IMC}. Estas por debajo del peso requerido.")

elif IMC >= 18.5 and IMC <= 24.9:
    print(f"El Indice de Masa Corporal es de {IMC}. Estas saludable.")

elif IMC >= 25.0 and IMC <= 29.9:
    print(f"El Indice de Masa Corporal es de {IMC}. Estas con sobrepeso.")

elif IMC >= 30.0 and IMC <= 39.9:
    print(f"El Indice de Masa Corporal es de {IMC}. Eres obeso.")

elif IMC >= 40:
    print(f"El Indice de Masa Corporal es de {IMC}. Tienes obesidad mórbida.")