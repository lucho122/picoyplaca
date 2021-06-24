from datetime import date, datetime as dt

def circular(date: str, time: str, licensePlate: str):
    # Reglas
    circularDias = {0: [1, 2],
                    1: [3, 4],
                    2: [5, 6],
                    3: [7, 8],
                    4: [9, 0]}
    limiteHoras = [["07:00", "16:00"],["09:30", "19:30"]]

    # Procedimiento
    lastDigit = int(licensePlate[-1])
    datetime = dt.strptime(date + " " + time, '%d/%m/%Y %H:%M')
    weeksDay = datetime.weekday()
    if ((weeksDay in circularDias) and (lastDigit not in circularDias[weeksDay])):
        return False

    dayTime = datetime.strftime("%H:%M")
    if ((dayTime > limiteHoras[0][0] and dayTime < limiteHoras[1][0]) or
        (dayTime > limiteHoras[0][1] and dayTime < limiteHoras[1][1])):
        return True
    return False

paramsDate = input("Ingresa la fecha cojudo (dd/mm/yyyy): ")
paramsTime = input("A que hora vas a salir por el pan (HH:mm): ")
paramsLicensePlate = input("Ingresa la placa de tu nave (XXX-0000): ")

print("Resultado: ", circular(paramsDate, paramsTime, paramsLicensePlate))