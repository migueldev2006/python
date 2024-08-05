camisas = int(input("Ingrese el número de camisas: "))
valorCamisa = 20000

totalPagar = (valorCamisa - (valorCamisa * 0.2)) if (camisas >= 3) else (valorCamisa - (valorCamisa * 0.1))
print(totalPagar)
                                                                   