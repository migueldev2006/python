from datetime import datetime

def diferencia_entre_fechas(fecha1, fecha2):
    fecha1 = datetime.strptime(fecha1, '%Y-%m-%d')
    fecha2 = datetime.strptime(fecha2, '%Y-%m-%d')
    diferencia = fecha2 - fecha1
    return abs(diferencia.days)

def main():
    fecha1 = input("Ingrese la primera fecha (en formato YYYY-MM-DD): ")
    fecha2 = input("Ingrese la segunda fecha (en formato YYYY-MM-DD): ")

    try:
        diferencia = diferencia_entre_fechas(fecha1, fecha2)
        print(f"La diferencia en días entre las fechas es: {diferencia} días.")
    except ValueError:
        print("Por favor ingrese las fechas en el formato correcto (YYYY-MM-DD).")

if __name__ == "__main__":
    main()
