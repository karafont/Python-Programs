def getFat():
    fatGrams = float(
        input("Please enter how many grams of fat you have consumed today: "))

    return fatGrams


def getCarbs():
    carbGrams = float(
        input("Please enter how many grams of carbohydrates you have eaten today: "))

    return carbGrams


def calcFat(fatGrams):
    calsFromFat = fatGrams * 9

    return calsFromFat


def calcCarbs(carbGrams):
    calsFromCarbs = carbGrams * 4

    return calsFromCarbs


def calcCals(calsFromFat, calsFromCarbs):
    totalCals = calsFromFat + calsFromCarbs

    return totalCals


def printCals(totalCals, calsFromFat, calsFromCarbs):
    print("Today, you have consumed", calsFromFat, "calories from fat. \n"+
          "You have consumed", calsFromCarbs, "calories from carbohydrates. \n"+
          "In total, you have consumed", totalCals, "calories from fat and carbohydrates.")

def main ():
    fatGrams = getFat()
    carbGrams = getCarbs()
    calsFromFat = calcFat(fatGrams)
    calsFromCarbs = calcCarbs(carbGrams)
    totalCals = calcCals(calsFromFat, calsFromCarbs)
    printCals(totalCals, calsFromFat, calsFromCarbs)

main ()
