edad = int(input("Ingrese su edad: "))

if (edad >= 18):
    pregunta = input("¿Tiene licencia de conducir? ")
    if (pregunta =="si"):
        print("Puedes coducir")
    elif (pregunta == "no"):
        print("Debes obtener una licencia de conducir primero.")

else:
    print("No puedes conducir.")