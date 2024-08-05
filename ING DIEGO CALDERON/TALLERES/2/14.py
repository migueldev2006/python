letra = input("Ingrese una letra: ")

letra = letra.lower()

if (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
    print(f"La letra {letra} es una vocal.")
    
else:
    print(F"La letra {letra} es una consonante.")