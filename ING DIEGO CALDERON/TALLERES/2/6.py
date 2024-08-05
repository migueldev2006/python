edad = input("Ingrese la edad: ")
genero = input("Ingrese su genero: ")


if (int(edad) >= 60 and genero == "M"):
    print("Ya estas en la edad de pensionarte.")
    
elif (int(edad) >= 54 and genero == "F"):
    print("Ya estas en la edad de pensionate.")

elif (int(edad) < 60 and genero == "M"):
    print("No estas en edad para pensionarte.")   
    
elif (int(edad) < 54 and genero == "F"):
    print("No estas en edad para pensionarte.")   
    
else:
    print("No hay coincidencias con tu genero.")  