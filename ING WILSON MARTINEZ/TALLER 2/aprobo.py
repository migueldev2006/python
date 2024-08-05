nombre = input("Digite nombre :")

nota1 = input(("Digite nota 1 :"))
nota2 = input(("Digite nota 2 :"))
nota3 = input(("Digite nota 3 :"))

final = (float(nota1)+float(nota2)+float(nota3))/3

if (final >=3.0):
    print(nombre, " Aprobo")
else:
    print(nombre, " Reprobo")
