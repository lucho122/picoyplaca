from datetime import date, datetime as dt

def canCirculate(date: str, time: str, licensePlate: str):
    # Rules
    noCirculateDays = {0: [1, 2],
                    1: [3, 4],
                    2: [5, 6],
                    3: [7, 8],
                    4: [9, 0]}
    timePeriodsLimits = [["07:00", "16:00"],["09:30", "19:30"]]

    # Data treatment and logic inmplementation
    lastDigit = int(licensePlate[-1])
    datetime = dt.strptime(date + " " + time, '%d/%m/%Y %H:%M')
    weeksDay = datetime.weekday()

    if (weeksDay not in noCirculateDays):
        return True
    elif (lastDigit in noCirculateDays[weeksDay]):
        return False

    dayTime = datetime.strftime("%H:%M")

    for i in range(len(timePeriodsLimits)):
        if ((dayTime >= timePeriodsLimits[0][i]) and (dayTime <= timePeriodsLimits[1][i])):
            return False
    return True

if __name__ == '__main__':
    paramsDate = input("Ingrese la fecha (dd/mm/yyyy): ")
    paramsTime = input("Ingrese la hora deseada (HH:mm): ")
    paramsLicensePlate = input("Ingrese la placa del vehiculo (XXX-0000): ")

    circulateResult = "Usted puede circular" if canCirculate(paramsDate, paramsTime, paramsLicensePlate) else "Usted NO puede circular"
    print("Resultado: ", circulateResult)